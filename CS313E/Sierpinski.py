# File: Sierpinski.py

# Description: Draws Sierpinski's Curve or Gasket

import math, turtle

def drawGasket (ttl, size):
  if size < 10:
    return
  for iter in range (3):
    ttl.forward (size / 2)
    insertGasket (ttl, size)
    ttl.forward (size / 2)
    ttl.right (120)

def insertGasket (ttl, size):
  ttl.left (120)
  drawGasket (ttl, size / 2)
  ttl.right (120)

def oneSide (ttl, s, diag, level):
  if (level == 0):
    return
  else:
    oneSide (ttl, s, diag, level - 1)
    ttl.right (45); ttl.forward (diag); ttl.right (45)
    oneSide (ttl, s, diag, level - 1)
    ttl.left (90); ttl.forward (s); ttl.left (90)
    oneSide (ttl, s, diag, level - 1)
    ttl.right (45); ttl.forward (diag); ttl.right (45)
    oneSide (ttl, s, diag, level - 1)

def curve (ttl, s, level):
  diag = s / math.sqrt (2)
  for iter in range (4):
    oneSide (ttl, s, diag, level)
    ttl.right (45)
    ttl.forward (diag)
    ttl.right (45)

def main():
  # put label on top of page
  turtle.title ('Recursive Figures')

  # setup screen size
  turtle.setup (1000, 1000, 0, 0)

  # create a turtle object
  ttl = turtle.Turtle()

  # draw the sierpinski curve
  # curve (ttl, 15, 3)

  # draw gasket
  drawGasket (ttl, 200)

  # persist drawing
  turtle.done()

main()
