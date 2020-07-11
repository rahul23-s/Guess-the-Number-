import random


n=random.randint(1,100)

guess=10
print("\n-----------------GUESS THE INTEGER","  |This is a INTEGER guessing Game|------------------")
print("Guesses: 10")
while True:
    if guess==0:
        print("GAME OVER :(","\nInteger was :",n)
        break
    num1=int(input("Guess the INTEGER upto 100:"))
    guess=guess-1
    if num1>100 :
        print("INVALID ENTRY!!!\nTry Again")
        continue
    if num1<n or num1>n:
        print("Wrong Guess","Try Again!")
        if num1<n:
            print("Increase your value","                 Guesses Left:",guess)
        elif num1>n:
            print("Decrease your value","                 Guesses Left:",guess)
      #  print("Guesses Left:",guess)
        continue
    if num1==n:
        print("Correct Guess!!!!!!",",YOU WON")
        print("You Took ",10-guess,"Guess to Complete")
        break
