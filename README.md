# JupyterQuestions
JupyterQuestions is a tool that consists of a main.py file to launch the educator terminal based interactions, this main.py interfaces with functions from conversion subpackage to produce control.ipnb, 
this control notebook allows the user further interactions including using split_quiz_xml.py for moodle xml files that contain multiple quizzes, and the ability to create new quizzes from scratch.

There is an implemented example of a multi-cell quiz, followed by a single-cell quiz as the last cell of the notebook, see : src/example/Python_Declare_Variables.ipynb

# Requirements
python 3.9 +
Packages: listed in 'requirements.txt'
Windows 10 / 11, other OS not tested

# Build steps
Ensure python 3.9 or greater is installed

optionally: To create a virtual environment for the tool run:
  * pip install venv 
  * python -m venv myenvname
  * myenvname\scripts\activate
  
install all project packages in active venv:
  * pip install -e requirements.txt

# Test steps

Primary tests can be ran with venv activated 
  * python src/test.py

# Secondary tests

While in src directory, venv activated, and config.json has [multicellversion":"Y"], 
* run main.py's main method either in terminal or jupyter notebook via main.ipynb
when prompted run with default file for testing purposes, after completion examine output in new user directory
   - there should be control.ipynb, three files titled Python_Declare_Variables with .ipynb and .json(if user accepted prompt) and .py file-extensions.
