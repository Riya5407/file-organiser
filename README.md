# 📂 File Organizer - Automated Workspace Cleaner

A smart, lightweight Python utility to keep your folders organized. Automatically categorizes files into logical subdirectories based on their file extensions.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Automation](https://img.shields.io/badge/Task-Automation-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

---

## 🚀 Key Features

-   **⚡ Fast Execution:** Instantly analyzes and organizes large directories.
-   **📁 Smart Categorization:** Pre-defined rules for Images, Documents, Videos, Audio, Archives, Scripts, and more.
-   **🛡️ Collision Handling:** Automatically renames files if a duplicate exists in the destination (e.g., `image_1.jpg`).
-   **🧹 Default Fallback:** Catches all unknown file types and moves them to an "Others" folder.
-   **🛠️ Simple UI:** Easy-to-use command-line interface.

## 📁 Supported File Types

| Category | Extensions |
| :--- | :--- |
| **Images** | `.jpg`, `.jpeg`, `.png`, `.gif` |
| **Documents** | `.pdf`, `.docx`, `.txt` |
| **Videos** | `.mp4`, `.avi`, `.mkv` |
| **Audio** | `.mp3`, `.wav`, `.aac` |
| **Archives** | `.zip`, `.rar`, `.tar`, `.gz` |
| **Scripts** | `.py`, `.js`, `.sh` |
| **Other** | Everything else! |

---

## 🛠️ Installation & Usage

### 1. Prerequisites
Make sure you have [Python](https://www.python.org/) installed.

### 2. Clone the Repository
```bash
git clone https://github.com/Riya5407/file-organizer.git
cd file-organizer
```

### 3. Run the Script
```bash
python main.py
```

### 4. Input the Path
The script will prompt you for the folder path you wish to clean up.
```text
Enter the path of the folder you want to organize: C:\Users\YourName\Downloads
```

---

## ⚙️ How it Works
1.  **Read Dir:** Scans all files in the input directory.
2.  **Match Ext:** Checks the file extension against the pre-defined categories.
3.  **Ensure Folder:** Creates the target subfolder if it doesn't already exist.
4.  **Move & Rename:** Moves the file safely, handling any naming conflicts gracefully.

---

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request if you have ideas for new categories or features.

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---
*Developed with ❤️ by [Riya5407](https://github.com/Riya5407)*
