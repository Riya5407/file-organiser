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
python main.py
# Enter folder path when prompted
What it does:
Scans a directory
Sorts files into Images/, Documents/, Videos/, Audio/, Archives/, Scripts/, Others/
Auto-renames on collision (file_1.jpg, file_2.jpg)
Supported categories:
Table
Category	Extensions
Images	.jpg, .jpeg, .png, .gif
Documents	.pdf, .docx, .txt
Videos	.mp4, .avi, .mkv
Audio	.mp3, .wav, .aac
Archives	.zip, .rar, .tar, .gz
Scripts	.py, .js, .sh
🔍 v2: Smart Organizer (scanner.py)
Production-grade tool built on lessons from v1. Handles the messy reality of real folders.
bash
# Step 1: Always preview first
python scanner.py --path "C:\Users\You\Downloads" --dry-run

# Step 2: Execute when satisfied
python scanner.py --path "C:\Users\You\Downloads" --output "C:\Users\You\Desktop\Organized"
What v2 Adds
Table
Capability	How It Works
True duplicate detection	SHA-256 content hashing — catches renamed copies
Dry-run safety	Preview every move before touching files
Date organization	PDFs/2026-06/report.pdf instead of dumping in one folder
Cross-drive moves	shutil.move() handles C: → D: seamlessly
Smart hashing	Skips hashing files with unique sizes (2-10x faster)
Collision handling	file.jpg → file_1.jpg → file_2.jpg automatically
Ignored directories	Skips .git/, node_modules/, __pycache__/, .venv/
JSON audit trail	organizer_report.json logs every action for review
CLI Reference
Table
Flag	Description	Default
--path	Source directory to organize	~/Downloads
--output	Destination for organized files	~/Desktop/Organized_Files
--dry-run	Preview without moving anything	False
🛠️ Installation
bash
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