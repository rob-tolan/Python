#"Rolling Dice Simulator-Python"
"""
Spyder Editor

This is a temporary script file.
"""
import random
num1=random(1,6)
num2=random(1,6)
rolled_num = random.randint(1,6)
print("You rolled: ", rolled_num)
while True:
    rolled_num = random.randint(1,6)
    print("The dice rolled and you got: ", rolled_num)
    input("Press any key to roll again.")
answer=input()
    