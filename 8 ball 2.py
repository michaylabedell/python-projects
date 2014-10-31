import random


print("welcome to my domain")


answers = ['yes','no','maybe','heck no techno','my sources say no','jaja says yes to you,','lalalala sorry i didnt hear that please repeat','why do you ask?']

while True: 
   print("what is your question")
   question = input('> ')
   answer = random.choice(answers)
   print(answer)
   
