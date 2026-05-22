# Otto Hilska -- Meeting Notes & Backgrounder

## Meeting Notes

**Call:** 2026-05-21, 30 min, with Otto Hilska (CEO, Swarmia)

- Looking for anyone **"doing software at scale"** -- that's their ICP signal
- **Dogfooding their own product** -- using Swarmia internally to measure their own team
- Long-term investments **do** pay off -- and Swarmia lets you see the short-term signal that confirms it sooner
- Developers use the metrics to **build the case against bit rot** -- data as internal advocacy tool
- Their team is at **2x output** vs. teams that pushed AI hard but had untested codebases underneath
- **Myth of the 10x developer** -- what they actually see in the data is ~10% gains, not 10x; hype vs. reality gap is a product positioning angle for them

---

## Meeting Prep

**Meeting:** Thursday, 2026-05-22 (30 min), booked via Jess Wolfe  
**Context:** Jess offered the link after Michael complimented her GenAI Day session  
**Meeting link framing:** "Partner" slot -- utm_campaign=genai-day-2026

---

## Otto Hilska

- **Role:** Founder & CEO, Swarmia (since 2019)
- **LinkedIn:** [linkedin.com/in/hilska](https://www.linkedin.com/in/hilska/)
- **Location:** Helsinki, Finland
- **Forbes Technology Council:** Member since Oct 2023

### Career arc

| Role                  | Company                                          | Years        |
|-----------------------|--------------------------------------------------|--------------|
| Co-founder & CEO      | Flowdock (chat for dev teams -- sold to HipChat) | 2011-2013    |
| Product Line Director | Rally Software                                   | 2013-2015    |
| VP Engineering        | Smartly.io                                       | 2015-2018    |
| Chief Product Officer | Smartly.io                                       | 2018-2019    |
| Founder & CEO         | Swarmia                                          | 2019-present |

**Pattern:** Serial builder. Built a developer communication tool (Flowdock), scaled an ad-tech SaaS to 100+ eng (Smartly.io), then started Swarmia. He comes from product/engineering leadership, not sales or marketing. Conversations with him will be technical and direct.

**Public voice:** Posts on LinkedIn about AI coding tool measurement, developer visibility, engineering org design. His take on GenAI coding tools (Copilot, Cursor) centers on whether you can actually measure their productivity impact -- not hype, evidence.

**Podcast:** Modern CTO (Oct 2023) -- topic was "upleveling conversations" and why better communication drives business progress. He thinks in systems.

---

## Swarmia -- The Product

**What it is:** Engineering intelligence platform for engineering leaders and CTOs.

**Core problem it solves:** Engineering teams have no shared, trusted view of their own productivity. Product teams have analytics; eng teams have vibes and Jira tickets. Swarmia gives eng leaders the same data-informed visibility that product teams have for user behavior.

### What it measures

- **DORA metrics** -- deployment frequency, lead time, change failure rate, mean time to recovery
- **Flow metrics** -- cycle time, batch size, PR throughput, review time
- **Investment allocation** -- feature work vs. bugs vs. debt (how is team time actually spent?)
- **Developer experience** -- recurring surveys, qualitative feedback analysis

### AI-specific features (directly relevant to Michael's work)

- Tracks **GitHub Copilot, Cursor, and Claude Code** license usage -- who has it, who's actually using it, unused licenses
- Compares **AI-assisted PRs vs non-AI PRs** across cycle time, throughput, batch size, review time
- Surfaces adoption trends by team -- who's leading, who's lagging
- Detects workflow inefficiencies and proposes team-specific actions (AI-powered signals)

**Translation:** Swarmia can show *before/after* data when a team starts adopting AI tools. That's measurement for exactly the coaching work Michael does.

### Company facts

- Founded: 2019, Helsinki, Finland
- Funding: $11M Series A (Karma Ventures, DIG Ventures, Alven, Lifeline Ventures)
- G2 Leader: Spring 2026 reports
- Pricing: ~$4,500-$27,000/yr depending on team size; free tier for teams ≤ 9 devs
- Integrations: GitHub, GitLab, Jira, Linear

---

## Jess Wolfe's Talk -- Quick Reference

**Title:** "Stop Using a Sledgehammer: Matching AI Autonomy to the Task at Hand"

### Framework: Five Levels of AI Autonomy

| Level | Name              | Description                                    |
|-------|-------------------|------------------------------------------------|
| L1    | Assist            | Autocomplete, inline suggestion                |
| L2    | Conversational    | Back-and-forth chat (where most teams plateau) |
| L3    | Task Agent        | Agent executes a bounded task                  |
| L4    | Autonomous        | Agent runs without human checkpoint            |
| L5    | Agentic Avalanche | Agents orchestrating agents                    |

**Key insights:**

- The human chooses the level -- not the tool, not the task
- Most teams plateau at L2 because that's all they've been trained on
- Higher is NOT better; right-sizing to the task is the goal
- Core refrain: "Do you have a clear Definition of Done? DoD is your Definition of 'Ready for AI'"
- Audience engagement: interactive examples throughout -- show, don't tell

**Your connection point with Jess:** You told her the L1-L5 engagement style impressed you more than the framework itself. She connects people to Otto.

---

## Otto's Presence at GenAI Day

| Role                | Details                                                                                                                              |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Sponsor/partner** | Swarmia was an event sponsor; Jess presented as their CSM                                                                            |
| **Not a speaker**   | Otto didn't appear on stage; Jess was the Swarmia voice                                                                              |
| **Poster**          | Otto's LinkedIn post on GenAI coding tools (Copilot, Cursor productivity measurement) predates the event but is thematically aligned |
| **Meeting offer**   | Partner meeting slots published with utm_campaign=genai-day-2026 -- this is a channel he's actively working                          |

---

## The Conversation

### Your positioning (from notes.md)

> "I help teams build AI adoption habits. You measure whether it's working. I don't have clients to send you today, but I want to understand your product well enough to know when to recommend it -- and whether there's a referral relationship that makes sense."

That framing is honest and correct. Don't oversell. He's a founder -- he'll see through anything inflated.

### Complementary, not competing

- Michael helps teams build the habit and the muscle (mob programming, embedded coaching, time-boxed engagements)
- Swarmia measures whether it's working (adoption rates, PR velocity, DORA trends)
- A team that hires Michael and deploys Swarmia gets both the doing and the seeing

### Questions worth asking

1. "Who typically brings Swarmia in -- the CTO, or someone on the team?" (Tells you the buying pattern)
2. "When a team shows low AI adoption in your data, what do they usually do about it?" (Is there a services gap he's aware of?)
3. "What does a good partner referral look like for you?" (Direct; he'll appreciate it)

### What to listen for

- Does he have a services/implementation partner model, or is it pure SaaS?
- Does he see coaching/facilitation practitioners as a referral channel?
- What's the typical eng team size using Swarmia? (Helps you know if your clients would be a fit)

---

## Quick Intro (30-second version)

> "I work with engineering teams on AI adoption -- specifically helping them build the habit and the muscle, not just the license. Mob programming with AI in the loop is my main vehicle. What you build is the measurement layer that shows whether any of that is working. I wanted to understand your product well enough to know when to recommend it."

---

## Post-meeting message to Otto

LinkedIn connection request:

> Otto -- good conversation today. The 10% vs. 10x reframe is one I'll be using. Teams doing software at scale who are serious about measurement are exactly where I work. Let's stay connected.

---

## Post-meeting message to Jess

> Jess -- just got off the call with Otto. Useful conversation. Appreciate you making the introduction.

(Keep it short. She didn't reply to your pre-meeting note -- acknowledge the intro, nothing more.)

---

## Sources

- [Otto Hilska -- Crunchbase](https://www.crunchbase.com/person/otto-hilska)
- [Otto Hilska -- The Org](https://theorg.com/org/swarmia/org-chart/otto-hilska)
- [Swarmia About Us](https://www.swarmia.com/about-us/)
- [Swarmia AI adoption metrics docs](https://help.swarmia.com/ai-assistant-metrics/ai-adoption-metrics)
- [Swarmia AI tools docs](https://help.swarmia.com/features/ai-tools)
- [Swarmia $11M Series A](https://technews180.com/funding-news/swarmia-raises-11m-series-a-to-scale-engineering-tools/)
- [Swarmia G2 Reviews 2026](https://www.g2.com/products/swarmia/reviews)
- [Otto Hilska -- Modern CTO Podcast](https://moderncto.io/otto-hilska/)
- [Otto Hilska -- Eventible Speaker Profile](https://www.eventible.com/speakers/profile/otto-hilska-2812)
- [Measuring productivity impact of AI coding tools -- Swarmia blog](https://www.swarmia.com/blog/productivity-impact-of-ai-coding-tools/)
