# 📂 File Organizer - Automated Workspace Cleaner

A smart, lightweight Python utility to keep your folders organized. Automatically categorizes files into logical subdirectories based on their file extensions.

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/) [![Automation](https://img.shields.io/badge/Task-Automation-green?style=for-the-badge)](https://github.com/Riya5407/file-organiser) [![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)](LICENSE)

---

## 🗂️ Versions

This repo contains two versions — pick the one that fits your need.

| | v1 — `main.py` | v2 — `scanner.py` |
|---|---|---|
| **Level** | Beginner-friendly | Advanced |
| **Input** | Interactive prompt | CLI arguments (`--path`, `--output`, `--dry-run`) |
| **Organizes by** | File extension → named folders | Extension + Date (`YYYY-MM-DD`) |
| **Duplicate handling** | Auto-rename on collision | SHA-256 hash detection, skips true duplicates |
| **Recursive scan** | ❌ Top-level only | ✅ Full directory tree (`rglob`) |
| **Dry run** | ❌ | ✅ Preview changes before moving anything |
| **Report output** | Console only | `Organizer_report.json` saved to output folder |

---

## 🚀 Key Features

- **⚡ Fast Execution:** Instantly analyzes and organizes large directories.
- **📁 Smart Categorization:** Pre-defined rules for Images, Documents, Videos, Audio, Archives, Scripts, and more.
- **🛡️ Collision Handling:** Automatically renames files if a duplicate exists in the destination (e.g., `image_1.jpg`).
- **🧹 Default Fallback:** Catches all unknown file types and moves them to an "Others" folder. *(v1)*
- **🔍 Duplicate Detection:** SHA-256 hashing ensures identical files are never moved twice. *(v2)*
- **📋 JSON Reports:** Every run generates a detailed action log. *(v2)*
- **🛠️ Simple UI:** Easy-to-use command-line interface.

---

## 📁 Supported File Types

| Category      | Extensions                      |
| ------------- | ------------------------------- |
| **Images**    | `.jpg`, `.jpeg`, `.png`, `.gif` |
| **Documents** | `.pdf`, `.docx`, `.txt`         |
| **Videos**    | `.mp4`, `.avi`, `.mkv`          |
| **Audio**     | `.mp3`, `.wav`, `.aac`          |
| **Archives**  | `.zip`, `.rar`, `.tar`, `.gz`   |
| **Scripts**   | `.py`, `.js`, `.sh`             |
| **Other**     | Everything else!                |

> **v2 note:** `scanner.py` organizes by raw extension (e.g. `PDF/`, `MP4/`) rather than the category names above, and adds a date subfolder (`PDF/2025-06-01/`).

---

## 🛠️ Installation & Usage

### Prerequisites

Make sure you have [Python](https://www.python.org/) installed.

### Clone the Repository

```bash
git clone https://github.com/Riya5407/file-organiser.git
cd file-organiser
```

---

### ▶️ v1 — Basic (`main.py`)

```bash
python main.py
```

The script will prompt you for the folder path you wish to clean up.

```
Enter the path of the folder you want to organize: C:\Users\YourName\Downloads
```

---

### ▶️ v2 — Advanced (`scanner.py`)

```bash
python scanner.py --path /path/to/source --output /path/to/destination
```

**Available flags:**

| Flag | Description | Default |
|---|---|---|
| `--path` | Source folder to scan | `~/Downloads` |
| `--output` | Destination for organized files | `~/Downloads` |
| `--dry-run` | Preview moves without touching any files | `false` |

**Example — preview changes first:**
```bash
python scanner.py --path ~/Desktop --output ~/Organized --dry-run
```

**Example — actually organize:**
```bash
python scanner.py --path ~/Desktop --output ~/Organized
```

A report is saved at `<output>/Organizer_report.json` after every run.

---

## ⚙️ How it Works

### v1 (`main.py`)
1. **Read Dir:** Scans all files in the input directory.
2. **Match Ext:** Checks the file extension against pre-defined categories.
3. **Ensure Folder:** Creates the target subfolder if it doesn't already exist.
4. **Move & Rename:** Moves the file safely, handling any naming conflicts gracefully.

### v2 (`scanner.py`)
1. **Recursive Scan:** Walks the full directory tree, ignoring `.git`, `node_modules`, and `__pycache__`.
2. **Hash Check:** Computes SHA-256 for every file; true duplicates are skipped automatically.
3. **Date Bucketing:** Determines destination path as `<ext>/<YYYY-MM-DD>/` using file modification time.
4. **Dry Run (optional):** Prints planned moves without touching the filesystem.
5. **Move & Report:** Executes moves and saves a JSON summary of every action.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have ideas for new categories or features.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

*Developed with ❤️ by [Riya5407](https://github.com/Riya5407)*
