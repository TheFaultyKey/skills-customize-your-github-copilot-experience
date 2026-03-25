#!/usr/bin/env python3
"""Starter code for Python Text Processing assignment.

Usage:
    python3 starter-code.py input.txt cleaned.txt --top 10

This script provides simple helpers for cleaning text and computing word frequencies.
"""
import argparse
import collections
import string
from pathlib import Path


def clean_text(text: str) -> str:
    translator = str.maketrans('', '', string.punctuation)
    cleaned = text.translate(translator)
    cleaned = ' '.join(cleaned.split()).lower()
    return cleaned


def read_file(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def write_file(path: Path, text: str) -> None:
    path.write_text(text, encoding='utf-8')


def word_frequencies(text: str) -> collections.Counter:
    words = text.split()
    return collections.Counter(words)


def main():
    parser = argparse.ArgumentParser(description='Text processing starter')
    parser.add_argument('input', help='Input text file')
    parser.add_argument('output', help='Output cleaned file')
    parser.add_argument('--top', type=int, default=10, help='Top N words to show')
    args = parser.parse_args()

    inp = Path(args.input)
    out = Path(args.output)

    raw = read_file(inp)
    cleaned = clean_text(raw)
    write_file(out, cleaned)

    freqs = word_frequencies(cleaned)
    for word, count in freqs.most_common(args.top):
        print(f"{word}: {count}")


if __name__ == '__main__':
    main()
