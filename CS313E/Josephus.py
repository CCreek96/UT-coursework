#  File: Josephus.py

#  Description: Simulates the Joesphus problem


#  Date Created: 4/1/2018

#  Date Last Modified: 4/2/2018

class Link(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class CircularList(object):
    
    # Constructor
    def __init__(self):
        self.head = None

    # Insert an element (value) into the list
    def insert(self, item):
        new_link = Link (item)
        current = self.head
        new_link.next = self.head

        if (self.head != None):
        	while (current.next != self.head):
        		current = current.next
        	current.next = new_link
        else:
        	new_link.next = new_link
        self.head = new_link

    # Find the link with the given key (value)
    def find (self, key):
      current = self.head

      while (current.data != key):
      	if (current.next == self.first):
      	  return None
      	else:
      	  current = current.next

      return current

    # Delete a link with a given key (value)
    def delete (self, key):
        if self.head == None:
            return None

        current = self.head
        previous = self.head
        
        while previous.next != self.head:
            previous = previous.next

        while current.data != key:
            if current.next == self.head:
                return None
            previous = current
            current = current.next

        if current == self.head:
            if self.head == self.head.next:
                self.head = None
                return current
            else:
                self.head = current.next
                
        previous.next = current.next
        return current

    def delete_after (self, start, n):
        if self.head == None:
            return None
        
        current = self.head
        while (current.data != start):
            current = current.next
            
        count = 1
        
        while (count != n):
            current = current.next
            count += 1
            
        self.delete(current.data)

        return current.next

    def __str__(self):
        if self.head == None:
            return "None"
        else:
            ztring = "["
            current = self.head
            while current.next != self.head:
                ztring += str(current.data) + ","
                current = current.next
            ztring += str(current.data) + "]"
            return ztring

def main():

    with open ("josephus.txt", "r") as file:
        n = int(file.readline().strip())
        start = int(file.readline().strip())
        tick = int(file.readline().strip())

    soldiers = CircularList()

    # populate list with soldiers
    for i in range(start, n + 1):
        soldiers.insert(i)

    # While the last link does not point to itsself
    #### SLiGHTLY BROKEN ####
    while (soldiers.head.next != soldiers.head):
        first = soldiers.delete_after(start, tick)
        first = first.data
        print(first)

    print(soldiers.head.data)

main()

        
