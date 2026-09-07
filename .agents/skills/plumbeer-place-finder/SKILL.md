---
name: plumbeer-place-finder
description: >-
  Find and profile local businesses or venues near a location for outreach,
  prospecting, or lead-gen: search a radius around a place (default São
  Bernardo do Campo, 10km), rank the top N (default 10), and enrich each one
  with WhatsApp number, Instagram handle plus follower/following counts,
  Google reviews rating, website, and email — via web search and Instagram
  by default, with room for other sources. Use this whenever the user asks
  to "find places near X", "build a list of businesses/leads", "find
  salons/restaurants/shops with Instagram and WhatsApp", wants a prospecting
  or lead-gen list of local venues, or asks for a directory of places with
  contact info — even if they only name a neighborhood, business type, or
  radius without spelling out the full pipeline. Walks the user through a
  STAR-tracked plan they approve before searching, executes one task at a
  time with checkpoints, and finishes with a Results table (places found)
  and a Missing table (places that couldn't be completed and why, e.g. a
  mandatory field was missing).
compatibility: >-
  Needs web search (and ideally web fetch) to discover and enrich places.
  There is no dedicated Instagram or Google Maps API assumed — both are
  reached through ordinary web search/fetch, which is fragile (login walls,
  rate limits) and should be dependency-checked before committing to a plan.
metadata:
  author: plumbeer
  version: "1.0"
  category: research
---

# Place Finder

Build a list of local businesses or venues near a location, then enrich each one with contact and social info — for outreach, prospecting, or lead-gen. This is a research pipeline with real gaps (blocked scrapes, missing phone numbers, ambiguous name matches): treat every gap as data to report, not a reason to guess or silently drop a lead.

