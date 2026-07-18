# speedread-skill

**Read content written by your coding agent 3.5x faster.**

![MIT license](https://img.shields.io/badge/license-MIT-green) ![zero dependencies](https://img.shields.io/badge/dependencies-none-blue)

https://github.com/user-attachments/assets/20ed5914-c4fb-488b-b61e-d14ee8191761

Coding agents produce a lot of text to read. Even with conciseness prompts, I got tired of scrolling through mine. With this skill, the agent writes its report as markdown, bundles it into a single self-contained HTML file, and opens it in your browser as an [RSVP](https://en.wikipedia.org/wiki/Rapid_serial_visual_presentation) speed-reader that shows one word at a time at a fixed focal point. The range runs from 100 to 1600 WPM. 

Right off the bat, most people can get 2.5-3.5x reading speed increase, and with practice, you could read at upwards of 6x.

The reader is built around markdown structure:

- **Headings** stream through the same anchor point in ALL CAPS and your focus color, so you register a new section without your eyes ever moving
- `←`/`→` jump between sections; `,`/`.` nudge by 15 words
- A **time saved** readout for the current report at your settings, plus an all-time counter measured against the commonly cited average reading speed of 238 WPM
- **Bold** words run about 25% slower, and `inline code` holds longer in monospace
- **Code blocks and tables** stop the stream and display whole until you continue
- Lists, paragraphs, and long words each get their own pause rules
- Press **D** anytime for a fully rendered document view

All of the settings above are saved and tweakable between sessions. 

## Try it in ten seconds

Open [`reader.html`](reader.html) in a browser. It ships with a built-in demo document. Press Space.

## Install

**Claude Code**: clone it into your skills directory.

```bash
# available in every project
git clone https://github.com/jordan-gibbs/speedread-skill ~/.claude/skills/speedread-report

# or just this project
git clone https://github.com/jordan-gibbs/speedread-skill .claude/skills/speedread-report
```

Then ask for it naturally ("audit this repo and give me a report I can speedread") or invoke it directly with `/speedread-report`.

**Any other agent** (Cursor, Codex, custom): point it at [`SKILL.md`](SKILL.md). The instructions are plain markdown that covers the writing guidelines for RSVP-friendly reports and how to bundle the file and open it, so any agent that can write files and run a shell command can follow them.

**No agent at all**: the injector works standalone.

```bash
python scripts/inject.py my-report.md --open
```

## How it works

1. **The agent writes the report** following the authoring rules in `SKILL.md`: conclusions first, a heading every 100–200 words, bold on the numbers that matter. Reports written for RSVP read far better than ones that weren't.
2. **The markdown is injected** into a copy of `reader.html`. A sentinel line gets replaced, and `</script` sequences get escaped so code samples can't truncate the page.
3. **The file opens in your browser.** There's no server or build step. The whole reader is one HTML file, markdown parser and settings panel included.

## Controls

| Key | Action |
| --- | --- |
| `Space` | Play / pause / continue past a block |
| `←` `→` | Previous / next section |
| `,` `.` | Skip back / forward 15 words |
| `R` | Restart |
| `D` | Toggle full document view |
| `Esc` | Pause (or close document view) |

Settings persist in `localStorage` between reports: speed, font size, sentence pause, letter spacing, focus position, highlight color, five monospace fonts, and dark mode. The **Markdown Pacing** panel exposes the structural rules as well. Heading slowdown, paragraph and list-item pauses, bold and code slowdown, and ramp-up length are all adjustable and saved, with a one-click reset to defaults.

## Privacy

Your report never leaves your machine. The only network request that the reader makes is for a Google Fonts stylesheet, and if you're offline it falls back to system fonts.

## Credits

The RSVP engine is a portable cousin of the reader at [speedread.life](https://speedread.life); the ORP centering and the sentence-end detection started there.

## Contributing

Issues and PRs are welcome. I've kept everything in one file (`reader.html`) on purpose. Keep changes dependency-free and self-contained.

## License

[MIT](LICENSE)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=jordan-gibbs/speedread-skill&type=Date)](https://star-history.com/#jordan-gibbs/speedread-skill&Date)
