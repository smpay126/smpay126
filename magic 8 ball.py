import random
name = input("type your name:\n")
question = input("what is your quetion:\n") 
print(name +" Asks: "+ question)
print("Magic 8-Ball's answer: ")
random_number = random.randint(1,9) 
if random_number == 1:
  print("Yes - definitely.")
elif random_number == 2:
  print("It is decidedly so.")
elif random_number == 3:
  print("Without a doubt.")
elif random_number == 4:
  print("Reply hazy, try again")
elif random_number == 5:
  print("Ask again later.")
elif random_number == 6:
  print("Better not tell you now.")
elif random_number == 7:
  print("My sources say no.")
elif random_number == 8:
  print("Outlook not so good.")
elif random_number == 9:
  print("Very doubtful.")
if question == "":
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")