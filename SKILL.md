---
name: speedread-report
description: Turn a markdown summary/report into a pop-up RSVP speed-reader the user can consume at 500+ WPM. Use when the user asks for a report, summary, digest, or research writeup they want to "speedread", or says things like "make me a report and load it into the reader". Writes the report as markdown, injects it into a self-contained HTML reader, and opens it in the browser.
---

# SpeedRead Report

Produce a markdown report, ship it into the bundled `reader.html` template, and pop it open in the user's browser. The reader paces the text semantically: headings hold and reset the speed ramp, bold terms slow down, code blocks and tables pause the stream entirely.

There are four steps. Do them all in one go — the user should ask once and see the reader open.

## Step 1 — Write the report (RSVP authoring rules)

Write the report as a normal `.md` file, but author it for single-word streaming. These rules make the difference between a pleasant 500 WPM read and a wall of mush:

- **Front-load conclusions.** TL;DR or verdict first, evidence after. The reader can bail out early.
- **A `##` heading every 100–200 words.** Headings are the reader's pause points and its navigation targets (←/→ jump by section). Use `###` for sub-points. Exactly one `#` title at the top — it becomes the document title.
- **Short sentences.** Under ~20 words. Sentence-end pauses are the reader's rhythm; long sentences starve it.
- **Bold the load-bearing tokens.** Key numbers, names, verdicts: `**43% regression**`. The reader slows ~25% on bold words and the user's eye catches them.
- **Bullets over dense prose** for enumerable facts. Each item gets its own end-pause.
- **Code blocks and tables halt playback** and display whole until the user presses Space. Use them sparingly and keep them narrow (< ~80 chars wide, < ~20 rows).
- **No raw HTML, no images.** Images are reduced to their alt text; links are reduced to their link text (so make the text meaningful, not "here").
- Sweet spot is **300–2,500 words**. Above that, split into multiple reports.

## Step 2 — Inject into the template

Use the bundled injector (in this skill's directory):

```bash
python scripts/inject.py report.md
```

It writes `report.speedread.html` next to the report (add `-o path` to override, `--open` to also launch the browser). PowerShell alternative if Python is unavailable:

```powershell
.\scripts\inject.ps1 report.md
```

If you cannot run the scripts, do the injection manually: copy `reader.html`, escape `</script` as `<\/script` in the markdown (the reader un-escapes it — without this, an HTML/JS code block in the report would truncate the document), then replace the single sentinel line `%%SPEEDREAD_CONTENT%%` with the escaped markdown.

```python
import pathlib, re
text = pathlib.Path("report.md").read_text(encoding="utf-8")
text = re.sub(r"</script", r"<\\/script", text, flags=re.I)
html = pathlib.Path("reader.html").read_text(encoding="utf-8")
pathlib.Path("report.speedread.html").write_text(
    html.replace("%%SPEEDREAD_CONTENT%%", text), encoding="utf-8")
```

## Step 3 — Open it

- Windows: `Start-Process "report.speedread.html"` (PowerShell) or `start "" "report.speedread.html"` (cmd)
- macOS: `open report.speedread.html`
- Linux: `xdg-open report.speedread.html`

(Or pass `--open` to `inject.py` and skip this step.)

## Step 4 — Tell the user

After opening, give the user a one-line recap of the controls:

> Space = play/pause · ← → = jump sections · , . = ±15 words · R = restart · D = full document view · click the word to play/pause. All settings (speed, font size, sentence pause, letter spacing, focus position, highlight color, font, dark mode, and the Markdown Pacing panel for heading/paragraph/list/bold/code timing) save automatically in your browser.

## Notes

- The reader is one self-contained file: no server, no dependencies, no build step. The report never leaves the user's machine (the only network request is a Google Fonts stylesheet, which falls back to system fonts offline).
- Preferences persist via `localStorage`.
- Opening `reader.html` directly (sentinel un-replaced) shows a built-in demo — useful for a quick smoke test.
- The keyboard shortcuts require a desktop browser; on mobile, tapping the word toggles play/pause.
