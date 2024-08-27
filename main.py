'''
New Zealand Quiz
Kereru Kohere
Quiz program
22/07/2024
version 3
quiz about aouteroa
'''
#import
import time
#variables
Score = 0
Str_answer = []
Str_name = ''
#Intro, it asks for name and introduces you into the quiz.
print("Welcome to my quiz about New Zealand! Please enter name below.")
Str_name = input("Enter name: ")
#This print makes it so there is a space between text
print()
print(f'Hello {Str_name}, I am going to give you a question and you will answer.')
#this python code make it so the program pauses for that amount of time
time.sleep(4)
print("If you answer 3 or more out of 6 incorrect, then you have failed.")
time.sleep(3)
print()
print("Make sure to type the letters a,b,c or d. Good luck:)")
print("Starting...")
print()

#Quetion 1
time.sleep(4)
print("Question 1: What is the maori name for Stewart Island?")
#Whats the moari name for Stewart Island? Answer = Rakiura
print('''
a)Rakiura
b)Makiura
c)Papanuku
d)Stewart Island''')
#This lets you answer the question and gives you points if you get it correct.
Str_answer= input ("Enter option here: ") 
if Str_answer.lower() == "a":
  Score += 1
  print("Score:",Score)
  print("Correct")
  #If you dont answer the qeustion with a, c or d then you are incorrect
elif Str_answer.lower() in ["b", "c", "d"]:
 print(f"The answer is (a) 'Rakiura', not {Str_answer} ")
  #If anthing else then it say invalid and you get it incorrect. i havent added a loop.
else:
 print("Invalid answer")
time.sleep(0.5)
print()


#Question 2
print('2. What is New Zealands most well known bird?')
print('''
a)Eagle 
b)Kea 
c)Kereru 
d)Kiwi ''')
Str_answer= input ("Enter option here: ") 
if Str_answer.lower() == "d":
 Score += 1
 print("Score:",Score)
 print("Correct")
elif Str_answer.lower() in ["b", "c", "a"]:
 print(f"The answer is (d) 'Kiwi', not {Str_answer} ")
else:
 print("Invalid answer")
time.sleep(0.5)


#Question 3
print()
print('''3. New Zealand has the longest town name in the world. 
True or False?''')
Str_answer= input ("Enter option here: ") 
if Str_answer.lower() == "true":
  Score += 1
  print("Score:",Score)
  print('Correct')
elif Str_answer.lower() == "false":
  print("Incorrect")
else: 
   print("Invalid answer")
time.sleep(0.5)


#Question 4
print()
print("""4. New Zealand's population have more maori than european. 
True or False? """)
Str_answer= input ("Enter option here: ") 
if Str_answer.lower() == "false":
 Score += 1
 print("Score:",Score)
 print("Correct")
elif Str_answer.lower() == "true":
  print("Incorrect")
else:
  print("Invalid answer")
  time.sleep(0.5)

#Question 5
print()
print('5. What is New Zealands capital?')
print('''a)Auckland 
b)Christchurch
c)Wellington    
d)Rotorua ''')
Str_answer= input ("Enter option here: ") 
if Str_answer.lower() == "c":
  Score += 1
  print("Score:",Score)
  print("Correct")
elif Str_answer.lower() in ["b", "a", "d"]:
 print(f"The answer is (c) 'Wellington', not {Str_answer} ")
else:
 print("Invalid answer")
time.sleep(0.5)

#Question 6
print()
print('6. What is aukland famous for? ')
print('''
a)Firework shows 
b)Sky tower
c)Blue lake
d)whāwimokita ''')
Str_answer= input ("Enter option here: ") 
if Str_answer.lower() == "b":
  Score += 1
  print("Score:",Score)
  print("Correct")
elif Str_answer.lower() in ["a", "c", "d"]:
 print(f"The answer is (b) 'Sky tower', not {Str_answer}. ")
else:
 print("Invalid answer")
time.sleep(0.5)

#Ending
print()
print(f"you got, {Score} out of 6 correct.")
if Score > 3:
  print("Well done, you have passed!")
else:
  print("You have failed, better luck next time.")