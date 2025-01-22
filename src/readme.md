# Readme

Put a brief description of your code here. This should at least describe the file structure.
JupyterMoodleQuestions is a tool that consists of a main.py file to launch the educator terminal based interactions, this main.py interfaces with functions from convert_xml.py and split_quiz_xml.py

## Build instructions

**You must** include the instructions necessary to build and deploy this project successfully. If appropriate, also include 
instructions to run automated tests. 

### Requirements

List the all of the pre-requisites software required to set up your project (e.g. compilers, packages, libraries, OS, hardware)

* python 3.9 +
* Packages: listed in 'requirements.txt'
* Tested on windows 10

### Build steps

List the steps required to build software. 

1. Ensure python 3.9 or greater is installed
2. optional : pip install venv if not already present, run python -m venv, then activate the virtual environment by calling venv\scripts\activate
3. install all project packages:
    pip install -e requirements.txt 

### Test steps

List steps needed to show your software works. This might be running a test suite, or just starting the program; but something that could be used to verify your code is working correctly.

while in src directory, run main.py's main method and when prompted run with default file for testing purposes, examine output in new user directory - there should be control.ipynb, three files titled Python_Declare_Variables with .ipynb and .json(if user accepted prompt) and .py file-extensions.

