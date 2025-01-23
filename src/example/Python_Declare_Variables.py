
def question1():
	name = f"Python Declare - Assign numeric multiple choice"
	question = f"""
 prompt = 'Hello'
a = 4
b = len(prompt)
c = 6
c = a
a = b
a = c
c = a + b + c
 What does c equal?
"""
	choices = {'A': '4', 'B': ' 15\n', 'C': ' 13\n', 'D': ' 14\n', 'E': ' Error\n'}
	feedbackquestion1= {'A': 'you are wrong', 'B': 'you are wrong', 'C': 'you are correct', 'D': 'you are wrong', 'E': 'you are wrong'}
	print(f"Question name : Python Declare - Assign numeric multiple choice")
	print(f"{question}")
	print("--------------------")
	for option, answer in choices.items():
		print(f"{option}: {answer}")
	return feedbackquestion1
def answer1(feedbackquestion1, score):
	user_response = input("Choose the correct answer from ['A', 'B', 'C', 'D', 'E']: ")
	print(feedbackquestion1[user_response.upper()])
	if user_response.upper() == "C":
		score += 1
	return score

def question2():
	name = f"Python Declare - Assign numeric multiple choice"
	question = f"""
 prompt = 'Hello'
a = 4
b = len(prompt)
c = 6
c = a
a = b
a = c
c = a + b + c

 What is the final value of  c
?
"""
	choices = {'A': '4', 'B': ' 15\n', 'C': ' 13\n', 'D': ' 14\n', 'E': ' Error\n'}
	feedbackquestion2= {'A': 'you are wrong', 'B': 'you are wrong', 'C': 'you are correct', 'D': 'you are wrong', 'E': 'you are wrong'}
	print(f"Question name : Python Declare - Assign numeric multiple choice")
	print(f"{question}")
	print("--------------------")
	for option, answer in choices.items():
		print(f"{option}: {answer}")
	return feedbackquestion2
def answer2(feedbackquestion2, score):
	user_response = input("Choose the correct answer from ['A', 'B', 'C', 'D', 'E']: ")
	print(feedbackquestion2[user_response.upper()])
	if user_response.upper() == "C":
		score += 1
	return score

def question3():
	name = f"What is '2' in the following code?"
	question = f"""
 
 What best describes the artefact  2  in the following code?
 result = result*2
 
  
  
"""
	choices = {'A': ' Value\n', 'B': ' Statement\n', 'C': ' Operator\n', 'D': ' Variable\n', 'E': ' Expression\n', 'F': ' None of the above\n'}
	feedbackquestion3= {'A': 'you are correct', 'B': 'you are wrong', 'C': 'you are wrong', 'D': 'you are wrong', 'E': 'you are wrong', 'F': 'you are wrong'}
	print(f"Question name : What is '2' in the following code?")
	print(f"{question}")
	print("--------------------")
	for option, answer in choices.items():
		print(f"{option}: {answer}")
	return feedbackquestion3
def answer3(feedbackquestion3, score):
	user_response = input("Choose the correct answer from ['A', 'B', 'C', 'D', 'E', 'F']: ")
	print(feedbackquestion3[user_response.upper()])
	if user_response.upper() == "A":
		score += 1
	return score

def question4():
	name = f"What is 'result = result*2' in the following code?"
	question = f"""
 
 What is best describes the artefact  result = result*2 &nbsp;in the following code?
 result = result*2
 
  
  
"""
	choices = {'A': ' Value\n', 'B': ' Statement\n', 'C': ' Operator\n', 'D': ' Variable\n', 'E': ' Expression\n', 'F': ' None of the above\n'}
	feedbackquestion4= {'A': 'you are wrong', 'B': 'you are correct', 'C': 'you are wrong', 'D': 'you are wrong', 'E': 'you are wrong', 'F': 'you are wrong'}
	print(f"Question name : What is 'result = result*2' in the following code?")
	print(f"{question}")
	print("--------------------")
	for option, answer in choices.items():
		print(f"{option}: {answer}")
	return feedbackquestion4
def answer4(feedbackquestion4, score):
	user_response = input("Choose the correct answer from ['A', 'B', 'C', 'D', 'E', 'F']: ")
	print(feedbackquestion4[user_response.upper()])
	if user_response.upper() == "B":
		score += 1
	return score

def question5():
	name = f"What is 'result' in the following code?"
	question = f"""
 
 What best describes the artefact  result &nbsp;in the following code?
 result = result*2
  
 
"""
	choices = {'A': ' Value\n', 'B': ' Statement\n', 'C': ' Operator\n', 'D': ' Variable\n', 'E': ' Expression\n', 'F': ' None of the above\n'}
	feedbackquestion5= {'A': 'you are wrong', 'B': 'you are wrong', 'C': 'you are wrong', 'D': 'you are correct', 'E': 'you are wrong', 'F': 'you are wrong'}
	print(f"Question name : What is 'result' in the following code?")
	print(f"{question}")
	print("--------------------")
	for option, answer in choices.items():
		print(f"{option}: {answer}")
	return feedbackquestion5
def answer5(feedbackquestion5, score):
	user_response = input("Choose the correct answer from ['A', 'B', 'C', 'D', 'E', 'F']: ")
	print(feedbackquestion5[user_response.upper()])
	if user_response.upper() == "D":
		score += 1
	return score

def question6():
	name = f"What is 'result*2' in the following code?"
	question = f"""
 
 What best describes the artefact  result*2  in the following code?
 result = result*2
  
 
"""
	choices = {'A': ' Value\n', 'B': ' Statement\n', 'C': ' Operator\n', 'D': ' Variable\n', 'E': ' Expression\n', 'F': ' None of the above\n'}
	feedbackquestion6= {'A': 'you are wrong', 'B': 'you are wrong', 'C': 'you are wrong', 'D': 'you are wrong', 'E': 'you are correct', 'F': 'you are wrong'}
	print(f"Question name : What is 'result*2' in the following code?")
	print(f"{question}")
	print("--------------------")
	for option, answer in choices.items():
		print(f"{option}: {answer}")
	return feedbackquestion6
def answer6(feedbackquestion6, score):
	user_response = input("Choose the correct answer from ['A', 'B', 'C', 'D', 'E', 'F']: ")
	print(feedbackquestion6[user_response.upper()])
	if user_response.upper() == "E":
		score += 1
	return score
