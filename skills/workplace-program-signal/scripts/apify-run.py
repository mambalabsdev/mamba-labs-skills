#!/usr/bin/env python3
"""Run a Mamba Labs actor on Apify directly, for actors that have no MCP tool.

Usage:
    APIFY_TOKEN=... python3 scripts/apify-run.py <actor slug> [input.json] [--out items.json]

With no input file, the runnable example in scripts/inputs/<actor slug>.json is used.
The token is read from the APIFY_TOKEN environment variable and is never printed.
Get one at https://console.apify.com/account/integrations. The run bills your own
Apify account at the actor's Store price.

Provider keys. An input file may reference environment variables instead of holding a
key: "${SERPER_API_KEY}" must be set, "${PROSPEO_API_KEY?}" is optional and is dropped
when unset, and "_requires_any": [["A", "B"]] means at least one of A or B must be set.
The script fills them in at run time, never writes them anywhere, and stops before
starting the run when a required key is missing, so no usage is spent on a run that
cannot return results.

The script starts the run, waits for it to finish, and writes the dataset items to the
output file (default: <actor slug>-items.json). It exits non zero when the run fails or
returns zero items, so a skill never mistakes an empty run for a result.

Exit codes: 0 items written, 1 failed, 2 run succeeded with zero items, 3 a required
key or a working certificate store is missing. Standard library only, no install needed.
"""
import json, os, re, ssl, sys, time, urllib.request, urllib.error

API = "https://api.apify.com/v2"
HERE = os.path.dirname(os.path.abspath(__file__))
ACTORS = json.load(open(os.path.join(HERE, "actors.json")))
SYSTEM_CA_FILES = ["/etc/ssl/cert.pem", "/etc/ssl/certs/ca-certificates.crt", "/etc/pki/tls/certs/ca-bundle.crt"]
CERT_HELP = ("Python on this machine cannot verify HTTPS certificates. Fix it once, then rerun: "
             "on a python.org install on macOS run 'Install Certificates.command' from the Python "
             "folder in Applications, or run with SSL_CERT_FILE pointing at a CA bundle, for example "
             "SSL_CERT_FILE=/etc/ssl/cert.pem.")


def ssl_context():
    """A context that can verify api.apify.com. Order: SSL_CERT_FILE or the default store,
    then certifi if installed, then the system CA bundle. Returns (context, source)."""
    ctx = ssl.create_default_context()
    if os.environ.get("SSL_CERT_FILE") or ctx.cert_store_stats().get("x509_ca", 0) > 0:
        return ctx, "default"
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where()), "certifi"
    except ImportError:
        pass
    for f in SYSTEM_CA_FILES:
        if os.path.exists(f):
            return ssl.create_default_context(cafile=f), f
    return ctx, "default"


CTX, CTX_SOURCE = ssl_context()


def call(method, path, token, body=None):
    req = urllib.request.Request(API + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None)
    req.add_header("Authorization", "Bearer " + token)
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return json.loads(r.read().decode())


def report_charges(run_id, actor_id, token):
    """Print what the run bills: its charged events priced at the actor's Store list
    price. usageTotalUsd is platform compute only and is a small fraction of what a
    pay per event actor charges, so it is never reported as the cost."""
    try:
        # Charged events settle after the run finishes; a read at SUCCEEDED can be
        # short. Re read until two reads 15 seconds apart agree, for up to 90 seconds.
        counts, waited = None, 0
        while waited <= 90:
            now_counts = call("GET", "/actor-runs/%s" % run_id, token)["data"].get("chargedEventCounts") or {}
            if now_counts == counts:
                break
            counts = now_counts
            time.sleep(15)
            waited += 15
        act = call("GET", "/acts/%s" % actor_id, token)["data"]
    except (urllib.error.URLError, KeyError, ValueError) as e:
        print("Charges: could not be read (%s). Read them on the run page in the Apify Console." % e)
        return
    now = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
    infos = [i for i in act.get("pricingInfos") or [] if (i.get("startedAt") or "") <= now]
    events = ((infos[-1].get("pricingPerEvent") or {}).get("actorChargeEvents") or {}) if infos else {}
    total, parts = 0.0, []
    for name, n in sorted(counts.items()):
        if not n:
            continue
        ev = events.get(name) or {}
        tiers = ev.get("eventTieredPricingUsd") or {}
        price = (tiers.get("FREE") or {}).get("tieredEventPriceUsd", ev.get("eventPriceUsd"))
        if price is None:
            parts.append("%d x %s (price not listed)" % (n, name))
            continue
        total += n * price
        parts.append("%d x %s at %.4f USD" % (n, name, price))
    if not parts:
        print("Charges: no charged events recorded on this run yet. Check the run page in a minute.")
        return
    print("Charges at Store list price: %.4f USD (%s). This is what the run bills your Apify "
          "account; a paid Apify plan can lower the per event price." % (total, "; ".join(parts)))


