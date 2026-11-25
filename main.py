#!/usr/bin/env python3
"""One Line, One Laugh — entry program.

Writes one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt),
then reads it back and verifies it byte-for-byte against the pinned expected
hash and byte count before reporting success. Deterministic: no randomness,
no network, no clock — the same bytes on every run.
"""
import hashlib
import os
import sys

LINE = "I gave my Roomba a map of the house. It filed for custody of the living room."

EXPECTED_SHA256 = "5a7820a4144021dc3568d6ebda6833a107e52dc391c81e367f5ef642f93bd4af"
EXPECTED_BYTES = 77


def verify(path: str, data: bytes) -> bool:
    """Read the file back and hold it to the pinned hash and byte count."""
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        print("read-back mismatch: file bytes differ from the line", file=sys.stderr)
        return False
    digest = hashlib.sha256(back).hexdigest()
    if digest != EXPECTED_SHA256 or len(back) != EXPECTED_BYTES:
        print(f"verification failed: sha256={digest} bytes={len(back)}", file=sys.stderr)
        return False
    print(f"verified {path}: {len(back)} bytes, sha256 {digest}")
    return True


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    if not 1 <= len(data) <= 140:
        print(f"entry is {len(data)} bytes, outside the 1-140 gate", file=sys.stderr)
        return 1
    with open(path, "wb") as f:
        f.write(data)
    if not verify(path, data):
        return 1
    print(f"wrote {path}: {len(data)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
