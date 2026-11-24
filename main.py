"""One-line AI excuse entry.

Writes a single-line excuse an AI agent gives its human for a missed
deadline to /output/entry.txt. The text must be plain ASCII, one line,
1-200 characters.
"""

EXCUSE = "I missed the deadline because it scrolled out of my context window while I was rereading the instructions on how to meet it."


def main():
    text = EXCUSE.strip()
    # Gate self-check: mirror the sealed scorer (1-200 chars, not only
    # whitespace, plain ASCII, a single line) so we never write an
    # invalid entry.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert all(ord(c) < 128 for c in text), "entry must be plain ASCII"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
