#If a new spot chosen is already chosen
def checkdifference(new):
  Choice = True
  for i in range(picks):
    if new == chosen[i]:
      Choice = False
  if Choice == True:
    return True
  else:
    return False

#If specific requirments for a win is met, then the player wins
def checkwin(player):
  isWin = False
  if player == 1:
    areacheck = area1
    player = "player1"
  elif player == 2:
    areacheck = area2
    player = "player2"
  for i in range (len(areacheck)):
    if areacheck[i] %3 == 1:
      if ((areacheck[i]+1) in areacheck) and ((areacheck[i]+2) in areacheck):
        print(player, "won horozontally")
        isWin = True
    if areacheck[i] <= 3:
      if ((areacheck[i]+3) in areacheck) and ((areacheck[i]+6) in areacheck):
        print(player, "won vertically")
        isWin = True
    if areacheck[i] == 1:
      if ((areacheck[i]+4) in areacheck) and ((areacheck[i]+8) in areacheck):
        print(player, "won diagonally from top left to bottom right")
        isWin = True
    if areacheck[i] == 3:
      if ((areacheck[i]+2) in areacheck) and ((areacheck[i]+4) in areacheck):
        print(player, "won diagonally from top right to bottom left")
        isWin = True
    if isWin == True:
      global win
      win = True

print("Welcome to tic tac toe!")
#area of players choices
area1 = []
area2 = []
#area of total chosen squares
chosen = []
#Counts how many choices made in total per player
Choices_1 = 0
Choices_2 = 0
#Counts choices in total
picks = 0
win = False
#Visual asthetics
grid = ["-","-","-","-","-","-","-","-","-"]

print(grid[0],grid[1],grid[2])
print(grid[3],grid[4],grid[5])
print(grid[6],grid[7],grid[8])

while picks < 9 and win == False:

#Player1's turn
  while Choices_1 < 5 and win == False:
    print("Player 1 choose a square")
    player1 = input()
    if player1.isnumeric():
      player1 = int(player1)
      if 1 <= player1 and player1<=9:
          if checkdifference(player1):
            Choices_1 += 1
            area1.append(player1)
            chosen.append(player1)
            picks += 1
            print("player one chose", player1)
            grid[player1-1] = "X"
            checkwin(1)
            break
          else:
            print("already chosen")
      else:
        print("not in range 1-9")
    else:
      print("not numeric")

#Player2's turn
  if win == False and picks!= 9:
    print(grid[0],grid[1],grid[2])
    print(grid[3],grid[4],grid[5])
    print(grid[6],grid[7],grid[8])
  while Choices_2 < 4 and win == False:
    print("Player 2 choose a square")
    player2 = input()
    if player2.isnumeric():
      player2 = int(player2)
      if 1 <= player2 and player2<=9:
          if checkdifference(player2):
            Choices_2 += 1
            area2.append(player2)
            chosen.append(player2)
            picks += 1
            print("player two chose", player2)
            grid[player2-1] = "O"
            checkwin(2)
            break
          else:
            print("already chosen")
      else:
        print("not in range 1-9")
    else:
      print("not numeric")
  print(grid[0],grid[1],grid[2])
  print(grid[3],grid[4],grid[5])
  print(grid[6],grid[7],grid[8])
if win == False:
  print("it is a tie!!")
