import random
# by importint random we can use the random module without any error
'''
Game information:
1 for snake
-1 for water
0 for gun
snake vs water -> snake will win
water vs gun -> water will win
gun vs snake -> gun will win
'''
computer = random.choice([-1, 0, 1]) # By using random choice module the computer can choose a random number
youstr = input("Enter what you wanna choose: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

# Now we have 2 numbers , one chose by user and one randomly chose by the computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
  print("It's a draw!!")
 
else: 
  if(computer == -1 and you == 1):
    print("You Win!!")
  elif(computer == -1 and you == 0):
    print("You Lose :( ")
  elif(computer == 1 and you == -1):
    print("You Lose :( ")
  elif(computer == 1 and you == 0):
    print("You Win!!")
  elif(computer == 0 and you == 1):
    print("You Lose :( ")
  elif(computer == 0 and you == -1):
    print("You Win!!")
  else:
    print("Something went wrong!!") 
 
 

