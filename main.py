"""Six Words, One Story — make.fun entry.

Writes the story, exactly six words, to entry.txt in the output
directory the grader provides (MAKEFUN_OUTPUT_DIR, default /output).
Standard library only; no network, no files read.
"""

import os

STORY = "The clone sued for its childhood."


def main():
    words = STORY.split()
    if len(words) != 6:
        raise ValueError(f"story must be exactly six words, got {len(words)}")
    if not (1 <= len(STORY) <= 60):
        raise ValueError("story must be 1 to 60 characters for the gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
