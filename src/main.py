
import os
import json
from xml.etree import ElementTree as ET
from conversion.json_functions import *
from conversion.xml_functions import *
from conversion.notebook_functions import *


global config 
config = os.path.join(os.path.dirname(__file__), 'config.json')
config = json.load(open(config, 'r'))

#      MAIN PROGRAM      #
def main():
    #choose between single cell or multicell version of the program via config file
    if config["multicellversion"].upper() == "Y":
        multicellversion()
    elif config["multicellversion"].upper() == "N":
        singlecellversion()
    else:
        print("config error - multicellversion must be Y or N")
    return

def singlecellversion():
    if os.path.exists('./src'):
        os.chdir('./src')
    os.makedirs('./user', exist_ok=True)
    create_control_notebook(config=config)
    


def multicellversion():
    choice = input("run with default xml file? y/n: ")
    if choice == "n":
        file = input("Enter the path to or name of the file if it is in this directory: ")
        filetype = ""
        if file.endswith(".xml"):
            xml = open(xml, "r")
            filetype = "xml"
        elif file.endswith(".json"):
            jsonfile = open(file, "r")
            filetype = "json"
    else:
        if os.path.exists("initialQuestions.xml"):
            xml = open("initialQuestions.xml", "r")
        elif os.path.exists("./src/initialQuestions.xml"):
            xml = open("./src/initialQuestions.xml", "r")
        filetype = "xml"
    #parse xml to string
    #check if src exists below current directory
    if os.path.exists('./src'):
        os.chdir('./src')
    os.makedirs('./user', exist_ok=True)
    if filetype == "xml":
        xml = xml.read()
        jsonlist, category_text, quizfilename = create_quiz_notebook(xml,config)
        
        create_control_notebook(config,quizfilename,category_text)
        print(f"Quiz created for {category_text} in user folder")
        save_json_to_file(jsonlist, quizfilename,config)
        
    elif filetype == "json":
        quizrun(file)
    return

def quizrun(quiztopic, quizcomponent):#function runs any json quiz in single cell , quiztopic such as "declaring variables", quizcomponent such as "final test"
    try:
        quiztopic = quiztopic.lower().strip()
        quizcomponent = quizcomponent.lower().strip()
        #make sure os is on src directory
        if os.path.exists('./src'):
            os.chdir('./src')

        if config["usedefaultuserdir"].upper() == "Y":
            #check if user directory exists if not go to else
            if os.path.exists('./user'):
                os.chdir('./user')
            for item in os.listdir():
                if quiztopic in item.lower():
                    print(quiztopic + " found")
                    #if item is file, check if quizcomponent is in filename, if so set filepath to that file
                    if os.path.isfile(item):
                        if quizcomponent in item.lower() and item.endswith(".json"):
                            #give full path to file in os not relative
                            filepath  = os.path.abspath(item)
                    #if item is folder, if so go into folder and check for file with quizcomponent in name
                    elif os.path.isdir(item):
                        os.chdir(f'./{item}')
                        for file in os.listdir():
                            if quizcomponent in file.lower() and file.endswith(".json"):
                                filepath = os.path.abspath(file)
        else:#if not user directory then server directory
            for folder in os.listdir('./server'):
                if quiztopic in folder.lower():
                    print(quiztopic + " found")
                    for file in os.listdir(f'./server/{folder}'):
                        if quizcomponent in file.lower() and file.endswith(".json"):
                            filepath = f'./server/{folder}/{file}'

            
        scoredict = {}
        file = open(filepath,"r")
        questions = json.load(file)
        for question in questions.keys():
            for qdict in questions[question]:
                if "link" in qdict:
                    break
                print("Question: " + questions[question][qdict]["name"])
                for line in questions[question][qdict]["question"]:
                    print(questions[question][qdict]["question"][line])
                print("Choices:")
                for key,choice in questions[question][qdict]["choices"].items():
                    print(key + ": " + choice)
                answer = input("Enter your answer: ")
                #catches user input to end the quiz early
                if answer.lower() in ["quit","exit"]:
                    raise Exception("Quiz aborted")
                print("Your answer: " + answer.upper())
                #if answer is already uppercase letter, no need to convert
                #if answer is lowercase, convert to uppercase
                if answer.islower():
                    answer = answer.upper()
                if answer == questions[question][qdict]["correct_answer"]:
                    print("Correct! : " + questions[question][qdict]["feedback"][answer] + "\n")
                    scoredict[qdict] = 1
                else:
                    scoredict[qdict] = 0
                    print("Incorrect! The correct answer is: " + questions[question][qdict]["correct_answer"]+ "\n")
                    if answer in questions[question][qdict]["feedback"]:
                        print("Feedback: " + questions[question][qdict]["feedback"][answer]+ "\n")
        print("Quiz complete! Here are your results: ")
        #score section
        scoreout = score(scoredict, questions)

        #check exceptions, either filename wrong so not found, or user ends loop early and causes keyerror, in which case close gracefully telling the user the attempt was aborted
    except FileNotFoundError:
        print("File not found")
    except KeyError as e:
        print("Key error: " + str(e))
            
        #in all other exceptions, print the error message
    except Exception as e:
        print("Error: " + str(e))
    return



def score(scoredict, questions):
    score = sum(scoredict.values())
    for key in scoredict.keys():
        print(f"{key}: {scoredict[key]}")
    print(f"Score: {score}/{len(scoredict)}")
    average = score/len(scoredict)
    for linkname, linkdict in questions["weightedlinks"].items():
        if average >= linkdict["weight"]:
            print(f"{linkname} and the average is: {average}")
            for key in linkdict["links"]:
                print(key + ": " + linkdict["links"][key])
    return score
                    

if __name__ == "__main__":
    main()
