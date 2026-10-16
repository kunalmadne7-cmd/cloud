# MASTER CASE STUDY: OmniRetail Group — IT Strategy & Operating Model Transformation

**PwC USI Technology Consulting Interview Preparation | Module 4 Complete Revision (Hinglish)**

> Yeh ek hi case hai jo poore Module 4 ke 13 concepts ko ek business problem se jodta hai.
> Saare numbers **fictional** hain. Jo figure brief mein diya gaya tha use **[CASE FACT]** bola gaya hai; jo maine banaya hai use **[ILLUSTRATIVE ASSUMPTION]** bola gaya hai. Koi bhi figure real industry benchmark nahi hai.

---

## CONTENTS

- **Part 0** — Case Fact Sheet (saare numbers ek jagah)
- **Part 1** — Problem statement (beginner-friendly)
- **Part 2** — Consultant case kaise shuru karta hai
- **Part 3** — Master Issue Tree
- **Part 4** — Case ko step-by-step solve karna (Steps 1–13)
  - Step 1 IT Strategy & Business Alignment
  - Step 2 Current vs Target Architecture
  - Step 3 IT Operating Model
  - Step 4 Centralized vs Decentralized IT
  - Step 5 IT Governance (+ RACI)
  - Step 6 IT Organization
  - Step 7 Application Rationalization
  - Step 8 Build vs Buy (+ 5-year TCO)
  - Step 9 Outsourcing
  - Step 10 Managed Services (+ SLA)
  - Step 11 Vendor Management
  - Step 12 IT Cost Optimization (+ Savings Bridge)
  - Step 13 18-month Roadmap
- **Part 5** — CEO ke liye Final Recommendation
- **Part 6** — Master Revision Flowchart (A, B, C)
- **Part 7** — Interview Preparation
- **Part 8** — Final Revision Sheet
- **Part 9** — Interviewer ko 3–5 minute mein poora case kaise walk-through karein

---

# PART 0: CASE FACT SHEET (Single Source of Truth)

Poore document mein sirf yahi numbers use honge. Revise karte waqt yahan wapas aao.

### 0.1 Company basics

| Item | Value | Type |
|---|---|---|
| Annual revenue | ₹5,000 crore | [CASE FACT] |
| Annual IT expenditure | ₹250 crore (= 5.0% of revenue) | [CASE FACT] |
| 3-year IT spend increase | 35% → 3 saal pehle spend = 250 ÷ 1.35 = **₹185.2 crore** | [CASE FACT] + calculation |
| CEO target | Recurring annual IT spend 15% kam = **₹37.5 crore**, within 18 months → target run-rate **₹212.5 crore** | [CASE FACT] |
| Digital sales growth | +25% next year | [CASE FACT] |
| Current digital sales | ₹1,000 crore (20% of revenue) → ₹1,250 crore next year | [ILLUSTRATIVE ASSUMPTION] |
| Business applications | 120 | [CASE FACT] |
| Divisions | 3: Fashion & Lifestyle (original), Grocery & Daily Needs (acquired), Home & Electronics (acquired) | [CASE FACT: 3] + names illustrative |
| Countries | 5: India, UAE, Saudi Arabia, Singapore, Indonesia | [CASE FACT: 5] + names illustrative |
| Stores | ~1,200 stores | [ILLUSTRATIVE ASSUMPTION] |
| Internal IT staff | 650 people, average fully-loaded cost ₹10 lakh/year → ₹65 crore | [ILLUSTRATIVE ASSUMPTION] |
| Data centres | 4 (acquisitions ki wajah se) | [ILLUSTRATIVE ASSUMPTION] |
| IT vendors | 210 vendors; top 20 = ~75% of external spend | [ILLUSTRATIVE ASSUMPTION] |
| Revenue growth in last 3 years | ~15% (IT spend 35% badha → IT cost revenue se tez badha) | [ILLUSTRATIVE ASSUMPTION] |

### 0.2 ₹250 crore IT spend ka breakdown (MECE cost pools)

**Rule (double-counting rokne ke liye):** Har rupee sirf EK pool mein jayega.
- Software licence/subscription ka paisa → "Applications & Licences" pool.
- Cloud bill, data centre, network, laptops → "Infrastructure & Cloud" pool.
- Company ke apne employees → "People" pool.
- Bahar ke logon ki services (contractors, managed services, helpdesk vendor, consulting) → "Vendors & External Services" pool.
- Baaki (training, travel, audit, misc) → "Other".

| # | Cost Pool | ₹ crore | Sub-components [ILLUSTRATIVE] |
|---|---|---|---|
| 1 | Infrastructure & Cloud | **70** | Public cloud 30 (Prod compute 14, Non-prod 8, Storage 5, Network/other cloud services 3; isme e-commerce workloads ≈ ₹10 cr) · On-prem data centres 28 (4 DCs; 2 chhote DCs = ₹8 cr) · Network 6 · End-user devices 6 |
| 2 | Applications & Software Licences | **60** | Business app licences/subscriptions 38 · Productivity/collaboration suite 12 · Database & middleware licences 10 |
| 3 | People & IT Operations (internal) | **65** | 650 staff × ₹10 lakh |
| 4 | Vendors & External Services | **45** | App development/support contractors 25 · Infra/cloud ops vendors 8 · Helpdesk vendors 5 · Consulting/project services 7 |
| 5 | Other IT | **10** | Training, travel, audits, misc |
| | **Total** | **250** | 70+60+65+45+10 = 250 ✔ |

### 0.3 Final answer preview (detail Step 12 mein)

| Item | ₹ crore |
|---|---|
| Core savings levers (9 levers, net recurring) | 39.4 |
| Gap-closing levers (2) | 2.7 |
| Headwinds (digital growth + security/data reinvestment) | −4.5 |
| **Net recurring reduction (exit run-rate, Month 18)** | **37.6 (15.04%)** |
| Final run-rate | 212.4 (target 212.5 ✔, buffer sirf ₹0.1 cr) |
| One-time implementation cost | 39.5 |
| Cumulative cash impact in 18 months | ≈ −10.5 (investment phase); cash break-even ≈ Month 22 |
| Contingency pipeline (extra) | 4.2 |
| Risk-adjusted view | ~13.7% (with pipeline) → CEO ko clearly batana hai |

---

# PART 1: PROBLEM STATEMENT (Simple Language Mein)

### 1.1 Company ki kahani

OmniRetail Group ek multinational retail company hai. Iske paas **physical stores** bhi hain aur **online sales channel** (website + mobile app) bhi. Company ne pichhle kuch saalon mein doosri companies **acquire** (khareed) ki — Grocery business aur Home & Electronics business. Problem yeh hai ki jab aap company khareedte ho, to uske saath uska poora IT bhi aa jata hai: uska ERP, uska CRM, uske servers, uske vendors, uske contracts.

Kisi ne in sabko **integrate ya simplify** nahi kiya. Result:
- 2 ERP, 2 CRM, 2 ITSM tools, 3 collaboration tools, 2 BI tools chal rahe hain (same kaam, double paisa).
- 4 data centres hain.
- Cloud pe migration hua, lekin purane servers band nahi hue (double running).
- 210 vendors hain, har division apna contract khud karta hai.
- Koi bhi bada decision lene mein mahine lag jaate hain kyunki pata hi nahi ki decide kaun karega.

Isliye IT spend 3 saal mein ₹185.2 cr se ₹250 cr ho gaya (+35%), jabki revenue sirf ~15% badha [ILLUSTRATIVE].

> **Simple analogy:** Socho ek joint family mein teen bhai alag-alag shaadi karke apne-apne ghar ka saaman le aaye. Ab ghar mein 3 fridge, 3 washing machine, 3 internet connection hain. Bill bahut aa raha hai. Lekin aap simply 2 fridge bech nahi sakte — pehle dekhna padega kaunsa fridge kaun use karta hai, kaunsa achha hai, aur kisi ki dawaai to kisi fridge mein nahi rakhi.

### 1.2 CEO actually kya chahta hai?

CEO ki baat ko todo:

1. **"Recurring annual IT expenditure 15% kam karo"** → Har saal ka chalne wala kharcha (run-rate) ₹250 cr se ₹212.5 cr pe lana hai. Matlab **₹37.5 crore per year** ki permanent kami. Ek baar ka discount ya ek saal ke liye project rokna isme count nahi hoga (woh recurring nahi hai).
2. **"18 months mein"** → Month 18 tak ka run-rate ₹212.5 cr hona chahiye.
3. **"Digital growth ko nuksaan nahi"** → Online sales 25% badhengi. Iske liye e-commerce platform scale karna padega — jo cloud cost badhayega. To savings ko yeh growth cost bhi absorb karni hai.
4. **"Customer experience, cybersecurity, reliability ko nuksaan nahi"** → Hum security tools kaat ke, ya support team aadhi karke "saving" nahi dikha sakte. Yeh **guardrails** (seemaayein) hain.

### 1.3 Yeh mushkil kyun hai?

| Challenge | Kyun mushkil |
|---|---|
| Cost kam + growth zyada, dono ek saath | Growth ke liye naya paisa chahiye; cost cutting ke liye kam paisa. Dono conflict karte hain. |
| Savings ke liye pehle investment chahiye | Application band karne ke liye data migrate karna, integration badalna, training — sab ek-baar ka kharcha (one-time cost). |
| Acquisitions ki complexity | Har division ki apni process, apna data, apne log. Politics bhi hai. |
| Local regulations | 5 countries ke data protection, tax, fiscal rules alag. Sab kuch centralize nahi kar sakte. |
| Savings ka double-counting | Agar ek app retire kiya to licence bhi bacha, vendor bill bhi kam hua — isko do baar count kar diya to fake savings. |
| 18 months chhota time | Bade changes (jaise ERP consolidation) ka benefit sirf end mein aayega. |

### 1.4 Success kaisa dikhta hai?

| Dimension | Success measure |
|---|---|
| Cost | Month 18 annualized recurring IT spend ≤ ₹212.5 cr (constant prices pe, Part 2 dekho) |
| Digital growth | Digital sales ₹1,250 cr support ho; peak season mein site down na ho |
| Reliability | Critical systems availability (e.g., e-commerce 99.9%+) maintain ya improve |
| Security | Koi bhi critical security control kam na ho; unsupported systems kam hon |
| Customer experience | Click & collect, real-time stock visibility jaisi capabilities improve hon |
| Sustainability | Cost dobara na badhe → governance + FinOps + vendor management permanent ho |

---

# PART 2: CONSULTANT CASE KAISE SHURU KARTA HAI

### 2.1 Problem restatement (interview mein pehli line)

> "Agar main sahi samjha: OmniRetail ka IT spend ₹250 crore hai, jo 3 saal mein 35% badha hai, revenue se kaafi tez. CEO chahte hain ki 18 mahine mein recurring IT spend 15% — yaani ₹37.5 crore per year — kam ho, lekin digital growth (25%), customer experience, security aur reliability compromise na ho. To humara kaam hai: cost kahan se aa raha hai yeh samajhna, sustainable savings levers dhundhna, aur ek implementable roadmap dena. Kya main sahi samjha?"

**Kyun zaroori:** Isse interviewer ko dikhta hai ki aapne objective (₹37.5 cr), timeline (18 months) aur constraints (growth, security, CX) teeno pakad liye.

### 2.2 Most important clarifying questions (aur unka purpose)

| # | Question | Kyun poochna zaroori hai | Assumed answer [ILLUSTRATIVE] |
|---|---|---|---|
| 1 | 15% target **run-rate** pe hai (Month 18 ka annual spend) ya 18 months ka **total cash**? | Dono ka maths bilkul alag hai. Run-rate mein permanent change chahiye; cash mein timing matter karti hai. | Exit run-rate at Month 18. |
| 2 | Target **constant prices** pe hai ya nominal? (Salary increments, FX change) | Agar salary har saal 8% badhti hai to woh ₹5+ cr ka headwind hai jo hamare control mein nahi. Measurement rule pehle fix karna. | Constant prices (salary inflation & FX alag track honge), lekin **volume growth aur new investments include** honge. |
| 3 | Digital growth ka IT cost bhi isi ₹212.5 cr mein fit karna hai? | Agar haan, to savings ko growth headwind bhi cover karna padega. | Haan, include. |
| 4 | Koi **one-time investment budget** available hai? Payback expectation? | Savings ke liye migration cost lagegi. Budget nahi hai to sirf quick wins possible. | Haan, approx ₹40 cr one-time, payback < 2 years acceptable. |
| 5 | **No-go areas** kya hain? (e.g., layoffs, specific vendors, peak season freeze) | Constraints pehle pata ho to galat recommendation nahi doge. | Forced layoffs nahi; festive season (Oct–Dec) mein critical system change freeze. |
| 6 | Kaunse **cost categories ka data** available hai? (GL, contracts, CMDB, cloud bills) | Analysis data pe depend karta hai. | GL by cost centre, contract register (incomplete), ServiceNow CMDB (partial), cloud billing. |
| 7 | **Decision rights** abhi kiske paas hain — group CIO ya division heads? | Agar CIO ke paas power nahi to recommendation implement nahi hogi. Governance issue ka early signal. | Divisions apna IT budget khud control karte hain. |
| 8 | Koi **regulatory/data residency** constraints countries mein? | Centralization aur cloud decisions pe direct impact. | Kuch countries mein personal data / financial records in-country rakhne ki requirement (Legal confirm karega). |
| 9 | Koi **ongoing contracts/renewals** jo lock-in create karte hain? | Bina exit clause ke contract todna mehnga. Savings timing renewal pe depend. | ~60% licence spend agle 18 months mein renew hoga. |
| 10 | Security ka **current posture** kaisa hai? Recent incidents? | Yeh guardrail hai; agar weak hai to reinvestment chahiye. | 2 legacy systems unsupported OS pe; 24x7 monitoring nahi. |

> **Interview tip:** 10 questions mat poochho. Interview mein 3–4 sabse important poochho (1, 2/3, 4, 5) aur baaki ko "assumptions" bolke aage badho.

### 2.3 Information jo already hai vs missing

| Already hai (Facts) | Missing (chahiye) |
|---|---|
| Revenue ₹5,000 cr, IT ₹250 cr | ₹250 cr ka cost-pool breakdown (pehla analysis) |
| 3-yr growth 35% | Growth ke **drivers** (kya badha, kyun) |
| 120 applications | Har app ka cost, usage, owner, health, overlap |
| 3 divisions, 5 countries | Kaun kya decide karta hai (decision rights) |
| Digital growth 25% | Digital growth ka IT capacity impact |
| Target 15% in 18 months | Contract renewal dates, exit clauses, utilization |
| Suspected problems (duplicate apps, cloud waste, expensive vendors, slow decisions) | In suspicions ka **evidence** |

### 2.4 Facts vs Assumptions vs Hypotheses vs Findings — farak samjho

Yeh consulting ka sabse important discipline hai. Galat category mein cheez daali to recommendation weak ho jayegi.

| Type | Matlab | OmniRetail Example |
|---|---|---|
| **Fact** | Verified data, client ne diya ya documents mein hai | IT spend ₹250 cr hai. |
| **Assumption** | Analysis aage badhane ke liye maani gayi cheez; baad mein validate karni hai | Average IT employee cost ₹10 lakh hai. |
| **Hypothesis** | Ek testable guess ki problem kyun hai | "Acquired companies ke duplicate apps cost badha rahe hain." |
| **Finding** | Data se prove/disprove hui baat | "120 mein se 34 apps ka functional overlap hai; inka annual cost ₹X cr hai." |
| **Conclusion / Recommendation** | Findings se nikla action | "CRM-B ko CRM-A mein consolidate karo." |

**Flow:** Fact + Assumption → Hypothesis banao → Data se test karo → Finding → Recommendation.

### 2.5 Initial hypotheses: IT cost kyun badha?

3 saal mein increase = ₹250 − ₹185.2 = **₹64.8 cr**. Hypotheses (baad mein spend analysis se validate):

| # | Hypothesis | Agar sahi hai, to evidence kya dikhega | Est. contribution [ILLUSTRATIVE, to be validated] |
|---|---|---|---|
| H1 | Acquisitions se duplicate apps, DCs, teams aaye aur kabhi consolidate nahi hue | Same capability ke 2–3 apps; 4 DCs; 3 parallel IT teams | ₹25.0 cr |
| H2 | Cloud migration hua lekin on-prem band nahi hua (dual running) + cloud waste | Cloud bill tez badha jabki DC cost flat; idle VMs | ₹15.0 cr |
| H3 | Vendor/contractor sprawl — har division alag vendor, alag rate | 210 vendors, same service ke alag rates | ₹12.0 cr |
| H4 | Legitimate increase — security & compliance (achha kharcha) | New security tools, audit requirements | ₹6.0 cr |
| H5 | Salary inflation | Same headcount, higher cost | ₹6.8 cr |
| | **Total** | | **₹64.8 cr ✔** |

**Insight:** Saara increase "bura" nahi hai. H4 (security) aur H5 (inflation) cut nahi karne. Asli target H1, H2, H3 + baaki inefficiencies (licence waste, weak demand governance) hain.

### 2.6 Pehle kaunse analyses karein aur kyun

| Order | Analysis | Kya milega | Kyun pehle |
|---|---|---|---|
| 1 | **Spend baseline / spend cube** (cost pool × division × country × vendor) | ₹250 cr kahan ja raha hai | Bina baseline ke savings measure hi nahi ho sakte |
| 2 | **3-year variance analysis** | Increase ke drivers (H1–H5 test) | Pata chalega kaunsa hissa addressable hai |
| 3 | **Application inventory** (CMDB + finance + interviews) | 120 apps ka cost, usage, overlap, health | Sabse bada lever yahi hoga |
| 4 | **Cloud & infra utilization** | Idle/oversized resources, DC utilization | Quick wins mil sakte hain |
| 5 | **Contract register + renewal calendar** | Kab kaunsa contract renew, exit clause | Savings timing yahi decide karega |
| 6 | **Demand/project pipeline review** | Duplicate/low-value projects | Future cost ko rokna |
| 7 | **Org & decision-rights interviews** | Kaun kya decide karta hai, duplication | Implementation ke liye zaroori |

> **ServiceNow connection (aapke background se):** Application inventory ke liye ServiceNow CMDB / Application Portfolio Management module ek bada source hota hai. Lekin CMDB aksar incomplete hota hai — isliye finance data (kisko payment ja raha hai) aur interviews se cross-check karna padta hai.

---

# PART 3: MASTER ISSUE TREE

### 3.1 Key Question

> **"How can OmniRetail reduce recurring IT expenditure by 15% (₹37.5 cr) within 18 months while supporting digital growth and maintaining service quality and security?"**

### 3.2 Compact Issue Tree (ASCII)

```
                    +------------------------------------------------------+
                    |  KEY QUESTION: Recurring IT spend -15% (Rs 37.5 cr)  |
                    |  in 18 months, growth + quality + security protected |
                    +--------------------------+---------------------------+
                                               |
        +-----------------------+--------------+--------------+------------------------+
        |                       |                             |                        |
        v                       v                             v                        v
 +--------------+     +-------------------+        +--------------------+     +-------------------+
 | 1. WHERE     |     | 2. WHAT do we     |        | 3. HOW do we       |     | 4. HOW do we      |
 | should IT    |     |  run & what can   |        |  source & buy?     |     |  deliver & track? |
 | money go?    |     |  we remove/reduce?|        |                    |     |                   |
 | (Direction)  |     |  (Cost levers)    |        |  (Sourcing/price)  |     |  (Execution)      |
 +------+-------+     +---------+---------+        +---------+----------+     +---------+---------+
        |                       |                            |                          |
   A. IT strategy &       D. Application               F. Build vs Buy            I. Roadmap, risks
      business               portfolio &               G. Outsourcing &              & benefits
      alignment              rationalization              managed services            tracking
   B. Current vs          E. Infrastructure &          H. Vendor management
      target                 cloud spend                  & procurement
      architecture        C. Operating model,
                             org & governance
                             (people cost +
                              demand control)
```

**Kaise padhein:** 4 buckets → 9 branches (A–I).
- Bucket 1 (A, B) = **Guardrails + direction**: kya protect karna hai, future state kya hai.
- Bucket 2 (C, D, E) = **Volume levers**: kya hata sakte hain / kam use kar sakte hain.
- Bucket 3 (F, G, H) = **Sourcing & price levers**: jo chahiye, use sasta/better kaise lein.
- Bucket 4 (I) = **Execution**: kaise karein, risk kaise control karein, savings kaise prove karein.