PLACEHOLDER = re.compile(r"^\$\{([A-Z0-9_]+)(\??)\}$")


def fill(value, missing):
    """Replace ${NAME} placeholders from the environment. Optional ones that are unset
    are dropped from objects and lists. Required ones that are unset go into missing."""
    if isinstance(value, dict):
        out = {}
        for k, v in value.items():
            if k.startswith("_"):
                continue
            v2 = fill(v, missing)
            if v2 is not None:
                out[k] = v2
        return out
    if isinstance(value, list):
        return [x for x in (fill(v, missing) for v in value) if x is not None]
    if isinstance(value, str):
        m = PLACEHOLDER.match(value)
        if m:
            got = os.environ.get(m.group(1), "").strip()
            if got:
                return got
            if not m.group(2):
                missing.append(m.group(1))
            return None
    return value


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    if "--out" in argv:
        out_i = argv.index("--out") + 1
        args = [a for a in args if a != argv[out_i]]
    if not args or args[0] not in ACTORS:
        print("usage: apify-run.py <actor slug> [input.json] [--out items.json]")
        print("actors in this skill: %s" % ", ".join(sorted(ACTORS)))
        return 1
    token = os.environ.get("APIFY_TOKEN", "").strip()
    if not token:
        print("APIFY_TOKEN is not set. Ask the user for an Apify API token; do not guess one.")
        return 3
    slug = args[0]
    actor_id = ACTORS[slug]["id"]
    inp_path = args[1] if len(args) > 1 else os.path.join(HERE, "inputs", slug + ".json")
    raw = json.load(open(inp_path))
    missing = []
    payload = fill(raw, missing)
    for group in raw.get("_requires_any", []) if isinstance(raw, dict) else []:
        if not any(os.environ.get(v, "").strip() for v in group):
            missing.append(" or ".join(group))
    if missing:
        print("MISSING KEY: set %s in the environment before running %s. Stop and tell the user "
              "which key is missing; the run was not started and nothing was billed."
              % (", ".join(dict.fromkeys(missing)), slug))
        return 3
    out = "%s-items.json" % slug
    if "--out" in argv:
        out = argv[argv.index("--out") + 1]

    try:
        run = call("POST", "/acts/%s/runs" % actor_id, token, payload)["data"]
    except urllib.error.HTTPError as e:
        print("START FAILED: HTTP %d %s" % (e.code, e.read().decode()[:300]))
        return 1
    except urllib.error.URLError as e:
        if "CERTIFICATE_VERIFY_FAILED" in str(e.reason):
            print("CERTIFICATE ERROR: " + CERT_HELP)
            return 3
        print("NETWORK ERROR: could not reach api.apify.com (%s). Check the connection and rerun." % e.reason)
        return 1
    run_id = run["id"]
    print("started %s run %s" % (slug, run_id))
    status = run["status"]
    waited = 0
    while status in ("READY", "RUNNING"):
        time.sleep(10)
        waited += 10
        try:
            run = call("GET", "/actor-runs/%s" % run_id, token)["data"]
        except urllib.error.URLError as e:
            print("  poll failed (%s), retrying" % getattr(e, "reason", e))
            continue
        status = run["status"]
        if waited % 60 == 0:
            print("  %s after %d s" % (status, waited))
    if status != "SUCCEEDED":
        print("RUN %s: %s. No items were written." % (status, run_id))
        return 1
    items = call("GET", "/datasets/%s/items?clean=true&format=json" % run["defaultDatasetId"], token)
    json.dump(items, open(out, "w"), indent=2)
    print("SUCCEEDED: %d items written to %s" % (len(items), out))
    report_charges(run_id, actor_id, token)
    # Some actors append a run summary row, or write a notice row such as "No people
    # found" for an input that returned nothing. Neither is a result, so neither counts.
    rows = [i for i in items if not (isinstance(i, dict) and (i.get("is_summary_row") or i.get("row_status") in ("summary", "notice")))]
    if len(rows) != len(items):
        print("  %d of the %d items are result rows; the rest are summary or notice rows." % (len(rows), len(items)))
    if not rows:
        print("EMPTY: the run succeeded but returned no result rows. Report this, do not treat it as a result.")
        return 2
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except ssl.SSLError as e:
        print("CERTIFICATE ERROR: " + CERT_HELP)
        sys.exit(3)
    except KeyboardInterrupt:
        sys.exit(1)
