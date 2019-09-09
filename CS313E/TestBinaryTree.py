#  File: TestBinaryTree.py

#  Description: Tests a Binary Tree

#  Date Created: 4/13/18

#  Date Last Modified: 4/15/18

def print_level_helper(self, eNode, level):
  if eNode == None:
    return

  if (level > 1):
    return print_level_helper(self, eNode.lchild, level - 1), print_level_helper(self, eNode.rchild, level - 1)

  else:
    print( str(eNode.data))

def num_nodes_helper(self, dNode):
  if dNode == None:
    return 0
  else:
    return 1 + num_nodes_helper(self, dNode.lchild) + num_nodes_helper(self, dNode.rchild)

def get_height_helper(self, cNode):
  if cNode == None:
    return 0
  else:
    return 1 + max(get_height_helper(self, cNode.lchild), get_height_helper(self, cNode.rchild))

def is_similar_helper(self, aNode, bNode):
  if (aNode == None) and (bNode == None):
    return True

  #Is aNode a leaf and bNode not, vice versa
  if (aNode.lchild == None and aNode.rchild == None):
    if (bNode.lchild != None or bNode.rchild != None):
      return False
    
  if (bNode.lchild == None and bNode.rchild == None):
    if (aNode.lchild != None or aNode.rchild != None):
      return False

  #Is aNode none, is bNode none
  if (aNode == None and bNode != None) or (aNode != None and bNode == None):
    return False

  #If aNode.data == bNode.data
  if (aNode.data != bNode.data):
    return False

  return ((is_similar_helper(self, aNode.lchild, aNode.lchild) and is_similar_helper(self, aNode.rchild, aNode.rchild)) and (aNode.data == bNode.data))

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # insert a node in a tree
  def insert (self, val):
    new_node = Node (val)

    if (self.root == None):
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lchild
        else:
          current = current.rchild
      if (val < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # in order traversal - left, center, right
  def in_order (self, aNode):
    if (aNode != None):
      self.in_order (aNode.lchild)
      print (aNode.data)
      self.in_order (aNode.rchild)   

  # Returns true if two binary trees are similar
  def is_similar (self, pNode):
    return is_similar_helper(self, self.root, pNode.root)

  # Prints out all nodes at the given level
  def print_level (self, level): 
    return print_level_helper(self, self.root, level)
  
  # Returns the height of the tree
  def get_height (self):
    return get_height_helper(self, self.root)
  
  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
    return num_nodes_helper(self, self.root)

def main():
    
    # Create three trees - two are the same and the third is different 
    t1 = Tree()
    t2 = Tree()
    t3 = Tree()
    
    nodes1 = [8,6,7,5,3,0,9]
    nodes2 = [8,6,7,5,3,0,9]
    nodes3 = [6,7,8,9,9,9,8,2,1,2]

    for i in nodes1:
        t1.insert(i)
    for j in nodes2:
        t2.insert(j)
    for k in nodes3:
        t3.insert(k)


    # Printing out each tree
    print("\n        T R E E S:", "\n1:", nodes1, "\n2:", nodes2, "\n3:", nodes3, "\n")
    
    # Test your method is_similar()
    print("Tree 1 is similar to tree 2?: ", t1.is_similar(t2))
    print("Tree 1 is similar to tree 3?: ", t1.is_similar(t3), "\n")
    
    # Print the various levels of two of the trees that are different
    lvl = 3
    print("Prints level", lvl, "of Tree 1")
    t1.print_level(lvl)
    print("Prints level", lvl, "of Tree 2")
    t3.print_level(lvl)
    print()
    
    # Get the height of the two trees that are different
    print("Height of Tree 1:", t1.get_height())
    print("Height of Tree 3:", t3.get_height(), "\n")
    
    # Get the total number of nodes a binary search tree
    print("Nodes in Tree 1:", t1.num_nodes())
    print("Nodes in Tree 3:", t3.num_nodes())
    
main()