**MECE check:** Har rupee ek pool mein hai (Part 0.2), aur har saving ek hi lever ko assign hogi. Order fixed hai:
**ELIMINATE (retire/consolidate) → REDUCE volume (optimize) → RE-PRICE (negotiate) → RE-SOURCE (outsourcing/MS) → AUTOMATE.**
Har agla lever sirf "bache hue" cost base pe chalega. Isse double-counting nahi hoti.

### 3.3 Har branch detail mein

| Branch | Matlab | Issue tree mein kyun | Key questions | Hypothesis | Confirm/Reject karne wala evidence |
|---|---|---|---|---|---|
| **A. IT strategy & alignment** | IT ka paisa business goals ke hisaab se ja raha hai ya nahi | Bina iske hum galat jagah cut kar denge (e.g., digital) | Business priorities kya hain? Spend unse match karta hai? Run vs Change ratio? | "Spend ka bada hissa legacy run pe hai, digital pe kam" | Spend mapped to goals; ~82% run / 18% change [ILLUSTRATIVE] → confirm |
| **B. Architecture** | Systems kaise bane hain, kaise jude hain | Duplicate systems aur integration complexity cost badhati hai | Kitne duplicate platforms? Kitne point-to-point interfaces? Unsupported systems? | "Duplicate platforms + spaghetti integration se cost & risk badhe" | Capability map pe 2–3 apps per capability; 300+ interfaces [ILLUSTRATIVE] |
| **C. Operating model, org, governance** | Log, process, decision rights | Slow decisions, duplicate teams, uncontrolled demand | Kaun decide karta hai? Duplicate roles? Project approval kaise hota hai? | "3 parallel IT teams + weak demand governance" | Org map, role duplication analysis, project pipeline review |
| **D. Application portfolio** | 120 apps ka review & disposition | Sabse bada addressable cost | Kaunse apps duplicate/low value/unhealthy? | "≥25% apps retire/consolidate candidates" | App inventory: cost, usage, overlap, health |
| **E. Infra & cloud** | DCs, servers, cloud, network, devices | Dual running + cloud waste | Utilization kitna? Kitne DCs zaroori? Non-prod 24x7 kyun? | "Cloud ka 20–25% waste; 2 DCs band ho sakte hain" | Cloud utilization data, DC capacity report |
| **F. Build vs Buy** | Naye/replace capabilities kaise source karein | Galat choice = high TCO ya lock-in | Capability differentiating hai ya commodity? 5-yr TCO? | "Commodity capabilities ke liye custom build mehnga pad raha hai" | TCO comparison, market scan |
| **G. Outsourcing & managed services** | Kaunsa kaam bahar, kaunsa andar | Fragmented local vendors costly; core skills andar chahiye | Kya strategic hai? Market mature hai? | "Helpdesk + infra ops consolidate karne se cost & quality better" | Ticket data, vendor SLAs, market RFP responses |
| **H. Vendor & procurement** | Contracts, price, licence utilization | Price aur contract terms se savings | Kaun se contracts renew? Utilization? Benchmarks? | "Licences 15% unused; rates inconsistent" | Licence usage reports, rate card comparison |
| **I. Roadmap & benefits** | Sequencing, risks, KPIs, savings tracking | Bina iske savings sirf paper pe | Dependencies? Quick wins? Kaise measure? | "Savings tracking nahi hai to savings leak hoti hain" | Finance-validated baseline, monthly tracker |

**Double-counting example (yaad rakho):** CRM-B retire kiya → uska licence (₹), hosting (₹), aur vendor support (₹) — teeno **Branch D (App rationalization)** mein count. Fir Branch H (vendor negotiation) sirf **bache hue** contracts pe chalega. Branch E (cloud FinOps) un VMs pe saving claim nahi karega jo CRM-B ke saath delete ho gaye.


---

# PART 4: CASE KO STEP-BY-STEP SOLVE KARNA

Har step mein 6 cheezein: **(1) Kya pata karna hai? (2) Kyun zaroori? (3) Kaunsa data? (4) Kaise analyse? (5) Result ka matlab? (6) Recommendation.**

---

## STEP 1 — IT STRATEGY & BUSINESS ALIGNMENT

### 1.1 Concept simple mein

- **Business strategy** = Company kahan jeetna chahti hai aur kaise (e.g., "online growth + store profitability + customer loyalty").
- **IT strategy** = Technology us business strategy ko kaise support karegi: kaunsi capabilities chahiye, kahan invest karna, kahan cost kam karna, kya risk accept nahi karna.
- **Alignment** = IT ka har bada rupee kisi business goal se juda hona chahiye. Agar paisa aisi cheez pe ja raha hai jo kisi goal ko support nahi karti → misalignment.

> **Analogy:** Business strategy destination hai (Mumbai se Goa jaana). IT strategy gaadi aur route hai. Agar aap truck kharid rahe ho jab bike se kaam chal jaata, ya bina petrol ke Ferrari — dono misaligned.

### 1.2 Six-question analysis

| Q | Answer |
|---|---|
| 1. Kya pata karna hai? | IT spend business priorities ke saath match karta hai ya nahi; kahan over-invest, kahan under-invest. |
| 2. Kyun? | Bina iske hum digital ya security jaise critical areas mein bhi cut kar denge. Alignment batata hai **kya protect karna, kya cut karna**. |
| 3. Data | Business strategy documents, ₹250 cr spend by category, project portfolio (45 projects [ILLUSTRATIVE]), business leaders ke interviews. |
| 4. Analysis | (a) Spend ko "Run" (business chalana) vs "Change/Grow" (naya banana) mein todo. (b) Har project ko business goal se map karo. (c) Value vs cost matrix. |
| 5. Result | ~82% spend (₹205 cr) Run pe, ~18% (₹45 cr) Change pe [ILLUSTRATIVE]. Change budget ka bhi ~30% duplicate/low-value projects pe. Digital ko jitna chahiye utna nahi mil raha. |
| 6. Decision | Run cost kam karo ("Save to Invest"), digital/security protect karo, har naye investment ko business KPI se jodo. |

### 1.3 Business goals → IT capabilities → Initiatives → KPIs

| Business Goal | Required IT Capability | Initiative | KPI |
|---|---|---|---|
| Digital sales +25% (₹1,000 → ₹1,250 cr) | Scalable e-commerce, real-time inventory visibility, personalization | E-commerce modernization; store–online inventory integration; personalization (hybrid build) | Digital revenue; site availability (99.9%+); page load time; conversion rate |
| IT cost −15% (₹37.5 cr) | Lean app portfolio, optimized cloud, strong vendor mgmt | App rationalization; FinOps; vendor consolidation | Recurring IT run-rate; IT spend % revenue; cost per transaction |
| Customer experience | Single customer view, unified loyalty | CRM consolidation (CRM-B → CRM-A); data platform | NPS; repeat purchase rate; click & collect fulfilment time |
| Cybersecurity | IAM, 24x7 monitoring, no unsupported systems | Managed SOC; MFA/PAM; retire unsupported apps | # critical vulnerabilities; % apps with SSO/MFA; mean time to detect |
| Operational reliability | Stable store POS, supply chain systems | POS modernization; WMS replacement; DR testing | POS uptime; incidents per month; stock accuracy |
| Faster decisions / post-merger integration | Clear governance, single ERP | Governance model; Grocery ERP consolidation | Decision cycle time; # ERPs; project approval time |

### 1.4 Prioritization of technology initiatives

Simple **Value vs Effort/Risk** 2x2:

```
              HIGH VALUE
                  |
   +--------------+--------------+
   | BIG BETS     | QUICK WINS   |
   | (plan well)  | (do first)   |
   | - ERP consol.| - Cloud      |
   | - E-com      |   FinOps     |
   |   modernize  | - Licence    |
   | - Mgd svcs   |   harvesting |
   |              | - Retire BI-2|
   +--------------+--------------+  <-- LOW effort/risk on right
   | AVOID/DEFER  | FILL-INS     |
   | - Low-value  | - Device     |
   |   custom     |   lifecycle  |
   |   projects   | - ITSM-2     |
   |              |   consolid.  |
   +--------------+--------------+
              LOW VALUE
   HIGH effort/risk           LOW effort/risk
```

Scoring criteria: business value (revenue/CX), cost saving, risk reduction, effort, dependency. Security/compliance "must-do" items prioritization ke bahar hain — woh hamesha karne hain.

### 1.5 Sabse sasta option hamesha best kyun nahi?

| Cheap option | Hidden problem |
|---|---|
| E-commerce ko cheap shared hosting pe rakhna | Festive peak pe crash → revenue loss (Step 10 mein dekhoge: ₹19,000/minute average) |
| Security monitoring band karna | Ek breach ka cost (fines, reputation, downtime) saalon ki saving kha jaata hai |
| Sabse sasta vendor | Poor SLA, high attrition, knowledge loss |
| Custom build "kyunki apne log free hain" | Internal logon ka bhi cost hai + maintenance forever |

**Rule:** Decision **Total Cost of Ownership (TCO) + business value + risk** pe hota hai, sirf sticker price pe nahi.

---

## STEP 2 — CURRENT VS TARGET ARCHITECTURE

### 2.1 Concept

- **Enterprise architecture** = Company ke saare systems ka "city map" — kaunsa system kya karta hai, data kahan hai, systems kaise baat karte hain, kahan host hain, kaun access kar sakta hai.
- **Current state (As-Is)** = Abhi kaisa hai. **Target state (To-Be)** = Future mein kaisa hona chahiye. **Gap** = Dono ka farak. **Roadmap** = Gap bharne ka plan.

### 2.2 Current-State Architecture (As-Is)

```
 ==========================  CURRENT STATE (AS-IS)  ===========================

 CHANNELS:   [Stores: POS-1 (India/SEA)]  [Stores: POS-ME (UAE/KSA)]  [Website+App]
                  |    \                       |                         |
                  |     \ (nightly batch      | (file transfer)          | (custom code)
                  |      \  files)            |                          |
 ---------------- | ------\------------------ | ------------------------ | -----------
 DIVISION         |  FASHION         |  GROCERY (acquired) |  HOME & ELEC (acquired)
 APPS:            |                  |                     |
           [Group ERP] <---------X---> [Grocery Legacy ERP]   [Group ERP - same]
           [CRM-A SaaS]          |    [ITSM-2]   (X)        [CRM-B custom] (X)
           [ServiceNow ITSM]     |    [BI-2 old reports]    [Old Finance Archive]
           [Legacy WMS] <--------+--> [Legacy HR/Payroll] (shared, unsupported OS)
                  \         \         /         /
                   \  ~300+ POINT-TO-POINT INTERFACES ("spaghetti")  (X)
                    \  no central middleware; failures found late
 ----------------------------------------------------------------------------------
 DATA:  [DB-1] [DB-2] [DB-3] ... customer data in 3 places, stock data in 4 places (X)
        No single customer view; reports don't match
 ----------------------------------------------------------------------------------
 INFRA: [DC-1 India main] [DC-2 Grocery] [DC-3 Middle East colo] [DC-4 India small]
        +  [Public Cloud: e-commerce + some lifted apps, no tagging, 24x7 non-prod] (X)
        Dual running: apps moved to cloud but old servers still on (X)
 ----------------------------------------------------------------------------------
 IDENTITY & SECURITY: 3 separate directories, no SSO for many apps,
        MFA partial, shared admin accounts, no 24x7 monitoring (X)
        2 apps on unsupported OS (Grocery ERP, HR/Payroll) (X)
 ==================================================================================
 (X) = problem area
```

### 2.3 Current architecture ki main problems

| Problem | Example | Impact |
|---|---|---|
| Duplicate systems | 2 ERPs, 2 CRMs, 2 ITSM, 2 BI | Double licence, double support, double skills |
| Disconnected data | Customer data 3 jagah | Personalization nahi, loyalty broken, reports mismatch |
| Integration failures | 300+ point-to-point interfaces, nightly batch | Online stock galat → order cancel → bad CX |
| Legacy systems | Grocery ERP, HR/Payroll on unsupported OS | Security risk, expensive extended support |
| Security risks | No SSO, partial MFA, shared admin accounts | Breach risk, audit findings |
| High maintenance | 4 DCs + cloud dual running | Paying twice for same workload |

### 2.4 Target-State Architecture (To-Be)

```
 ==========================  TARGET STATE (TO-BE)  ============================

 CHANNELS:  [Stores: Cloud-managed POS]  [Website + Mobile App]  [Contact Centre]
                        \                       |                      /
 ------------------------\-----------------------|---------------------/-----------
 EXPERIENCE / API LAYER:   [ API GATEWAY  -  security, throttling, reuse of APIs ]
 ----------------------------------------------|------------------------------------
 INTEGRATION LAYER:        [ INTEGRATION PLATFORM (iPaaS) + EVENT STREAMING ]
                             real-time stock & order events; monitored flows
 ----------------------------------------------|------------------------------------
 CORE PLATFORMS (one per capability):
   [Group ERP]  [CRM-A]  [SaaS WMS]  [SaaS HR/Payroll]  [ServiceNow ITSM]
   [Modernized E-commerce: modular services]  [Personalization & Loyalty (built)]
   [Local fiscal POS add-on for KSA/UAE - kept local for regulation]
 ----------------------------------------------|------------------------------------
 DATA PLATFORM:  [ Single customer view | Inventory data | Analytics/BI (one tool) ]
                 + Data archive (low-cost, read-only) for legal retention
 ----------------------------------------------|------------------------------------
 INFRASTRUCTURE (Hybrid):
   [DC-1 Primary (India)] + [DR site]  +  [Public Cloud Landing Zone]
   + [In-country cloud region for data-residency workloads]
   FinOps: tagging, auto-scheduling, rightsizing, commitments
 -----------------------------------------------------------------------------------
 CROSS-CUTTING (applies to every layer):
   IAM: single directory + SSO + MFA + Privileged Access Mgmt (PAM)
   SECURITY: 24x7 SOC (managed) + SIEM + endpoint protection + WAF + vuln mgmt
   OBSERVABILITY: monitoring & alerting via ITSM;  BACKUP & DR tested twice/yr
 ===================================================================================
```

### 2.5 Har component plain language mein

| Component | Simple explanation |
|---|---|
| **POS (Point of Sale)** | Store ka billing system. Cloud-managed POS = central se update/monitor ho sakta hai, har store mein bada server nahi chahiye. |
| **E-commerce platform** | Website/app ka backend. "Modular services" = alag-alag parts (cart, payment, catalogue) alag scale ho sakte hain. |
| **ERP (Enterprise Resource Planning)** | Finance, purchase, inventory accounting, supply chain ka core system. |
| **CRM (Customer Relationship Management)** | Customer data, loyalty, campaigns, service history. |
| **WMS (Warehouse Management System)** | Warehouse mein stock, picking, packing. |
| **API (Application Programming Interface)** | Do systems ke baat karne ka standard "darwaza". API Gateway = sab darwazon ka ek security guard + traffic controller. |
| **Middleware / Integration platform (iPaaS)** | Systems ko jodne wala central "post office". Point-to-point ki jagah sab ek jagah se jaata hai → monitor karna aasaan. iPaaS = cloud-based integration platform. |
| **Event streaming** | Jaise hi store mein sale hui, "event" turant sab systems ko pata chalta hai (real-time stock). |
| **Data platform** | Saara data ek jagah, clean, ek "truth". Single customer view = ek customer ki poori history ek jagah. |
| **Landing zone** | Cloud mein pre-configured, secure "plot" — networking, security, tagging rules pehle se set. |
| **DR (Disaster Recovery)** | Backup site; primary down ho to business chalta rahe. |
| **IAM (Identity & Access Management)** | Kaun hai (identity) aur kya access kar sakta hai. SSO = ek login sab apps ke liye. MFA = password + OTP. PAM = admin/privileged accounts ka strict control. |
| **SOC (Security Operations Centre)** | 24x7 team jo security alerts monitor karti hai. SIEM = tool jo saare logs collect karke suspicious activity dhundhta hai. |
| **WAF (Web Application Firewall)** | Website ko hacking attacks se bachane wala filter. |
| **FinOps** | Cloud cost ko engineering + finance milke manage karein — kaun kitna use kar raha, waste kahan. |

### 2.6 As-Is vs To-Be vs Gap vs Action

| Area | As-Is | To-Be | Gap | Recommended Action |
|---|---|---|---|---|
| ERP | 2 ERPs (Group + Grocery legacy, unsupported OS) | 1 Group ERP | Grocery on separate, risky ERP | Consolidate Grocery into Group ERP (go-live M15) |
| CRM | CRM-A (SaaS) + CRM-B (custom) | 1 CRM (CRM-A) | Customer data split | Consolidate CRM-B → CRM-A (M9) |
| Store POS | Old POS with in-store servers; ME stores on local fiscal POS | Cloud-managed POS; local fiscal add-on where law requires | Hard to update, server cost | Modernize POS (phased by M12); keep ME fiscal POS local |
| E-commerce | Monolith, scaling hard | Modular, auto-scaling | Can't handle +25% peak efficiently | Modernize (digital budget ₹10 cr, separate) |
| Integration | 300+ point-to-point, batch | API gateway + iPaaS + events | No monitoring, slow | Build integration platform; migrate critical flows first |
| Data | Customer data 3 places | Single customer view | No personalization | Data platform (+₹0.5 cr recurring reinvestment) |
| Infra | 4 DCs + cloud, dual running | 1 DC + DR + cloud landing zone + local region | 2 extra DCs, waste | Close 2 DCs (M12); FinOps |
| IAM | 3 directories, partial MFA | Single directory, SSO, MFA, PAM | Access risk | IAM programme (PAM +₹0.5 cr recurring) |
| Security monitoring | Office-hours only | 24x7 managed SOC | Blind at night | Managed SOC (+₹1.0 cr recurring) |
| ITSM | ServiceNow + ITSM-2 | ServiceNow only | Duplicate | Consolidate ITSM-2 (M6) |

### 2.7 Important principle

> Target architecture **business requirements se** banti hai, fashion se nahi. "Microservices", "AI", "everything on cloud" sirf tab jab koi business problem solve ho. Example: Middle East ka fiscal POS local isliye rakha kyunki local tax compliance chahiye — "standardization" ke naam pe usse hatana business ko risk mein daal dega. Aur Group ERP ko abhi naye version pe migrate nahi kar rahe (18 months mein do bade ERP changes ek saath risky hain) — woh baad ka decision hai.

---

## STEP 3 — IT OPERATING MODEL

### 3.1 Concept: Operating model kya hai?

**IT operating model** = IT department **kaam kaise karta hai** — kaun log, kaunsi skills, kaunse processes, kaunse tools, kaun decide karta hai, kaunsa kaam andar/bahar, business ke saath kaise milke kaam karta hai, performance kaise measure hota hai.

| Cheez | Kya batati hai | Example |
|---|---|---|
| IT strategy | **KYA** karna hai aur **KYUN** | "Digital growth support karo, cost 15% kam karo" |
| Operating model | **KAISE** karna hai | "Product teams, central platforms, federated governance, managed services for helpdesk" |
| Org chart | **KAUN** kisko report karta hai (operating model ka sirf ek hissa) | "CISO reports to CIO" |

> **Analogy:** Restaurant ki strategy = "Fast, affordable North Indian food". Operating model = central kitchen ya har branch mein kitchen? Chef kaun? Vegetables supplier se ya khud? Order kaise flow karega? Org chart sirf yeh batata hai ki manager kaun hai.

### 3.2 Operating model ke components — OmniRetail ka As-Is vs To-Be

| Component | Current problems (As-Is) | Recommended future (To-Be) |
|---|---|---|
| **People & skills** | 3 divisional IT teams, same skills duplicate (3 ERP teams, 3 infra teams); cloud/FinOps/security/data skills kam | Shared platform teams; reskill legacy staff into cloud, data, security; no duplicate skill pools |
| **Processes** | Har division ka alag change, incident, project process | Standard ITIL-based processes on one ServiceNow; one demand intake; one architecture review |
| **Technology platforms** | Duplicate tools | One ITSM, one BI, one collaboration suite, shared cloud landing zone |
| **Roles & accountability** | App owner pata nahi; "IT ka problem hai" mindset | Har app ka business owner + IT product owner; clear RACI |
| **Sourcing** | 210 vendors, local contracts | Strategic partners (4 app vendors, 1 MSP for infra+helpdesk, 1 MSSP for SOC) |
| **Business–IT collaboration** | Business IT ko "order taker" samajhta hai | Business Relationship Managers (BRMs) per division; joint product teams |
| **Delivery** | Project-based; project khatam, team gayab, knowledge gayab | Product-based teams (long-lived) for key areas: Digital Commerce, Store Experience, Supply Chain, Customer & Loyalty, Finance & HR platforms |
| **Operations** | Reactive firefighting; no 24x7 monitoring | Proactive monitoring, automation, SLAs with vendors |
| **Performance management** | Sirf budget track hota hai | KPIs: cost, availability, delivery speed, user satisfaction, security |

