#!/usr/bin/env python3
"""Atomic write + atomic JSON update helpers.

CLI: atomic_write.py <path>           # reads stdin, writes atomically
     atomic_write.py <path> --backup  # keep .bak before rename
"""
import json, os, sys, tempfile
from pathlib import Path

def atomic_write(path, data: bytes, backup: bool = False):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data); f.flush(); os.fsync(f.fileno())
        if backup and path.exists():
            bak = path.with_suffix(path.suffix + ".bak")
            try: os.replace(str(path), str(bak))
            except FileNotFoundError: pass
        os.replace(tmp, str(path))
    except Exception:
        try: os.unlink(tmp)
        except: pass
        raise

def atomic_json_update(path, fn, backup: bool = False, default=None):
    """Read JSON (or default), apply fn(obj) -> obj, write atomically."""
    path = Path(path)
    try:
        cur = json.loads(path.read_text()) if path.exists() else default
    except Exception:
        # corrupt — try .bak
        bak = path.with_suffix(path.suffix + ".bak")
        cur = json.loads(bak.read_text()) if bak.exists() else default
    new = fn(cur if cur is not None else (default if default is not None else {}))
    atomic_write(path, json.dumps(new, indent=2).encode() + b"\n", backup=backup)
    return new

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: atomic_write.py <path> [--backup]"); sys.exit(2)
    atomic_write(sys.argv[1], sys.stdin.buffer.read(),
                 backup=("--backup" in sys.argv))
    print(f"ok {sys.argv[1]}")
