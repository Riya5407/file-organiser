# 📂 File Organizer

<div align="center">

**Automated workspace cleaning — from simple sorting to production-grade duplicate detection.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## 🚀 What's Inside

| Tool | Purpose | Best For |
|------|---------|----------|
| **`main.py`** | Fast extension-based sorting | Quick cleanups, known folders |
| **`scanner.py`** | Smart duplicate-aware organizer | Large downloads, messy archives, safety-first workflows |

Both tools are **non-destructive by default** and handle filename collisions automatically.

---

## 📁 v1: Extension Organizer (`main.py`)

The original. Lightweight, interactive, zero configuration.

```bash
git clone https://github.com/Riya5407/file-organiser.git
cd file-organiser
Requires: Python 3.10+ (standard library + no external deps for v1; v2 uses pathlib, hashlib, argparse, json, datetime, shutil, collections — all built-in)
📊 v1 vs v2: When to Use What
Table
Scenario	Use
"I have 50 files, just sort them"	main.py
"My Downloads has 10,000 files and I don't know what's in there"	scanner.py --dry-run
"I think I have duplicate photos everywhere"	scanner.py
"I need to organize a work folder safely"	scanner.py --dry-run first
"I'm on a slow/old machine"	main.py (no hashing overhead)
🧠 Design Notes
v1 taught me: File I/O, path manipulation, basic categorization logic.
v2 taught me: Hashing, memory efficiency (chunked reads), CLI design, defensive programming (dry-runs, error handling), cross-platform path handling, and why "production-grade" means "never surprise the user."
This repo is a learning log, not just a tool.
🤝 Contributing
Issues and PRs welcome. Particularly interested in:
rich integration for terminal UI
Config file support (YAML rules for custom categories)
pytest test coverage
📄 License
MIT License — see LICENSE for details.
<div align="center">
Built with ❤️ by Riya5407
</div>
```