# 📚 PDF Chapter Splitter – Organize Structured PDFs by Sections

This tool was created to help you **split a structured PDF (such as a book, manual, thesis, or lecture compilation)** into separate PDFs — one for each **chapter** or **section**, based on the internal outline you see in most PDF readers (like Adobe Acrobat or Preview).

The goal is to make large documents easier to **read, navigate, review, or process using AI tools** such as ChatGPT — for example, by allowing you to ask for summaries of specific chapters, or translate materials chapter by chapter when they're written in a foreign language.

---

## 🛡️ Legal and Ethical Use

> ❗ **Important Notice**  
> This program assumes you **own the legal rights** to manipulate the PDF file you're using, or that the material is in the public domain or under a license that allows such processing.  
>  
> The author **respects intellectual property rights** and **does not condone piracy**. All books and materials the author finds valuable are **purchased** and used within the bounds of the law.  
>  
> 📜 Please use this tool **responsibly** and only for **legitimate, ethical, and legal purposes**.  
>  
> ⚖️ **You are solely responsible** for how you use this software. The author takes no legal responsibility for improper or unauthorized usage.  
>  
> ✨ *In short: do good things with good tools. We believe in Karma.*

---

## ⚙️ How It Works

When you run the script, it:

1. Reads the PDF file’s built-in outline or table of contents.
2. Splits the document into **one file per section or chapter**, based on those bookmarks.
3. Saves the output files with meaningful names (based on chapter titles), making them easy to process individually.

📁 The result: a folder full of smaller PDFs — one per chapter — that you can read, share, or analyze more easily.

This is especially useful when working with:

- Long textbooks or academic books
- Lecture notes or teaching materials
- Public reports or structured manuals
- Any PDF with a consistent section structure

---


# 🐍 Python Project Setup Guide

This repository contains a Python program that uses external dependencies. To make it easy for you to run the program safely and consistently, we've included a `requirements.txt` file and optional setup scripts.

---

## ⚙️ How to Set Up the Project

There are **two ways** to run this project:

---

### ✅ Option 1: Using a Virtual Environment (recommended)

This method creates an isolated Python environment just for this project, preventing conflicts with your system Python or other projects.

#### 🔧 Setup Instructions

1. **Clone the repository**

   If you're viewing this on GitHub, click the green `<> Code` button and copy the URL.  
   Then, in your terminal:

   ```bash
   git clone <URL-of-this-repo>
   cd <folder-name-of-this-repo>
   ```

2. **Run the setup script:**

   - On **Linux/macOS**:
     ```bash
     bash setup.sh
     ```

   - On **Windows** (Command Prompt or double-click):
     ```bat
     setup.bat
     ```

This will:
- Create a virtual environment in the folder `.venv`
- Activate the environment
- Install all required dependencies from `requirements.txt`

#### ▶️ How to Activate the Virtual Environment Later

- **Linux/macOS:**
  ```bash
  source .venv/bin/activate
  ```

- **Windows:**
  ```bat
  .venv\Scripts\activate
  ```

To deactivate it:
```bash
deactivate
```

---

### ❗ Option 2: Without Virtual Environment (not recommended)

If you prefer not to use a virtual environment, you can install the dependencies globally:

```bash
pip install -r requirements.txt
```

#### ⚠️ Be aware:
- This might cause conflicts with other Python projects on your system.
- It’s harder to reproduce the same environment across machines.
- It may require admin privileges and could be difficult to clean up.

---

## 📄 Files in This Repository

- `requirements.txt` – List of required Python packages
- `setup.sh` – Setup script for Linux/macOS
- `setup.bat` – Setup script for Windows
- Python source code

---

## 🤝 Contributions

Feel free to open issues or submit pull requests if you find a bug or want to suggest improvements!

---

## 🧪 Tested on

- Python 3.10+
- pip 21+

---

Happy coding! 🚀
