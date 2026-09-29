# Filing download checklist

## Status: nothing has been downloaded yet

The session that set up this folder (29 Sep 2026) ran in a cloud container whose network policy
refused every document host with **HTTP 403 at the proxy**:

`www.lalpathlabs.com`, `media.lalpathlabs.com`, `www.thyrocare.com`, `investor.thyrocare.com`,
`www.bseindia.com`, `api.bseindia.com`, `www.nseindia.com`, `nsearchives.nseindia.com`,
`www.sebi.gov.in`, `web.archive.org`, plus news and aggregator sites.

`fetch/fetch_filings.py` was run against the known URLs in `fetch/manifest_known_urls.json` and
failed on all 7 with `Tunnel connection failed: 403 Forbidden`. The folders are in place and
empty (`.gitkeep` only).

**To fix:** allow those domains in the environment's network settings (or run the commands
below on your own machine), then:

```bash
cd DLPL_Thyrocare_Deal

# 1. The URLs already identified
python3 fetch/fetch_filings.py --out . --no-scaffold --manifest fetch/manifest_known_urls.json

# 2. Harvest everything else from each IR page, review the destinations, then fetch
python3 fetch/harvest_links.py https://www.lalpathlabs.com/investor-relations --json > fetch/dlpl.json
python3 fetch/harvest_links.py https://investor.thyrocare.com/ --json > fetch/thyro.json
#    edit destinations to prefix Dr_Lal_PathLabs/ or Thyrocare/, then:
python3 fetch/fetch_filings.py --out . --no-scaffold --manifest fetch/dlpl.json
python3 fetch/fetch_filings.py --out . --no-scaffold --manifest fetch/thyro.json
```

`fetch_filings.py` checks each file really is a PDF, not an HTML error page saved as `.pdf`.

## What goes where

Identifiers: **DLPL** is BSE 539524, NSE `LALPATHLAB`. **Thyrocare** is BSE 539871, NSE `THYROCARE`.

### Dr_Lal_PathLabs/

| Folder | Documents | Where to find them |
|---|---|---|
| 01_Annual_Reports | AR FY24, FY25, FY26 | lalpathlabs.com → Investor Relations → Annual Reports; BSE → 539524 → Annual Reports |
| 02_IPO_RHP | Dec 2015 RHP (optional; listed >5 years ago) | SEBI / BSE archive |
| 03_Investor_Presentations | Q1 FY24 → Q1 FY27 earnings presentations (13) | IR page. Known URL: Q4 FY25 `media.lalpathlabs.com/2025-04/Earnings-Presentation.pdf` |
| 04_Earnings_Calls | Q1 FY24 → Q1 FY27 transcripts (13) | IR page; BSE announcements about 1 week after results |
| 05_Quarterly_Results | Q1 FY24 → Q1 FY27 results filings and press releases | IR page; BSE "Financial Results" |
| 06_Other | Credit rating rationale, BRSR, Suburban and SN Genelab acquisition disclosures | CRISIL/ICRA; BSE announcements |

### Thyrocare/

| Folder | Documents | Where to find them |
|---|---|---|
| 01_Annual_Reports | AR FY24, FY25, FY26 | investor.thyrocare.com; BSE → 539871 |
| 02_IPO_RHP | Apr 2016 RHP (optional) | SEBI / BSE archive |
| 03_Investor_Presentations | Q1 FY24 → Q1 FY27 (13) | investor.thyrocare.com |
| 04_Earnings_Calls | Q1 FY24 → Q1 FY27 transcripts (13) | investor.thyrocare.com; BSE |
| 05_Quarterly_Results | Q1 FY24 → Q1 FY27 results | investor.thyrocare.com; BSE. Known: Q4 FY24 filing of 14 May 2024 (in manifest) |
| 06_Other | Bonus issue (2:1, record date 28 Nov 2025) postal ballot / outcome | BSE announcements |
| 07_Deal_Filings/Shareholding_Patterns | Quarterly shareholding patterns Jun 2021 → Sep 2026 | `investor.thyrocare.com/investors-information/shareholding-pattern/`; BSE → Shareholding Pattern |
| 07_Deal_Filings/Docon_Stake_Sales_and_Pledges | SAST Reg 29(2) disclosures for the Oct 2025 and 13 Aug 2026 sales; Reg 31 pledge creation and release disclosures (incl. 11 Aug and ~14–17 Aug 2026 releases); NCLT order on the Docon → API Holdings amalgamation (effective 3 Sep 2026) | BSE announcements for 539871, "Insider trading / SAST" section |
| 07_Deal_Filings/2021_Open_Offer | Public announcement (Jun 2021); detailed public statement; **draft letter of offer** (`sebi.gov.in/sebi_data/commondocs/jul-2021/ThyrocareDLOF_p.pdf`, in manifest); final letter of offer; post-offer advertisement (Sep 2021); SPA summary | SEBI → Filings → Takeovers → Letter of Offer; BSE; manager to the offer's website |

Files in the manifest marked `_UNVERIFIED` are BSE attachments that search results linked to the
company. Their contents were not seen. Rename them once opened.

## Tick-list

- [ ] DLPL AR FY24 · FY25 · FY26
- [ ] Thyrocare AR FY24 · FY25 · FY26
- [ ] DLPL presentations ×13 · transcripts ×13 · results ×13
- [ ] Thyrocare presentations ×13 · transcripts ×13 · results ×13
- [ ] Thyrocare shareholding patterns (Jun 2021 → Sep 2026)
- [ ] Docon Oct 2025 and Aug 2026 SAST sale disclosures
- [ ] Docon pledge creation and release disclosures
- [ ] 2021 open offer: PA, DPS, DLOF, LOF, post-offer ad
