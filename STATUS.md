# STATUS

## What was built

A beginner manual on low-energy productivity for ADHD brains, published by
Asdale Dynamics, LLC (Indiana, formed October 2026). Plain English, warm,
shame-free, tested, local-first — no account, no app, no tracking.

- `docs/` — beginner manual in markdown:
  - `README.md` — manual overview and contents
  - `introduction.md` — what low-energy productivity means, shame-free framing
  - `tiny-tasks.md` — breaking work into steps small enough to start
  - `body-doubling.md` — working alongside another person
  - `energy-friendly-routines.md` — matching tasks to the energy you have
  - `printable-worksheets.md` — index of printable worksheets
- `site/` — static HTML version of the manual:
  - `index.html` — landing page
  - `tiny-tasks.html`, `body-doubling.html`, `energy-routines.html`,
    `worksheets.html`
  - `assets/css/style.css` — calm warm styles with print-friendly overrides
  - `assets/js/main.js` — mobile menu and print hint
- `worksheets/` — printable worksheets (HTML, formatted for print via
  File → Print), each with a non-printing "Return to the site" link:
  - `tiny-task-planner.html`
  - `body-doubling-session-log.html`
  - `energy-map.html`
  - `gentle-daily-routine.html`
- `LICENSE` — MIT License, copyright line exactly
  `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — project overview crediting Asdale Dynamics, LLC and Dylan
  Asdale; includes what's inside, how to use, how to test, and LLC context
- `package.json` — npm test/lint/verify scripts
- `verify.py` — link/HTML/license/secret verification script
- `STATUS.md` — this file

Git: initialized, commits on `master`, plain messages, no co-author
trailers, existing git identity used. Nothing pushed, no remote created,
nothing published.

## How to run it

- Read the manual: open any file in `docs/`, or browse `site/index.html` in a
  web browser.
- Print worksheets: open any file in `worksheets/`, then File → Print
  (Ctrl+P / Cmd+P). Black and white recommended.
- No build step, no server, no install. Open files directly from this folder.
- Run checks: `npm test` (runs `verify.py`) and `npm run lint`
  (runs htmlhint).

## Verification results

- `python3 verify.py` / `npm test`: 9 HTML files checked, 0 errors, 0 warnings.
  - All internal links resolve to existing files
  - No external URLs (local-first)
  - `LICENSE` contains the exact copyright line
  - `README.md` credits Asdale Dynamics, LLC
  - Docs links to worksheets all resolve
  - Secret/key pattern scan: clean
- `npx htmlhint site/**/*.html worksheets/**/*.html` / `npm run lint`: 9
  files scanned, no errors.
- `npm test` exits 0.

## Known gaps

- Worksheets are HTML-for-print, not fillable PDFs; printing requires a
  browser and printer (or print-to-PDF).
- No PDF export of the full manual.
- Verification covers links and markup only, not visual rendering or
  screen-reader testing.
- Body-doubling solo options are suggestions only; no pairing service is
  included.
- Content is educational/life-admin support, not medical advice (consistent
  with Asdale Dynamics' healthcare-worker aid scope).
