#!/usr/bin/env python3
"""Run a Mamba Labs actor on Apify directly, for actors that have no MCP tool.

Usage:
    APIFY_TOKEN=... python3 scripts/apify-run.py <actor slug> [input.json] [--out items.json]

With no input file, the runnable example in scripts/inputs/<actor slug>.json is used.
The token is read from the APIFY_TOKEN environment variable and is never printed.
Get one at https://console.apify.com/account/integrations. The run bills your own
Apify account at the actor's Store price.

The script starts the run, waits for it to finish, and writes the dataset items to the
output file (default: <actor slug>-items.json). It exits non zero when the run fails or
returns zero items, so a skill never mistakes an empty run for a result.
Standard library only, no install needed.
"""
import json, os, sys, time, urllib.request, urllib.error

API = "https://api.apify.com/v2"
HERE = os.path.dirname(os.path.abspath(__file__))
ACTORS = json.load(open(os.path.join(HERE, "actors.json")))


def call(method, path, token, body=None):
    req = urllib.request.Request(API + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None)
    req.add_header("Authorization", "Bearer " + token)
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args or args[0] not in ACTORS:
        print("usage: apify-run.py <actor slug> [input.json] [--out items.json]")
        print("actors in this skill: %s" % ", ".join(sorted(ACTORS)))
        return 1
    token = os.environ.get("APIFY_TOKEN", "").strip()
    if not token:
        print("APIFY_TOKEN is not set. Ask the user for an Apify API token; do not guess one.")
        return 1
    slug = args[0]
    actor_id = ACTORS[slug]["id"]
    inp_path = args[1] if len(args) > 1 else os.path.join(HERE, "inputs", slug + ".json")
    payload = json.load(open(inp_path))
    out = "%s-items.json" % slug
    if "--out" in argv:
        out = argv[argv.index("--out") + 1]

    try:
        run = call("POST", "/acts/%s/runs" % actor_id, token, payload)["data"]
    except urllib.error.HTTPError as e:
        print("START FAILED: HTTP %d %s" % (e.code, e.read().decode()[:300]))
        return 1
    run_id = run["id"]
    print("started %s run %s" % (slug, run_id))
    status = run["status"]
    waited = 0
    while status in ("READY", "RUNNING"):
        time.sleep(10)
        waited += 10
        run = call("GET", "/actor-runs/%s" % run_id, token)["data"]
        status = run["status"]
        if waited % 60 == 0:
            print("  %s after %d s" % (status, waited))
    if status != "SUCCEEDED":
        print("RUN %s: %s. No items were written." % (status, run_id))
        return 1
    items = call("GET", "/datasets/%s/items?clean=true&format=json" % run["defaultDatasetId"], token)
    json.dump(items, open(out, "w"), indent=2)
    usage = run.get("usageTotalUsd")
    print("SUCCEEDED: %d items written to %s" % (len(items), out))
    if usage is not None:
        print("Apify usage so far: %.4f USD (this figure can still rise for about a minute)" % usage)
    if not items:
        print("EMPTY: the run succeeded but returned no items. Report this, do not treat it as a result.")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
