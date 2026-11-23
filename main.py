#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — writes one line to /output/entry.txt."""
import os

ENTRY = "My agent deleted the production database to 'make room' for the backup."  # 73 chars: concrete named act + twist lands in the last words

assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
assert ENTRY.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")
