import nbformat as nbf
import os
import json
from conversion.xml_functions import xml_to_jupyter_cells

def create_control_notebook(config, quizfilename=None, category_text=None ):
    #create control notebook with link to quiz if it does not exist, otherwise add link to quiz if it does not already exist
    #check cwd is src, if not move and src is previous level, move back until src is base level
    if "src" in os.getcwd():
        while os.path.basename(os.getcwd()) != "src":
            os.chdir("..")
        
    if os.path.exists('./user/control.ipynb'):
        controlnb = nbf.read('./user/control.ipynb', as_version=4)
        if config["multicellversion"].upper() == "Y":
            if not any({quizfilename in cell['source'] for cell in controlnb['cells']}):
                controlnb['cells'].append(nbf.v4.new_markdown_cell(f"# [Click for {category_text} ]({quizfilename}.ipynb)"))
    else:
        controlnb = nbf.v4.new_notebook()
        #new python cells
        if config["multicellversion"].upper() == "Y":
            controlnb['cells'] = [nbf.v4.new_markdown_cell(f"# [Click for {category_text} ]({quizfilename}.ipynb)")]
        controlnb['cells'].append(nbf.v4.new_code_cell(f"#RUN THIS CELL FIRST\nimport sys\nsys.path.append('..')"))
        controlnb['cells'].append(nbf.v4.new_code_cell(f"#Create new json quiz by running this cell\nfrom conversion.notebook_functions import create_new_quiz\ncreate_new_quiz()"))
        controlnb['cells'].append(nbf.v4.new_code_cell(f"#Add quiz cell to existing notebook? Run this cell if so.\nfilename = input(\"path to existing ipynb file\")\nquiztopic = input(\"Input topic of stored quiz file : such as \'declare variables\'\")\nquizcomponent = input(\"Input component of stored topic: such as \'final test\'\")\nfrom conversion.notebook_functions import add_quiz_cell\nadd_quiz_cell(quiztopic, quizcomponent)"))
        controlnb["cells"].append(nbf.v4.new_code_cell(f"#Add folder of xml quizzes to existing ipynb\nfrom split_quiz_xml import xml_quizzes_to_jsons\nxml_quizzes_to_jsons()"))
    nbf.write(controlnb, './user/control.ipynb')
    #print control notebook path
    print(f"Control notebook created at {os.path.abspath('./user/control.ipynb')}")
    return 

def create_new_quiz():
    create = input("Would you like to create a new quiz? y/n: ")
    if create.upper() == "Y":
        nameofquiz = input("Enter the name of the quiz: ")
        quizdict = {}
        quizout ={nameofquiz: quizdict}
        questionnum = 0
        while True:
            questionname = input("Enter the question name: ")
            questiontext = input("Enter the questiontext: ")
            choices = input ("Enter the choices separated by commas in format A: choice, B: choice, etc: ")
            choices = dict((x.strip(), y.strip()) for x, y in (element.split(':') for element in choices.split(',')))
            feedback = input("Enter the feedback separated by commas in format A: feedback, B: feedback, etc: ")
            feedback = dict((x.strip(), y.strip()) for x, y in (element.split(':') for element in feedback.split(',')))
            correctanswer = input("Enter the answer: ")
            quizdict[f"question{questionnum}"] = {"name": questionname, "question": questiontext, "choices": choices, "feedback": feedback , "correct_answer": correctanswer}
            addmore = input("Would you like to add another question? y/n: ")
            if addmore.upper() == "N":
                break
        with open(f'{nameofquiz}.json', 'w') as f:
            quizout[nameofquiz] = quizdict
            f.write(json.dumps(quizout, indent=4))
            f.close()
    return


def create_quiz_notebook(xml,config):
        # open a new jupyter notebook and write the cells to it, config is a json file 
    jsonlist,questionlist,category_text,filename= xml_to_jupyter_cells(xml)
    nb = nbf.v4.new_notebook() 
    #starting cell defining global score must be run on notebook opening
    numquestions = len(questionlist)
    #import * from specifc question python file
    nb['cells'] = [nbf.v4.new_code_cell(f"from {filename} import *\nscore=0\nprint(f'Please run all cells in order')")]
    for question in questionlist:
        nb['cells'].append(nbf.v4.new_code_cell(question))
    
    #final cell prints the score then locks the score and prevents further changes
    nb['cells'].append(nbf.v4.new_code_cell(f"""
import shelve
with shelve.open('run_once_flag') as db:
    if not db.get('already_run',False):
        db['already_run'] = True
        print(f'You scored {{score}} out of {numquestions}')
        print('This cell will not run again')
    else:
        print("you have finished your attempt already")
        print('This cell will not run again')"""))
    #create new filename as categorytext.ipynb, formatted for windows compatibility
    #reads "usedefaultuserdir":"Y" from config file to determine if user wants to use default directory
    if config["usedefaultuserdir"].upper() == "Y":
        nbf.write(nb, f'./user/{filename}.ipynb')
    else:
        nbf.write(nb, f'./{filename}.ipynb')
    return jsonlist, category_text, filename

def add_quiz_cell(pathtoexistfile, quiztopic, quizcomponent):
    #check if jsonpath is not json data
    #takes the name of ipynb file and appends using nbf a cell to run quizrun from to the end
    nb = nbf.read(pathtoexistfile, as_version=4)
    #check json path is in correct format ("/ replacing all \ to avoid escape characters)
    cell = nbf.v4.new_code_cell(f'import sys\nsys.path.append(\'..\')\nfrom main import *\nquizrun("{quiztopic}", "{quizcomponent}")')
    nb.cells.append(cell)
    nbf.write(nb, pathtoexistfile)
    print(f"Quiz {nb} cell added to {pathtoexistfile}")
    return 