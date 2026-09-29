#!/usr/bin/env python3
"""List PDF links on an investor-relations page, optionally filtered by keyword.

Use this to build a manifest for fetch_filings.py once the IR sites are reachable:

  python3 harvest_links.py https://www.lalpathlabs.com/investor-relations annual transcript presentation
  python3 harvest_links.py https://investor.thyrocare.com/ shareholding "open offer" --json > thyro.json

With --json the output is a [url, suggested_destination] list; review the destinations before
passing it to fetch_filings.py --manifest.
"""
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin

FOLDERS = [
    ("annual", "01_Annual_Reports"), ("prospectus", "02_IPO_RHP"), ("rhp", "02_IPO_RHP"),
    ("presentation", "03_Investor_Presentations"), ("transcript", "04_Earnings_Calls"),
    ("concall", "04_Earnings_Calls"), ("result", "05_Quarterly_Results"),
    ("shareholding", "07_Deal_Filings/Shareholding_Patterns"),
    ("open offer", "07_Deal_Filings/2021_Open_Offer"), ("letter of offer", "07_Deal_Filings/2021_Open_Offer"),
    ("sast", "07_Deal_Filings/Docon_Stake_Sales_and_Pledges"), ("pledge", "07_Deal_Filings/Docon_Stake_Sales_and_Pledges"),
]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self._href, self._text = [], None, []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self._href, self._text = dict(attrs).get("href"), []

    def handle_data(self, data):
        if self._href:
            self._text.append(data.strip())

    def handle_endtag(self, tag):
        if tag == "a" and self._href:
            self.links.append((self._href, " ".join(t for t in self._text if t)))
            self._href = None


def folder_for(label):
    low = label.lower()
    return next((f for k, f in FOLDERS if k in low), "06_Other")


def main():
    args = [a for a in sys.argv[1:] if a != "--json"]
    if not args:
        sys.exit(__doc__)
    page, keywords = args[0], [k.lower() for k in args[1:]]
    req = urllib.request.Request(page, headers={"User-Agent": "Mozilla/5.0"})
    parser = Links()
    parser.feed(urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace"))
    rows = []
    for href, text in parser.links:
        url = urljoin(page, href)
        label = f"{text} {url}"
        if not url.lower().split("?")[0].endswith(".pdf"):
            continue
        if keywords and not any(k in label.lower() for k in keywords):
            continue
        name = re.sub(r"[^A-Za-z0-9._-]+", "_", text or url.rsplit("/", 1)[-1])[:80].strip("_")
        rows.append([url, f"{folder_for(label)}/{name or 'file'}.pdf".replace(".pdf.pdf", ".pdf")])
    if "--json" in sys.argv:
        print(json.dumps(rows, indent=2))
    else:
        for url, dest in rows:
            print(f"{dest}\t{url}")


if __name__ == "__main__":
    main()
