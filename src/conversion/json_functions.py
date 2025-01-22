import json
import os
import xml.etree.ElementTree as ETree
from conversion.xml_functions import format_xml_to_text

def xml_to_jsonlist(xml_string):
    #function which takes an xml string, isolates multiple choice questions and converts them into a json string
    root = ETree.fromstring(xml_string)
    jsonlist = []
    qnum = 0
    for question in root.findall(".//question"):
        if question.attrib['type'] == 'multichoice':
            name = question.find(".//name/text").text.strip()
            name = format_xml_to_text(name)
            question_text = question.find(".//questiontext/text").text.strip()
            question_text = format_xml_to_text(question_text)
            question_text = f'f"""\n{question_text}"""'
            answer_elements = question.findall(".//answer")
            choices = {} 
            feedback = {}
            for idx, answer in enumerate(answer_elements):
                print (idx, answer)
                if answer.find(".//text") != None:
                    choice_text = answer.find(".//text").text.strip()
                    choice_text = format_xml_to_text(choice_text)
                    fraction = int(answer.attrib['fraction'])
                    option_label = chr(65 + idx)
                    choices[option_label] = choice_text
                    if fraction == 100:
                        correct_answer = option_label
                    feedback[option_label] = "you are correct" if fraction == 100 else "you are wrong"
            #everything in question_text is a string, so we need to convert it to a string despite it being python code
            qnum += 1
            qname =  "question"+str(qnum)
            jsondata = {qname: {"name": name, "question": question_text, "choices": choices, "feedback": feedback, "correct_answer": correct_answer}}
            jsonlist.append(jsondata)
    return jsonlist

def jsonlist_to_json(data):
    #takes a list of dictionaries and converts it to a json string
    #json format where qname is the key and the value is a dictionary with name, question, choices, feedback and correct_answer
    jsonoutformat = {}
    toplevel = "quiz"
    jsonoutformat[toplevel] = {}
    for quizname in data:
        for qnum, qcontent in quizname.items():
            jsonoutformat[toplevel][qnum] = {}
            for qpart, content in qcontent.items():
                if qpart == "question":
                    #use replace to remove the f",  f""" , and """ from the string
                    content = content.replace("f\"\"\"", "").replace("\"\"\"", "").replace("f\"", "").strip().strip(",")
                    content = {f"line{idx}": line for idx, line in enumerate(content.split("\n"))}
                jsonoutformat[toplevel][qnum][qpart] = content
    weightedlinks = {}
    #create a series of link with weights in increments of 0.2 from 0 to 1, placeholder link and info sections for educator manual editing
    weights = [0.0, 0.2, 0.4, 0.6, 0.8, 1]
    for weight in weights:
        weightedlinks[f"links{weight}"] = {"links":{"Click this generic link for further information":f"https://www.google.com"}, "weight": weight}
    jsonoutformat["weightedlinks"] = weightedlinks
    return json.dumps(jsonoutformat, indent=4)


def save_json_to_file(jsonlist, quizfilename,config):
    #takes a json string and a filename and writes the json string to the
    jsonfile = jsonlist_to_json(jsonlist)
    jsonprompt = input("Would you like to save the quiz data as a json file? y/n: ")
    if jsonprompt.upper() == "Y":
        if config["usedefaultuserdir"].upper() == "Y":
            with open(f'./user/{quizfilename}.json', 'w') as f:
                f.write(jsonfile)
                f.close()
        else:
            userdir = input("Enter the path to the directory where you would like to save the json file: ")
            with open(f'{userdir}/{quizfilename}.json', 'w') as f:
                f.write(jsonfile)
                f.close()
        return os.path.abspath(f'{quizfilename}.json')  
    return None