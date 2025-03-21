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
