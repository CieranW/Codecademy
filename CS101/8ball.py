import random
name = "Ryan"
question = "Is food necessary?"
answer = ""

random_number = random.randint(1, 20)
print(random_number)

if question == "":
    print("How am I supposed to answer when you didn't ask me anything?")
else:
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)

if random_number == 1:
    print("Yes - definitely")
elif random_number == 2:
    print("It is decidedly so")
elif random_number == 3:
    print("Without a doubt")
elif random_number == 4:
    print("Reply hazy, try again")
elif random_number == 5:
    print("Ask again later")
elif random_number == 6:
    print("Better not tell you now")
elif random_number == 7:
    print("My sources say no")
elif random_number == 8:
    print("Outlook not so good")
elif random_number == 9:
    print("Very doubtful")
elif random_number == 10:
    print("Fix your words")
elif random_number == 11:
    print("Why are you asking me this?")
elif random_number == 12:
    print("Are you dumb?")
elif random_number == 13:
    print("Guess we found the idiot")
elif random_number == 14:
    print("I'm too tired to bother")
elif random_number == 15:
    print("That'll be $999")
elif random_number == 16:
    print("This is why the population is declining")
elif random_number == 17:
    print("Who said that?")
elif random_number == 18:
    print("This is my favourite number")
elif random_number == 19:
    print("Why are you still here?")
elif random_number == 20:
    print("Time for bed")

else:
    print("ERROR")
