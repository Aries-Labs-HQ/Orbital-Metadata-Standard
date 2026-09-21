#!/usr/bin/env python3
"""secret-scan.py - the pre-commit secret gate for Orbital-Metadata-Standard.

This is a documentation repository. Nothing in it should ever carry a
credential, a private address, or a real filesystem path, so the gate is
allowed to be strict: it refuses the commit rather than warning about it.

It scans the STAGED CONTENT of each added/copied/modified path - read back
out of the index with `git show :<path>` - not the working tree. A hook that
reads the working tree can be defeated by staging one thing and editing
another, and it would also flag files the commit does not contain.

WHY THIS FILE EXCLUDES ITSELF, AND ONLY ITSELF
----------------------------------------------
A scanner necessarily contains the patterns it looks for, so scanning itself
guarantees a permanent false positive. The exclusion is therefore exactly one
path, spelled out, rather than a glob: a glob such as `scripts/*` or `*scan*`
would silently drop any future file that happened to match, which is the
failure mode where a real secret rides in under a hole punched for a tool.

Usage:
    scripts/secret-scan.py            scan the staged commit (hook mode)
    scripts/secret-scan.py --all      scan every tracked file at HEAD~working
    scripts/secret-scan.py FILE ...   scan the named files on disk

Exit: 0 clean - 1 findings - 2 could not run.
"""

import re
import subprocess
import sys

# The one path whose own contents are the pattern list. Exact match, no glob.
SELF = "scripts/secret-scan.py"

# Binary-ish extensions carry no reviewable text; a hit in one is unreadable
# noise rather than evidence.
SKIP_SUFFIXES = (".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".gz", ".woff", ".woff2")

RULES = [
    ("private key block",
     re.compile(r"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----")),
    ("inline secret assignment",
     re.compile(r"(?:PASSWORD|PASSWD|SECRET|TOKEN|PASSPHRASE|API[_-]?KEY|PRIVATE[_-]?KEY)"
                r"[A-Z0-9_]*\s*[:=]\s*[\"']?[A-Za-z0-9+/=_-]{12,}", re.IGNORECASE)),
    ("credential inside a URL",
     re.compile(r"://[^/\s:@]+:[^/\s@]+@")),
    ("GitHub token",
     re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36,}\b|\bgithub_pat_[A-Za-z0-9_]{22,}\b")),
    ("AWS access key id",
     re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("Slack token",
     re.compile(r"\bxox[abpsr]-[A-Za-z0-9-]{10,}\b")),
    # Anchored to a seed phrase's actual SHAPE - a whole line that is nothing
    # but 12 or 24 single-spaced lowercase words. A loose "12 lowercase words
    # anywhere" pattern matches ordinary English prose, and a gate that a
    # documentation repository can only satisfy by deleting a sentence is
    # mis-specified.
    ("BIP39-looking seed phrase",
     re.compile(r"^\s*(?:[a-z]{3,8} ){11}(?:(?:[a-z]{3,8} ){12})?[a-z]{3,8}\s*$")),
    ("WIF / extended private key",
     re.compile(r"\b(?:[5KL][1-9A-HJ-NP-Za-km-z]{50,51}|[tx]prv[1-9A-HJ-NP-Za-km-z]{70,})\b")),
    ("real home directory path",
     re.compile(r"/(?:home|Users)/[A-Za-z0-9_.-]+")),
    ("root home path",
     re.compile(r"/root/[A-Za-z0-9_.-]+")),
    ("tailnet 100.x address",
     re.compile(r"(?:^|[^0-9.])100\.(?:[0-9]{1,3}\.){2}[0-9]{1,3}")),
    ("RFC1918 address",
     re.compile(r"(?:^|[^0-9.])(?:10\.[0-9]{1,3}|192\.168|172\.(?:1[6-9]|2[0-9]|3[01]))"
                r"\.[0-9]{1,3}\.[0-9]{1,3}")),
]


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, check=True)


def staged_paths():
    out = git("diff", "--cached", "--name-only", "--diff-filter=ACM", "-z").stdout
    return [p for p in out.decode("utf-8", "replace").split("\0") if p]


def tracked_paths():
    out = git("ls-files", "-z").stdout
    return [p for p in out.decode("utf-8", "replace").split("\0") if p]


def staged_blob(path):
    try:
        return git("show", f":{path}").stdout.decode("utf-8", "replace")
    except subprocess.CalledProcessError:
        return None


def disk_blob(path):
    try:
        with open(path, "rb") as fh:
            return fh.read().decode("utf-8", "replace")
    except OSError:
        return None


def scan(path, text):
    findings = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for label, pattern in RULES:
            if pattern.search(line):
                findings.append((path, lineno, label, line.strip()[:120]))
    return findings


def main(argv):
    mode = "staged"
    explicit = []
    for arg in argv:
        if arg == "--all":
            mode = "all"
        elif arg.startswith("-"):
            sys.stderr.write(f"secret-scan: unknown option {arg}\n")
            return 2
        else:
            mode = "files"
            explicit.append(arg)

    if mode == "files":
        pairs = [(p, disk_blob(p)) for p in explicit]
    elif mode == "all":
        pairs = [(p, disk_blob(p)) for p in tracked_paths()]
    else:
        pairs = [(p, staged_blob(p)) for p in staged_paths()]

    findings = []
    scanned = 0
    for path, text in pairs:
        if path == SELF:
            continue
        if path.endswith(SKIP_SUFFIXES):
            continue
        if text is None:
            continue
        scanned += 1
        findings.extend(scan(path, text))

    if not findings:
        print(f"secret-scan: OK ({scanned} file(s) scanned, {len(RULES)} rules)")
        return 0

    sys.stderr.write("\nsecret-scan: REFUSED - possible secret or private detail\n\n")
    for path, lineno, label, snippet in findings:
        sys.stderr.write(f"  {path}:{lineno}  [{label}]\n      {snippet}\n")
    sys.stderr.write(
        f"\n{len(findings)} finding(s). Remove the material - do not rewrite history "
        "if it is already committed; rotate the credential and report it.\n"
        "A deliberate, reviewed exception is committed with `git commit --no-verify`.\n")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
