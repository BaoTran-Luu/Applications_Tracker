# 📊 Job Application Tracker


## 🌟 About the Project

A desktop application built with Python to help users organize, manage, and track their job applications in one place.
The application provides an overview of the job search process through an interactive dashboard, search functionality, and visual statistics.
It can be started from the command line or as a standalone Windows program (`.exe`), so it can be opened anytime without an editor.

## 🚀 Features

| Feature | Description |
|:---|:---|
| 📝 **Application Management** | Add, update, and delete job applications. |
| 🔍 **Search** | Search by company name or position. |
| 🏷️ **Status Filtering** | Filter applications by recruitment status. |
| 📊 **Dashboard** | Monitor application progress and statistics. |
| 🎨 **Data Visualization** | View job search statistics using a colorful bar chart. |
| 💾 **Data Persistence** | Store and retrieve application data using JSON. |
| 📅 **Date Management** | Automatically track application update dates. |
| 🖥️ **Desktop App** | Can be built into a standalone Windows program with PyInstaller. |

## 🛠️ Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Tkinter-2C3E50?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge" />
  <img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
</p>

Additional tools: `tkcalendar` · `PyInstaller` · `uv` · `GitHub`

## 🖥️ Application Preview
📊 Dashboard 📝 Application Management 🔍 Search & Filtering

  <img src="App Preview.png" width="85%" alt="Job Application Tracker Dashboard" />

## 📁 Project Structure

```text
application_tracker/
│
├── src/
│   └── application_tracker/
│       ├── __init__.py
│       ├── __main__.py
│       ├── job_application.py
│       ├── application_manager.py
│       ├── storage.py
│       └── gui.py
│
├── test/
├── run_app.py
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```
| File | Purpose |
|:---|:---|
| `job_application.py` | `JobApply` class with validation, plus conversion to and from dictionaries. |
| `application_manager.py` | Add, remove, update, and list applications; counts interviews. |
| `storage.py` | Save and load the applications as JSON. |
| `gui.py` | Tkinter interface, dashboard, table, and chart. |
| `run_app.py` | Start file used to build the Windows program. |

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/BaoTran-Luu/Applications_Tracker
```

**2. Navigate to the project directory**

```bash
cd application_tracker
```

**3. Install dependencies**

```bash
uv sync
```

**4. Run the application**

```bash
uv run python -m application_tracker.gui
```
## 💾 Where Is My Data Stored?

The application saves your data in a fixed location, so it works the same from the command line and from the `.exe`:

| System | File |
|:---|:---|
| Windows | `%APPDATA%\ApplicationTracker\applications.json` |
| Other systems | `~/ApplicationTracker/applications.json` |

To back up your data or move it to another computer, copy this file.

## 🪟 Build a Windows Program (.exe)

**1. Install PyInstaller**

```bash
uv add --dev pyinstaller
```

**2. Build the program**

```bash
uv run pyinstaller --onefile --windowed --name "Application Tracker" --paths src --hidden-import babel.numbers run_app.py
```

The finished program is created at `dist/Application Tracker.exe`. Move it to a folder of your choice and create a desktop shortcut.

## 🧠 What I Learned

Through this project, I gained practical experience in:

- Object-Oriented Programming (OOP).
- Desktop GUI development with Tkinter.
- CRUD operations.
- JSON data storage and retrieval.
- Search and filtering functionality.
- Input validation and error handling.
- Data visualization with Matplotlib.
- Python project management using uv.
- Packaging a Python app as a Windows program with PyInstaller.
- Version control with Git and GitHub.

## 🔮 Future Improvements

- [ ] Add CSV and Excel export functionality.
- [ ] Introduce additional dashboard visualizations.
- [ ] Improve the user interface and user experience.
- [ ] Expand automated testing.

## 👨‍💻 Author

**BAO TRAN LUU**

🎓 Master's Student in Econometrics  
💻 Python | Data Analytics | Econometrics

---

<p align="center">
  <strong>⭐ Thanks for visiting my project!</strong>
</p>