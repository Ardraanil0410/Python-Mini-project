correct_number=25
guess=0
while guess<10:
    guess = guess + 1
    guess_number = int(input("Please enter a number between 1 and 100 : "))
    if guess_number==correct_number:
        print("You have guessed the correct number")
        break
    elif guess_number!=correct_number:
        print(f"Sorry, Try Again!, you have {10-guess} left")
    elif guess_number!=correct_number and guess==10:
        print("Your chances are exhausted")
    else:
        ("End of game")
print("All chances gone")
