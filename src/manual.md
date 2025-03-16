# User manual 

To run Jupyter Moodle Questions educator tools follow the below steps

1. Open a terminal with microsoft command prompt or powershell

2. navigate to the src directory of this project using the cd command or start the terminal directly from file explorer in the src directory

3. if requirements are installed locally, activate venv with venv/Scripts/activate

4. with venv active type "python main.py" or run the main code cell in main.ipynb

5. proceed through prompts on the terminal / code cell output to interact with the initial tool setup

6. after using this step, a user directory with control.ipynb should be present under src/user directory, start jupyter notebooks with "jupyter notebook" in terminal, then navigate on your jupter notebook window on web browser to  src/user/control.ipynb, run cells in this notebook for further options.


Json format Quizzes processed from xml are found in src/user, these can be manually edited for correctness. 

config.json in ./src contains 
    * "usedefaultuserdir":"Y",   
     This is used to specific if src/user directory is used for output with Y or a new directory is prompted to be defined by the user if N
    * "jupyterhostaddr": "localhost",
    This allows the user to define the address of the jupyter notebook server, default is localhost
    * "multicellversion":"N"
    This allows the user to define if the tool should output a single cell quiz or a multi-cell quiz, default is single cell quiz with N
