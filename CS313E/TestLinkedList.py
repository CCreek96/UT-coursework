#  File: TestLinkedList.py

#  Description: Various functions for a linked list

#  Date Created: 3/29/2018

#  Date Last Modified: 3/30/2018

class Link (object):
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList (object):
  def __init__(self):
    self.first = None

  # get number of links
  def get_num_links (self):
    current = self.first
    count = 0
    if (current == None):
      return count
    while (current != None):
      count += 1
      current = current.next
    return count

  # add an item at the beginning of the list
  def insert_first (self, item):
    new_link = Link(item)

    new_link.next = self.first
    self.first = new_link

  # add an item at the end of a list
  def insert_last (self, item):
    new_link = Link (item)
    current = self.first

    if (current == None):
      self.first = new_link
      return

    while (current.next != None):
        current = current.next

    current.next = new_link

  # add an item in an ordered list in ascending order
  def insert_in_order (self, item):
    new_link = Link(item)
    current = self.first

    if (current == None or current.data > new_link.data):
      self.insert_first(new_link.data)
      return

    while (current.next != None and current.next.data <= new_link.data):
        current = current.next

    new_link.next = current.next
    current.next = new_link

  # search in an unordered list, return None if not found
  def find_unordered (self, item):
    current = self.first

    if (current == None):
      return None

    while (current.data != item):
      if (current.next == None):
        break
      else:
        current = current.next

    if (current.data == item):
      return current
    else:
      return None


  # Search in an ordered list, return None if not found
  def find_ordered (self, item):
    current = self.first

    if (current == None):
      return None

    while (current.data < item and current != None):
      if (current.next == None):
        break
      else:
        current = current.next

    if (current.data == item):
      return current.data
    else:
      return None

  # Delete and return Link from an unordered list or None if not found
  def delete_link (self, item):
    previous = self.first
    current = self.first

    if (current == None):
      return None

    while (current.data != item):
      if (current.next == None):
        return None
      else:
        previous = current
        current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    current = self.first
    s = ""
    count = 0

    if (current == None):
      return s

    while (current != None):
      s += str(current.data) + "  "
      current = current.next
      count += 1
      if (count % 10 == 0):
        s += "\n"

    return s

  # Copy the contents of a list and return new list
  def copy_list (self):
    current = self.first
    new_list = LinkedList()

    while (current != None):
      new_list.insert_last(current.data)
      current = current.next

    return new_list

  # Reverse the contents of a list and return new list
  def reverse_list (self):
    new_list = LinkedList()
    current = self.first

    while (current != None):
      new_list.insert_first(current.data)
      current = current.next

    return new_list

  # Sort the contents of a list in ascending order and return new list
  def sort_list (self):
    new_list = LinkedList()
    current = self.first

    while (current != None):
      new_list.insert_in_order(current.data)
      current = current.next

    return new_list


  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    current = self.first

    while(current != None):
      if(current.next == None):
        current = current.next
        continue
      elif(current.next.data < current.data):
        return False
      else:
        current = current.next

    if(current == None):
      return True

  # Return True if a list is empty or False otherwise
  def is_empty (self):
    return (self.first == None)

  # Merge two sorted lists and return new list in ascending order
  def merge_list (self, other):
    current1 = self.first
    current2 = other.first
    merged = LinkedList()

    while current1 != None:
      merged.insert_in_order(current1.data)
      current1 = current1.next

    while current2 != None:
      merged.insert_in_order(current2.data)
      current2 = current2.next

    return merged


  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    current1 = self.first
    current2 = other.first
    flag = True

    if (self.get_num_links() != other.get_num_links()):
      flag = False

    while (current1.next != None):
      if (current1.data != current2.data):
        flag = False
      else:
        current1 = current1.next
        current2 = current2.next

    return flag

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates (self):
    new_list = LinkedList()
    current = self.first

    while (current != None):
      if (new_list.find_ordered(current.data) != None):
        current = current.next
      else:
        new_list.insert_last(current.data)
        current = current.next

    return new_list

def main():

  ## SCRATCH WORK ##
  '''
  testLL = LinkedList()
  empy = LinkedList()
  testLL.insert_first(1)
  testLL.insert_first(2)
  testLL.insert_first(3)
  testLL.insert_first(4)
  testLL.insert_first(5)
  testLL.insert_first(6)
  testLL.insert_first(7)
  testLL.insert_first(8)
  testLL.insert_first(9)
  testLL.insert_first(11)

  print ('\ninsert Last test\n')
  testLL.insert_last(10)
  testLL.insert_last(20)
  print(testLL)
  print ('\nis empty test\n')
  print(testLL.is_empty())

  print ('\nget_num_links test\n')
  print(testLL.get_num_links())

  print ('\nis sorted test\n')
  print(testLL.is_sorted())

  print ('\nsort list test\n')
  print(testLL.sort_list())
  print ('\nis_sorted test\n')
  print(testLL.is_sorted())

  print ('\nis_equal test\n')
  print(testLL.is_equal(empy))

  print ('\ncopy_list test\n')
  x = testLL.copy_list()
  print(x)

  print ('\nreverse_list test\n')
  x = testLL.reverse_list()
  print(x)


  empy.insert_first(23)
  empy.insert_first(234)
  empy.insert_first(3998)
  x = testLL.merge_list(empy)
  print ('\nmerge_list test\n')
  print(x)
  print()


  x.insert_first(9)
  x.insert_first(9)
  x.insert_first(9)
  print(x)
  print()
  print ('\nremove_duplicates test\n')
  x = testLL.remove_duplicates()
  print(x)
  '''

if __name__ == "__main__":
  main()

