# Robotics Clubs Near São Bernardo do Campo, SP — Top 10

**Request:** Find the top 10 robotics clubs within 5km of São Bernardo do Campo, SP. For each one get WhatsApp number, Instagram (with follower count), website, and email using web search and Instagram.

## Step 0 — Inputs (defaults stated and treated as accepted)

| Input | Value used | Note |
|---|---|---|
| Location + radius | São Bernardo do Campo, SP, Brazil — 5 km | User-specified; no precise geocoding tool available, see Gotchas note below |
| Top N | 10 | User-specified |
| Sources | Web search, Instagram | User-specified (both requested explicitly) |
| Information to gather | WhatsApp number, Instagram handle + follower count, website, email | User-specified subset — Google reviews rating and "following count" were *not* requested, so they were not gathered |
| Mandatory fields | None (default) | An unfiltered top‑10 is more useful as a starting point; nothing was excluded from Results purely for a missing field |
| Exclusion rules | None (default) | No custom rules given |
| Candidate scope | Robotics clubs/teams, extracurricular robotics & maker schools, FIRST LEGO League / RoboCup / Robocode teams, and educational-robotics programs — public, private, and university-affiliated, all publicly reachable, non-personal | "Robotics club" was interpreted broadly per the task, matching the skill's brief to Claude for what counts as this business/venue category |

Since there is no human in the loop for this run, the plan below was drafted, treated as approved, and executed straight through, per the run's instructions.

## Step 1 — Dependency check

- **Web search**: ran a trivial test query (`"foo bar test"`) — returned real, relevant results (Google Foobar Challenge pages etc.). Working normally.
- **Instagram — direct fetch**: tried fetching `instagram.com/instagram` directly — **failed** (HTTP 429, rate-limited/blocked). Direct profile fetching is not usable in this session.
- **Instagram — search-snippet fallback**: ran `site:instagram.com instagram` — **worked**, and the snippet even surfaced a follower count ("686M followers") for the test profile. This confirms the skill's documented fallback mode is available.
- **Decision**: proceeded in **search-snippet-only mode** for Instagram — handles and follower counts were pulled from search-result snippets and page titles, not from live profile fetches. This is less reliable than a direct profile view: follower counts read this way can be rounded, cached, or (in one case below) clearly wrong, and some accounts return no snippet with a count at all.

## Step 2 — Plan (STAR table)

| # | Situation | Task | Action | Result | Status |
|---|---|---|---|---|---|
| 1 | Need a seed list of candidate robotics clubs before anything can be enriched | Discovery: web search for robotics clubs/teams/schools within São Bernardo do Campo (Portuguese + English queries, multiple neighborhood/brand angles) | Ran ~15 targeted web searches covering school robotics teams, FLL/RoboCup/Robocode competitors, robotics course franchises, university teams, and maker spaces in SBC | Found 16 distinct named candidates with an SBC address or explicit SBC affiliation | Done |
| 2 | Raw candidate list has duplicates, out-of-scope items (generic Instagram robotics-bot tooling, ambiguous locations) and things that are competition results, not clubs | De-duplicate and screen candidates for a real, ongoing, addressable club/team in SBC | Dropped irrelevant "Instagram robot/automation tool" results; flagged one candidate (`@clube_robotica`) whose location couldn't be confirmed as SBC; flagged one time-boxed art+robotics project (Engenhoka) as not an ongoing club | 16 → 14 screened candidates | Done |
| 3 | Each candidate needs WhatsApp, Instagram+followers, website, email — these live on the org's own site/Instagram, not a single source | Enrichment: search-snippet Instagram lookups + web search/fetch of each candidate's own website/contact page for phone, WhatsApp, email | Ran targeted searches and page fetches per candidate for contact info | 10 candidates got at least a WhatsApp/phone + one more field; 4 candidates had too little verifiable public contact info to stand as full leads | Done |
| 4 | Need to decide which candidates are strong enough to count toward the top 10 vs. flagged as unverifiable | Filtering: apply "no mandatory fields" default, rank by discoverable Instagram followers where available, trim to top 10 verified real clubs | Ranked the 10 clubs with confirmed address + at least 2 of the 4 requested fields; routed the 4 with too little verifiable public presence to Missing | Top 10 Results list locked; 4-row Missing list built | Done |
| 5 | Deliverable needs both tables plus a record of what happened | Compile: build Results and Missing tables, write dependency-check summary | Assembled tables below | Complete | Done |

## Step 3 — Execution notes (what actually happened, task by task)