### 3.3 Yeh operating model problems kaise solve karta hai

| Problem | Kaise fix hoga |
|---|---|
| **Delays** | Ek demand intake + clear decision thresholds (Step 5) → project approval 10 weeks se ~3 weeks [ILLUSTRATIVE target] |
| **Duplicate work** | Shared platforms + architecture review → koi division naya CRM nahi khareed sakta jab group CRM hai |
| **Unclear ownership** | Har app/platform ka named business owner + product owner; RACI |

---

## STEP 4 — CENTRALIZED VS DECENTRALIZED IT

### 4.1 Teen options

1. **Centralized IT** — Saare IT decisions, budget, teams ek central group IT mein.
2. **Decentralized IT** — Har division/country apna IT khud chalata hai (OmniRetail abhi yahi hai, isliye duplication).
3. **Federated / Hybrid IT** — Kuch cheezein central (standards, security, shared platforms, contracts), kuch local (business-specific features, local compliance).

### 4.2 Comparison

| Criteria | Centralized | Decentralized | Federated/Hybrid |
|---|---|---|---|
| Cost | Lowest (scale, no duplication) | Highest (duplication) | Low–Medium |
| Speed (local changes) | Slow (central queue) | Fast locally | Fast within guardrails |
| Security | Strong, consistent | Weak, inconsistent | Strong (central policy, local execution) |
| Standardization | High | Low | High on platforms, flexible on edge |
| Business flexibility | Low | High | Medium–High |
| Accountability | Clear for IT, weak business ownership | Clear locally, unclear group-wide | Clear if RACI defined |

### 4.3 Recommendation: Federated model

**Kyun:** OmniRetail ka problem decentralization ki duplication hai (cost), lekin full centralization 5 countries ke local regulations aur 3 different businesses (fashion vs grocery vs electronics) ki speed ko maar dega.

| CENTRALIZE (Group IT) | KEEP WITH DIVISIONS / COUNTRIES |
|---|---|
| Architecture standards & approved technology list | Divisional product backlog & feature priorities |
| Cybersecurity policy, IAM, SOC | Local security execution (store devices) within policy |
| Cloud landing zone, DCs, network contracts, FinOps | Division-specific digital features (e.g., grocery slot booking) |
| Core platforms: ERP, CRM, ITSM, data platform | Local regulatory implementation (tax, fiscal POS, e-invoicing) |
| Enterprise vendor contracts (> ₹50 lakh) & licence pool | Small local vendors (< ₹50 lakh) from approved list |
| IT budget consolidation & investment governance | Local store IT support coordination |
| Data standards (customer, product master) | Local language/content, marketing campaigns |

### 4.4 Local regulatory & business needs

- **Data residency:** Kuch countries mein personal data ya financial records ko in-country rakhna pad sakta hai (exact obligations Legal confirm kare — e.g., India ka DPDP Act, Saudi Arabia ka personal data law). Isliye target architecture mein **in-country cloud region** hai, aur Middle East DC band karte waqt workloads wahi ke local cloud region mein jayenge, India mein nahi.
- **Fiscal/tax systems:** Kuch countries mein POS ko local tax authority ke e-invoicing system se integrate karna hota hai → local fiscal add-on rakha.
- **Business differences:** Grocery mein fresh produce ka inventory turnover fast hai; fashion mein seasonal collections. Division product teams yeh nuance handle karenge, platform same rahega.

---

## STEP 5 — IT GOVERNANCE

### 5.1 Simple definition

**Governance** = Kaun decide karega, kis basis pe, kis limit tak, aur kaise check karenge ki decision sahi tha.
**Management** = Decision ko execute karna.

> **Analogy:** Cricket mein governance = rules, umpire, selection committee. Management = captain aur players ka match khelna.

OmniRetail mein governance nahi thi → har division apna app khareedta tha → 120 apps, 210 vendors.

### 5.2 Governance structure

```
                 +---------------------------------------+
                 | Board Audit & Risk Committee          |  (quarterly oversight:
                 | (oversight of tech risk & big spend)  |   security, major risks)
                 +-------------------+-------------------+
                                     |
                 +-------------------v-------------------+
                 | TECHNOLOGY INVESTMENT COUNCIL         |  monthly
                 | Chair: CFO | CIO, 3 Division heads,   |  - Approves > Rs 2 cr
                 | CISO (advisory)                       |  - Portfolio priorities
                 +---+-----------+-----------+-----------+  - Savings tracking
                     |           |           |
       +-------------v--+  +-----v-------+  +v----------------------+
       | ARCHITECTURE   |  | SECURITY &  |  | VENDOR & SOURCING     |
       | REVIEW BOARD   |  | RISK COUNCIL|  | COUNCIL               |
       | Lead: Ent.Arch.|  | Lead: CISO  |  | Lead: Procurement +   |
       | fortnightly    |  | monthly     |  | IT Vendor Mgmt Office |
       | - Standards    |  | - Policies  |  | - Contracts > Rs 50 L |
       | - New tech     |  | - Exceptions|  | - Renewals calendar   |
       +-------+--------+  +------+------+  +-----------+-----------+
               |                  |                     |
       +-------v------------------v---------------------v-----------+
       | VALUE REALIZATION OFFICE / PMO (with Finance)              |
       | - Savings tracker (expected -> validated -> realized)      |
       | - Project status, benefits, KPIs                           |
       +------------------------------------------------------------+
                               |
       Product teams / Division IT / Country IT (execute within guardrails)
```

### 5.3 Decision thresholds (bureaucracy kam rakhne ke liye)

| Investment size | Kaun approve karega | Turnaround target |
|---|---|---|
| < ₹50 lakh, within approved budget & standards | Division head + product owner | 1 week |
| ₹50 lakh – ₹2 cr | CIO + division head (ARB check if new tech) | 2 weeks |
| > ₹2 cr or new platform/vendor | Technology Investment Council | Next monthly meeting (max 4 weeks) |
| Security exception | Business risk owner, with CISO assessment | 2 weeks, time-bound |

### 5.4 Kaun kya decide karta hai

| Role | Decide/own karta hai |
|---|---|
| **CIO** | IT strategy, architecture standards approval, strategic vendors, IT budget execution |
| **Business leaders (division heads)** | Business priorities, business case ownership, app ownership, business risk acceptance |
| **Enterprise architects** | Standards, target architecture, design reviews, reuse |
| **CISO / cybersecurity leaders** | Security policy, risk assessment, security exceptions recommendation, SOC oversight |
| **Product owners** | Backlog prioritization, delivery of product outcomes |
| **Procurement / Vendor mgmt** | Sourcing process, negotiation, contract terms, vendor performance |
| **Finance (CFO)** | Investment approval (big), baseline, savings validation |

### 5.5 RACI matrix — 5 important decisions

**R = Responsible** (kaam karta hai) | **A = Accountable** (final "haan/naa", sirf EK person) | **C = Consulted** (decision se pehle raay li jaati hai, two-way) | **I = Informed** (decision ke baad bataya jaata hai, one-way)

