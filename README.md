Odoo-PostgreSQL Matrix Configurator
A clean, responsive FastAPI-based web dashboard that provides verified version compatibility matrices between Odoo releases, Python environments, and PostgreSQL engines.

🛠️ Prerequisites
Before running the application, make sure you have the following installed on your machine:

Python 3.10+ (Recommended) or higher

pip (Python package installer)

📦 Installation & Setup
Create your project folder and save the code provided above into a file named app.py.

Open a terminal inside that folder and install the required dependencies:

Bash
pip install fastapi uvicorn jinja2
🚀 How to Run the Application
You can spin up this application using any of the three methods detailed below. Once running, open your web browser and go to:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

Method 1: Using the Command Line (Terminal)
The simplest way to run the application is to execute the python file directly, which will invoke the built-in Uvicorn script.

Navigate to the directory containing your app.py file.

Run the file using Python:

Bash
python app.py
(Alternatively, you can start it directly via the Uvicorn CLI: uvicorn app:app --reload)

Method 2: Running in VS Code (Visual Studio Code)
Open your project folder in VS Code (File > Open Folder...).

Make sure you have the Python Extension installed.

Open the app.py file.

Run the file using one of these options:

The Easy Button: Click the Play Icon (Run Python File) in the top right corner of the editor window.

Using Native Debugging:

Press F5 or go to the Run and Debug tab on the left sidebar.

Click Run and Debug and choose Python File.

Method 3: Running in PyCharm (Community or Professional)
Open your project folder in PyCharm (File > Open...).

Configure the Interpreter (if not done automatically):

Go to Settings (or Preferences on macOS) > Project: <your_project_name> > Python Interpreter.

Ensure your selected interpreter has fastapi, uvicorn, and jinja2 installed.

Run the file:

Right-click anywhere inside the code editor of app.py.

Select Run 'app' from the context menu (or press Ctrl + Shift + F10 on Windows/Linux, Ctrl + Option + R on macOS).

PyCharm will create a permanent Run Configuration profile at the top right, allowing you to quickly hit the green Play button or Bug button (for debugging) in the future.

🛑 Stopping the Server
To stop the FastAPI application running in any of the environments above, click inside the active terminal panel/run console and press:

Ctrl + C