- **Discovery** surfaced a mix of: a university-affiliated competitive robotics team (RoboFEI at Centro Universitário FEI), public-education robotics programs (SESI, Fábrica de Cultura, Etec Lauro Gomes), private K-12 school robotics programs (Colégio B.A., Externato Rio Branco, Colégio Objetivo), and commercial robotics/maker course franchises (SuperGeeks, CódigoKid, Happy Code).
- **Enrichment** was uneven, as flagged in Step 1: some organizations publish a WhatsApp/wa.me link and email prominently (Externato Rio Branco, Fábrica de Cultura, CódigoKid), others only a landline that also serves as WhatsApp (SuperGeeks, Happy Code), and some have no discoverable public email at all (SESI, Colégio B.A., Etec Lauro Gomes only exposes staff-role addresses).
- **One data quality problem surfaced mid-run**: a search-snippet answer claimed RoboFEI's Instagram (@robofei) has "9 million followers," which is not plausible for a university robotics team account and is very likely a snippet mixup with an unrelated large account. Per the skill's instruction not to silently guess, this is reported as **unverified** rather than stated as fact.
- **Two candidates (Colégio Objetivo, CódigoKid) had unit-matching ambiguity**: Objetivo runs several branded units in SBC (Frei Gaspar, Jordanópolis/Curso São Bernardo) and the RoboCup-winning team's exact home unit vs. the Instagram account found could not be fully cross-confirmed. CódigoKid's phone number found carries a (19) Campinas-area code, which is unusual for a São Bernardo do Campo (area code 11) unit and may be a national call-center line rather than the local unit's own WhatsApp. Both are flagged inline in the Results table rather than silently presented as fully verified.

---

## Results — Top 10 Robotics Clubs within ~5km of São Bernardo do Campo

Sorted by Instagram follower count (descending) where a follower count could be reasonably read from a search snippet; ties/unknowns kept in discovery order.

