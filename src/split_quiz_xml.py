#script used to split individual quizes from a single xml file containing multiple quizes from one course topic
import xml.etree.ElementTree as ET
import os
from main import *
from conversion.xml_functions import *

config = os.path.join(os.path.dirname(__file__), 'config.json')
config = json.load(open(config, 'r'))

def main(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"Error parsing {filename}: {e}")
        return {}
    
    quizzes = {}
    namespace = {}
    current_category = None

    for question in root.findall('.//question', namespace):
        if question.get('type') == 'category':
            category_name = question.find('./category/text', namespace).text
            current_category = category_name
            quizzes[current_category] = ET.ElementTree(ET.Element('quiz'))
            quizzes[current_category].getroot().append(question)
        elif current_category is not None:
            quizzes[current_category].getroot().append(question)
    
    return quizzes

def xml_quizzes_to_jsons():
    #Add quiz cell to existing notebook? Run this if so.
    #filename = input("path to existing ipynb file")
    quizjsons = input("path to directory of json quiz files to use")

    for quizjson in os.listdir(quizjsons):
        print("quizjson", quizjson)
        quizjsonname = quizjson.split(".")[0]
        if quizjson.endswith(".xml"):
            #check if well formed
            try:
                with open(quizjsons + "/" + quizjson) as f:
                    quizjson = f.read()
            except:
                print("Error reading file", quizjson)
                continue
            jsonlist,questionlist, category_text, jsonfilename= xml_to_jupyter_cells(quizjson,savecells=False)
            jsonout = jsonlist_to_json(jsonlist)
            #save jsonout to file and save path
            #folder is filename minus extension from quizjsons path
            quizjsonfolder = os.path.basename(quizjsons).split(".")[0].split("-")[-3]
            
            if os.path.basename(os.getcwd()) == "user":
                os.chdir("..")
    
            #if config[localhost] is Y, save to user directory
            if config["usedefaultuserdir"].upper() == "Y":
                print("saving to user directory")
                os.makedirs("./user", exist_ok=True)
                os.makedirs(f"./user/{quizjsonfolder}", exist_ok=True)
                with open(f"./user/{quizjsonfolder}/{quizjsonname}.json", "w") as f:
                    f.write(jsonout)
                    path = os.path.abspath(f.name)
                    print("path", path)
                    f.close()
            else:
                #save in src/server/
                os.makedirs("./server", exist_ok=True)
                os.makedirs(f"./server/{quizjsonfolder}", exist_ok=True)
                with open(f"./server/{quizjsonfolder}/{quizjsonname}.json", "w") as f:
                    f.write(jsonout)
                    path = os.path.abspath(f.name)
                    f.close()


if __name__ == "__main__":
    #runs from ./2555900m_JPNotebookQuestions> in command line
    #prompt user for relative path to xml file
    filepath = input("Enter the relative path to the XML file: ")
    quizzes = main(filepath)
    filename = os.path.basename(filepath)
    output_dir = os.path.join("./src/user", f"{filename}_xmls")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for category, quiz in quizzes.items():
        cattype = category.split("/")[-1]
        quiz.write(os.path.join(output_dir, f"{cattype}.xml"), encoding='utf-8', xml_declaration=True)
        print(f"Created {os.path.join(output_dir, f'{cattype}.xml')}")
