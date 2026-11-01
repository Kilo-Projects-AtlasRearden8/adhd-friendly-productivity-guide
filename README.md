# Low-Energy Productivity for ADHD Brains

A beginner manual for getting things done when your energy is low, your
executive function is tired, and "just try harder" has never worked.

Covers tiny tasks, body-doubling, and energy-friendly routines, plus
printable worksheets you can fill out by hand. Plain English, warm,
shame-free, tested, and local-first — no account, no app, no tracking.

## Who this is for

This guide is for anyone who:

- Has ADHD (diagnosed or self-identified) and struggles to start tasks
- Runs out of energy before the day runs out of tasks
- Feels shame or guilt about unfinished to-do lists
- Wants a gentler, body-friendly way to be productive

You do not need a diagnosis to use this. You just need to be tired of
productivity advice that assumes unlimited willpower.

## What's inside

| Folder | Contents |
|--------|----------|
| `docs/` | Beginner manual in plain markdown: introduction, tiny tasks, body-doubling, energy-friendly routines, printable worksheets index |
| `site/` | Static HTML version of the manual — open any file in a browser |
| `worksheets/` | Printable worksheets: tiny task planner, body-doubling session log, energy map, gentle daily routine |
| `STATUS.md` | What was built, how to run it, verification results, known gaps |
| `LICENSE` | MIT License |

## Main ideas

**Tiny tasks.** Break work down until the first step feels ridiculous to skip.
A task that takes two minutes is a perfect place to start.

**Body-doubling.** Work alongside another person (in person or online) to help
your brain stay on track. You do not have to do the same task, or even talk.

**Energy-friendly routines.** Match tasks to the energy you actually have
today, not the energy you wish you had. Rest is part of the plan, not a
failure.

## How to use it

1. Read the manual in `docs/`, or open `site/index.html` in your browser for
   the web version.
2. Print any worksheet from `worksheets/` (File → Print, or Ctrl+P / Cmd+P)
   and fill it out by hand. Black and white saves ink.
3. There is no wrong way to fill these out. Blank is fine. Half-finished is
   fine.

## Test it

This project includes a verification script and HTML lint:

```bash
python3 verify.py        # link checks, license check, secret scan
npx htmlhint "site/**/*.html" "worksheets/**/*.html"  # markup lint
```

## Credit

Created and published by **Asdale Dynamics, LLC** (Indiana, formed October
2026). Asdale Dynamics makes beginner-friendly AI education, books, guides,
and practical tools — including accessible life-admin helpers like this one.

Dylan Asdale is a registered nurse turned AI author and founder of Asdale
Dynamics, LLC. His book *The Massive AI Manual* and hub site
dylanasdale.github.io explain AI "like a friend would": plain English, step by
step, never condescending.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.

## About Asdale Dynamics, LLC

Asdale Dynamics publishes beginner-friendly AI education, books, and guides,
plus practical tools and small-business helpers: AI tools and agents/MCP,
local AI, free AI coding, GitHub, automation, privacy, KDP/book publishing,
marketing, reselling, bookkeeping, accessible life-admin helpers, healthcare
worker AI aids (education only, never medical advice), and fun extras like
FFXIV and chess tools.
