# JupyterQuestions
JupyterQuestions is a tool that consists of a main.py file to launch the educator terminal based interactions, this main.py interfaces with functions from conversion subpackage and split_quiz_xml.py 
Further educator interactions are hosted via a control.ipynb jupyter notebook file.

There is an implemented example of a multi-cell quiz and a single-cell quiz, see : src/example/Python_Declare_Variables.ipynb

# Requirements
python 3.9 +
Packages: listed in 'requirements.txt'
Windows 10 / 11, other OS not tested

# Build steps
Ensure python 3.9 or greater is installed

optionally: To create a virtual environment for the tool run:
  * pip install venv 
  * python -m venv myenv
  * venv\scripts\activate
  
install all project packages:
  * pip install -e requirements.txt

# Test steps

Primary tests can be ran with venv activated 
  * python src/test.py

# Secondary tests

While in src directory and config[multicellversion":"Y"], 
* run main.py's main method 
when prompted run with default file for testing purposes, examine output in new user directory
   - there should be control.ipynb, three files titled Python_Declare_Variables with .ipynb and .json(if user accepted prompt) and .py file-extensions.