| Decision | CIO | Division head (business) | Ent. Architect | CISO | Product owner | Procurement | CFO/Finance |
|---|---|---|---|---|---|---|---|
| 1. Approve new IT investment > ₹2 cr (e.g., WMS replacement) | C | C | C | C | **R** (business case) | I | **A** (Council chair) |
| 2. Set architecture standard (e.g., "CRM-A is the only CRM") | **A** | C | **R** | C | C | I | I |
| 3. Retire an application (e.g., BI-2) | C | **A** (app's business owner) | C | C (data security) | **R** | I (contract exit) | C (savings) |
| 4. Select/renew strategic vendor (e.g., cloud MSP) | **A** | C | C | C | I | **R** | C |
| 5. Accept security risk exception (e.g., Grocery ERP on unsupported OS till M15) | C | **A** (risk owner) | I | **R** (risk assessment) | I | I | I |

**Examples se samjho:**
- Decision 3 (BI-2 retire): Product owner (R) migration plan banata hai; Fashion division head (A) final sign-off deta hai kyunki reports unke users use karte hain; CISO (C) batata hai data kaise securely delete/archive ho; Finance (C) saving validate karta hai; Procurement (I) ko bataya jaata hai taaki contract renew na ho.
- Decision 5: CISO risk *assess* karta hai lekin *accept* business owner karta hai — kyunki risk business ka hai, IT ka nahi. Isse "security IT ka problem hai" mindset tootta hai.

### 5.6 Controls bina bureaucracy ke

| Practice | Kaise help karta hai |
|---|---|
| Thresholds (5.3) | Chhote decisions fast, bade decisions controlled |
| Pre-approved patterns ("paved road") | Approved cloud services/templates use karo → ARB review skip |
| Time-boxed reviews | ARB 10 working days mein jawab de, warna default approve (low risk cases) |
| One intake form in ServiceNow | Alag-alag emails/forms nahi |
| Exceptions time-bound | Har exception ki expiry date |
| Review outcomes, not every step | Monthly KPI review, har ticket nahi |

---

## STEP 6 — IT ORGANIZATION

### 6.1 Current-state organization

```
                           CEO
          +---------------+---------------+----------------+
          |               |               |                |
    Fashion Div.     Grocery Div.     Home&Elec Div.      CFO
     Head             Head             Head                |
          |               |               |          Group IT (CIO)
     Fashion IT       Grocery IT      H&E IT          80 people
     180 people       170 people      120 people      (infra standards,
     (own ERP team,   (own ERP,       (own CRM-B      few shared services)
      infra, apps)     ITSM-2, DC)     team, infra)
          |               |               |
    5 Country IT managers (100 people) -- report to country business heads
    --------------------------------------------------------------------
    Total = 180 + 170 + 120 + 100 + 80 = 650
    Problems: CIO controls only 80 people; security sits inside infra;
    no Enterprise Architecture; no FinOps; vendor deals done by each division
```

### 6.2 Future-state organization (federated)

```
                               CIO (Group)
                                   |
  +--------+---------+---------+---+-----+----------+----------+-----------+
  |        |         |         |         |          |          |           |
 Enterp. Product &  Platform  CISO    Data &     IT Service  BRMs (3,    IT Vendor
 Archit. Engineer.  & Cloud   (Cyber- Analytics  Mgmt        one per     Mgmt Office
 (stds,  (product   Ops       security, (data    (ServiceNow, division) + IT Finance/
 target  teams:     (DC, cloud, IAM,    platform, helpdesk    business    FinOps &
 arch)   Commerce,  network,  SOC      BI)       vendor mgmt, partner)   Value Office
         Store,     FinOps)   oversight)         SLAs)
         Supply                  ^
         Chain,                  | dotted line to Board Audit & Risk Committee
         Customer,
         Fin&HR)
  Country IT leads (5): local compliance + store support; solid line to CIO,
  dotted line to country business head
```

### 6.3 Roles explained

| Role | Kya karta hai | OmniRetail mein kyun stronger ownership chahiye |
|---|---|---|
| **CIO** | Overall IT strategy, budget, delivery, risk | Abhi sirf 80 logon pe control; savings target ka single owner chahiye |
| **Enterprise Architecture** | Standards, target state, duplicate tech rokna | Abhi exist hi nahi karta → 120 apps ka ek reason |
| **Applications / Engineering** | Build, configure, maintain apps (product teams) | Divisional silos ko product lines mein organize karna |
| **Infrastructure / Cloud Ops** | DCs, cloud, network, uptime, FinOps | Dual running aur cloud waste ka owner nahi tha |
| **Cybersecurity (CISO)** | Policy, IAM, monitoring, incident response | Infra ke andar tha (conflict of interest — jo system chalata hai wahi apni security check kar raha tha) → independent line |
| **Data & Analytics** | Data platform, single customer view, BI | Digital growth/personalization ka foundation |
| **IT Service Management** | Incident, change, request processes, helpdesk vendor | 2 ITSM tools, inconsistent processes |
| **Product managers / BRMs** | Business ki need samajhna, priorities, value | Business–IT gap fill karna |
| **Procurement / Vendor mgmt** | Contracts, negotiation, vendor performance | 210 vendors, koi central view nahi |

### 6.4 Layoffs nahi — pehle evidence

Consultant directly "headcount 20% kaato" nahi bolega. Pehle assessment:

| Assessment | Kya dekhte hain | Example finding [ILLUSTRATIVE] |
|---|---|---|
| **Activity analysis** | Log actually kis kaam pe time lagate hain | 3 ERP support teams = 95 people; consolidated ERP ko ~70 chahiye |
| **Skills inventory** | Kaunsi skills hain vs future mein chahiye | Cloud/security/data skills ki kami: ~30 roles; legacy skills surplus |
| **Duplication** | Same role multiple jagah | 3 infra teams, 3 vendor coordinators |
| **Productivity/demand** | Ticket volume per person, backlog | Grocery IT ticket volume per agent Fashion ka 60% |
| **Operating requirements** | 24x7, peak season, local presence | Store support local chahiye; ME countries mein local leads chahiye |

**Approach:** Natural attrition (assume 12%/yr = ~78 people/yr [ILLUSTRATIVE]) + redeployment + reskilling. Duplicate roles khaali hone pe backfill nahi karna; surplus logon ko cloud/security/data roles mein reskill karna (jo warna bahar se hire karne padte — yeh **cost avoidance** hai, saving nahi). Net reduction target: ~40 positions over 18 months → 40 × ₹10 lakh = **₹4.0 cr** recurring (Step 12, Lever L8).


---

## STEP 7 — APPLICATION RATIONALIZATION (Critical Section)

### 7.1 Concept

**Application rationalization** = Saare applications ka review karke har ek ke liye decide karna: rakho, milao, sudhaaro, badlo, ya band karo. Goal: **kam apps, kam duplication, kam risk, kam cost — business capability same ya better.**

**Application portfolio** = Company ke saare apps ki list (120 apps) jaise investment portfolio — har app ek "investment" hai jiska cost aur value hai.

### 7.2 Six-question analysis

| Q | Answer |
|---|---|
| 1. Kya pata karna? | 120 apps mein se kaunse duplicate, low-value, unhealthy ya risky hain; kya karna hai har ek ke saath. |
| 2. Kyun? | Acquisitions ki wajah se sabse bada waste yahi hai (Hypothesis H1). Har app ke saath licence + hosting + support + skills + security risk aata hai. |
| 3. Data | CMDB/APM (ServiceNow), finance invoices (actual cost), usage logs (logins, transactions), architecture review (health), business owner interviews (value), contract register (exit terms), security scans. |
| 4. Analysis | Har app ko 2 axes pe score: **Business value** (criticality, usage, uniqueness) and **Technical health** (supportability, security, scalability, cost). Fir overlap check. Fir decision tree (7.4). |
| 5. Result | Sample 12 apps se **₹8.4 cr** net recurring; baaki 108 apps se **₹3.6 cr** → total **₹12.0 cr** net recurring. |
| 6. Decision | Waves mein execute karo: quick retirements pehle, bade consolidations baad mein; har retirement ke liye business owner sign-off. |

### 7.3 Five dispositions (simple definitions)

| Disposition | Matlab | Kab |
|---|---|---|
| **Retain** | Jaise hai waise rakho (cost optimize kar sakte ho) | High value + good health + no duplicate |
| **Consolidate** | Iska kaam doosre "strategic" app mein shift karo, yeh band | Duplicate capability hai aur target app requirement meet karta hai |
| **Modernize** | Same app/capability, technology upgrade (cloud, new version, re-architecture) | High value but poor/aging tech; differentiating ya no good market product |
| **Replace** | Naye product (usually SaaS) se badlo | Commodity capability + poor health + good market product available |
| **Retire** | Band karo (data archive kar sakte ho) | Low/no business need ya fully covered by other apps |

### 7.4 Disposition Decision Tree

```
                        +-----------------------------------+
                        | Does any business process or      |
                        | legal/regulatory need still use   |
                        | this app or its data?             |
                        +-----------------+-----------------+
                              NO          |          YES
                 +------------------------+------------------------+
                 v                                                 v
     +-------------------------+                +-------------------------------+
     | Must data be kept for   |                | Does another app already do   |
     | legal/audit reasons?    |                | the same job (overlap)?       |
     +-----+-------------+-----+                +-------+---------------+-------+
        YES|             |NO                       YES  |               | NO
           v             v                              v               v
   +---------------+ +--------+      +-----------------------+  +---------------------+
   | RETIRE app +  | | RETIRE |      | Can the strategic app |  | Is technical health |
   | ARCHIVE data  | +--------+      | meet needs (incl.     |  | OK? (supported,     |
   | (cheap,       |                 | local regulation)?    |  | secure, scalable)   |
   |  read-only)   |                 +-----+-----------+-----+  +-----+---------+-----+
   +---------------+                    YES|           |NO          YES|         |NO
                                           v           v               v         v
                                   +-------------+ +----------+ +-----------+ +------------------+
                                   | CONSOLIDATE | | RETAIN   | | RETAIN    | | Is capability    |
                                   | into        | | for now; | | (optimize | | commodity AND a  |
                                   | strategic   | | fix gap  | |  cost &   | | good market      |
                                   | app         | | or revisit| | contract)| | product exists?  |
                                   +-------------+ +----------+ +-----------+ +----+--------+----+
                                                                                YES|        |NO
                                                                                   v        v
                                                                            +---------+ +-----------+
                                                                            | REPLACE | | MODERNIZE |
                                                                            | (buy)   | | (upgrade/ |
                                                                            +---------+ | re-arch.) |
                                                                                        +-----------+
   Every branch: check business dependencies, contract exit date, data retention, security.
```

### 7.5 Sample inventory: 12 representative apps (out of 120)

**"Annual running cost"** = licence + hosting + external vendor support [ILLUSTRATIVE]. Internal staff cost isme nahi hai (woh Lever L8 operating model mein handle hota hai — double counting se bachne ke liye).

| # | Application | Business purpose | Criticality | Annual cost (₹ cr) | Usage | Technical health | Functional overlap | Security / compliance | Disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Group ERP | Finance, procurement, inventory accounting (Fashion, H&E) | Critical | 12.0 | 4,000 users, daily | Medium (version upgrade needed in 2–3 yrs) | Overlaps #2 | No major issue | **Retain** (strategic platform) |
| 2 | Grocery Legacy ERP | Same as #1 for Grocery | Critical | 3.5 | 600 users, daily | Poor — unsupported OS | High with #1 | Unpatched OS → audit finding | **Consolidate** into #1 |
| 3 | CRM-A (SaaS) | Customer, loyalty, campaigns (Fashion) | High | 4.0 | 900 users, high | Good | Overlaps #4 | Compliant, SSO enabled | **Retain** (strategic CRM) |
| 4 | CRM-B (custom-built) | Customer & warranty (H&E) | High | 1.8 | 250 users | Poor (old framework; only 2 people know code) | High with #3 | No MFA | **Consolidate** into #3 |
| 5 | Store POS (India + SEA) | Billing in ~1,000 stores | Critical | 5.0 | All stores, daily | Medium (in-store servers ageing) | None | Card-payment security scope | **Modernize** (cloud-managed POS) |
| 6 | E-commerce platform | Website/app sales (₹1,000 cr) | Critical | 6.0 | Very high | Medium (monolith, hard to scale) | None | WAF present | **Modernize** (growth enabler) |
| 7 | Legacy WMS | Warehouse operations (3 warehouses) | Critical | 2.5 | 400 users | Poor (vendor ending support) | Partial with ERP inventory | Patch gaps | **Replace** (SaaS WMS) |
| 8 | Legacy HR/Payroll | HR & payroll, 5 countries | High | 2.2 | All employees, monthly | Poor — unsupported OS | None | Employee personal data on unsupported OS | **Replace** (SaaS HR/payroll) |
| 9 | ITSM-2 | IT tickets (Grocery) | Medium | 1.0 | 120 IT staff | OK | Full overlap with ServiceNow | — | **Consolidate** into ServiceNow |
| 10 | BI-2 (old reporting) | 60 legacy reports (25 unused) | Low | 0.8 | 40 users | Poor | Full overlap with Group BI | — | **Retire** (migrate 35 reports) |
| 11 | Legacy Finance Archive | Historical records of acquired company | Low (ops) / High (legal) | 0.9 | ~10 auditor queries/yr | Poor | None | Records must be kept 8 yrs [ILLUSTRATIVE] | **Retire app + archive data** |
| 12 | Festive Campaign Planner | Plans festive promotions | Medium (seasonally high) | 0.4 | 15 users, ~4 campaigns/yr | Good | None | — | **Retain** |
| | **Total sample** | | | **40.1** | | | | | |

Check: 12.0+3.5+4.0+1.8+5.0+6.0+2.5+2.2+1.0+0.8+0.9+0.4 = **40.1** ✔
Disposition count: Retain 3 (#1, #3, #12), Consolidate 3 (#2, #4, #9), Modernize 2 (#5, #6), Replace 2 (#7, #8), Retire 2 (#10, #11).

### 7.6 Har app ka decision logic

1. **Group ERP — Retain:** Sabse zyada users, critical, health theek. Isko "strategic platform" banao jismein doosre ERP consolidate honge. Version upgrade 18 months ke baad plan karo (ek saath do ERP changes = too much risk).
2. **Grocery ERP — Consolidate:** Same capability Group ERP mein hai; unsupported OS ek security/audit risk hai. Lekin sabse complex move — isliye 15 months ka timeline.
3. **CRM-A — Retain:** SaaS, achhi health, SSO, scalable — target CRM.
4. **CRM-B — Consolidate:** Duplicate + key-person risk (sirf 2 log code jaante hain) + no MFA. Warranty process CRM-A mein configure ho sakta hai (fit-gap analysis se confirm).
5. **POS — Modernize:** Capability critical aur zaroori; problem technology (in-store servers) mein hai. Same vendor ka cloud-managed version → central updates, kam on-site support. Middle East stores ka local fiscal POS alag rakha (regulation).
6. **E-commerce — Modernize:** Digital growth ka engine. Iska goal saving nahi, **scalability** hai. Funding digital budget se (₹10 cr one-time, savings business case mein include nahi).
7. **WMS — Replace:** Warehouse management commodity capability hai (competitive advantage nahi), vendor support khatam ho raha hai, achhe SaaS products available → Replace.
8. **HR/Payroll — Replace:** Commodity, unsupported OS pe personal data → high risk. SaaS HR/payroll mein local payroll rules vendor maintain karta hai (Step 8 mein TCO).
9. **ITSM-2 — Consolidate:** ServiceNow already group standard. Ek ITSM = ek process, ek CMDB, ek reporting.
10. **BI-2 — Retire:** 60 mein se 25 reports koi use nahi karta; baaki 35 Group BI mein rebuild.
11. **Finance Archive — Retire + Archive:** App ka daily kaam zero hai, lekin data legal reasons se 8 saal rakhna hai. Mehnga app chalane ki jagah data ko low-cost read-only archive mein daalo, access controls ke saath.
12. **Festive Campaign Planner — Retain:** Sirf 15 users, saal mein 4 baar use — lekin festive season revenue ke liye critical, sasta (₹0.4 cr), health good, koi duplicate nahi. **Low usage ≠ low value.**

### 7.7 Low-usage app ko automatically retire kyun nahi karna chahiye

| Low-usage app type | Kyun zaroori ho sakta hai |
|---|---|
| Seasonal apps (Festive Campaign Planner) | Saal mein kuch din, lekin bada revenue impact |
| Legal/regulatory (Finance Archive, tax reporting) | Usage kam, lekin law requirement; band kiya to penalty |
| Year-end / audit tools | Saal mein ek baar, lekin financial close ke liye zaroori |
| DR / crisis tools | Normal time mein zero usage — emergency mein life-saver |
| Executive decision tools | 5 users, lekin CEO/board decisions |

**Rule:** Usage sirf ek signal hai. Decision = **value + legal need + dependencies + cost + risk**.

### 7.8 Savings calculation — sample actions

Definitions:
- **Gross recurring saving** = App band/badalne se jo annual cost hatega.
- **New recurring cost** = Replacement licences, extra users on target app, archive storage.
- **Net recurring saving** = Gross − New recurring cost.
- **One-time cost** = Migration, implementation, integration changes, testing, training, parallel running, contract termination fees. (Yeh "saving" se minus nahi hota annual mein; alag dikhaya jaata hai.)

| # | Action | Gross recurring | New recurring cost | **Net recurring** | One-time cost | Go-live | Full saving from |
|---|---|---|---|---|---|---|---|
| 2 | Grocery ERP → Group ERP | 3.5 | 0.8 (extra ERP users + support) | **2.7** | 9.0 | M15 | M16 |
| 4 | CRM-B → CRM-A | 1.8 | 0.6 (extra CRM-A licences) | **1.2** | 2.0 | M8 | M9 |
| 5 | POS modernize | 1.0 (store servers + on-site support) | 0.5 (cloud POS subscription uplift) | **0.5** | 4.0 | M12–M13 rollout | M14 |
| 7 | WMS replace (SaaS) | 2.5 | 1.4 (SaaS WMS) | **1.1** | 3.0 | M12 | M13 |
| 8 | HR/Payroll replace (SaaS) | 2.2 | 1.5 (SaaS + admin + integration support) | **0.7** | 2.5 | M12 | M13 |
| 9 | ITSM-2 → ServiceNow | 1.0 | 0.3 (extra ServiceNow fulfiller licences) | **0.7** | 0.8 | M6 | M7 |
| 10 | Retire BI-2 | 0.8 | 0.1 (extra Group BI licences) | **0.7** | 0.3 | M4 | M5 |
| 11 | Retire Finance Archive (+ data archive) | 0.9 | 0.1 (archive storage + read-only access) | **0.8** | 0.4 (incl. ₹0.1 cr termination fee) | M6 | M7 |
| | **Sample total** | **13.7** | **5.3** | **8.4** | **22.0** | | |

Line-by-line check:
- Gross: 3.5+1.8+1.0+2.5+2.2+1.0+0.8+0.9 = **13.7**
- New: 0.8+0.6+0.5+1.4+1.5+0.3+0.1+0.1 = **5.3**
- Net: 13.7 − 5.3 = **8.4** ✔
- One-time: 9.0+2.0+4.0+3.0+2.5+0.8+0.3+0.4 = **22.0** ✔
- Retain apps (#1, #3, #12) aur E-commerce modernize (#6) se is lever mein koi saving claim nahi.

**Grocery ERP one-time ₹9.0 cr ka breakdown [ILLUSTRATIVE]:**

| Item | ₹ cr | Kya hai |
|---|---|---|
| Data migration & cleansing | 2.0 | Masters (vendor, item, customer), open transactions; historical data → archive |
| Configuration & build (grocery processes: fresh produce, weighing) | 3.5 | Group ERP mein grocery-specific processes |
| Integration changes | 1.2 | ~40 interfaces (POS, WMS, banks) ko Group ERP pe repoint |
| Testing (incl. performance) | 1.0 | |
| Training & change management | 0.8 | 600 users |
| Parallel run & hypercare | 0.5 | 1 month parallel run; go-live ke baad 6 weeks extra support |
| **Total** | **9.0** | |

Grocery ERP ki payback: 9.0 ÷ 2.7 = **3.3 years** — long hai. Phir bhi kyun karein? Kyunki (a) unsupported OS ka security risk, (b) single ERP = single financial truth (faster month-end close), (c) future ERP upgrade sirf ek baar karna padega. **Decision sirf payback pe nahi, risk + strategic value pe bhi.**

### 7.9 Hidden factors jo account karne zaroori hain

| Factor | OmniRetail example | Kaise handle |
|---|---|---|
| Replacement licences | CRM-A ke 250 extra users = ₹0.6 cr | "New recurring cost" mein minus kiya |
| Migration & implementation | Grocery ERP ₹9.0 cr | One-time cost |
| Integration changes | ~40 interfaces repoint | One-time; integration platform reuse |
| Data retention | Grocery ERP history, Finance Archive | Low-cost archive (₹0.1 cr/yr) |
| Business dependencies | CRM-B warranty data → service centres use it | Dependency map; process test before switch-off |
| Downtime risk | ERP cutover | Weekend cutover, rollback plan, **no go-live in festive freeze (Oct–Dec)** |
| Contract termination | Archive app: ₹0.1 cr fee; ITSM-2 contract naturally ends M6 | Retire date ko contract end se align karo |

### 7.10 Remaining 108 apps (long tail)

| Step | Number |
|---|---|
| Apps screened | 108 |
| Candidates found (retire 12 + consolidate 13) | 25 apps |
| Their annual running cost | ₹8.0 cr |
| Expected net realization [ILLUSTRATIVE] | 45% (20% goes into replacement licences on target apps; ~25% will be found still needed after deeper review; ~10% contracts can't exit within 18 months → 100 − 20 − 25 − 10 = 45%) |
| Net recurring saving | 8.0 × 45% = **₹3.6 cr** |
| One-time cost | ₹2.5 cr |
| Average full-saving month | M10 |

### 7.11 Lever L1 total — Application Rationalization

| | ₹ cr |
|---|---|
| Sample 12 apps net recurring | 8.4 |
| Long tail net recurring | 3.6 |
| **Total net recurring (L1)** | **12.0** |
| One-time cost (22.0 + 2.5) | **24.5** |

**Cost-pool tagging of L1's ₹12.0 cr net [ILLUSTRATIVE]** (taaki doosre levers isse dobara count na karein):
- Applications & licences pool: −7.0
- Infrastructure & cloud pool: −2.5 (on-prem hosting 1.0 + cloud hosting 1.5)
- Vendors pool (app support contracts): −2.5
- Total = 7.0 + 2.5 + 2.5 = 12.0 ✔

**Validation evidence chahiye:** business owner sign-off on retirement, fit-gap analysis for consolidations, contract exit terms from Legal/Procurement, actual invoices (not CMDB estimates), usage logs over 12 months (seasonality capture karne ke liye).

---

## STEP 8 — BUILD VS BUY

### 8.1 Concept

- **Build** = Apni team (ya contracted developers) se custom software banana. Full control, lekin poori zimmedari bhi.
- **Buy** = Ready-made product (aaj kal mostly SaaS = Software as a Service, subscription pe) lena. Fast, proven, lekin vendor ke roadmap pe depend.
- **Hybrid** = Commodity part kharido, differentiating part khud banao (ya buy platform + build on top).

**Golden rule:** *"Buy for parity, build for differentiation."* Jahan har competitor same kaam karta hai (payroll), wahan khareedo. Jahan aap customers ke saamne alag dikhna chahte ho (personalization), wahan banane pe socho.

### 8.2 Three OmniRetail requirements

| # | Requirement | Type |
|---|---|---|
| R1 | HR & Payroll for 5 countries (replace legacy) | Standard/commodity |
| R2 | Personalized offers & unified loyalty across stores + online | Customer-facing, potentially differentiating |
| R3 | Real-time inventory sync between stores, warehouses and online (for click & collect, accurate online stock) | Specialized integration/automation |

### 8.3 Decision matrix (qualitative)

| Criterion | R1 HR/Payroll | R2 Personalization & Loyalty | R3 Real-time Inventory Sync |
|---|---|---|---|
| Strategic differentiation | Low (every company has payroll) | **High** (how customers experience OmniRetail) | Medium (enables CX, but plumbing) |
| Market availability | High (many mature SaaS) | Medium (loyalty/CDP engines exist; our personalization logic doesn't) | High for integration platforms; flows are company-specific |
| Time to implement | Buy: ~6 months; Build: ~12 months | Buy: fast but generic; Build: slow | Platform buy: fast; flows: medium |
| Customization need | Low–medium (local payroll rules — vendor maintains) | High | High (our systems, our events) |
| TCO | Buy lower (see 8.4) | Hybrid best balance | Hybrid lower than custom point-to-point long-term |
| Internal skills | Low payroll-tech skills | Some digital skills; need data scientists | Integration skills exist (to be strengthened) |
| Security | SaaS vendor certified, but due diligence needed | Customer data → strong controls either way | Central platform = better monitoring |
| Integration | Standard connectors to ERP/IAM | Needs CRM, e-com, POS, data platform | It *is* the integration |
| Vendor lock-in | Medium (exit clause + data export needed) | High if fully bought | Medium (use open API/event standards) |
| Maintenance | Vendor handles statutory updates | Build part = ongoing team | Platform by vendor, flows by us |
| **Recommendation** | **BUY** (SaaS) | **HYBRID** (buy loyalty/CDP engine, build personalization layer) | **HYBRID** (buy integration platform, build flows in-house) |

### 8.4 Worked 5-year TCO — R1 HR/Payroll (Buy vs Build vs Status quo)

**TCO (Total Cost of Ownership)** = Sirf purchase price nahi, 5 saal mein jo bhi kharcha hoga — implementation, licences, internal people, infra, upgrades, integration, migration, exit. Horizon: 5 years from decision. Simplicity ke liye discounting (NPV) skip kiya hai — interview mein bolo ki real case mein NPV bhi dekhenge.

**Assumptions [ILLUSTRATIVE]:**
- Legacy cost: ₹2.2 cr/yr (same as app #8).
- Buy: 6-month implementation; Build: 12-month build. Jab tak naya live nahi, legacy chalta rahega.
- SaaS price locked flat for 5 years via negotiation.

**Option A — BUY (SaaS HR/Payroll)**

| Cost item | Calculation | ₹ cr (5-yr) |
|---|---|---|
| Implementation & configuration | one-time | 2.0 |
| Data migration | one-time | 0.3 |
| Integration (ERP, IAM, banks) | one-time | 0.2 |
| Legacy running during implementation | 0.5 yr × 2.2 | 1.1 |
| SaaS subscription | 5 yrs × 1.2 (paid from signing) | 6.0 |
| Internal admin (2 people) + integration support | 4.5 yrs × 0.3 (after go-live) | 1.35 |
| Upgrades | included in SaaS | 0.0 |
| Infrastructure | vendor-hosted | 0.0 |
| Exit / data extraction provision | one-time at end | 0.3 |
| **Total** | | **11.25** |

**Option B — BUILD (custom on cloud)**

| Cost item | Calculation | ₹ cr (5-yr) |
|---|---|---|
| Development (20 people × 1 yr × ₹12 lakh = 2.4) + design/testing 0.6 | one-time | 3.0 |
| Data migration | one-time | 0.3 |
| Integration | one-time | 0.4 |
| Legacy running during build | 1 yr × 2.2 | 2.2 |
| Infrastructure (cloud hosting) | 4 yrs × 0.3 | 1.2 |
| Maintenance team (8 people × ₹12 lakh ≈ 1.0) | 4 yrs × 1.0 | 4.0 |
| Statutory payroll rule updates, 5 countries | 4 yrs × 0.3 | 1.2 |
| Security testing & compliance | 4 yrs × 0.1 | 0.4 |
| Technology upgrade (year 4) | one-time | 0.5 |
| **Total** | | **13.2** |

**Option C — STATUS QUO (keep legacy)**

| Cost item | ₹ cr (5-yr) |
|---|---|
| Legacy running 5 × 2.2 | 11.0 |
| OS remediation / extended support | 0.8 |
| **Total** | **11.8** + unresolved security risk on personal data |

**Year-wise view:**

| Year | Buy | Build |
|---|---|---|
| Y1 | 2.5 one-time + 1.1 legacy + 1.2 subscription + 0.15 admin = 4.95 | 3.7 one-time + 2.2 legacy = 5.9 |
| Y2 | 1.5 | 1.7 |
| Y3 | 1.5 | 1.7 |
| Y4 | 1.5 | 1.7 + 0.5 upgrade = 2.2 |
| Y5 | 1.5 + 0.3 exit = 1.8 | 1.7 |
| **Total** | **11.25** | **13.2** |

**Result:** Buy (11.25) < Status quo (11.8) < Build (13.2). Buy, Build se **₹1.95 cr** sasta + 6 months faster + statutory updates vendor ki zimmedari.

**Important honest insight:** Buy vs status quo sirf ₹0.55 cr ka farak hai 5 saal mein. Toh asli reason **risk reduction** (unsupported OS pe personal data) aur compliance hai, savings secondary. Steady-state annual: 2.2 − 1.5 = **₹0.7 cr** (yahi number Step 7 mein L1 mein count hua — yahan dobara count nahi hoga).

**Trade-offs / mitigations:**
- Lock-in → contract mein data export format, exit assistance, price cap on renewal.
- Over-customization → "adopt, not adapt" principle; custom changes ARB approval se.
- Local payroll gaps → vendor ke local payroll partners; country-wise fit-gap.

### 8.5 R2 — Personalization & Loyalty: weighted scoring (1 = poor, 5 = excellent)

| Criterion | Weight | Build | Buy | Hybrid |
|---|---|---|---|---|
| Strategic differentiation | 20 | 5 | 2 | 4 |
| Market availability | 5 | 2 | 4 | 4 |
| Time to implement | 10 | 2 | 4 | 3 |
| Customization | 10 | 5 | 2 | 4 |
| TCO | 15 | 2 | 4 | 3 |
| Internal skills fit | 10 | 2 | 4 | 3 |
| Security | 10 | 3 | 4 | 4 |
| Integration | 10 | 3 | 3 | 4 |
| Vendor lock-in (5 = low lock-in) | 5 | 5 | 2 | 3 |
| Maintenance | 5 | 2 | 4 | 3 |
| **Weighted score (÷100)** | 100 | **3.25** | **3.20** | **3.55** |

Calculation (Build): 20×5 + 5×2 + 10×2 + 10×5 + 15×2 + 10×2 + 10×3 + 10×3 + 5×5 + 5×2 = 100+10+20+50+30+20+30+30+25+10 = 325 → 3.25
Buy: 40+20+40+20+60+40+40+30+10+20 = 320 → 3.20
Hybrid: 80+20+30+40+45+30+40+40+15+15 = 355 → 3.55

**Recommendation: Hybrid** — loyalty engine / customer data platform (commodity) buy karo; personalization rules, offer logic, store+online experience (differentiating) in-house product team banaye. Risk: weights subjective hain → sensitivity check karo (agar TCO ka weight 25 kar do to bhi kya Hybrid jeetta hai?). Funding: digital growth budget (savings case mein count nahi).

### 8.6 R3 — Real-time inventory sync

| Option | Pros | Cons |
|---|---|---|
| Build custom point-to-point | Cheap start | 300+ interfaces wali problem aur badhegi; monitoring nahi |
| Buy full order-management suite | Rich features | Bada, mehnga, existing ERP/WMS se overlap |
| **Hybrid: buy integration platform + build flows in-house** | Reusable platform, monitoring, our team owns business logic | Platform subscription; skills build karne honge |

**Recommendation:** Hybrid. Platform (iPaaS + event streaming) target architecture ka hissa hai; flows banana core skill hai — andar rakho. Lock-in kam karne ke liye open API/event standards use karo.

> **Lesson:** Na "always buy" na "always build". Teen requirements, teen alag answers: Buy, Hybrid, Hybrid — har ek ka reason differentiation, market maturity, TCO aur skills se aaya.


---

## STEP 9 — OUTSOURCING

### 9.1 Concept

**Outsourcing** = Koi IT activity ya function external company ko dena (contract ke through) — jaise helpdesk, development, infra operations. Forms: staff augmentation (bahar ke log, aapka control), project outsourcing (fixed scope deliverable), function outsourcing (poora function vendor chalata hai).

**Kyun outsource karte hain:** cost (scale/location advantage), specialized skills, 24x7 coverage, flexibility (demand ke hisaab se up/down).
**Kyun nahi:** strategic control loss, knowledge loss, vendor dependency, data/security risk.

### 9.2 Decision framework

```
                    STRATEGIC IMPORTANCE / SENSITIVITY
                         LOW                     HIGH
                 +-----------------------+-----------------------+
    VENDOR       |  OUTSOURCE / MANAGED  |  OUTSOURCE DELIVERY,  |
    MARKET       |  SERVICE              |  KEEP CONTROL         |
    MATURE       |  (helpdesk, infra ops)|  (SOC monitoring, ERP |
    (HIGH)       |                       |   implementation)     |
                 +-----------------------+-----------------------+
    VENDOR       |  CO-SOURCE / WAIT     |  KEEP IN-HOUSE        |
    MARKET       |  (niche tools; small  |  (core product dev,   |
    IMMATURE     |   scale)              |   strategic arch.)    |
    (LOW)        |                       |                       |
                 +-----------------------+-----------------------+
   Then check: internal capability, cost (TCO incl. vendor mgmt), regulatory constraints.
```

### 9.3 Activity-by-activity assessment

| Activity | Recommendation | Rationale | Key risks | Controls |
|---|---|---|---|---|
| **IT helpdesk** | **Outsource** — consolidate 4 local vendors into 1 managed service (part of L6) | Commodity, mature market, 24x7 & multilingual needed, volume-based | Poor employee experience; vendor doesn't know stores | SLA + user CSAT; knowledge base in **our** ServiceNow; local floor-walkers for stores |
| **Cloud infrastructure operations** | **Managed service** (Step 10) — keep cloud architecture & FinOps in-house | Mature market, 24x7 needed, automation tools vendors already have | Lock-in; vendor optimizes for own revenue | Cloud accounts owned by OmniRetail; FinOps team internal; exit clause |
| **ERP implementation (Grocery consolidation)** | **Outsource delivery** to a systems integrator (project), keep product owner, architect, data owner internal | One-time project; specialized skills not needed after | Scope creep, poor knowledge transfer, over-customization | Milestone-based payments; fit-gap sign-off; internal team shadows; KT before final payment |
| **Cybersecurity monitoring (SOC)** | **Outsource 24x7 monitoring** to managed security provider; keep CISO, policy, risk & incident decisions in-house | Building 24x7 SOC internally needs scarce skills; mature market | Vendor sees sensitive data; slow escalation; alert fatigue | Clear runbooks, escalation SLAs (e.g., critical alert to OmniRetail in 15 min), audit rights, data residency, quarterly drills |
| **Core business product development** (personalization, e-commerce) | **Keep in-house** (augment with contractors under internal leadership) | Differentiating; business knowledge & speed matter; IP should stay | Hiring difficulty, cost | Product teams; contractors max ~30% of team; code ownership internal |
| **Strategic architecture** | **Keep in-house** (advisory OK) | Decides future of whole landscape; vendor conflict of interest (vendor apni product recommend karega) | Skill gap | Hire/develop 4–5 enterprise architects; external advisors for reviews only |

### 9.4 Accountability kabhi outsource nahi hoti

> **Aap kaam (delivery) outsource kar sakte ho, zimmedari (accountability) nahi.**

Agar SOC vendor ne alert miss kiya aur customer data leak hua → regulator, customers aur media **OmniRetail** ko pakdenge, vendor ko nahi. Isliye:
- Risk owner hamesha OmniRetail ka business/CISO rahega.
- Contract mein security obligations, audit rights, breach notification timelines.
- **Vendor risk management:** onboarding se pehle security assessment, annual review.
- Internal team itni skilled rahe ki vendor ko challenge kar sake ("intelligent client" capability).

---

## STEP 10 — MANAGED SERVICES

### 10.1 Managed services vs general outsourcing

| | General outsourcing (e.g., staff augmentation, T&M project) | Managed services |
|---|---|---|
| Kya khareed rahe ho | Logon ka time / effort ya ek project | Ek **chalti hui service ka outcome** |
| Pricing | Per person-day / per project | Per unit (per workload, per ticket, per user) ya fixed + variable |
| Responsibility | Aap manage karte ho logon ko | Provider service ko SLAs ke against chalata hai, apne tools/process se |
| Duration | Often project-based | Ongoing (3–5 years) |
| Example | 10 contract developers for 6 months | "24x7 cloud operations for 1,200 workloads at 99.9% availability" |

> **Analogy:** Driver hire karna (outsourcing — aap batate ho kahan jaana, kab) vs Uber/cab subscription (managed service — aapko bas pahunchna hai; gaadi, driver, maintenance unki zimmedari; late hua to penalty).

### 10.2 Example: Cloud Managed Services Contract (OmniRetail ↔ Cloud MSP) [ILLUSTRATIVE]

**1. Service scope**
- In scope: 24x7 monitoring & operations of public cloud landing zone + DC-1 (primary) + DR site; ~1,200 managed workloads (VMs, containers, databases); OS patching; backup & restore; incident/problem/change execution through **OmniRetail's ServiceNow**; capacity management; infrastructure-as-code maintenance; monthly cost data for FinOps.
- Out of scope: application development, FinOps *decisions* (OmniRetail team), security policy (CISO), cloud consumption bill (OmniRetail pays cloud provider directly — no MSP markup).

**2. Service levels (SLAs)**

| Metric | Target | Measurement |
|---|---|---|
| Availability — Tier-1 services (e-commerce infra, POS cloud backend, ERP) | 99.9% monthly | End-to-end synthetic monitoring, not just server ping |
| Availability — Tier-2 | 99.5% monthly | |
| Availability — Tier-3 | 99.0% monthly | |
| Incident response (acknowledge + start work) | P1: 15 min · P2: 30 min · P3: 4 hrs · P4: 1 business day | ServiceNow timestamps |
| Incident resolution | P1: 4 hrs (95% of incidents) · P2: 8 hrs (95%) · P3: 3 business days (90%) | |
| Critical security patches | Within 7 days (95%) | Vulnerability scanner |
| Backup success | 99% daily; restore test quarterly | |
| Root cause analysis for every P1 | Within 5 business days | |

**3. Security obligations:** Comply with OmniRetail security policy; all admin access via OmniRetail's PAM tool (no shared accounts); background-verified staff; in-country workloads managed only per data-residency rules; security incident notification to OmniRetail within a defined short window (e.g., 2 hours for suspected breach — illustrative); annual independent audit + OmniRetail audit rights.

**4. Reporting & governance:** Real-time dashboard in ServiceNow; monthly service review (SLA, incidents, changes, risks); quarterly business review (improvement plan, automation, cost optimization ideas); annual benchmarking right.

**5. Pricing**
- Per managed workload: ₹4,000/month × 1,200 workloads = ₹48 lakh/month = **₹5.76 cr/yr**
- Fixed service-management fee: ₹6 lakh/month = **₹0.72 cr/yr**
- **Total ≈ ₹6.48 cr ≈ ₹6.5 cr/yr** (vs current infra-ops vendors ₹8.0 cr)
- Volume band ±10% at same price; beyond that, unit price applies (both up and down).
- Productivity commitment: unit price −3%/yr from year 2 (automation benefits shared).
- Rate card fixed for out-of-scope work; any extra charge needs written approval.

**6. Service credits:** Tier-1 availability below target → 5% of monthly fee per 0.1% shortfall (or part thereof), capped at 15%/month. 3 consecutive months of breach → termination right without penalty.

**7. Escalation matrix**

| Level | MSP | OmniRetail | Trigger / time |
|---|---|---|---|
| L1 | Service delivery manager | Head of ITSM | Any SLA risk, immediately |
| L2 | Account head | Head of Platform & Cloud Ops | P1 not resolved in 2 hrs; repeated breach |
| L3 | Regional executive | CIO | P1 > 4 hrs; security incident; 2 months breach |

**8. Exit & knowledge transfer:** Exit plan maintained from Day 1 and updated yearly; 6 months exit assistance at agreed rates; all runbooks, configurations, scripts and documentation stored in **OmniRetail's** repositories/knowledge base; cloud accounts, monitoring tools and licences owned by OmniRetail (or transferable); term 3 years + 2 optional 1-year extensions; no termination fee after year 2 (illustrative negotiated term).

**Combined managed-services lever (L6):** Infra/cloud ops ₹8.0 → ₹6.5 cr + Helpdesk (4 vendors) ₹5.0 → ₹4.0 cr. Gross saving = 1.5 + 1.0 = **₹2.5 cr**. New internal cost: service-integration/vendor management (3 people × ₹10 lakh) = ₹0.3 cr → **Net ₹2.2 cr**. One-time transition (parallel run, knowledge transfer) ₹1.5 cr. Cutover at **M12 — after festive season** (new vendor shadows incumbent during Oct–Dec peak), saving from M13.

### 10.3 SLA — simple numerical example

**SLA (Service Level Agreement)** = Contract mein likha measurable promise — "service itne % time available rahegi, problem itne time mein theek hogi; nahi hua to penalty (service credit)".

**Allowed downtime in a 30-day month:**
- Total minutes = 30 × 24 × 60 = **43,200 minutes**
- 99.9% → allowed downtime = 43,200 × 0.1% = **43.2 minutes**
- 99.95% → 43,200 × 0.05% = **21.6 minutes**
- 99.5% → 43,200 × 0.5% = **216 minutes (3.6 hours)**

**Scenario:** Ek month mein e-commerce infra **90 minutes** down raha.
- Availability = (43,200 − 90) ÷ 43,200 = 43,110 ÷ 43,200 = **99.79%**
- Shortfall vs 99.9% = **0.11%** → "per 0.1% or part thereof" = 2 steps → credit = 2 × 5% = **10%**
- Monthly fee = ₹6.48 cr ÷ 12 = **₹54 lakh** → service credit = **₹5.4 lakh**

**Business impact:**
- Digital sales = ₹1,000 cr/yr. Minutes in a year = 365 × 24 × 60 = 525,600.
- Average revenue per minute = ₹1,000 cr ÷ 525,600 = ₹10,00,00,00,000 ÷ 525,600 ≈ **₹19,000 per minute**
- 90 minutes ≈ **₹17 lakh** revenue at risk (average day; festive peak pe kai guna zyada ho sakta hai)

**Lesson:** Service credit (₹5.4 lakh) business loss (₹17 lakh+) ka chhota hissa hai. **SLA credits insurance nahi hain** — asli protection: achha architecture (redundancy, auto-scaling), DR, peak-season readiness, aur vendor ke saath root-cause fix obligations.

### 10.4 Risks and mitigations

| Risk | Example | Mitigation |
|---|---|---|
| Poor SLA design | Server "up" hai lekin website slow → SLA green, customer unhappy ("watermelon SLA": bahar green, andar red) | End-to-end service availability + user experience metrics (page load, CSAT) |
| Measuring response, not resolution | Vendor 15 min mein "acknowledge" karta hai, theek 2 din mein | Resolution SLAs + P1 RCA obligation |
| Vendor dependency / lock-in | Vendor ke proprietary tools; documentation unke paas | OmniRetail owns accounts, tools, documentation; exit plan from Day 1 |
| Hidden charges | "Out of scope" requests, after-hours premium, cloud resale markup | Clear scope catalogue, fixed rate card, direct cloud billing, monthly invoice review |
| Loss of internal knowledge | 3 saal baad koi andar nahi jaanta systems kaise chalte hain | Retain cloud architects + FinOps internally; quarterly KT sessions; runbooks in our ServiceNow |
| Credits too small to matter | Cap 15% → vendor breach "afford" kar sakta hai | Termination right for repeated breach; earn-back only after sustained performance |

---

## STEP 11 — VENDOR MANAGEMENT

### 11.1 Concept

**Vendor management** = Vendors ko select karna, contracts manage karna, performance track karna, risk control karna, aur relationship se value nikalna — **contract sign hone ke baad bhi**. Procurement = khareedne ka process; vendor management = poora lifecycle.

### 11.2 Vendor analysis for OmniRetail [ILLUSTRATIVE findings]

| Area | Kya dekha | Finding |
|---|---|---|
| **Vendor inventory** | Accounts payable + contract register | 210 IT vendors; third-party IT spend ≈ ₹175 cr (= ₹250 − ₹65 people − ₹10 other); top 20 vendors ≈ 75% (~₹131 cr); ~150 vendors below ₹10 lakh each |
| **Contract review** | Terms, renewal, escalation, exit | 35% contracts auto-renew; 40% have no "termination for convenience"; 3 vendors have 8–10% annual price escalation clauses |
| **Licence utilization** | Usage reports vs licences paid | Productivity suite: 9,000 licences, ~7,650 active (15% unused); premium tier given to everyone; database cores 20% unused (more after DC closure) |
| **Renewal dates** | Renewal calendar | ~60% of licence spend renews within next 18 months → negotiation window |
| **Price benchmarking** | Compare rates across our own vendors, competitive quotes, independent advisors | Same developer role costs vary up to ~1.7x across 6 app vendors (internal comparison) |
| **Duplicate suppliers** | Same service, multiple vendors | 14 app dev/support vendors; 4 helpdesk vendors; 2 infra ops vendors; 3 collaboration tools |
| **Service performance** | SLA reports, incidents, CSAT | Helpdesk CSAT low in Grocery; 2 vendors don't report SLAs at all |
| **Security & compliance** | Vendor risk assessments | 30% of critical vendors never security-assessed; ME infra vendor uses shared admin accounts |
| **Negotiation opportunities** | Volume, renewals, competition | Consolidated volume, multi-year commitments in exchange for price, harvesting before renewal |
| **Vendor consolidation** | Strategic partner model | 14 → 4 app partners; 6 infra/helpdesk vendors → 1 MSP |
| **Exit clauses** | Can we leave? At what cost? | Many contracts silent on data return & exit assistance → add in renewals |

### 11.3 Sample vendor scorecard

Weights: Cost competitiveness 25%, Service performance 25%, Security & compliance 20%, Contract flexibility 15%, Innovation & relationship 15%. Score 1 (poor) – 5 (excellent).

| Vendor [fictional] | Service | Annual spend (₹ cr) | Cost (25) | Performance (25) | Security (20) | Flexibility (15) | Innovation (15) | **Weighted score** | Action |
|---|---|---|---|---|---|---|---|---|---|
| V1 CloudCore | Infra ops (Fashion) | 5.0 | 3 | 4 | 4 | 3 | 3 | **3.45** | Invite to MSP RFP |
| V2 AppServe | App dev/support | 9.0 | 2 | 3 | 3 | 2 | 2 | **2.45** | Renegotiate rate card / consolidate |
| V3 DeskOne | Helpdesk (India) | 2.5 | 3 | 2 | 3 | 3 | 2 | **2.60** | Replace via consolidated MSP |
| V4 SoftSuite | Productivity suite licences | 12.0 | 2 | 4 | 5 | 2 | 4 | **3.40** | Strategic — harvest + tier + renegotiate |
| V5 DataBase Corp | DB & middleware licences | 10.0 | 1 | 4 | 4 | 1 | 2 | **2.50** | Renegotiate (shelfware) after DC plan |
| V6 GulfTech | Infra support (Middle East) | 1.5 | 3 | 3 | 2 | 4 | 2 | **2.80** | Exit as DC-3 closes; fix security gap meanwhile |

Example calc (V1): 0.25×3 + 0.25×4 + 0.20×4 + 0.15×3 + 0.15×3 = 0.75+1.00+0.80+0.45+0.45 = **3.45**

### 11.4 Kise pehle renegotiate karein? (Prioritization)

**Priority = Spend size × Savings potential × Renewal urgency × Our leverage**

| Priority | Vendor | Why first | Renewal |
|---|---|---|---|
| 1 | V4 SoftSuite (₹12 cr) | Biggest spend; 15% unused + over-tiering; renewal soon | M5 |
| 2 | V2 AppServe (₹9 cr) | Rate card well above our other vendors; consolidation leverage | M6 |
| 3 | V5 DataBase Corp (₹10 cr) | Shelfware; but negotiate **after** DC consolidation design so we know true need (dependency) | M7 |
| 4 | V1, V3, V6 + others | Bundle into one MSP RFP (competitive tension) | RFP M4–M8, cutover M12 |

**Leverage tips:** Renewal se 6 months pehle start; usage data ready rakho; credible alternative (RFP) rakho; volume consolidation offer karo; multi-year commitment sirf price caps aur exit rights ke badle.

### 11.5 Vendor savings vs application savings — double counting kaise rokein

**Sequence (Part 3):** Eliminate → Reduce volume → Re-price → Re-source → Automate.

| Example | Kahan count hoga | Kahan NAHI |
|---|---|---|
| CRM-B retire → AppServe ka CRM-B support contract khatam | L1 (App rationalization) | L5 vendor consolidation base se pehle hi minus |
| SoftSuite ke 1,350 unused licences hataye | L4 (Licence optimization — volume) | L5 sirf bache hue licences ke price pe |
| SoftSuite ne bache licences pe 5% kam price diya | L5 (Vendor negotiation — price) | — |
| DB cores shelfware after DC closure | L4 (licences) | L2 (DC lever) sirf facility/hardware/colocation count karta hai |
| SoftSuite ne 8% increase maanga, humne 0% pe lock kiya | **Cost avoidance** — bridge mein nahi | Savings mein nahi (baseline se spend kam nahi hua) |

**L4 Licence optimization (volume) — calculation [ILLUSTRATIVE]:**
- Productivity suite ₹12 cr: harvest 15% unused = 12 × 15% = **₹1.8 cr**; downgrade 30% of remaining users from premium to standard (40% cheaper): 12 × 85% × 30% × 40% = **₹1.2 cr** → **₹3.0 cr**
- DB & middleware ₹10 cr: 20% shelfware cores = **₹2.0 cr** (depends on DC consolidation)
- End-user SaaS sprawl (3 collaboration tools → 1, other duplicates): **₹1.0 cr**
- Gross = 3.0 + 2.0 + 1.0 = **₹6.0 cr**; new cost: software asset management tool + 2 analysts = ₹0.4 cr → **Net L4 = ₹5.6 cr**

**L5 Vendor negotiation (price) — calculation [ILLUSTRATIVE]:**
- Licence base after L1 & L4: 60 − 7.0 − 6.0 = ₹47 cr; renewing within window ≈ ₹30 cr × 5% price improvement = **₹1.5 cr**
- App dev/support services: 25 − 2.5 (already removed via L1) = ₹22.5 cr; minus ₹2.5 cr locked till 2029 = ₹20 cr addressable × 10% (rate-card harmonization + volume consolidation 14 → 4 partners) = **₹2.0 cr**
- **Net L5 = 1.5 + 2.0 = ₹3.5 cr**

**Validation evidence:** signed contracts/amendments, new purchase orders at new price, invoices in finance system.


---

## STEP 12 — IT COST OPTIMIZATION (Sab kuch yahan judta hai)

### 12.1 Concept

**IT cost optimization** ≠ cost cutting. Cost cutting = "har department 15% kaato" (blind). Cost optimization = **waste hatao, value protect karo, savings ko sustainable banao, aur kuch savings growth/security mein reinvest karo**.

Key terms:
- **Recurring (run-rate) saving** = Har saal repeat hone wali kami (e.g., licence band → har saal bachega).
- **One-time cost** = Savings paane ke liye ek baar ka kharcha (migration, transition).
- **Net recurring saving** = Gross recurring saving − naye recurring costs.
- **Exit run-rate** = Month 18 ka monthly spend × 12 (seasonality adjust karke).
- **Cumulative cash saving** = 18 months mein actually kitna paisa bacha (timing pe depend) − one-time costs.
- **Cost avoidance** = Future mein badhne wala kharcha roka (e.g., vendor price increase reject, hardware refresh avoid). Baseline se kam nahi hua, isliye **target ke against count nahi**.

### 12.2 Baseline (₹250 cr) — recap

| Pool | ₹ cr |
|---|---|
| Infrastructure & Cloud | 70 |
| Applications & Licences | 60 |
| People (internal) | 65 |
| Vendors & External Services | 45 |
| Other | 10 |
| **Total** | **250** |

### 12.3 Savings levers — economics

Order: **Eliminate → Reduce volume → Re-price → Re-source → Automate → Organize → Govern demand.** Har lever ka base pichhle levers ke baad ka bacha hua cost hai.

| # | Lever | Current cost base | Root cause | Proposed action | Gross recurring | New recurring cost / overlap adj. | **Net recurring** | One-time cost |
|---|---|---|---|---|---|---|---|---|
| L1 | Application rationalization | 120 apps (sample ₹40.1 cr + long-tail candidates ₹8.0 cr) | Acquisitions; no portfolio governance | Retire/consolidate/replace per Step 7 | 18.9 | −6.9 (replacement licences, extra users, archive) | **12.0** | 24.5 |
| L2 | Infra right-sizing / DC consolidation | On-prem ₹28 cr (DC-2 + DC-3 = ₹8 cr) | Acquired DCs never consolidated; dual running | Close DC-3 (to in-country cloud region, M8) & DC-2 (after Grocery ERP, M16); DC-4 becomes DR | 7.0 (8.0 − 1.0 already in L1) | −3.0 (hosting moved workloads) | **4.0** | 4.5 |
| L3 | Cloud resource optimization (FinOps) | Public cloud ₹30 cr | No tagging/ownership, 24x7 non-prod, oversized VMs, no commitments | Schedule non-prod, rightsize, commitments, storage tiering | 7.0 | −0.4 overlap with L1; −0.8 FinOps tool + team | **5.8** | 0.5 |
| L4 | Licence optimization (volume) | Licences after L1 ≈ ₹53 cr | Shelfware, over-tiering, SaaS sprawl | Harvest, downgrade tiers, remove duplicate end-user tools | 6.0 | −0.4 (asset mgmt tool + 2 analysts) | **5.6** | 0.3 |
| L5 | Vendor negotiation & consolidation (price) | Licence renewals ₹30 cr + addressable services ₹20 cr | Fragmented buying, no benchmarking | Renewal negotiation (5%), 14 → 4 app partners (10%) | 3.5 | 0 | **3.5** | 0.5 |
| L6 | Managed services consolidation | Infra ops ₹8 cr + helpdesk ₹5 cr | 6 local vendors, no scale | 1 MSP (cloud/infra) + consolidated helpdesk | 2.5 | −0.3 (service integration team) | **2.2** | 1.5 |
| L7 | Automation & productivity | New helpdesk contract ₹4.0 cr | ~30% tickets are password/access/how-to | Self-service, virtual agent, auto-remediation (ServiceNow) → 25% fewer tickets | 1.0 | −0.2 (automation licences) | **0.8** | 0.8 |
| L8 | Operating model improvements | People ₹65 cr | 3 parallel IT teams, duplicate roles | Federated model; no backfill of ~40 duplicate roles via attrition; reskill | 4.0 | 0 | **4.0** | 1.5 |
| L9 | Demand & investment governance | Consulting/project services ₹7 cr; 45-project pipeline | No prioritization; duplicate projects | Stop/merge 12 low-value projects; thresholds; budget line permanently reduced | 1.5 | 0 | **1.5** | 0.2 |
| | **Core levers total** | | | | **51.4** | **−12.0** | **39.4** | **34.3** |

Line-by-line check:
- Gross = 18.9 + 7.0 + 7.0 + 6.0 + 3.5 + 2.5 + 1.0 + 4.0 + 1.5 = **51.4**
- Deductions = 6.9 + 3.0 + 1.2 + 0.4 + 0 + 0.3 + 0.2 + 0 + 0 = **12.0**
- Net = 51.4 − 12.0 = **39.4** ✔ (= 12.0+4.0+5.8+5.6+3.5+2.2+0.8+4.0+1.5)
- One-time = 24.5 + 4.5 + 0.5 + 0.3 + 0.5 + 1.5 + 0.8 + 1.5 + 0.2 = **34.3**

**L3 FinOps gross ₹7.0 cr — calculation [ILLUSTRATIVE]:**
- Non-prod ₹8 cr: 50% of non-prod can be scheduled to business hours (60 of 168 hrs/week) → 8 × 50% × (1 − 60/168) = 4 × 0.643 = **₹2.6 cr**
- Prod compute ₹14 cr: 25% oversized by one size (≈ half cost) → 14 × 25% × 50% = **₹1.75 cr**
- Commitment discounts: steady prod compute after rightsizing (14 − 1.75 = 12.25) × 60% committed × 25% discount = **₹1.84 cr**
- Storage ₹5 cr: 20% cold/orphan data, tiering/deleting saves ~80% of its cost → 5 × 20% × 80% = **₹0.8 cr**
- Total ≈ 2.6 + 1.75 + 1.84 + 0.8 = **₹7.0 cr**
- Overlap with L1: retired apps' cloud hosting ₹1.5 cr × ~23% (7.0 ÷ 30) ≈ **₹0.4 cr** → minus (L1 already counted those resources fully)

**L2 DC consolidation:** DC-2 + DC-3 annual cost ₹8.0 cr − ₹1.0 cr hosting of apps retired in L1 = ₹7.0 cr gross; − ₹3.0 cr to host moved workloads in DC-1 / in-country cloud region = **₹4.0 cr net** (DC-3 ₹1.5 cr, DC-2 ₹2.5 cr). Avoided hardware refresh in closed DCs = **cost avoidance**, not counted.

### 12.4 Savings levers — execution

| # | Timeline (full saving from) | Owner | Key risks | KPI |
|---|---|---|---|---|
| L1 | Phased M5 → M16 | CIO + business app owners; EA lead | Business resistance, migration failure, hidden dependencies | # apps (120 → ~90); ₹ run cost of portfolio |
| L2 | DC-3 from M9; DC-2 from M17 | Head of Platform & Cloud Ops | Migration outage; data residency breach | # DCs (4 → 2); ₹ on-prem cost |
| L3 | M4 | FinOps lead | Performance impact from aggressive rightsizing | % tagged spend (target > 95%); cloud cost per order; utilization |
| L4 | M7 (aligned to renewals) | IT Vendor Mgmt Office / SAM lead | Licence audit by vendor; user complaints on downgrade | % licences active; ₹ licence cost |
| L5 | M7 average | Procurement + IT VMO | Vendor pushback, quality drop after rate cut | Price vs previous contract; # vendors (210 → <120) |
| L6 | M13 (cutover M12, after peak) | Head of ITSM + Head of Platform | Transition outage; knowledge loss | SLA attainment; CSAT; cost per ticket |
| L7 | M13 | Head of ITSM | Low adoption of self-service | % tickets self-served; ticket volume |
| L8 | Linear to M18 | CIO + CHRO | Attrition of critical skills; morale | Headcount vs plan; % roles reskilled; critical-skill attrition |
| L9 | M4 | CFO + CIO (Investment Council) | Projects reappear under new names | % spend on approved portfolio; # projects |

**Evidence that would validate each assumption:** L1 — sign-offs, fit-gap, contract exit letters; L2 — migration plan & colocation exit notice; L3 — 3 months of cloud bills post-change; L4 — 90-day usage logs; L5 — signed amendments; L6 — RFP responses (actual bids, not estimates); L7 — ticket categorization of last 12 months; L8 — role-level activity analysis & attrition data; L9 — revised budget with stopped projects removed.

### 12.5 Headwinds (costs that go UP)

| Headwind | Calculation | ₹ cr/yr |
|---|---|---|
| Digital growth: e-commerce cloud | E-commerce cloud ₹10 cr × 25% growth (conservative linear assumption) | +2.5 |
| Reinvestment: managed SOC (24x7) | Security guardrail | +1.0 |
| Reinvestment: PAM/IAM licences | Security guardrail | +0.5 |
| Reinvestment: data platform | Single customer view for digital growth | +0.5 |
| **Total headwinds** | | **+4.5** |

### 12.6 First pass result and the GAP

- 250.0 − 39.4 (core levers) = 210.6
- + 4.5 (headwinds) = **215.1**
- Target = 212.5 → **Gap = 215.1 − 212.5 = ₹2.6 cr** ❌ Target NOT met yet

**Additional options to close the gap:**

| # | Option | Calculation | Net ₹ cr | One-time | Risk | Decision |
|---|---|---|---|---|---|---|
| G1 | End-user device lifecycle 4 → 5 years (non-critical roles) | Devices ₹6 cr/yr; refreshing 1/5 instead of 1/4 of fleet per year = 20% fewer purchases → 6 × 20% | 1.2 | 0.2 (battery/SSD upgrades) | Older devices; security support | **Include** (only devices still receiving security updates) |
| G2 | Store network: MPLS → SD-WAN (managed, over business internet) | Network ₹6 cr × 25% [ILLUSTRATIVE] | 1.5 | 2.0 | Store connectivity outage | **Include** (pilot 50 stores M7–M8, rollout M12–M15 after peak; POS offline mode) |
| P1 | Wave-2 app rationalization | Next 10 candidates | 1.0 | 0.8 | Needs validation | Contingency |
| P2 | E-commerce elasticity (autoscaling + caching) reduces growth headwind | 2.5 → 1.8 | 0.7 | in digital budget | Depends on modernization | Contingency |
| P3 | Backup/storage tiering (Grocery history) | | 0.5 | 0.2 | Low | Contingency |
| P4 | Telecom & misc contract renegotiation ("Other" pool) | | 0.5 | 0.1 | Low | Contingency |
| P5 | Delivery-location mix in app-support contracts | | 1.5 | 0.3 | Quality, time-zone | Contingency |

G1 + G2 = 1.2 + 1.5 = **2.7** > gap 2.6 → include in plan. One-time added = 0.2 + 2.0 = 2.2.
Contingency pipeline (P1–P5) = 1.0+0.7+0.5+0.5+1.5 = **₹4.2 cr** (not in bridge; activated if levers slip).

### 12.7 FINAL SAVINGS BRIDGE (exit run-rate, Month 18)

```
 Rs crore (annual recurring run-rate)
 -----------------------------------------------------------------------
  250.0  ##########################  BASELINE recurring IT spend
  -12.0  L1 Application rationalization ............ = 238.0
   -4.0  L2 DC consolidation / infra right-sizing .. = 234.0
   -5.8  L3 Cloud FinOps ............................ = 228.2
   -5.6  L4 Licence optimization (volume) .......... = 222.6
   -3.5  L5 Vendor negotiation (price) ............. = 219.1
   -2.2  L6 Managed services consolidation ......... = 216.9
   -0.8  L7 Automation .............................. = 216.1
   -4.0  L8 Operating model (attrition, no layoffs)  = 212.1
   -1.5  L9 Demand governance ....................... = 210.6
   +2.5  Headwind: digital growth (cloud) ......... = 213.1
   +2.0  Reinvestment: security + data ............ = 215.1  <- GAP 2.6
   -1.2  G1 Device lifecycle ........................ = 213.9
   -1.5  G2 Store network SD-WAN ................... = 212.4
 -----------------------------------------------------------------------
  212.4  ######################    FINAL RUN-RATE   (target 212.5)
         Net reduction = 250.0 - 212.4 = 37.6 cr = 15.04%  -> TARGET MET
         Buffer = 37.6 - 37.5 = 0.1 cr (VERY THIN -> contingency 4.2 cr)
 -----------------------------------------------------------------------
```

Math: Total savings = 39.4 + 2.7 = 42.1; minus headwinds 4.5 = **37.6**; 37.6 ÷ 250 = **15.04%**.

### 12.8 Double-counting check — pool-level reconciliation

Har lever ko uske cost pool mein tag kiya. Agar pool-wise final numbers ka total bridge ke final (212.4) se match kare → koi double counting nahi.

| Pool | Baseline | Changes | Final |
|---|---|---|---|
| Infra & Cloud | 70.0 | L1 −2.5, L2 −4.0, L3 −5.8, growth +2.5, data platform +0.5, G1 −1.2, G2 −1.5 | **58.0** |
| Apps & Licences | 60.0 | L1 −7.0, L4 −5.6, L5 −1.5, PAM +0.5 | **46.4** |
| People | 65.0 | L8 −4.0 | **61.0** |
| Vendors & Services | 45.0 | L1 −2.5, L5 −2.0, L6 −2.2, L7 −0.8, L9 −1.5, managed SOC +1.0 | **37.0** |
| Other | 10.0 | — | **10.0** |
| **Total** | **250.0** | | **212.4** ✔ |

(Note: small cross-pool items like FinOps analysts or automation licences are netted inside their own lever for simplicity.)

**Double-counting rules applied:**
1. Retired app ka licence + hosting + support → sirf L1.
2. DC lever (L2) se retired apps ki hosting (₹1.0 cr) minus.
3. FinOps (L3) se retired apps ke cloud resources ki savings (₹0.4 cr) minus.
4. Licence volume (L4) pehle, price (L5) baad mein — sirf bache hue base pe.
5. Managed services (L6) price/scale; automation (L7) sirf ticket volume — naye contract base pe.
6. Internal staff savings sirf L8 mein (apps ke internal support staff bhi yahin).
7. Cost avoidance (hardware refresh avoided ~₹6 cr, vendor price increase avoided, 30 digital roles filled by reskilling instead of hiring) **bridge mein nahi**.

### 12.9 Run-rate vs cumulative cash (18 months)

**Run-rate at Month 18 = ₹37.6 cr/yr** — lekin 18 months mein actually kitna cash bacha?

Calendar [ILLUSTRATIVE]: M1 = Feb 2027 → M18 = Jul 2028. **Festive change freeze: Oct–Dec 2027 = M9–M11** (no critical go-lives).

Formula: Cumulative saving = Annual net saving × (months of full saving within 18 months ÷ 12)

| Lever | Net annual | Full saving from | Months in window | Cumulative (₹ cr) |
|---|---|---|---|---|
| L1 (per-app, see below) | 12.0 | M5–M16 | various | 7.8 |
| L2 | 4.0 (DC-3 1.5 from M9; DC-2 2.5 from M17) | | 10 & 2 | 1.5×10/12 + 2.5×2/12 = 1.25 + 0.42 = 1.7 |
| L3 | 5.8 | M4 | 15 | 7.3 |
| L4 | 5.6 | M7 | 12 | 5.6 |
| L5 | 3.5 | M7 | 12 | 3.5 |
| L6 | 2.2 | M13 | 6 | 1.1 |
| L7 | 0.8 | M13 | 6 | 0.4 |
| L8 | 4.0 | linear ramp to M18 | avg ~9.5 | 3.2 |
| L9 | 1.5 | M4 | 15 | 1.9 |
| G1 | 1.2 | M7 | 12 | 1.2 |
| G2 | 1.5 | M16 | 3 | 0.4 |
| **Gross savings in window** | | | | **34.1** |
| Headwind: growth (ramps to 2.5 by M12) | | | | −2.6 |
| Reinvestment 2.0 from M4 | | | 15 | −2.5 |
| **Net recurring benefit in window** | | | | **29.0** |
| One-time costs (34.3 core + 2.2 G1/G2 + 3.0 programme mgmt & contingency) | | | | **−39.5** |
| **Cumulative cash impact (18 months)** | | | | **≈ −10.5** |

L1 per-app (months in window): BI-2 0.7×14/12 = 0.82 · ITSM-2 0.7×12/12 = 0.70 · Archive 0.8×12/12 = 0.80 · CRM-B 1.2×10/12 = 1.00 · HR 0.7×6/12 = 0.35 · WMS 1.1×6/12 = 0.55 · POS 0.5×5/12 = 0.21 · ERP 2.7×3/12 = 0.68 · Long tail 3.6×9/12 = 2.70 → **7.8**
L8 ramp: run-rate grows linearly to 4.0 by M18 → (4.0/12) × (1+2+…+18)/18 = 0.333 × 171/18 = 0.333 × 9.5 ≈ **3.2**
Growth headwind: ramps to 2.5 over 12 months, then flat 6 months → (2.5/12)×(78/12) + 2.5×6/12 = 1.35 + 1.25 ≈ **2.6**

**Interpretation:**
- Run-rate target (₹37.6 cr/yr from M18) **met**.
- But 18 months ke andar cash **−₹10.5 cr** (investment phase). Monthly net benefit after M18 = 37.6 ÷ 12 = ₹3.13 cr → 10.5 ÷ 3.13 ≈ 3.4 months → **cash break-even ≈ Month 22**.
- CEO/CFO ko yeh clearly batana: "Savings ka paisa pehle lagana padega; Month 22 ke baad har saal ~₹37.6 cr bachenge."

### 12.10 Risk-adjusted view (honesty check)

Har lever ki confidence alag hai [ILLUSTRATIVE weights]:

| Confidence | Levers | Net ₹ cr | Weight | Risk-adjusted |
|---|---|---|---|---|
| High (data-driven, low dependency) | L3, L4, L9 | 12.9 | 95% | 12.3 |
| Medium | L2, L5, L6, L7, L8, G1 | 15.7 | 85% | 13.3 |
| Lower (complex migrations) | L1, G2 | 13.5 | 75% | 10.1 |
| **Total** | | **42.1** | | **35.7** |
| Less headwinds | | | | −4.5 |
| **Risk-adjusted net** | | | | **31.2 (12.5%)** |
| + Contingency pipeline 4.2 × 70% | | | | +2.9 |
| **Risk-adjusted incl. pipeline** | | | | **≈ 34.2 (13.7%)** |

**Message to CEO:** "Expected case 15.0% deliver karta hai, lekin buffer bahut thin hai. Risk-adjusted 12.5–13.7%. Hum monthly track karenge, contingency levers ready rakhenge, aur agar Month 9 tak validated savings plan se 10% peeche hain to contingency activate karenge ya aapse additional levers (e.g., deeper sourcing change) pe decision lenge." — **Target achieved claim tabhi jab bridge numerically dikhaye; risk bhi saath mein batao.**

### 12.11 Expected vs Validated vs Realized savings

| Stage | Matlab | Evidence | OmniRetail example |
|---|---|---|---|
| **Expected (identified)** | Analysis se estimate | Data analysis, assumptions | "BI-2 retire karne se ₹0.7 cr bachega" |
| **Validated (committed)** | Owner + Finance ne confirm kiya; action decided/signed | Business sign-off, signed contract, Finance-agreed baseline | Fashion head ne BI-2 retirement approve kiya; vendor ko termination notice gaya |
| **Realized (banked)** | Actual spend mein dikh raha hai | GL/invoices; budget line reduced | M5 se BI-2 invoices band; FY budget ₹0.7 cr kam |

Savings tracker mein har lever in teen stages se guzarta hai. CEO ko "realized" number pe trust hota hai.

---

## STEP 13 — 18-MONTH TRANSFORMATION ROADMAP

**Calendar [ILLUSTRATIVE]:** M1 = Feb 2027 · Festive freeze M9–M11 (Oct–Dec 2027) · M18 = Jul 2028.

```
 Month:   1   2   3 | 4   5   6 | 7   8   9  10  11  12 | 13  14  15  16  17  18
          [Day 1-30]
          [-- Days 31-90 --]
                     [-- M4-6 --]
                                 [------ M7-12 --------]
                                             [FREEZE ]
                                                         [------ M13-18 -------]
 Governance  ####################################################################
 FinOps        ######  (savings from M4) ...............................
 App ration.         BI-2 X    ITSM-2/Archive X  CRM-B X        HR,WMS X  POS X  ERP X
 Vendors              V4  V2  V5 renewals ......
 DC consol.                 DC-3 migrate -> close M8 ...................... DC-2 close M16
 Sourcing          RFP M4 -------- select M8 -- shadow M9-11 -- cutover M12
 Org model          design ----- live M6 -- attrition-based ramp ------------------->
 SD-WAN                             pilot M7-8              rollout M12-15
 Security    (no cuts) managed SOC from M4; IAM/PAM rollout ..........................
```

### Phase 1 — First 30 days: Mobilize & stop the bleeding

| Element | Details |
|---|---|
| Key actions | Set up Value Realization Office (with Finance); validate ₹250 cr baseline by pool; charter Technology Investment Council & thresholds; **moratorium on new apps/vendors without architecture review**; quick FinOps (non-prod scheduling, orphan cleanup, tagging policy); build contract renewal calendar; start app inventory data collection; define "no-cut" security list |
| Dependencies | CEO mandate; Finance data access; CMDB + invoices |
| Owner | CIO (programme sponsor), CFO (baseline), Transformation lead |
| Deliverables | Validated baseline; governance charter; savings tracker; renewal calendar; communication plan |
| Risks | Divisions resist central control; data gaps |
| KPIs | Baseline signed off; % cloud spend tagged; # purchase requests through new governance |
| Savings / benefits | ~₹1.5 cr run-rate initiated (FinOps scheduling); spending discipline from Day 1 |

### Phase 2 — Days 31–90: Diagnose & decide

| Element | Details |
|---|---|
| Key actions | Complete 120-app assessment & dispositions (business sign-offs); FinOps rightsizing + commitments; stop/merge 12 low-value projects; DC consolidation design (incl. data residency); vendor wave-1 prep (V4, V2, V5); federated org & RACI design; launch MSP & SOC RFPs (M4); target architecture v1 |
| Dependencies | Phase 1 baseline; business owner availability; Legal on data residency |
| Owner | EA lead (apps & architecture), FinOps lead, Procurement, CIO + CHRO (org) |
| Deliverables | App disposition list with business case; target architecture; org design; RFPs issued; updated savings plan by lever |
| Risks | Analysis paralysis; politics on which CRM/ERP "wins" |
| KPIs | % apps with approved disposition; L3 savings in cloud bill; # projects stopped |
| Savings / benefits | L3 (5.8) + L9 (1.5) actioned → **~₹7.3 cr run-rate** from M4 |

### Phase 3 — Months 4–6: Quick wins & foundations

| Element | Details |
|---|---|
| Key actions | Retire BI-2 (M4); consolidate ITSM-2 into ServiceNow (M6); retire Finance Archive with data archive (M6); renegotiate V4 (M5) & V2 (M6); licence harvesting & tier downgrades; managed SOC live (M4); select HR SaaS & SaaS WMS (contract M6); start CRM-B migration; DC-3 migration to in-country cloud region; new IT org live (M6) with BRMs, EA team, independent CISO line |
| Dependencies | Dispositions approved; renewal dates; RFP evaluations |
| Owner | Product owners (retirements), IT VMO, CISO, CIO |
| Deliverables | 3 apps retired; signed renewals; managed SOC operational; new org announced |
| Risks | Reports missing after BI-2 retire; user pushback on licence downgrades |
| KPIs | Apps retired; licence utilization %; SOC mean time to detect; vendor count |
| Savings / benefits | Actions done for **~₹19.8 cr gross run-rate** (realized from M7: L3, L9, BI-2, ITSM-2, Archive, L4, L5, G1) |

### Phase 4 — Months 7–12: Scale & transition (protect the festive season)

| Element | Details |
|---|---|
| Key actions | V5 renegotiation (M7, after DC design); device lifecycle policy effective M7 (approved M6); SD-WAN pilot 50 stores (M7–M8); **CRM-B go-live M8** (before freeze); **DC-3 closed M8**; long-tail retirements; MSP selected (M8), **shadows incumbent during freeze M9–M11**; **freeze M9–M11** — no critical changes; **MSP cutover, HR SaaS & SaaS WMS go-live in M12** (after peak); POS rollout starts M12; integration platform live for inventory sync |
| Dependencies | Phase 3 contracts; freeze calendar; data migration readiness |
| Owner | Head of Platform & Cloud Ops, Head of ITSM, product owners, CHRO (HR system) |
| Deliverables | CRM consolidated; 1 DC closed; MSP transitioned; HR & WMS live |
| Risks | Peak-season outages; transition knowledge loss; payroll errors at go-live |
| KPIs | E-commerce availability during peak (≥ 99.9%); payroll accuracy; SLA attainment; CSAT |
| Savings / benefits | **~₹33.6 cr gross run-rate** actioned by M12 (net of ₹4.5 cr headwinds ≈ ₹29.1 cr) |

### Phase 5 — Months 13–18: Complete big moves & embed

| Element | Details |
|---|---|
| Key actions | Automation (self-service, virtual agent) on new helpdesk (M13); POS rollout complete (M13); SD-WAN rollout complete (M15); **Grocery ERP → Group ERP go-live M15**; DC-2 closed M16; wave-2 app candidates assessed (contingency); Finance validates M18 exit run-rate; handover to BAU governance (quarterly portfolio review, FinOps, vendor reviews) |
| Dependencies | ERP data migration; integration platform; DC-2 depends on ERP retirement |
| Owner | CIO, Group ERP product owner, CFO (validation) |
| Deliverables | Single ERP; 2 DCs (primary + DR); validated run-rate report; continuous improvement plan |
| Risks | ERP cutover issues; slippage pushing DC-2 savings beyond M18 |
| KPIs | # ERPs = 1; # DCs = 2; exit run-rate ≤ ₹212.5 cr; month-end close time |
| Savings / benefits | **₹42.1 cr gross − ₹4.5 cr headwinds = ₹37.6 cr net run-rate** at M18 |

### How everything fits together

```
 TARGET ARCHITECTURE  --> tells us WHICH apps/DCs survive (Steps 2, 7)
 OPERATING MODEL      --> tells us WHO runs them and HOW (Steps 3, 4, 6)
 GOVERNANCE           --> ensures new waste doesn't come back (Step 5)
 APP RATIONALIZATION  --> biggest single lever (Step 7)
 BUILD vs BUY         --> how replacements are sourced (Step 8)
 SOURCING / MS        --> who delivers commodity services (Steps 9, 10)
 VENDOR MGMT          --> what we pay & on what terms (Step 11)
 COST OPTIMIZATION    --> adds it all up, without double counting (Step 12)
 ROADMAP              --> sequences it safely, tracks benefits (Step 13)
```


---

# PART 5: FINAL RECOMMENDATION (CEO ke saamne — interview-ready)

### 1. Our recommendation

> "Hum recommend karte hain ki OmniRetail ek **18-month 'Simplify, Optimize, Reinvest' IT transformation** kare: duplicate applications aur data centres hatao, cloud aur licences ko optimize karo, vendors aur sourcing consolidate karo, aur ek **federated IT operating model** with strong governance lagao — taaki savings permanent rahein. Isse **₹37.6 crore annual recurring reduction (15.04%)** milta hai, jabki ₹4.5 crore digital growth aur security mein reinvest hota hai."

### 2. Supporting actions (5)

1. **Simplify the portfolio:** 120 → ~90 apps; 2 ERPs → 1, 2 CRMs → 1, 2 ITSM → 1; 4 DCs → 2 (L1 + L2 = ₹16.0 cr).
2. **Optimize consumption:** Cloud FinOps + licence harvesting + device lifecycle (L3 + L4 + G1 = ₹12.6 cr).
3. **Re-source and re-price:** Vendor consolidation (210 → <120), renegotiation, one MSP for infra + helpdesk, automation, SD-WAN (L5 + L6 + L7 + G2 = ₹8.0 cr).
4. **Federated operating model & governance:** Central platforms/standards/security; divisions own product priorities; attrition-based de-duplication, no forced layoffs; demand governance (L8 + L9 = ₹5.5 cr).
5. **Protect & reinvest:** Managed 24x7 SOC, IAM/PAM, data platform, e-commerce scalability (−₹4.5 cr headwinds absorbed).

Check: 16.0 + 12.6 + 8.0 + 5.5 = 42.1; − 4.5 = **37.6** ✔

### 3. Expected recurring annual savings — exact calculation

| | ₹ cr |
|---|---|
| Baseline | 250.0 |
| Core levers L1–L9 | −39.4 |
| Gap closers G1–G2 | −2.7 |
| Digital growth headwind | +2.5 |
| Security & data reinvestment | +2.0 |
| **Exit run-rate (M18)** | **212.4** |
| **Reduction** | **37.6 = 15.04%** (target 37.5 ✔; buffer 0.1) |

### 4. One-time investment
**₹39.5 cr** (core levers 34.3 + G1/G2 2.2 + programme management & contingency 3.0). E-commerce modernization (₹10 cr) is funded separately from the digital growth budget.

### 5. Timeline
- Day 90: ~₹7.3 cr run-rate actioned (FinOps, demand governance)
- Month 6: ~₹19.8 cr gross actioned
- Month 12: ~₹33.6 cr gross (≈ ₹29.1 cr net of headwinds), festive season protected
- Month 18: **₹37.6 cr net run-rate**; cumulative cash ≈ −₹10.5 cr; **cash break-even ≈ Month 22**

### 6. Business benefits beyond cost
- Digital growth to ₹1,250 cr supported with scalable e-commerce and real-time inventory (fewer cancelled orders, click & collect)
- Single customer view → personalization & unified loyalty
- Security: unsupported systems removed, 24x7 monitoring, MFA/PAM
- Faster decisions (approval cycle weeks instead of months), single financial truth (one ERP)
- Lower complexity = faster future change

### 7. Major risks & mitigations

| Risk | Mitigation |
|---|---|
| Thin buffer (₹0.1 cr); risk-adjusted ~12.5–13.7% | ₹4.2 cr contingency pipeline; monthly tracker; trigger at M9 if validated savings < 90% of plan |
| ERP consolidation slips → DC-2 & ERP savings (₹5.2 cr) slip past M18 | Dedicated SI with milestone payments; early data migration; go/no-go gates |
| Peak-season outage during changes | Change freeze M9–M11; MSP shadowing; rollback plans |
| Business resistance to retirement | Business owners accountable (RACI); savings shown in their P&L |
| Knowledge loss through outsourcing | Intelligent-client team retained; documentation owned by OmniRetail; exit clauses |
| Critical-skill attrition | Reskilling, retention for key roles, no forced layoffs |
| Savings leakage (cost creeps back) | Governance thresholds, FinOps, vendor management office, quarterly portfolio review |

### 8. KPIs to track

| Category | KPI |
|---|---|
| Cost | Recurring IT run-rate (₹212.5 cr target); IT spend % revenue (5.0% → ~4.3% at flat revenue); cloud cost per online order |
| Savings | Expected vs validated vs realized (₹ cr) by lever |
| Portfolio | # apps, # ERPs/CRMs, # DCs, # vendors |
| Reliability | Tier-1 availability; P1 incidents; MTTR (mean time to restore) |
| Security | Unsupported systems count; % apps with SSO/MFA; mean time to detect |
| Growth/CX | Digital revenue; conversion; order cancellation due to stock errors; NPS |
| People | Critical-skill attrition; % staff reskilled; employee CSAT with IT |

---

# PART 6: ONE MASTER REVISION FLOWCHART

Poore Module 4 ko 3 connected flowcharts mein dekho: **A → B → C**, aur feedback loops wapas upar jaate hain.

### Flowchart A — Strategy & Architecture

```
+=====================================================================+
|                    A. STRATEGY & ARCHITECTURE                       |
+=====================================================================+

  +-------------------------------+
  | BUSINESS GOALS                |  Digital +25%, cost -15%, CX,
  | (what the business needs)     |  security, reliability
  +---------------+---------------+
                  |
                  v
  +-------------------------------+
  | [1] IT STRATEGY & ALIGNMENT   |  Map spend to goals; Run vs Change;
  |  "Where should IT money go?"  |  protect (digital, security), cut (waste)
  +---------------+---------------+
                  |
                  v
  +-------------------------------+
  | CURRENT-STATE ASSESSMENT      |  Spend baseline (Rs 250 cr by pool),
  | (facts, not opinions)         |  3-yr drivers, app inventory, infra,
  |                               |  contracts, org & decision rights
  +---------------+---------------+
                  |
                  v
  +-------------------------------+
  | [2] TARGET ARCHITECTURE       |  One platform per capability, API +
  |     & GAP ANALYSIS            |  integration layer, data platform,
  |  "What should the future      |  hybrid infra, IAM + SOC
  |   landscape look like?"       |  As-Is -> To-Be -> Gap -> Action
  +---------------+---------------+
                  |
                  +-----------------------> to Flowchart B
```

### Flowchart B — Operating Model & Sourcing

```
+=====================================================================+
|                 B. OPERATING MODEL & SOURCING                       |
+=====================================================================+
  from A (target architecture + gaps)
                  |
                  v
  +-------------------------------+
  | [3] IT OPERATING MODEL        |  People, process, technology, sourcing,
  |  "HOW will IT work?"          |  business-IT collaboration, delivery
  +---------------+---------------+
                  |
                  v
  +-------------------------------+
  | [4] CENTRALIZED vs            |  Choose FEDERATED: central standards,
  |     DECENTRALIZED             |  security, platforms, contracts;
  |  "WHERE are decisions made?"  |  local products & regulation
  +---------------+---------------+
                  |
                  v
  +-------------------------------+      +----------------------------+
  | [5] GOVERNANCE                |----->| [6] IT ORGANIZATION        |
  |  "WHO decides, with what      |      |  "WHO sits where?"         |
  |   thresholds?" RACI, councils |      |  CIO, EA, CISO, product,   |
  +---------------+---------------+      |  platform, BRMs, VMO       |
                  |                      +-------------+--------------+
                  v                                    |
  +-------------------------------+                    |
  | [7] APPLICATION PORTFOLIO     |<-------------------+
  |     RATIONALIZATION           |  Retain / Consolidate / Modernize /
  |  "WHAT do we keep?"           |  Replace / Retire (decision tree)
  +---------------+---------------+
                  |  for every Replace / Modernize / new need
                  v
  +-------------------------------+
  | [8] BUILD vs BUY              |  Differentiating -> build/hybrid
  |  "HOW do we get it?"          |  Commodity -> buy;  5-yr TCO
  +---------------+---------------+
                  |  who delivers & runs it?
                  v
  +-------------------------------+      +----------------------------+
  | [9] OUTSOURCING               |----->| [10] MANAGED SERVICES      |
  |  "In-house or external?"      |      |  outcome-based, SLAs,      |
  |  Keep strategic; outsource    |      |  pricing, exit clauses     |
  |  commodity; keep accountability|     +-------------+--------------+
  +---------------+---------------+                    |
                  |                                    |
                  v                                    v
  +-------------------------------------------------------------+
  | [11] VENDOR MANAGEMENT                                       |
  |  inventory, contracts, utilization, renewals, benchmarks,    |
  |  scorecards, consolidation, exit                              |
  +------------------------------+------------------------------+
                                 |
                                 +----------------> to Flowchart C
```

### Flowchart C — Cost Optimization & Implementation

```
+=====================================================================+
|            C. COST OPTIMIZATION & IMPLEMENTATION                    |
+=====================================================================+
  from B (dispositions, sourcing, vendor actions)
                  |
                  v
  +-----------------------------------------------------------+
  | [12] IT COST OPTIMIZATION                                  |
  |  Baseline 250 -> ELIMINATE -> REDUCE -> RE-PRICE ->        |
  |  RE-SOURCE -> AUTOMATE -> ORGANIZE -> GOVERN DEMAND        |
  |  minus headwinds (growth, reinvest) = 215.1 -> GAP 2.6     |
  |  + gap closers -> 212.4  (37.6 cr = 15.04%)                |
  |  Check: pool reconciliation (no double counting)           |
  +-----------------------------+-----------------------------+
                                |
                  Target met?  -+- NO --> add options / contingency
                                |         (loop back to [7], [11], [12])
                               YES
                                |
                                v
  +-----------------------------------------------------------+
  | [13] ROADMAP, KPIs & BENEFITS TRACKING                     |
  |  Day 30 -> Day 90 -> M6 -> M12 (freeze) -> M18             |
  |  Expected -> Validated -> Realized savings                 |
  +-----------------------------+-----------------------------+
                                |
                                v
  +-----------------------------------------------------------+
  | CONTINUOUS IMPROVEMENT (BAU governance)                    |
  |  quarterly portfolio review, FinOps, vendor reviews        |
  +-----------------------------------------------------------+

  FEEDBACK LOOPS (results change earlier decisions):
  ---------------------------------------------------
  (a) Savings slip at M9  -----------------> back to [12] activate contingency
  (b) Consolidation fit-gap fails ---------> back to [7] change disposition
                                              (Consolidate -> Retain/Modernize)
  (c) Vendor bids too high ----------------> back to [8]/[9] rethink sourcing
  (d) Regulation/data residency found -----> back to [2]/[4] adjust architecture
                                              & centralization
  (e) Business priorities change ----------> back to [1] re-align strategy
  (f) Governance too slow (bottleneck) ----> back to [5] change thresholds
```

### Poori logic — simple Hinglish mein (interview mein bina notes ke bolne layak)

1. **Business goals se shuru karo.** IT apne aap mein goal nahi hai. OmniRetail ko digital growth chahiye, cost kam chahiye, security aur reliability chahiye.
2. **IT strategy** batati hai paisa kahan jaana chahiye — kya protect karna (digital, security) aur kahan waste hai (duplicates, idle cloud).
3. **Current state assess karo** — facts se: ₹250 cr kahan ja raha hai, kyun badha (acquisitions, dual running, vendor sprawl), kitne apps, kitne DCs, kaun decide karta hai.
4. **Target architecture** banao — business needs ke basis pe: har capability ka ek platform, beech mein integration layer, ek data platform, hybrid infra, strong IAM/security. Gap = roadmap ka input.
5. **Operating model** decide karta hai IT kaise kaam karega — log, process, tools, sourcing, business ke saath collaboration.
6. **Centralized vs decentralized** — hum federated choose karte hain: standards, security, platforms, contracts central; product priorities aur local regulation divisions/countries ke paas.
7. **Governance** — kaun decide karega, kis threshold pe; RACI se accountability clear; controls bina bureaucracy.
8. **Organization** — CIO ke neeche EA, product teams, platform/cloud, CISO, data, ITSM, BRMs, vendor office. Layoffs nahi — pehle evidence, phir attrition aur reskilling.
9. **Application rationalization** — 120 apps pe decision tree: retain, consolidate, modernize, replace, retire. Low usage ≠ low value.
10. **Build vs buy** — jo cheez replace/naya chahiye: commodity kharido, differentiating banao ya hybrid; 5-yr TCO se decide.
11. **Outsourcing & managed services** — commodity services (helpdesk, infra ops, SOC monitoring) bahar, strategic cheezein (architecture, core product) andar; accountability hamesha humari; SLAs, pricing, exit clauses achhe se design.
12. **Vendor management** — contracts, utilization, renewals, benchmarks, scorecards, consolidation; volume pehle, price baad mein.
13. **Cost optimization** — sab levers ko ek bridge mein jodo, fixed order mein, double counting check ke saath, headwinds minus karke. Gap hai to aur options. Run-rate vs cash alag dikhao.
14. **Roadmap** — quick wins pehle, bade changes baad mein, festive season protect, savings expected → validated → realized track. **Feedback loops**: agar kuch slip ho, wapas jaake decisions badlo.


---

# PART 7: INTERVIEW PREPARATION

## 7.1 Ten likely PwC Technology Consulting questions + strong sample answers

**Q1. "Walk me through how you would approach this case."**
> "Main pehle objective clear karunga: ₹37.5 cr recurring reduction in 18 months, with digital growth, security aur reliability as guardrails. Phir 3 clarifications: target run-rate pe hai ya cash; constant prices ya nominal; one-time budget kitna hai. Uske baad ₹250 cr ka baseline by cost pool banaunga aur 3-year increase ke drivers dhundhunga. Mera structure 4 buckets ka hai: (1) direction — strategy & target architecture; (2) volume levers — apps, infra/cloud, operating model; (3) sourcing & price — build/buy, outsourcing, vendors; (4) execution — roadmap aur benefits tracking. Savings ek fixed order mein count karunga — eliminate, reduce, re-price, re-source, automate — taaki double counting na ho. End mein ek bridge dikhaunga jo headwinds ke baad bhi target hit kare, aur risk-adjusted view bhi."

**Q2. "Why not simply move everything to the cloud?"**
> "Cloud ek tool hai, strategy nahi. Teen reasons: (1) Cost — lift-and-shift without optimization cost badha sakta hai; OmniRetail mein already dual running aur idle cloud resources hain. (2) Fit — kuch workloads stable aur predictable hain, kuch legacy apps cloud ke liye bane hi nahi; unhe retire/replace karna better hai, migrate nahi. (3) Regulation — kuch data in-country rakhna padta hai. Isliye hum workload-by-workload decide karte hain: retire pehle, phir SaaS replace, phir jahan value hai wahan cloud. Hamare plan mein bhi DC-1 + DR rehta hai aur DC-3 ko in-country cloud region mein le jaate hain — 'cloud where it makes sense'."

**Q3. "Why not outsource the entire IT department?"**
> "Delivery outsource ho sakti hai, accountability nahi. Strategic architecture, core digital products jaise personalization, aur security decisions business ke liye differentiating aur sensitive hain — vendor ko dene se control aur IP jaata hai, aur vendor ka conflict of interest hota hai. Commodity services — helpdesk, infra ops, 24x7 SOC monitoring — hum outsource/managed service kar rahe hain jahan market mature hai. Aur ek 'intelligent client' team andar rakhni zaroori hai jo vendor ko manage aur challenge kar sake; warna knowledge loss aur lock-in hota hai."

**Q4. "How do you know the proposed savings are achievable?"**
> "Teen tarike se. (1) Har lever ka evidence: cloud bills aur utilization, licence usage logs, contract renewal dates, RFP mein actual vendor bids — estimates nahi. (2) Savings ko expected → validated → realized mein track karte hain; validated tab jab business owner sign kare ya contract sign ho, realized tab jab GL mein dikhe. (3) Risk-adjust karte hain: hamara expected case 15.04% hai lekin risk-adjusted ~12.5–13.7%, isliye ₹4.2 cr ka contingency pipeline hai aur Month 9 pe trigger point. Main CEO ko yeh nahi bolunga ki 15% guaranteed hai — main bolunga plan 15% deliver karta hai, aur yeh risks hain aur yeh hamara backup hai."

**Q5. "How do you prioritize application retirement?"**
> "Pehle decision tree: koi business ya legal need hai? Overlap hai? Health kaisi hai? Phir prioritization: (1) net saving size, (2) ease — dependencies, data migration, integrations, (3) risk — security issues jaise unsupported OS ko priority, (4) contract timing — retirement ko renewal se align karo taaki termination fee na lage. Quick wins jaise BI-2 aur ITSM-2 pehle, Grocery ERP jaise complex consolidations baad mein. Aur low usage ka matlab automatically retire nahi — Festive Campaign Planner saal mein 4 baar chalta hai lekin festive revenue ke liye critical hai."

**Q6. "What would you do if the CIO disagrees with business leadership?"** (e.g., CIO wants CRM-B consolidated; Home & Electronics head wants to keep it)
> "Main pehle dono ki concern samjhunga — CIO cost, security aur standardization dekh rahe hain; division head ko dar hai ki warranty process toot jayega. Phir facts pe le jaaunga: fit-gap analysis — kya CRM-A warranty process handle kar sakta hai? Kya gaps hain aur unka cost? Dono options ka TCO aur risk. Agar gap real hai to solution ho sakta hai: CRM-A pe warranty extension configure karna. Final decision governance forum — Technology Investment Council — mein jaayega jahan RACI clear hai. Consultant ka role ek side lena nahi, balki decision ko data-driven aur transparent banana hai."

**Q7. "What if the savings target conflicts with digital growth?"**
> "Yeh conflict real hai — digital growth se e-commerce cloud ~₹2.5 cr badhega. Main teen cheezein karunga: (1) Growth cost ko bridge mein explicitly headwind dikhaunga, chhupaunga nahi. (2) Run cost ke waste se 'save to invest' — hamare plan mein ₹42.1 cr gross savings se ₹4.5 cr reinvest hota hai. (3) Unit economics track karunga — cloud cost per online order girna chahiye even if total badhe. Agar phir bhi conflict ho, CEO ko trade-off ke saath option dunga: target ko growth-adjusted measure karna (e.g., excluding volume-driven cost) ya extra levers activate karna. Growth ko kaatna last option hai kyunki ₹1,250 cr digital revenue ₹2.5 cr cloud cost se kahin bada hai."

**Q8. "How do you distinguish cost savings from cost avoidance?"**
> "Cost saving = baseline se actual spend kam hua — budget mein dikhta hai. Cost avoidance = future mein jo kharcha badhne wala tha woh roka — baseline se spend kam nahi hota. Example: SoftSuite ne 8% increase maanga, humne 0% pe lock kiya — woh avoidance hai. Agar 5% kam karwaya to woh saving hai. CEO ka target recurring spend reduction ka hai, isliye bridge mein sirf savings count karte hain; avoidance alag report karte hain taaki value dikhe lekin target inflate na ho."

**Q9. "Should OmniRetail centralize IT?"**
> "Full centralization nahi — federated. Abhi decentralized hai isliye 2 ERPs, 2 CRMs, 4 DCs, 210 vendors. Lekin 5 countries ke regulations aur 3 alag businesses ki speed ke liye kuch flexibility chahiye. Central: architecture standards, security & IAM, cloud/DC/network, core platforms, enterprise contracts, data standards. Local: division product backlogs, local regulatory implementation jaise fiscal POS, small local vendors from approved list. Isse cost aur security centralization jaisi, speed decentralization jaisi milti hai."

**Q10. "How do you avoid double-counting savings?"**
> "Teen rules: (1) Har rupee ek hi cost pool mein — licences, infra, people, vendors, other. (2) Levers fixed order mein — eliminate, reduce volume, re-price, re-source, automate — aur har lever sirf bache hue base pe. Jaise CRM-B retire hua to uska licence, hosting, support teeno app rationalization mein; vendor negotiation sirf bache contracts pe. (3) End mein pool-level reconciliation — har pool ka final number add karke bridge ke final ₹212.4 cr se match karna chahiye. Aur cost avoidance bridge mein nahi jaata."

## 7.2 Five follow-up questions that challenge your assumptions

**F1. "Your long-tail realization is 45%. Why not 80%?"**
> "45% conservative hai kyunki teen leakages hain: ~20% replacement licences mein jaata hai, ~25% apps deeper review mein needed niklenge, ~10% contracts window mein exit nahi ho sakte. Agar data se pata chale ki leakage kam hai, to upside hai. Lekin plan conservative assumption pe bana hai — better under-promise."

**F2. "What if the Grocery ERP consolidation slips by 4 months?"**
> "ERP saving ₹2.7 cr + DC-2 ₹2.5 cr (kyunki DC-2 ERP pe depend hai) = ₹5.2 cr M18 run-rate se nikal jaayega. 37.6 − 5.2 = ₹32.4 cr (12.96%). Contingency ₹4.2 cr activate karein to 36.6 — abhi bhi ₹0.9 cr short. To options: additional wave-2 levers, ya CEO ko transparently batana ki 15% Month 22 tak aayega. Isliye ERP pe go/no-go gates aur early data migration critical hain."

**F3. "Digital sales grow 40%, not 25%. Now what?"**
> "Headwind = ₹10 cr × 40% = ₹4.0 cr instead of ₹2.5 cr → extra ₹1.5 cr → run-rate 213.9, target se ₹1.4 cr miss. Lekin yeh 'achhi problem' hai — revenue ₹1,400 cr ho gaya. Main recommend karunga: e-commerce elasticity (P2, ₹0.7 cr) + unit-cost KPI (cloud cost per order), aur CEO se target ko volume-adjusted measure karne ki baat — growth ko punish nahi karna chahiye."

**F4. "You assumed no layoffs. If the CEO is open to layoffs, would you increase L8?"**
> "Sirf evidence ke saath. Abhi activity analysis ~40 duplicate roles dikhata hai jo attrition se cover ho jaate hain. Bina analysis ke headcount kaatne se critical skills ja sakti hain — ERP consolidation aur MSP transition ke beech yeh bada risk hai. Agar deeper analysis aur surplus dikhaye, to phased, fair approach with severance cost (one-time) aur knowledge-transfer plan — aur yeh 18 months ke baad, big transitions ke baad, better hai."

**F5. "5% vendor price reduction and 10% services reduction — aren't these made up?"**
> "Yeh illustrative planning assumptions hain, benchmarks nahi. Validate karne ke liye: competitive RFP bids, apne hi vendors ke rate cards compare (same role pe 1.7x variance mila), independent price benchmarking. Sensitivity: licence renewals pe har 1% = ₹0.3 cr, services pe har 1% = ₹0.2 cr. Agar 5% ki jagah 3% mile to ₹0.6 cr kam — contingency se cover."

## 7.3 Three numerical questions — fully worked

**N1. SLA & downtime.** "Tier-1 SLA 99.95% hai. 30-day month mein e-commerce 40 minutes down raha. Allowed downtime, actual availability, service credit (5% of ₹54 lakh monthly fee per 0.1% shortfall or part thereof), aur revenue at risk (digital sales ₹1,000 cr/yr) batao."

| Step | Calculation | Result |
|---|---|---|
| Minutes in month | 30 × 24 × 60 | 43,200 min |
| Allowed downtime | 43,200 × (100% − 99.95%) = 43,200 × 0.0005 | **21.6 min** |
| Actual availability | (43,200 − 40) ÷ 43,200 = 43,160 ÷ 43,200 | **99.907%** |
| Shortfall | 99.95% − 99.907% | 0.043% → 1 step |
| Service credit | 1 × 5% × ₹54 lakh | **₹2.7 lakh** |
| Revenue per minute | ₹1,000 cr ÷ 525,600 min | ≈ ₹19,000/min |
| Revenue at risk | 40 × ₹19,000 | **≈ ₹7.6 lakh** (average day) |

Insight: Credit < business loss → SLA ke saath resilience bhi chahiye.

**N2. Cloud scheduling.** "Dev/test environments ka cost ₹2 cr/yr hai, 24x7 chalte hain. Agar inhe sirf weekdays 12 hours (8am–8pm) chalayein, aur 20% environments ko 24x7 rehna zaroori hai, to annual saving?"

| Step | Calculation | Result |
|---|---|---|
| Hours per week (24x7) | 24 × 7 | 168 |
| Scheduled hours | 12 × 5 | 60 |
| % time running | 60 ÷ 168 | 35.7% |
| % saving on scheduled envs | 100% − 35.7% | 64.3% |
| Schedulable cost | ₹2 cr × 80% | ₹1.6 cr |
| **Annual saving** | ₹1.6 cr × 64.3% | **≈ ₹1.03 cr** |

Note: Pay-as-you-go compute pe valid hai; storage cost scheduling se kam nahi hota — real case mein compute vs storage split karo.

**N3. Savings vs avoidance + payback.** "Ek ₹10 cr/yr software contract renew ho raha hai. Vendor ne +8% maanga. Humne negotiate karke −3% (₹9.7 cr) karwaya. Saving kitni count hogi, avoidance kitna? Aur CRM-B consolidation (one-time ₹2.0 cr, net ₹1.2 cr/yr) ka payback?"

| Item | Calculation | Result |
|---|---|---|
| Vendor proposal | 10 × 1.08 | ₹10.8 cr |
| Negotiated | 10 × 0.97 | ₹9.7 cr |
| **Saving vs baseline (counts toward target)** | 10.0 − 9.7 | **₹0.3 cr** |
| **Cost avoidance (report separately)** | 10.8 − 10.0 | **₹0.8 cr** |
| Total "negotiation value" (for vendor team scorecard only) | 10.8 − 9.7 | ₹1.1 cr |
| **CRM-B payback** | 2.0 ÷ 1.2 | **1.67 yrs ≈ 20 months** |

Trap: Candidate bolta hai "₹1.1 cr saving" — galat. Target ke against sirf ₹0.3 cr.

## 7.4 Five common candidate mistakes (and how to avoid)

| # | Mistake | Avoid kaise karein |
|---|---|---|
| 1 | Seedha solution pe jump ("cloud pe le jao", "outsource karo") | Pehle restate + clarify + baseline + structure |
| 2 | Savings double count karna | Cost pools + lever order + pool reconciliation |
| 3 | One-time aur recurring mix karna; implementation cost ignore karna | Har lever ke liye gross, new recurring, net, one-time alag columns |
| 4 | Guardrails tod dena — security/digital kaatna, bina evidence layoffs | Pehle "no-cut list"; headwinds aur reinvestment bridge mein dikhao; evidence-based org changes |
| 5 | "Target achieved" claim bina bridge ke; assumptions chhupana; risk na batana | Numerical bridge + label assumptions + risk-adjusted view + contingency |

## 7.5 Key formulas & definitions

| Term | Formula / meaning |
|---|---|
| IT spend % revenue | IT spend ÷ Revenue (250 ÷ 5,000 = 5.0%) |
| Target saving | Baseline × target % (250 × 15% = 37.5) |
| Net recurring saving | Gross recurring saving − New recurring costs |
| Exit run-rate | Month-18 spend × 12 (seasonality adjusted) |
| Cumulative saving (window) | Σ Net annual saving × (months realized ÷ 12) |
| Cumulative cash impact | Cumulative net savings − One-time costs |
| Simple payback | One-time cost ÷ Net annual saving |
| TCO | One-time (implementation, migration, integration) + Recurring (licences, people, infra, maintenance) + Upgrades + Exit, over fixed horizon |
| Availability | (Total time − Downtime) ÷ Total time |
| Allowed downtime | Total time × (1 − SLA %) |
| Weighted score | Σ (Weight × Score) ÷ Σ Weights |
| Licence utilization | Active users ÷ Licences paid |
| Cost avoidance | Proposed/future cost − Baseline (not counted in reduction) |
| Run vs Change | Run = keep the lights on; Change = new capability/growth |
| Risk-adjusted saving | Σ (Lever saving × confidence %) |

---

# PART 8: FINAL REVISION SHEET

## 8.1 All 13 concepts — one line each

| # | Concept | One-line definition | Key decision question | Key risk |
|---|---|---|---|---|
| 1 | IT Strategy & Alignment | IT investments business goals ko kaise support karenge | "Har bada IT rupee kis business goal ko serve karta hai?" | Cheap option chun ke growth/security ko nuksaan |
| 2 | Current vs Target Architecture | Aaj ka landscape vs future landscape aur unke beech gap | "Har capability ke liye ek strategic platform kaunsa?" | Trendy tech adopt karna bina business need ke |
| 3 | IT Operating Model | IT kaise kaam karta hai — people, process, tech, sourcing, collaboration | "Kaam kaise flow karega aur kaun own karega?" | Sirf org chart badalna, kaam ka tareeka nahi |
| 4 | Centralized vs Decentralized | Decisions/resources kahan baithte hain | "Kya central, kya local rahega?" | Over-centralization se speed aur local compliance ko nuksaan |
| 5 | IT Governance | Decision rights, thresholds, oversight | "Kaun, kis limit tak, kis basis pe decide karega?" | Bureaucracy — approvals slow |
| 6 | IT Organization | Roles, reporting lines, skills | "Kaunse roles ko stronger ownership chahiye?" | Bina evidence layoffs → critical skill loss |
| 7 | Application Rationalization | Har app ke liye Retain/Consolidate/Modernize/Replace/Retire | "Is app ki business value aur health kya hai?" | Low-usage critical app retire kar dena; hidden dependencies |
| 8 | Build vs Buy | Custom banana vs ready product vs hybrid | "Yeh differentiating hai ya commodity? 5-yr TCO?" | Lock-in (buy) ya maintenance burden (build) |
| 9 | Outsourcing | Activities external parties ko dena | "Strategic/sensitive hai? Market mature hai?" | Accountability outsource hone ka bhram; knowledge loss |
| 10 | Managed Services | Outcome-based ongoing service with SLAs | "Kya SLAs business outcome measure karte hain?" | Watermelon SLAs, hidden charges, dependency |
| 11 | Vendor Management | Contract-to-exit vendor lifecycle management | "Kise pehle renegotiate karein?" | Volume se pehle price negotiate karna; double count |
| 12 | IT Cost Optimization | Waste hatao, value protect karo, sustainable savings | "Kya bridge headwinds ke baad target hit karta hai?" | Double counting; one-time vs recurring confusion |
| 13 | Roadmap & Benefits Tracking | Sequenced plan with owners, KPIs, savings stages | "Quick wins aur big bets ka safe sequence kya hai?" | Peak season outage; savings leakage |

## 8.2 Master issue tree (compact)

```
KEY Q: -15% recurring IT spend (Rs 37.5 cr) in 18 months, growth/quality/security safe
 |
 +-- 1. DIRECTION ........ A. Strategy & alignment | B. Current vs target architecture
 +-- 2. VOLUME LEVERS .... C. Op model, org, governance | D. App portfolio | E. Infra & cloud
 +-- 3. SOURCING & PRICE . F. Build vs buy | G. Outsourcing & managed services | H. Vendors
 +-- 4. EXECUTION ........ I. Roadmap, risks, benefits tracking
 Order: ELIMINATE -> REDUCE -> RE-PRICE -> RE-SOURCE -> AUTOMATE  (no double counting)
```

## 8.3 Final savings bridge (compact)

```
250.0 baseline
 -12.0 L1 Apps | -4.0 L2 DCs | -5.8 L3 FinOps | -5.6 L4 Licences | -3.5 L5 Vendors
 -2.2 L6 Managed svcs | -0.8 L7 Automation | -4.0 L8 Op model | -1.5 L9 Demand gov
 = 210.6
 +2.5 digital growth | +2.0 security & data reinvest   = 215.1  (gap 2.6)
 -1.2 G1 devices | -1.5 G2 SD-WAN                        = 212.4
 => -37.6 cr = 15.04% (target 15%) | One-time 39.5 | 18-mo cash -10.5 | break-even ~M22
 => Risk-adjusted 12.5% (13.7% with 4.2 cr contingency)
```

## 8.4 18-month roadmap (compact)

| Phase | Focus | Key milestones | Run-rate actioned |
|---|---|---|---|
| Day 1–30 | Mobilize | Baseline, governance, purchase moratorium, FinOps quick fixes | ~₹1.5 cr |
| Day 31–90 | Diagnose & decide | App dispositions, DC design, stop 12 projects, RFPs, org design | ~₹7.3 cr |
| M4–6 | Quick wins | BI-2, ITSM-2, Archive retired; V4/V2 renegotiated; SOC live; new org | ~₹19.8 cr |
| M7–12 | Scale, protect peak | CRM-B (M8), DC-3 (M8), freeze M9–11, MSP/HR/WMS (M12) | ~₹33.6 cr gross |
| M13–18 | Big moves, embed | POS, SD-WAN, Grocery ERP (M15), DC-2 (M16), validate run-rate | ₹42.1 gross → **₹37.6 net** |

## 8.5 Five most important interview takeaways

1. **Structure before solution:** restate → clarify (run-rate? constant prices? budget?) → baseline → issue tree.
2. **Guardrails are part of the answer:** digital growth aur security ke costs bridge mein headwinds ki tarah dikhao.
3. **No double counting:** cost pools + lever order + pool reconciliation; avoidance alag.
4. **Recurring ≠ one-time ≠ cash:** run-rate target met ho sakta hai jab 18-month cash negative ho.
5. **Honesty wins:** assumptions label karo, risk-adjusted view do, contingency rakho; "target met" sirf jab numbers dikhayein.

---

# PART 9: INTERVIEWER KO 3–5 MINUTE MEIN POORA CASE KAISE WALK-THROUGH KAREIN

**Script (bolne ki speed pe ~4 minute). Brackets mein timing.**

**[0:00–0:30] Problem & objective**
> "OmniRetail ₹5,000 crore ka multinational retailer hai — stores plus online, 3 divisions, 5 countries, acquisitions se grow hua. IT spend ₹250 crore hai, 3 saal mein 35% badha, revenue se tez. CEO chahte hain 18 months mein recurring IT spend 15% — ₹37.5 crore — kam ho, bina digital growth (25%), customer experience, security aur reliability ko nuksaan pahunchaye. Maine clarify kiya ki target Month-18 run-rate pe hai, constant prices pe, aur growth costs include hain."

**[0:30–1:00] Diagnosis**
> "Baseline ko 5 pools mein toda: infra & cloud 70, licences 60, people 65, vendors 45, other 10. 3-year increase ₹64.8 crore ka analysis kiya: zyaadatar acquisitions ki duplication, cloud dual running aur vendor sprawl — lekin security aur inflation wala hissa legitimate hai, use nahi kaatna."

**[1:00–1:45] Structure & target state**
> "Mera issue tree 4 buckets ka tha: direction, volume levers, sourcing & price, execution. Target architecture mein har capability ka ek platform — ek ERP, ek CRM, ek ITSM — integration aur data platform ke saath, hybrid infra aur strong IAM/SOC. Operating model federated: standards, security, platforms aur contracts central; product priorities aur local regulations divisions/countries ke paas. Governance mein investment council, architecture board, thresholds aur RACI — taaki waste wapas na aaye."

**[1:45–2:45] Levers & numbers**
> "Savings fixed order mein count ki — eliminate, reduce, re-price, re-source, automate — double counting se bachne ke liye. Application rationalization ₹12 crore — jaise CRM-B ko CRM-A mein consolidate, Grocery ERP ko Group ERP mein, BI-2 retire — lekin low-usage critical apps retain. DC consolidation ₹4, cloud FinOps ₹5.8, licence optimization ₹5.6, vendor negotiation ₹3.5, managed services ₹2.2, automation ₹0.8, operating model ₹4 — bina layoffs, attrition se — aur demand governance ₹1.5. Total ₹39.4 crore. Lekin digital growth aur security/data reinvestment ₹4.5 crore add karte hain, to ₹2.6 crore ka gap tha. Device lifecycle aur store SD-WAN se ₹2.7 crore aur laaye. Final: ₹37.6 crore, yaani 15.04% — target just met."

**[2:45–3:30] Investment, timing, risk**
> "One-time investment ₹39.5 crore. Run-rate Month 18 pe achieve hota hai, lekin 18 months ka cumulative cash lagbhag −₹10.5 crore hai; break-even Month 22 ke aas-paas. Buffer thin hai — risk-adjusted 12.5 se 13.7% — isliye ₹4.2 crore contingency pipeline aur Month 9 trigger point rakha. Biggest risk Grocery ERP consolidation hai, kyunki DC-2 closure bhi uspe depend karta hai."

**[3:30–4:15] Roadmap & close**
> "Roadmap: pehle 30 din mobilize aur governance; 90 din mein portfolio decisions aur FinOps quick wins; Months 4–6 mein retirements aur renegotiations; 7–12 mein bade transitions, festive season freeze ke saath; 13–18 mein ERP consolidation aur DC-2 closure. Savings ko expected, validated, realized mein Finance ke saath track karenge. Cost ke alawa benefits: scalable e-commerce, single customer view, unsupported systems khatam, faster decisions. Meri recommendation: 'Simplify, Optimize, Reinvest' programme approve karein, contingency ke saath."

**Delivery tips:**
- Numbers round aur confident bolo; har bade number ke saath "kyunki" lagao.
- Interviewer beech mein roke to us branch pe jao (issue tree tumhara map hai).
- End hamesha recommendation + risk + next step pe.

---

*End of Master Case. Saare figures illustrative/fictional hain aur sirf learning ke liye hain.*
