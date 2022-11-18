from copy import deepcopy
import random
import os
# from time import sleep
# print("Screen will now be cleared in 5 Seconds")
 
# Waiting for 5 seconds to clear the screen
# sleep(5)
 

HEIGHT = 6
WIDTH = 7
def initialize():
  #Sets up the empty board.

  board = []
  for i in range(HEIGHT):
    # makes 7 _ indexes in the board array
    board.append(["_"] * WIDTH)
  return board


# def correct_input(col):
#   if col 
  
def print_board(board):
  '''
  Prints out a correct formatted board.
  '''
  print(" ")
  print ("1 2 3 4 5 6 7")
  print("_" * 13)
  for row in board:
    # attaches 6 | to _ and prints board for first time empty9
    print("|".join(row))


def get_move(board, player):
  '''
  Takes the board and the player as parameter. Askes the player to input a
  column and checks if the entry is valid.
  '''
  print("Your the letter P ")
  col = input("enter a column number {}: ".format(player))
  while not col.isdigit():
    col = input("Give a number between 1 and 7")
  col = int(col)
  # check if column is valid
  if col < 1 or col > WIDTH :
    input("Invalid input. Enter a number between 1 and 7.")
    col = get_move(board, player)

  # convert from indexing from 1 to indexing from 0
  col = col - 1

  # check if column is full
  col_full = True
  for i in range(HEIGHT):
    if board[i][col] == "_":
      col_full = False
      break
  if col_full:
    print("That column is full. Please try again.")
    col = get_move(board, player)
  return col


def get_comp_move(board, comp, user):
  '''
  Checks if any entry would result in a win, otherwise makes a random move.
  '''
  # Check if the computer can win in one move
  for col in range(WIDTH):
    # Create a copy of the board
    temp_board = deepcopy(board)

    temp_board = make_move(temp_board, comp, col)
    if check_win(temp_board) == comp:
      return col

  # Check if the user can win next move
  for col in range(WIDTH):
    # Create a copy of the board
    temp_board = deepcopy(board)
    temp_board = make_move(temp_board, user, col)
    if check_win(temp_board) == user:
      return col
      
  # Choose a random column
  col = random.randint(0, WIDTH - 1)
  return col


def make_move(board, player, col):
  '''
  Takes the board, the player, and the player's entry and makes the move based
  on the board configuration and the entry.
  '''
  row = 0
  for i in range(HEIGHT):
    if board[i][col] == "_":
      row = i
    else:
      break
  board[row][col] = player
  return board


def check_win(board):
  '''
  This function takes the board as a parameter and checks if someone has won
  the game. If so, it returns the player that has won. Otherwise, it returns
  an empty string.
  '''
  # Check horizontal for winner
  for row in range(HEIGHT):
    for col in range(WIDTH - 3):
      if (board[row][col] == board[row][col + 1] == board[row][col + 2] \
      == board[row][col + 3]) and (board[row][col] != "_"):
        return board[row][col]
  # Check vertical for winner
  for col in range(WIDTH):
    for row in range(HEIGHT - 3):
      if (board[row][col] == board[row + 1][col] == board[row + 2][col] \
      == board[row + 3][col]) and (board[row][col] != "_"):
        return board[row][col]

  # Check diagonal (top-left to bottom-right) for winner
  for row in range(HEIGHT - 3):
    for col in range(WIDTH - 3):
      if (board[row][col] == board[row + 1][col + 1] == \
      board[row + 2][col + 2] == board[row + 3][col + 3]) \
      and (board[row][col] != "_"):
        return board[row][col]
  # Check diagonal (bottom-left to top-right) for winner
  for row in range(HEIGHT - 1, HEIGHT - 3, -1):
    for col in range(WIDTH - 3):
      if (board[row][col] == board[row - 1][col + 1] == \
      board[row - 2][col + 2] == board[row - 3][col + 3]) \
      and (board[row][col] != "_"):
        return board[row][col]
  # Check if board is full
  full = True
  for row in range(HEIGHT):
    for col in range(WIDTH):
      if board[row][col] == "_":
        full = False
      break
  if full:
        return "Tie"

  # If none of the above are true then the game is not over
  return ""


def main():
  # Sets up the game and runs the game loop until the game is over.
  board = initialize()
  player = "P"
  winner = ""

  while winner == "":
    # Clearing the Screen
    os.system('clear')
    print_board(board)
    if player == "P":
      print("User's turn")
      col = get_move(board, player)
      board = make_move(board, player, col)
      player = "C"
    else:
      print(" ")
      print("Computer's turn")
      col = get_comp_move(board, "C", "P")
      board = make_move(board, player, col)
      player = "P"

    winner = check_win(board)

  print_board(board)
  if winner == "Tie":
    print("Tie game.")
  else:
    print(" ")
    print("Player {} wins!".format(winner))
if __name__ == "__main__":
  main()
