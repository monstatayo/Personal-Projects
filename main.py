# THIS CODE WAS CREATED BY GABRIEL KIM | 12/03/2020

from itertools import permutations  
from itertools import combinations  
import random
import time
import turtle


turtle.speed(0)



def match(permutations, positions):

  #This function is intended to be fed permutations of current values created through combinations of checkTaken. It returns true for any match.

  if positions in permutations:
    return True

def checkPositions(first, second, third):

  #This function acts as the meat of the algorithm and what runs under the hood. Using itertools, 3 values are fed into this function, a list of permutations from them are created. Winning combinations of all types are then generated through winningCombos. Remember, any number fed through this function is guaranteed to have been already claimed by a player by the time it is invoked. It returns true if these three numbers exist within any of the feasible combinations, and sends a boolean to checkTaken

  currentCombo = (first,second,third)

  winningCombos = [permutations([1,2,3]), permutations([4,5,6]), permutations([7,8,9]), permutations([9,6,3]), permutations([8,5,2]), permutations([7,4,1]), permutations([7,5,3]), permutations([9,5,1])]

  for i in winningCombos:
    winner = match(i, currentCombo)
    if winner == True:
      return True
  
  return False
  
def checkTaken(taken):

  # this function is basically the finished product of the process that checks for any winning combinations dynamically during the game. It calls checkPositions which for any combinations of 3 values that exist in the list, and takes all possible combinations into play as long as taken has 3 or more elements. It will return if a player wins or not.

  comb = combinations(taken, 3)

  for i in list(comb):
    if (checkPositions(i[0], i[1], i[2]) == True):
      return True
  
  return False


def newBoard():

  # This function uses turtle to draw a new board.

  turtle.backward(150)
  turtle.forward(300)
  turtle.left(90)
  turtle.penup()
  turtle.forward(100)
  turtle.pendown()
  turtle.left(90)
  turtle.forward(300)
  turtle.right(90)
  turtle.penup()
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.pendown()
  turtle.forward(300)
  turtle.penup()
  turtle.left(90)
  turtle.forward(100)
  turtle.left(90)
  turtle.pendown()
  turtle.forward(300)
  turtle.penup()
  turtle.left(180)
  turtle.forward(150)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)

def xAt(position):

  # This function designates a precise location for the numerical position given, and uses drawX() to create the shape.

  if (position == 1):
    turtle.penup()
    turtle.left(135)
    turtle.forward(150)
    drawX()

  elif (position == 2):
    turtle.penup()
    turtle.left(180)
    turtle.forward(100)
    turtle.left(45)
    drawX()

  elif (position == 3):
    turtle.penup()
    turtle.right(135)
    turtle.forward(150)
    drawX()

  elif (position == 4):
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.left(45)
    drawX()

  elif (position == 5):
    turtle.left(45)
    drawX()
    

  elif (position == 6):
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.left(45)
    drawX()

  elif (position == 7):
    turtle.penup()
    turtle.left(45)
    turtle.forward(150)
    drawX()

  elif (position == 8):
    turtle.penup()
    turtle.forward(100)
    turtle.left(45)
    drawX()

  elif (position == 9):
    turtle.penup()
    turtle.right(45)
    turtle.forward(150)
    drawX()
  
  turtle.setheading(90)

def oAt(position):

  # This function designates a precise location for the numerical position given, and uses drawO() to create the shape.


  if (position == 1):
    turtle.penup()
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(100)
    drawO()
  
  elif (position == 2):
    turtle.penup()
    turtle.backward(50)
    turtle.left(90)
    drawO()
  
  elif (position == 3):
    turtle.penup()
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(180)
    drawO()

  elif (position == 4):
    turtle.penup()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    drawO()

  elif (position == 5):
    turtle.penup()
    turtle.forward(50)
    turtle.left(90)
    drawO()

  elif (position == 6):
    turtle.penup()
    turtle.forward(50)
    turtle.left(90)
    turtle.backward(100)
    drawO()

  elif (position == 7):
    turtle.penup()
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(100)
    drawO()
  
  elif (position == 8):
    turtle.penup()
    turtle.forward(150)
    turtle.left(90)
    drawO()

  elif (position == 9):
    turtle.penup()
    turtle.forward(150)
    turtle.left(90)
    turtle.backward(100)
    drawO()
  
  turtle.setheading(90)

def drawX():

    # This function creates the "X" shape in a certain spot designated by xAt.

  turtle.pendown()
  turtle.forward(50)
  turtle.backward(100)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.backward(100)
  turtle.penup()
  turtle.goto(0,50)

def drawO():

    # This function creates the "O" shape in a certain spot designated by oAt()

  turtle.pendown()
  turtle.circle(45)
  turtle.penup()
  turtle.goto(0,50) 

def drawPosition(position, player):

  # This is a utility function that uses the draw and at functions appropriately given the player numbers.

  if (position > 0 and position < 10):

    if (player == 1):
      xAt(position)

    elif(player == 2):
      oAt(position)

  else:
     print("Invalid position!")



def mainGame():

  # This is the main menu of the game. It creates a new board and prints a menu. It uses a coin flip to designate which player goes first via RNG.

  newBoard()
  print("TIC-TAC-TOE\n")
  time.sleep(1)

  first = input("(X) Player 1 : ")
  second = input("(O) Player 2: ")

  print("\nLet's flip a coin!\n")
  time.sleep(1)
  print("...")
  time.sleep(1)
  print("...")
  time.sleep(1)
  print("...\n")
  time.sleep(1)

  startingTurn = random.randint(1,2)

  if (startingTurn == 1):
    print("First turn goes to", first)
    firstturn = first
    secondturn = second

  elif(startingTurn == 2):
    print("First turn goes to", second)
    firstturn = second
    secondturn = first

  print("\n\n")

  #The lists below indicate the availability of positions throughout the course of the game. As each player claims a spot, an available position in spacesLeft is taken out and put into either player's list of claimed positions. The player lists are later fed through the permutation/combination related functions as the game progresses to check for the first winner.

  spacesLeft = [1,2,3,4,5,6,7,8,9]
  xTaken = []
  oTaken = []

  for i in range(1,10):      

    if (i % 2 == 1):

      print(firstturn + "`s turn!")
      pos = int(input("Pick a space: ")) 

      while(pos > 9 or pos < 1 or (pos not in spacesLeft)):
        pos = int(input("Pick a valid space!"))
      
      spacesLeft.remove(pos)
      xTaken.append(pos)
      
      drawPosition(pos, 1)

    elif (i % 2 == 0):

      print(secondturn + "`s turn!")
      pos = int(input("Pick a space: ")) 

      while(pos > 9 or pos < 1 or (pos not in spacesLeft)):
        pos = int(input("Pick a valid space!"))
      
      spacesLeft.remove(pos)
      oTaken.append(pos)
      
      drawPosition(pos, 2)


    if (i % 2 == 1):
       winner = checkTaken(xTaken)
       if (winner == True):
        print(firstturn + " wins!")
        endgame()

    elif (i % 2 == 0):
       winner = checkTaken(oTaken)
       if (winner == True):
        print(secondturn + " wins!")
        endgame()
      


def endgame():

  # A function to either start a new game or quit.

  select = input("Would you like to play again? (Y/N)")
  if (select == "Y" or select == "y"):
    mainGame()
  elif(select == "N" or select == "n"):
    exit()
  else:
    endgame()
      
    
endgame()