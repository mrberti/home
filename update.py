#!/usr/bin/env python3
"""
Simple python script to download "home" files from github.
"""
import os
from pathlib import Path
from argparse import ArgumentParser
import urllib.error
import urllib.request

URL_TEMPLATE = "https://raw.githubusercontent.com/mrberti/home/master/{filename}"
DEFAULT_FILES = [
    ".bash_aliases",
    ".bashrc",
    ".conkyrc",
    ".gitconfig",
    ".gvimrc",
    ".inputrc",
    ".minttyrc",
    ".profile",
    ".tmux.conf",
    ".vimrc",
    "DIR_COLORS.cygwin",

]
PROMPT_OVERWRITE = "Do you want to overwrite {filename}? [Y/n]"
VALID_YES = ["y", "j", "yes"]

def ask_yes_no(prompt, default="y"):
    print(prompt)
    try:
        choice = input().lower() or default
    except KeyboardInterrupt:
        print("User cancellation")
        raise SystemExit(1)
    return choice in VALID_YES

def main():
    parser = ArgumentParser()
    parser.add_argument(
        "files",
        nargs="*",
        default=DEFAULT_FILES,
        help="A list of files to be updated. If not specified, a default list is used.",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Force file overwriting",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=Path.home().absolute(),
        type=str,
        help="Output directory. Defaults to user $HOME.",
    )
    parser.add_argument(
        "-l",
        "--linesep",
        default=os.linesep,
        choices=["\n", "\r\n", "\r"],
        metavar=["\n", "\r\n", "\r"],
        help="Define the line separator to use. Defaults to `os.linesep`. Hint: When using bash, use $'\\n' to specify.",
    )

    args = parser.parse_args()
    files = args.files
    force = args.force
    outpath = Path(args.output)
    linesep = args.linesep
    print(f"Using line separator: {linesep!r}.")
    print(f"Using {outpath.absolute()} as output directory.")

    for filename in files:
        outfile: Path = outpath / filename
        if not force:
            if outfile.exists():
                if not ask_yes_no(PROMPT_OVERWRITE.format(filename=outfile.absolute())):
                    continue
        try:
            with urllib.request.urlopen(URL_TEMPLATE.format(filename=filename)) as req:
                data = req.read().decode("utf-8")
            print(f"Writing {filename} to {outfile.absolute()}")
            with open(outfile, "w", newline=linesep) as f_out:
                f_out.write(data)
        except urllib.error.HTTPError as exc:
            print(f"{filename}: {exc}")
        except FileNotFoundError as exc:
            print(f"{exc}")

if __name__ == "__main__":
    main()
