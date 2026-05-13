# Event Notes Conventions

Formatting guidelines for this event directory. Referenced by [CLAUDE.md](CLAUDE.md).

## Directory Structure

Each event directory contains:

- `notes.md` -- primary notes file (People + Sessions)
- `linkedin_post.md` -- promotional post and first comment
- `image_generation_prompt.md` -- DALL-E / ChatGPT prompts for post image
- `people.vcf` -- vCard 3.0, one VCARD per speaker (PERSON entries)
- `organizations.vcf` -- vCard 3.0, one VCARD per company (`X-ABShowAs:COMPANY`)
- `event.ics` -- VCALENDAR with one VEVENT per session + one full-day umbrella event
- `PROJECT.md` -- During Event (blank) and After Event (action items and flags)
- `CLAUDE.md` -- Claude Code context for this directory
- `event_notes_conventions.md` -- this file

## notes.md: People Section

Opening line: link to `people.vcf`.

Split into two subsections: **Existing Contacts** (already in Contacts.app / Daylite) and **New Contacts**.

Annotate repeat speakers with an italic line: `_Repeat speaker: GenAI Days #N, #N_`

Each person gets sub-bullets:

- LinkedIn: `<URL>`
- Bio: `<URL>` (if a speaker bio page exists)
- Company: `<URL>` (if a company website exists)
- Session: Session title -- `<event page URL>`
- Email / Phone: (if publicly available)
- Note: (flags, verification needed, strategic relevance)

Use `**bold**` to call out high-priority paid-work connections.

## notes.md: Sessions Section

Opening line: link to `event.ics`.

Sessions listed in **agenda order** (chronological by start time).

Each session heading format:

```markdown
### Session Title -- Speaker Name

HH:MM AM/PM EDT
```

Immediately after the time line, a bullet list:

- LinkedIn: `<URL>` for each speaker
- Company/Website: `<URL>`
- Event: `<event page URL>`

Then a blockquote with the **exact verbatim text** from the event page:

```markdown
> Exact text copied from the event page session description.
```

Then an empty `#### Notes - Session Title` subsection for live capture during the event.

## VCF Files

- Format: vCard 3.0
- PERSON entries: standard `N:` and `FN:` fields with `TITLE:`, `ORG:`, `URL;TYPE=LinkedIn:`, `URL;TYPE=Work:`, `EMAIL;TYPE=Work:`, `NOTE:`
- ORGANIZATION entries: empty `N:;;;;`, `FN:` and `ORG:` set to company name, `X-ABShowAs:COMPANY` (required for Daylite/macOS Contacts to recognize as company card)
- LinkedIn URLs in `URL;TYPE=LinkedIn:` field and mirrored in `NOTE:` field
- NOTE field format: `LinkedIn: URL\nBio: URL\nSession: title\nEvent: URL\nNote: flags`
- Import into Daylite via File > Import -- Daylite handles deduplication

## ICS File

- Format: iCalendar, TZID=America/New_York with full VTIMEZONE component
- One VEVENT per session: `SUMMARY:GenAI Day #N - Speaker Name - Session Title`
- One umbrella VEVENT: `SUMMARY:GenAI Day #N - Theme (Full Event)` covering full event start/end
- DESCRIPTION includes LinkedIn, company URL, topic summary, and event page URL
- Use PRODID: `-//Michael Wolf//GenAI Day N//EN`

## PROJECT.md

Two sections:

- **During Event** -- blank at creation; fill in live notes, chat connections, follow-up seeds
- **After Event** -- action items and verification flags; include done items with URLs and dates

## LinkedIn Post

In `linkedin_post.md`, the published post URL and date go immediately after the post body, before any comment sections:

```markdown
**Published:** YYYY-MM-DD
**Post URL:** <https://www.linkedin.com/posts/...>
```
