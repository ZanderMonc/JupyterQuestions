# JupyterQuestions
JupyterQuestions is a tool that consists of a main.py file to launch the educator terminal based interactions, this main.py interfaces with functions from convert_xml.py and split_quiz_xml.py

Requirements
List the all of the pre-requisites software required to set up your project (e.g. compilers, packages, libraries, OS, hardware)

python 3.9 +
Packages: listed in 'requirements.txt'
Windows 10 / 11, other OS not tested
Build steps
List the steps required to build software.

Ensure python 3.9 or greater is installed
optional : pip install venv if not already present, run python -m venv, then activate the virtual environment by calling venv\scripts\activate
install all project packages: pip install -e requirements.txt

Test steps

Primary tests can be ran with venv activated 
  python src/test.py

Secondary tests

While in src directory and config[multicellversion":"Y"], run main.py's main method and when prompted run with default file for testing purposes, examine output in new user directory - there should be control.ipynb, three files titled Python_Declare_Variables with .ipynb and .json(if user accepted prompt) and .py file-extensions.
