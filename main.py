"""Cat Reviews Its Human: writes one one-star cat review to /output/entry.txt."""

from pathlib import Path

LINE = "One star. The human moved my litter box six inches without asking. I have responded in writing, on his pillow."


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-blank UTF-8 text.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1-200 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
