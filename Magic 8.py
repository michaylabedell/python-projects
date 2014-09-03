import random


print("welcome to my domain")


answers = ['yes','no','maybe','apparently no','sadly no','sadly yes','cant tell','why did you ask me about miley cyrus earlier','why do you ask','potato?','i prefur killing titans than being asked that']

while True: 
   print("what is your question")
   question = input('> ')
   answer = random.choice(answers)
   print(answer) 
