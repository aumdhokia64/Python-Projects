import random

while True:
 items=["rock", "paper", "scissors"]

 computer = random.choice(items)

 user = input("Rock , Paper or Scissors ?: ").lower()
 print("Computer Chooses:", computer)

 if user == computer:
    print("Match Draw !!")
 elif user == "rock" and computer == "scissors":
    print("User Wins !!")
 elif user == "paper" and computer == "rock":
    print("User Wins !!")
 elif user == "scissors" and computer == "paper":
    print("User Wins !!")
    break
 else:
    print("Computer Wins !!")
    break