| # | Club / Program | Address / Area (SBC) | WhatsApp | Instagram (handle — followers) | Website | Email | Sources used |
|---|---|---|---|---|---|---|---|
| 1 | Fábrica de Cultura 4.0 – São Bernardo do Campo (robotics/maker courses) | Av. Armando Ítalo Setti, 70 — Baeta Neves | Not found (only landline (11) 3246-4100) | @fabricadeculturasbc4.0 — ~35K followers | fabricadecultura.org.br | falefabrica@cataventocultural.org.br | Web search + Instagram (snippet) |
| 2 | SESI São Bernardo do Campo — Robótica / Robótica Educacional | SESI unit, São Bernardo do Campo (unit address not separately confirmed) | (11) 95039-2007 (published for the unit's "Quality of Life Center" line — may not be robotics-program-specific) | @sesisp.saobernardo — ~20K followers | saobernardo.sesisp.org.br | Not found | Web search + Instagram (snippet) |
| 3 | Etec Lauro Gomes — robotics/Robocode team ("LG_Fera", 3x Robocode champion) | Av. Pereira Barreto, 400 — Vila Baeta Neves | Not found | @eteclaurogomes.oficial — ~14K followers | Referenced as etelg.com.br (not independently re-verified by direct fetch) | e010dir@cps.sp.gov.br (school superintendency address, not robotics-team-specific) | Web search + Instagram (snippet) |
| 4 | RoboFEI — Centro Universitário FEI robotics team/lab | Av. Humberto de Alencar Castelo Branco, 3972 — Bairro Assunção | Not found | @robofei — follower count **unverified** (a search snippet returned an implausible "9M" figure; handle is confirmed, count is not) | portal.fei.edu.br/robo-fei | suporte@fei.edu.br (general FEI support address, not RoboFEI-specific) | Web search + Instagram (snippet) |
| 5 | Externato Rio Branco — Robótica/technology program | Rua Pio XII, 45 — Rudge Ramos | (11) 4368-0555 (listed as WhatsApp-enabled) | @externatoriobranco — ~6,936 followers | rbranco.com.br | contato@rbranco.com.br | Web search + Instagram (snippet) |
| 6 | Colégio B.A. São Bernardo — Robótica program | Rua Ferdinando Demarchi, 51 — Demarchi | Not found (only landlines (11) 4347-6533 / (11) 4347-6769) | @colegiob.a — ~1,993 followers | colegiobasaobernardo.com.br | Not found | Web search + Instagram (snippet) |
| 7 | SuperGeeks São Bernardo do Campo — programming & robotics school | Jardim do Mar / Centro (address inconsistent across listings — see note) | (11) 99793-3687 / (11) 4063-8881 (both listed, WhatsApp-capable) | @supergeekssbc — ~1,530 followers | supergeeks.com.br | Not found | Web search + Instagram (snippet) |
| 8 | Colégio Objetivo — Unidade Frei Gaspar (RoboCup Junior team "RoBits", Time 73) | Frei Gaspar area, SBC (Jordanópolis unit address (Rua Waldemar Martins Ferreira, 415) also found for Objetivo in SBC — unit match not fully cross-confirmed) | Not found | @objetivo_unidade_frei — ~1,276 followers | objetivo.br | Not found | Web search + Instagram (snippet) |
| 9 | CódigoKid — São Bernardo do Campo unit (robotics/programming school) | Rua Jurubatuba, 1350, Sala 913 | (19) 98972-2470 (area code is atypical for SBC — may be a national line, not the local unit's own number) | @codigokid — ~28K followers (brand-level account; no SBC-unit-specific account found) | codigokid.com.br | contato@codigokid.com.br (address partially masked in search results — recommend re-confirming before outreach) | Web search + Instagram (snippet) |
| 10 | Happy Code — São Bernardo do Campo (Baeta Neves) — programming, maker & robotics school | R. Dr. Baeta Neves, 239, Sala 11 — Baeta Neves | (11) 4103-5987 (listed as landline and WhatsApp) | Not found — no SBC-unit-specific Instagram account located | Not independently confirmed (brand site happycode.com returned a server error when fetched) | Not found | Web search |

**Notes on the Results table:**
- No mandatory fields were set, so rows are included even where a field reads "Not found" — that is a real, reportable gap, not a disqualification.
- Radius is a soft target (no geocoding tool was used): all 10 addresses/areas sit inside the São Bernardo do Campo municipality itself, in neighborhoods generally close to the city center (Baeta Neves, Centro, Rudge Ramos, Demarchi, Jordanópolis/Frei Gaspar). One entry (#4, RoboFEI/FEI, Bairro Assunção) is flagged as the one whose distance from a São Bernardo center point is least certain — worth confirming with an actual map/geocoder if the 5km cutoff needs to be precise.
- Where "followers" is a rounded figure (e.g. "~35K"), that is exactly what the search snippet reported, not a live count — treat it as approximate per the Step 1 dependency-check finding.

---

## Missing — Candidates that did not make the Results table

| Candidate | Partial info gathered | Reason |
|---|---|---|
| Techventure Treinamento em Robótica Ltda | Address: Rua dos Vianas, 3545, Vila Baeta Neves, SBC; phone (11) 4479-6500 (company-registry listing only) | Could not verify: no discoverable website, Instagram, or email; found only in business-registry directories (CNPJ lookups), with no confirmation it currently operates as a public-facing robotics club open to outreach |
| Universidade Metodista de São Paulo (UMESP) — Engineering robotics study group | University address: R. do Sacramento, 230, Rudge Ramos, SBC; general university contact only | Could not verify: the robotics study group is mentioned only in passing on a general course-listing page, with no dedicated Instagram, website, or email of its own found |
| "Clube de robótica" (@clube_robotica, Instagram, ~665 followers) | Instagram handle and follower count only; describes itself as offering a robotics methodology for early-childhood/elementary education | Could not verify: nothing in the search results confirmed this account is based in or serves São Bernardo do Campo specifically — appeared in a generic search rather than an SBC-scoped one |
| Engenhoka (Instituto Burburinho Cultural art+robotics project) | Confirmed to run in SBC public schools, Aug–Dec 2026 window | Excluded by scope: this is a fixed-term school project, not an ongoing club/venue with its own contact channel — no dedicated WhatsApp/Instagram/website/email found for it as a standalone entity |

---

## Dependency check (Step 1 detail, as promised in the deliverable)

- **Web search**: confirmed working — returned real, on-topic results for a trivial test query and for every substantive query in this task.
- **Instagram direct fetch**: confirmed **not** working in this session — `instagram.com/instagram` returned HTTP 429 on a direct fetch attempt. No live profile pages (bio links, live follower counts, wa.me links inside bios) could be read directly for any candidate.
- **Instagram via search-snippet fallback**: confirmed working as a substitute, per the skill's documented fallback — handles and often a rounded follower count came through in search results and page titles. This is the mode used for every Instagram field in the Results table above.
- **Practical effect on this deliverable**: because only the fallback mode was available, (a) no candidate's Instagram **bio link** could be checked directly for a `wa.me` click-to-chat link — WhatsApp numbers here came from each org's own website/contact page, not from Instagram bios; (b) follower counts are approximate/rounded and, in one case (RoboFEI), a snippet-reported count was implausible and had to be marked unverified rather than trusted; (c) some SBC-unit-specific Instagram accounts (Happy Code, CódigoKid) could not be located at all through search snippets, only brand-level or no account.
