import random

#String and List Manupilation
def display(board):
  print(f'''
  {board[7]}|{board[8]}|{board[9]}                 7 | 8 | 9
  ---+---+---               ---+---+---
  {board[4]}|{board[5]}|{board[6]}    Positions->  4 | 5 | 6
  ---+---+---               ---+---+---
  {board[1]}|{board[2]}|{board[3]}                 1 | 2 | 3
  ''')

#-------------------------------------------------------
#Filling the board of Game
def valid_input():
  while True:
    pos = input("Enter Position: ")
    if pos != ' ':                  #Checks if inout is Space
      if int(pos) in range(1,10):   #Typecasting into Int data type
        pos = int(pos)              #permanently typecasted
        break                       #without break, it will keep taking the input
      print('Not Valid Position\n')
    else:
      print("Thank You for Playing Tic-Tac-Toe!")
      exit()
  return int(pos)



#-------------------------------------------------------
def valid_pos(turn, board):
  print(f'{turn} chance')
  pos = valid_input()         #Input stored in 'pos' variable
  while True:
    if board[pos] == '  ':    #List Manipulation (Check if that position is empty or not for assigning)io)
      board[pos] = turn
      break
  else:                       #If position is already filled
    print('Cannot Overwrite, Please select new Location')
    pos = valid_input()



#-------------------------------------------------------
#Taking User Input when anyon can play first
def userInput(board, symbol):
  sym1, sym2 = symbol[random.randint(0,1)]
  print(sym1, sym2)
  #Hardcoding that O will go first
    #print(f"{sym1} is going first\n\n")
  for i in range(9):
    if i%2==0:
      turn = ' '+sym1+' '
      valid_pos(turn, board)
    else:
      turn = ' '+sym2+' '
      valid_pos(turn, board)
    display(board)
    if i>=4:
      if check(board):
        display(board)
        print(f" '{turn}' WON")
        break
      if i == 8:
        print("None WON, Its A Tie!!")




#-------------------------------------------------------
#To Check if we won the game (Indices of Game)
#FLAG METHOD - IF IT IS HOISTED, IT IS TRUE; IF NOT, FALSE
def check(board): #(Value checking, not BITWISE checking)
  check = 0
  #Checking for any one ROW
  #three values not equal to blank but equal to each other
  if board[1] == board[2] == board[3] != ' ' or\
     board[4] == board[5] == board[6] != ' ' or\
     board[7] == board[8] == board[9] != ' ' or:  
     check = 1
  #Checking for any one COLUMN
  #three values not equal to blank but equal to each other
  elif board[1] == board[4] == board[7] != '    ' or\
       board[2] == board[5] == board[8] != '    ' or\
       board[3] == board[6] == board[9] != '    ' or:
       check = 1
  #Checking for any one DIAGONAL
  #three values not equal to blank but equal to each other
  elif board[1] == board[5] == board[9] != '    ' or\
       board[3] == board[5] == board[7] != '    ' or:
       check = 1
  return check


#-------------------------------------------------------
def game():
  board = ["Just to adjust loc :)", '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']
#Selection of Symbol
  symbol = [('X', 'O'), ('O', 'X')]
  while True:
    marker = input("\nEnter your marker: ").upper()
    if marker == ' ':
      print("Thank You for Playing Tic-Tac-Toe!")
      exit()
    if marker == 'X' or marker == 'O':
      userInput(board, symbol)
      break
    else:
      print('Wrong Marker (X, O) Please Enter Again. \n')
  #display(board)

#-------------------------------------------------------
def main():
  again = 'Y'              #Hardcoding
  while again == 'Y':
    print('Press [space] for input whenever you want to stop the game')
    game()
    again = input("Press 'Y/N' to Play Again! ").upper()
main()