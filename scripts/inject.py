#!/usr/bin/env python3
"""Bundle a markdown report into a self-contained SpeedRead reader page."""
import argparse
import pathlib
import re
import sys
import webbrowser

SENTINEL = "%%SPEEDREAD_CONTENT%%"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inject a markdown file into the SpeedRead reader template."
    )
    parser.add_argument("markdown", help="path to the report .md file")
    parser.add_argument(
        "-t", "--template",
        help="path to reader.html (default: bundled next to this script)",
    )
    parser.add_argument(
        "-o", "--output",
        help="output path (default: <markdown>.speedread.html)",
    )
    parser.add_argument(
        "--open", action="store_true", help="open the result in your browser"
    )
    args = parser.parse_args()

    md_path = pathlib.Path(args.markdown)
    tpl_path = (
        pathlib.Path(args.template)
        if args.template
        else pathlib.Path(__file__).resolve().parent.parent / "reader.html"
    )
    out_path = (
        pathlib.Path(args.output)
        if args.output
        else md_path.with_suffix(".speedread.html")
    )

    text = md_path.read_text(encoding="utf-8")
    # Escape closing script tags so a code sample can't truncate the page;
    # the reader reverses this on load.
    text = re.sub(r"</script", r"<\\/script", text, flags=re.I)

    html = tpl_path.read_text(encoding="utf-8")
    if html.count(SENTINEL) != 1:
        sys.exit(f"template {tpl_path} is missing the {SENTINEL} sentinel")

    out_path.write_text(html.replace(SENTINEL, text), encoding="utf-8")
    print(out_path)

    if args.open:
        webbrowser.open(out_path.resolve().as_uri())


if __name__ == "__main__":
    main()
