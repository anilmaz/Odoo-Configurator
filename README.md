# Odoo-PostgreSQL Matrix Configurator

A clean, light, responsive FastAPI-based web dashboard that provides verified version compatibility matrices between Odoo releases, Python environments, and PostgreSQL engines.

---

## 🛠️ Prerequisites

Before running the application, make sure you have the following installed on your machine:
* **Python 3.10+** (Recommended) or higher
* `pip` (Python package installer)

---

## 📦 Installation & Setup

1. **Create your project folder** and save your code into a file named **`app.py`**.
2. **Open a terminal** inside that folder and install the required dependencies:
   ```bash
   pip install fastapi uvicorn jinja2

   🚀 How to Run the Application
You can spin up this application using any of the three methods detailed below. Once running, open your web browser and navigate to:
👉 http://127.0.0.1:8000

Method 1: Using the Command Line (Terminal)
The simplest way to run the application is to execute the python file directly, which will invoke the built-in Uvicorn block within the script.

Open your terminal or command prompt.

Navigate to the directory containing your app.py file:

Bash
cd /path/to/your/project
Run the file using Python:

Bash
python app.py

   *(Alternatively, you can start it directly via the Uvicorn CLI framework: `uvicorn app:app --reload`)*

---

### Method 2: Running in VS Code (Visual Studio Code)

1. Open your project folder in VS Code (`File` > `Open Folder...`).
2. Make sure you have the official **Python Extension** installed.
3. Open the `app.py` file in your editor pane.
4. Run the file using one of these options:
   * **The Quick Run Button:** Click the **Play Icon (Run Python File)** located in the top-right corner of the editor window.
   * **Using Debug Mode:** 
     1. Press `F5` or switch to the **Run and Debug** view on the left-hand sidebar (the play icon with a bug).
     2. Click **Run and Debug** and choose **Python File** from the dropdown context menu.

---

### Method 3: Running in PyCharm (Community or Professional)

1. Open your project folder in PyCharm (`File` > `Open...`).
2. **Configure the Project Interpreter** (if not done automatically):
   * Open `Settings` (or `Preferences` on macOS) > `Project: <your_project_name>` > `Python Interpreter`.
   * Ensure your current interpreter has `fastapi`, `uvicorn`, and `jinja2` installed.
3. **Execute the File:**
   * Right-click anywhere inside the code editor interface of your open `app.py` file.
   * Select **Run 'app'** from the context menu (or use the hotkey `Ctrl + Shift + F10` on Windows/Linux, `Ctrl + Option + R` on macOS).
4. PyCharm will automatically generate a permanent Run Configuration profile at the top right, allowing you to hit the green **Play** button (Run) or **Bug** button (Debug) for future operations.

---

## 🛑 Stopping the Server

To cleanly shutdown the FastAPI running engine in any of the active environments above, click inside the active terminal panel or run console and press:
* **`Ctrl + C`**
