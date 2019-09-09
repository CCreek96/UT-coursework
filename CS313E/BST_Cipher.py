#  File: BST_Cipher.py

#  Date Created: 17 April 2018

#  Date Last Modified: 05 May 2018

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
    self.root = None
    encrypt_str = encrypt_str.lower()
    for ch in encrypt_str:
        if (ch.isalpha() or ch == ' '):
            self.insert (ch)


  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    new_node = Node (ch)
    if (self.root == None):
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (ch == current.data):
          return
        elif (ch < current.data):
          current = current.lchild
        else:
          current = current.rchild
      if (ch < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    output = ''
    current = self.root
    if (current.data == ch):
      return '*'
    else:
        while (current != None) and (current.data != ch):
          if (current == None):
            return ''
          elif (ch < current.data):
            current = current.lchild
            output += '<'
          else:
            current = current.rchild
            output += '>'


    return output


  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    current = self.root

    for item in st:
      if (current == None):
          return ''
      elif (item == '*'):
          return self.root.data
      elif (item == '<'):
          current = current.lchild
      else:
          current = current.rchild

    return current.data


  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    st = st.lower()
    output = ''
    for ch in st:
        if (ch.isalpha() or ch == ' '):
            item = self.search (ch)
            if (item != ''):
                output += item + '!'
    return output[:-1]

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    output = ''
    st = st.split('!')
    for item in st:
        output += self.traverse(item)
    return output

def main():


  # key = input('Enter encryption key: ')
  key = 'the quick brown fox jumps over the lazy dog'
  encrypt_tree = Tree(key)

  encrypt = input('Enter string to be encrypted: ')
  st = encrypt_tree.encrypt(encrypt)
  print ('Encrypted string: {}'.format(st))

  decrypt = input('Enter string to be decrypted: ')
  st = encrypt_tree.decrypt(decrypt)
  print ('Decrypted string: {}'.format(st))


main()
