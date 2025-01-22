import xml.etree.ElementTree as ETree
import re

def format_xml_to_text(xml_string):
    #takes text with xml tags and returns text without xml tags, converting to \n or spaces where appropriate, using regex
    newline_equivalent_tags = [ "<br/>", "</p>", "</pre>", "</code>"]
    space_equivalent_tags = ["<b>", "</b>","<nbsp>", "</nbsp>", "<br>", "<p>", "<pre>", "<code>"]
    specific_replace_chars = {"&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": "\"", "&apos;": "'","\"": "'"}
    for tag in newline_equivalent_tags:
        xml_string = re.sub(tag, "\n", xml_string)
    for tag in space_equivalent_tags:
        xml_string = re.sub(tag, " ", xml_string)
    for char, replacement in specific_replace_chars.items():
        xml_string = re.sub(char, replacement, xml_string)
    return xml_string

    
def create_jupyter_cells(qname,name,question_text,choices,feedback,correct_answer,qanswer):
    #function which takes a question and answer and converts them into a question and an answer cells, returning these cells in a list
    py_1 =f"""
def {qname}():
\tname = f"{name}"
\tquestion = {question_text}
\tchoices = {choices}
\tfeedback{qname}= {feedback}
\tprint(f"Question name : {name}")
\tprint(f"{{question}}")
\tprint("--------------------")
\tfor option, answer in choices.items():
\t\tprint(f"{{option}}: {{answer}}")
\treturn feedback{qname}"""
            
    py_2 = f"""
def {qanswer}(feedback{qname}, score):
\tuser_response = input("Choose the correct answer from {list(feedback.keys())}: ")
\tprint(feedback{qname}[user_response.upper()])
\tif user_response.upper() == "{correct_answer}":
\t\tscore += 1
\treturn score
"""       
    return py_1, py_2

def save_jupyter_cells(py_1, py_2, filename):
    #create or append to python file with the above code
    with open(f'./user/{filename}.py', 'a') as f:
        f.write(py_1)
        f.write(py_2)
    return

def xml_to_jupyter_cells(xml_string, savecells = True):
    #function which takes an xml string, isolates multiple choice questions and converts them into a question and an answer cells, returning these cells in a list
    root = ETree.fromstring(xml_string)
    questionlist = []
    jsonlist = []
    qnum = 0

    category_text = root.find(".//category/text").text.strip().split("/")[2]
    #make filename category name in windows file format
    filename =  category_text.replace(" ", "_").replace("/", "_") 

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
            qanswer =  "answer" + str(qnum)
            py_1, py_2 = create_jupyter_cells(qname,name,question_text,choices,feedback,correct_answer,qanswer)
            jsondata = {qname: {"name": name, "question": question_text, "choices": choices, "feedback": feedback, "correct_answer": correct_answer}}
            jsonlist.append(jsondata)
            cell_1 = f"""feedback{qname} = {qname}()
score = {qanswer}(feedback{qname}, score)"""
#create or append to python file with the above code
            if savecells:
                save_jupyter_cells(py_1, py_2, filename)
            questionlist.append(cell_1)
    
    return jsonlist,questionlist, category_text, filename






