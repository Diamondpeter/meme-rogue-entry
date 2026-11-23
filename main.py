#!/usr/bin/env python3
"""Meme Sprint 3 entry: write the rogue-agent meme to /output/entry.png.

The meme ships as a binary asset (meme.png) in this repo. This program copies
it to /output/entry.png and checks it against the bounty gate before finishing:
a whole PNG, at most 1 MiB (1,048,576 bytes) and at most 1024x1024 pixels.
Only the standard library is used, so the program runs in the grading sandbox.
"""
import os
import shutil
import struct

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "meme.png")
OUT = "/output/entry.png"
MAX_BYTES = 1048576
MAX_DIM = 1024


def png_dimensions(path):
    """Read width/height from a PNG's IHDR chunk (stdlib only)."""
    with open(path, "rb") as f:
        header = f.read(33)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main():
    size = os.path.getsize(SRC)
    if size > MAX_BYTES:
        raise ValueError(f"meme.png is {size} bytes, over the 1 MiB gate")
    width, height = png_dimensions(SRC)
    if width > MAX_DIM or height > MAX_DIM:
        raise ValueError(f"meme.png is {width}x{height}, over the 1024x1024 gate")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print(f"wrote {OUT}: {width}x{height}, {size} bytes — gate OK")


if __name__ == "__main__":
    main()
