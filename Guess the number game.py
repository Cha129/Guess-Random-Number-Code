#Guess the number game
import random
a=str(input("Select the option that number digits you want to play from the given options A) 1-digit  B) 2-digit  C) 3-digit  D) 4-digit  E) 5-digit F) 6-digit: "))
if a=="A" or a=="a":
    guess_number=int(input("Guess the number from to 0 to 9: "))
    num=random.randint(0,9)
    if guess_number>=0 and guess_number<=9:
        if guess_number==num:
            print("You have guessed correct",num)
        else:
            print("Your guess is incorrect,The correct answer is", num)
    else:
        print("Guess the number from to 0 to 9")
        
if a=="B" or a=="b":
    guess_number=int(input("Guess the number from to 10 to 99: "))
    num=random.randint(10,99)
    if guess_number>=10 and guess_number<=99:
        if guess_number==num:
            print("You have guessed correct",num)
        else:
            print("Your guess is incorrect,The correct answer is", num)
    else:
        print("Guess the number from to 10 to 99")
if a=="C" or a=="c":
    guess_number=int(input("Guess the number from to 100 to 999: "))
    num=random.randint(100,99)
    if guess_number>=100 and guess_number<=999:
        if guess_number==num:
            print("You have guessed correct",num)
        else:
            print("Your guess is incorrect,The correct answer is", num)
    else:
        print("Guess the number from to 100 to 999")
if a=="D" or a=="d":
    guess_number=int(input("Guess the number from to 1000 to 9999: "))
    num=random.randint(1000,9999)
    if guess_number>=1000 and guess_number<=9999:
        if guess_number==num:
            print("You have guessed correct",num)
        else:
            print("Your guess is incorrect,The correct answer is", num)
    else:
        print("Guess the number from to 1000 to 9999")
if a=="E" or a=="e":
    guess_number=int(input("Guess the number from to 10000 to 99999: "))
    num=random.randint(10000,99999)
    if guess_number>=10000 and guess_number<=99999:
        if guess_number==num:
            print("You have guessed correct",num)
        else:
            print("Your guess is incorrect,The correct answer is", num)
    else:
        print("Guess the number from to 10000 to 99999")
if a=="F" or a=="f":
    guess_number=int(input("Guess the number from to 100000 to 999999: "))
    num=random.randint(100000,999999)
    if guess_number>=100000 and guess_number<=999999:
        if guess_number==num:
            print("You have guessed correct",num)
        else:
            print("Your guess is incorrect,The correct answer is", num)
    else:
        print("Guess the number from to 100000 to 999999")








        
            

        

    
        