Two things stay separate throughout: **sources** are *where you discover candidate places* (web search, Instagram, others). **Information fields** are *what you enrich each candidate with* — regardless of which sources were picked, a field is gathered wherever it actually lives (Google reviews always means a Google lookup; a WhatsApp number is usually on the place's own website or Instagram bio, not a "WhatsApp source"). Don't conflate the two when planning tasks.

---

## Step 0 — Gather inputs

Collect these, using `AskUserQuestion` for the multi-select ones if it's available, otherwise asking in plain chat. State each default as you go rather than making the user recite the whole spec back:

| Input | Default |
|---|---|
| Location + radius | São Bernardo do Campo, SP, Brazil — 10 km |
| Top N results | 10 |
| Sources | Web search, Instagram |
| Information to gather | WhatsApp number, Instagram handle, Instagram followers/following, Google reviews rating, website, email |
| Exclusion rules | None |

**Sources** — options are Web search, Instagram, and anything else the user names (Google Maps, Yelp, a local directory, TripAdvisor…) as free text. More sources found means more candidates to de-duplicate later, not more information per candidate.

**Information to gather** — the same six standard fields listed above, plus a free-text "other" (e.g. "opening hours", "owner's name"). Every one of these is expensive (a search + a fetch per candidate, sometimes more), so don't silently gather fields nobody asked for.

**Exclusion rules** — this is what routes a candidate into the Results table versus the Missing table. It has two parts:
1. **Mandatory fields** — pick from the same list as "information to gather" (plus "other"). If a selected field is marked mandatory and a candidate is missing it, that candidate goes to Missing, not Results.
2. **Custom rules** (the "other" option) — free text like "no chains", "must currently be open", "under 500 Instagram followers." Apply these as a filter once the field they depend on has been gathered.

Default to **no mandatory fields and no custom rules** — an unfiltered top-N list is more useful as a starting point than a silently-shrunk one, and it's cheap for the user to tighten later. Don't default to "all fields mandatory" just because the field list happens to be reused — say the default out loud so the user can tighten it if they actually want a strict lead list.

If radius, top N, or a source truly can't be inferred, ask — don't guess. Everything else, state the default and move on.

---

## Step 1 — Dependency check

Before building any plan, sanity-check every selected source. A pipeline built on a broken dependency wastes the user's time on a plan that can't execute — flag this up front, not after task 6 fails.

- **Web search** — run one trivial query (e.g. `"foo bar test"`) through the search tool and confirm it returns real results, not an error or empty page.
- **Instagram** — try fetching one well-known public profile directly (e.g. `instagram.com/instagram`). Instagram frequently serves a login wall or blocks unauthenticated fetches entirely — if the direct fetch fails, fall back to reaching Instagram data through ordinary web search (`site:instagram.com <query>`), which surfaces less (often just the handle and a snippet, not live follower counts) but usually still works. Tell the user which mode you're in — direct profile access vs. search-snippet-only — since it changes how complete the Instagram fields will be.
- **Any other named source** — same idea: one cheap real request, confirmed before relying on it.

If a source fails outright, tell the user immediately, propose dropping it or a fallback, and get their answer before building the plan around it.

---

## Step 2 — Build the plan (STAR table)

Break the work into tasks and track them in a table with these columns: **#, Situation, Task, Action, Result, Status**. Fill in Situation and Task before executing anything; Action, Result, and Status update live in Step 3.

A typical breakdown:

1. **Discovery** — one task per selected source, searching the location+radius for the requested kind of place. Pull noticeably more than N candidates up front (exclusions and duplicates will shrink the pool) and de-duplicate by name/address across sources before counting toward N.
2. **Enrichment** — group by where the data actually lives rather than one task per field: e.g. "visit each candidate's website/Instagram bio for WhatsApp, email, website" is one task even though it covers three fields; "look up each candidate's Google reviews rating" is its own task since it's a different lookup entirely.
3. **Filtering** — apply mandatory fields and custom exclusion rules, sort the survivors, trim to top N. **If fewer than N genuine candidates survive, don't pad the Results table with weak or unconfirmed fits to reach N** — report the true count and route the best near-misses to Missing with the specific reason they didn't qualify (out of radius, wrong category, an unconfirmed field). A short, honest list beats a full one padded with a guess — this is the same "don't guess, report gaps" principle as the rest of the skill, applied to the count itself, not just individual fields.
4. **Compile** — build the Results and Missing tables.

Situation is the *why* ("need a seed list of candidate places before anything else can be enriched"), not a restatement of the task.

Present the table to the user and iterate on it until they approve — don't start Step 3 on an unapproved plan, even if the defaults from Step 0 seemed uncontroversial. Plans change once someone sees the concrete task list.

---

## Step 3 — Execute one task at a time

Work through the STAR table top to bottom, one row at a time:

1. Set that row's Status to "In progress."
2. Do the work.
3. Fill in Action (what you actually did/searched/fetched) and Result (what came out of it — counts, notable gaps).
4. **On failure or a materially incomplete result** (e.g. a source returned nothing, half the candidates have no discoverable website): stop, flag it to the user with what happened, propose a follow-up (retry, fallback source, lower the bar, skip the field for this run), and wait for their answer before moving to the next row. Don't silently downgrade scope on your own judgment.
5. **On success**, show the user a preview of that task's output (the candidate list so far, the fields just gathered) and iterate if they want changes before locking it in.
6. Once they confirm the row is done, set Status to "Done" and move to the next row.

This preview-and-confirm loop is the main defense against the two failure modes that make this kind of list useless: junk candidates (wrong business, permanently closed, duplicate) compounding through later enrichment steps, and enrichment quietly stalling on a blocked source without anyone noticing until the final table looks thin.

---

## Step 4 — Compile the Results table

Columns: place name, address/area, plus one column per selected information field, plus a "sources used" column noting where each piece of data came from (useful for spot-checking later).

Sort by whatever signal is most relevant to the request (Instagram followers, Google rating, or just discovery order) and trim to top N **after** exclusions — don't count excluded candidates toward N.

## Step 5 — Compile the Missing table

Every candidate that didn't make the Results table goes here, with a specific reason — never a generic "failed":
- `Missing mandatory field: <field>` — say which one.
- `Excluded by rule: <rule>` — quote the custom rule.
- `Could not verify: <what blocked it>` — e.g. "Instagram blocked automated access to this profile."
- `Duplicate of <other candidate>`.

Include whatever partial info was already gathered for that candidate — a half-complete lead is still worth handing back, not silently discarding.

Update the STAR table's final Status column once both tables are built, and present all three tables together as the deliverable.

---

## Output formats

Default to rendering all three tables directly in chat as normal markdown tables — that's the "built-in" format and needs nothing extra.

If the user wants an alternate format, offer:
- **Markdown** — same tables, saved to a `.md` file.
- **CSV** — Results and Missing as separate `.csv` files (STAR is a process log, not usually worth exporting).
- **List** — a plain bullet list per place, one line per field.
- **JSON** — an array of objects, one per place, keyed by field name; include a `status: "found" | "missing"` and, for missing entries, a `reason` key.

Only generate the file(s) once the user asks for a specific format — don't produce every format speculatively.

---

## Gotchas

- **"Radius" is usually a soft target, not a computed distance.** Without a geocoding/Maps API, radius is approximated by reasoning about which neighborhoods/streets fall within roughly that distance of the center — say so, and ask the user to flag anything that looks clearly outside if precision actually matters for their use case.
- **Instagram scraping is fragile by nature** — login walls, rate limits, and layout changes are the normal case, not an edge case. The Step 1 dependency check exists specifically so this surfaces before the plan is built, not after task 3 quietly returns nothing.
- **Name collisions are common** — chains, franchises, and generic names (e.g. a bakery called "Doce Sabor") produce multiple real candidates. Don't merge or pick one arbitrarily; list them separately unless the user says otherwise.
- **A WhatsApp "number" is often a `wa.me/<number>` click-to-chat link**, not a phone number printed on the page — check bio links and website footers for `wa.me` or `api.whatsapp.com` links, not just digit strings.
- **This is for public business contact info, not private individuals.** If a request drifts toward finding a specific person's personal accounts or contact details rather than a business's public presence, stop and clarify scope with the user before continuing.
- **Google reviews rating needs a Google lookup regardless of which sources were picked** — it's an information field, not a source; don't skip it because "Google Maps" wasn't selected as a source, and don't treat picking Instagram as a source as license to skip a real Google search for this field.
