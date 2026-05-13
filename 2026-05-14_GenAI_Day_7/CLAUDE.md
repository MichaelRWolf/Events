# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This directory captures notes, contacts, and artifacts for **GenAI Day #7: The Rise of Agentic AI** (SoftEd, 2026-05-14, Zoom). Michael attends this recurring series not primarily for information -- he already knows enough -- but to make **connections that lead to paid work**. Every artifact here should serve that goal.

## Parent Repo

This directory lives inside the `Events` git repo at `/Users/michael/repos/Events/`. Pre-commit hooks are defined there and apply here.

### Checks

```bash
# From the Events repo root
pre-commit run --all-files

# Setup (first time after clone)
./scripts/setup
```

Hooks enforce: markdownlint (with auto-fix), markdown-table-formatter (column alignment), fix-ligatures/smartquotes/unicode-dashes on markdown, shellcheck, and a block on `.org` files.

## Files

| File                         | Purpose                                                                    |
|------------------------------|----------------------------------------------------------------------------|
| `notes.md`                   | Session notes and speaker list (People + Sessions sections)                |
| `people.vcf`                 | vCard 3.0 contact cards for all 13 speakers                                |
| `organizations.vcf`          | vCard 3.0 company cards (X-ABShowAs:COMPANY for Daylite)                   |
| `event.ics`                  | Calendar events -- 12 sessions + full-day umbrella (TZID=America/New_York) |
| `PROJECT.md`                 | During Event (live capture) + After Event (action items and flags)         |
| `linkedin_post.md`           | Promotional post and first comment                                         |
| `image_generation_prompt.md` | DALL-E / ChatGPT prompts for the LinkedIn header image                     |
| `event_notes_conventions.md` | Formatting guidelines for this directory structure                         |

Template for new events lives at `../YYYY-MM-DD_Template_Files_for_New_Event/`.

See [event_notes_conventions.md](event_notes_conventions.md) for formatting rules governing notes.md, VCF files, ICS files, and PROJECT.md.

## GenAI Day Series Context

Michael has attended two previous events in this series:

- **Day 4** (October 2024) -- Key takeaway: Generic AI gives generic results; real ROI requires preloading company-specific knowledge (George Churchwell). Most AI projects fail from poor adoption, not bad tech (Om Hashmi).
- **Day 5** (March 2025) -- Key contacts: Skills Development Group team (Chris Knotts, Marc Balcer, Lara Hill, Andy Cooper, Mark Lane); George Churchwell (Mt. Tam Innovations); Zaki Medina (REVIVE Healthcare).

Returning speaker at Day 7: **George Churchwell**, **Zaki Medina**, and David Mantica (host/curator).

## Strategic Intent for Day 7

Michael's target outcomes, ranked:

1. **Conversations with sponsor/presenter orgs that hire or place people** -- IntePros (Stacy Gonyou, staffing), AI Connection Club (Tony Rockliff), Loudon AiGile Network (Toby Rao)
2. **Follow-up threads that can turn into consulting or facilitation work** -- Jordan Plawner (Pacific AI Advisory), George Churchwell (Mt. Tam Innovations)
3. **LinkedIn connections with signal** -- anyone who asks a real question or contributes substance in chat

The goal is **fire, not information**: leave with 2-3 real conversations in progress, not more notes.

## Michael's Motivations and Goals

**The real driver:** Michael needs paid work. Financial, mental health, and relational pressures are real and present. Not someday -- now.

**The pattern to break:** He has been in "ready-ready-ready" mode -- learning, preparing, attending events, accumulating knowledge and contacts -- without converting any of it into paid engagements. He has enough knowledge. Too much. The bottleneck is not skill or information. It is the absence of fire: commitments, conversations in motion, money changing hands.

**What success looks like at this event:** Not more notes. Not more LinkedIn connections. Two or three real conversations that could turn into money within 90 days. A follow-up thread already in motion before the Zoom closes.

**Non-goal:** Learning about AI. Michael already knows this field at depth. If a Claude session is helping him prepare for this event, the question is always "does this help him get paid?" not "does this help him understand something new?"

## Michael's Positioning

He translates between technical depth and organizational reality in AI adoption contexts. Strongest where problems are under-defined, "best practices" have outlived their context, and progress requires changing how people think. Roles that fit: technical enablement lead, AI learning/workflow designer, team effectiveness coach.

See `/Users/michael/repos/Job_Search/visible_paid_work/work_that_finds_me.md` for full framing.
