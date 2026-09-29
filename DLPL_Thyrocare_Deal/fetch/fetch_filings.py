#!/usr/bin/env python3
"""Download company filings and verify each one is a real PDF.

The failure this guards against: investor-relations sites happily return a 200 with an HTML
error page, a login wall, or a redirect stub. Saved with a .pdf extension it looks fine in a
directory listing and then blows up when you try to read it. Every file is checked for the
%PDF magic bytes and a plausible size before it counts as downloaded.

Usage
-----
  # From a manifest (preferred for a full pull)
  fetch_filings.py --base https://www.example.com --out "Company Name" --manifest m.json

  # Ad hoc, repeatable
  fetch_filings.py --out "Company Name" \
      --url https://x.com/ar2026.pdf 01_Annual_Reports/AR_FY2026.pdf \
      --url https://x.com/q4.pdf     05_Quarterly_Results/Q4FY26.pdf

Manifest format — a list of [url_or_path, destination] pairs. If --base is given, entries
starting with "/" are treated as paths relative to it:

  [
    ["/investors/agm/annual-report-2025-26.pdf", "01_Annual_Reports/AR_FY2026.pdf"],
    ["https://other.com/rhp.pdf",                "02_IPO_RHP/RHP.pdf"]
  ]
"""

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

FOLDERS = [
    "01_Annual_Reports",
    "02_IPO_RHP",
    "03_Investor_Presentations",
    "04_Earnings_Calls",
    "05_Quarterly_Results",
    "06_Other",
]

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
MIN_BYTES = 20_000  # anything smaller is almost certainly an error page, not a filing


def human(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.0f}{unit}"
        n /= 1024
    return f"{n:.1f}TB"


def fetch(url, dest, timeout=180):
    """Download url to dest. Returns (ok, message)."""
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    # Spaces and other stray characters are common in IR hrefs.
    safe = urllib.parse.quote(url, safe=":/?#[]@!$&'()*+,;=%~")
    req = urllib.request.Request(safe, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"

    if len(data) < MIN_BYTES:
        return False, f"too small ({human(len(data))}) — likely an error page"
    if not data.lstrip()[:5].startswith(b"%PDF"):
        head = data.lstrip()[:60].decode("utf-8", "replace").replace("\n", " ")
        return False, f"not a PDF (starts with: {head!r})"

    with open(dest, "wb") as f:
        f.write(data)
    return True, human(len(data))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--out", required=True, help="Output folder for this company")
    p.add_argument("--base", default="", help="Base URL prefixed to manifest entries starting with /")
    p.add_argument("--manifest", help="JSON file of [url, destination] pairs")
    p.add_argument("--url", nargs=2, action="append", metavar=("URL", "DEST"),
                   help="A single url/destination pair; repeatable")
    p.add_argument("--timeout", type=int, default=180)
    p.add_argument("--no-scaffold", action="store_true", help="Skip creating the standard subfolders")
    args = p.parse_args()

    if not args.no_scaffold:
        for d in FOLDERS:
            os.makedirs(os.path.join(args.out, d), exist_ok=True)

    jobs = []
    if args.manifest:
        with open(args.manifest) as f:
            jobs += [tuple(x) for x in json.load(f)]
    if args.url:
        jobs += [tuple(x) for x in args.url]

    if not jobs:
        print("Nothing to download. Folder scaffold created at:", args.out)
        return 0

    ok = failed = 0
    fails = []
    for url, dest in jobs:
        full = args.base.rstrip("/") + url if url.startswith("/") else url
        path = os.path.join(args.out, dest)
        good, msg = fetch(full, path, args.timeout)
        if good:
            ok += 1
            print(f"  OK    {msg:>8}  {dest}")
        else:
            failed += 1
            fails.append((dest, msg))
            print(f"  FAIL            {dest}  --  {msg}")

    print(f"\n{ok} downloaded, {failed} failed.")
    if fails:
        print("\nCould not retrieve (note these in your write-up rather than guessing at the contents):")
        for dest, msg in fails:
            print(f"  - {dest}: {msg}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
