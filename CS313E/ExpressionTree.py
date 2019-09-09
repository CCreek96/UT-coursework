#  File: ExpressionTree.py

#  Description: Expression Tree and InFix evaluation

#  Date Created: 4/10/18

#  Date Last Modified: 4/12/18

operators = ['+', '-', '*', '/']
pre = []
post = []

def readText(text):
  with open("expression.txt", "r") as txt:
    txt = txt.readline().rstrip()
  return txt

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack is empty
  def is_empty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  def createTree (self, expr):
    stack = Stack()
    tokens = expr.split()

    if self.root == None:
      self.root = Node(None)

    current = self.root

    for token in tokens:
      if (token == '('):
        stack.push(current)
        current.lChild = Node(None)
        current = current.lChild
      elif (token in operators):
        current.data = token
        stack.push(current)
        current.rChild = Node(None)
        current = current.rChild
      # If the current token is an operand, set the current node's data
      # value to the operand and make the current node equal to the parent
      # by popping the stack
      elif (token.isdigit()):
        current.data = token
        current = stack.pop()
      # If the current token is a right parenthesis make the current node
      # equal to the parent node by popping the stack if it is not empty
      elif (token == ')'):
        if (not stack.is_empty()):
          current = stack.pop()
        else:
          break
      else:
          continue

  def evaluate (self, aNode):
    stack = Stack()
    num = ""
    while len(aNode) > 0:
      c = aNode.pop(0)
      if c in "0123456789.":
        num += c
      else:
        if num != "":
          stack.push(num)
          num = ""
        if c in "+-*/":
          stack.push(c)
        elif c == ")":
          num2 = stack.pop()
          op = stack.pop()
          num1 = stack.pop()
          if op == "+":
            stack.push(str(float(num1) + float(num2)))
          elif op == "-":
            stack.push(str(float(num1) - float(num2)))
          elif op == "*":
            stack.push(str(float(num1) * float(num2)))
          elif op == "/":
            stack.push(str(float(num1) / float(num2)))
            
    return stack.pop()

  def preOrder (self, aNode):
    if (aNode != None):
      pre.append(aNode.data)
      self.preOrder (aNode.lChild)
      self.preOrder (aNode.rChild)

  def postOrder (self, aNode):
    if (aNode != None):
      self.postOrder (aNode.lChild)
      self.postOrder (aNode.rChild)
      post.append(aNode.data)

def main():
  expr = readText('expression.txt')
  tree = Tree()
  
  listExpr = []
  strPre = ""
  strPost = ""
  for token in expr:
    listExpr.append(token) #Lazily converting string expr to a list
  tree.createTree(expr)
  evaluated = tree.evaluate(listExpr)
  print("\n" + expr, "=", evaluated, "\n")

  tree.postOrder(tree.root)
  tree.preOrder(tree.root)

  for token in pre:
    strPre += token
    strPre += " "

  for token in post:
    strPost += token
    strPost += " "
    
  print("Prefix Expression:", strPre, "\n")
  print("Postfix Expression:", strPost)

main()
