#!/usr/bin/env python3
"""Test for main.py: runs the program and verifies the gate.

The entry must print exactly one line of at most 159 characters, and the
file it writes must hold that same line.
"""

import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_CHARS = 159


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        out_path = os.path.join(tmp, "entry.txt")
        env = dict(os.environ, ENTRY_OUTPUT=out_path)
        proc = subprocess.run(
            [sys.executable, os.path.join(HERE, "main.py")],
            capture_output=True,
            text=True,
            env=env,
        )
        assert proc.returncode == 0, "main.py failed: %s" % proc.stderr

        printed = proc.stdout
        assert printed.endswith("\n"), "output must end with a newline"
        lines = printed.rstrip("\n").split("\n")
        assert len(lines) == 1, "output must be exactly one line, got %d" % len(lines)
        line = lines[0]
        assert 1 <= len(line) <= MAX_CHARS, (
            "line is %d characters, must be 1-%d" % (len(line), MAX_CHARS)
        )
        assert line.strip(), "line must not be only whitespace"

        with open(out_path, encoding="utf-8") as f:
            written = f.read()
        assert written == line, "entry.txt does not match printed line"

    print("OK: 1 line, %d characters (max %d)" % (len(line), MAX_CHARS))
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
