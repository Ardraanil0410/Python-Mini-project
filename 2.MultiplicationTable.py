#Ask for a number from user
number = int(input("Please enter a number to calculate its table :  "))

#Header
print(f"\nMultiplication table for the number {number}:\n"+"-"*40)

#loop from 1 to 10
for i in range(1,11):
    multiple=number*i
    print(f"{i} x {number} = {multiple}")