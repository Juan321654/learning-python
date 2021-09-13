import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scossors = [rock, paper, scissors]
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissoes.\n"))

if choose > 2 or choose < 0:
    print("You type an invalid number, you lose!!!")

else:
  user_choose = rock_paper_scossors[choose]
  print("You choose\n\n")
  print(user_choose)

  computer_random_num = random.randint(0, 2)
  computer_choose = rock_paper_scossors[computer_random_num]
  print("Computer chose:\n")
  print(computer_choose)

  win_result = [[0, 2], [1, 0], [2, 1]]
  lose_result = [[0, 1], [1, 2], [2, 0]]
  result = [choose, computer_random_num]

  if result == win_result[0] or result == win_result[1] or result == win_result[2]:
      print("You win")

  elif result == lose_result[0] or result == lose_result[1] or result == lose_result[2]:
      print("You Lose")
  else:
      print("Draw")
