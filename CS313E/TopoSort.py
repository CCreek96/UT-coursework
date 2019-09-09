#  File: TopoSort.py

#  Description: Graph

#  Student Name: Brett Beese

#  Student UT EID: bgb727

#  Partner Name: Connor Creek

#  Partner UT EID: cac7376

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 4/28/18

#  Date Last Modified: 4/28/18

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Deque (object):
  def __init__ (self):
    self.deque = []

  def append (self, item):
    self.deque.append (item)

  def appendLeft (self, item):
    self.deque.insert (item, 0)

  def popLeft (self):
    return (self.deque.pop(0))

  def pop (self):
    return (self.deque.pop())

  # check what item is on top of the deque without removing it
  def peekRight (self):
    return self.dequeue[len(self.dequeue) - 1]

  # check what item is on bottom of the deque without removing it
  def peekLeft (self):
    return self.dequeue[0]

  def isEmpty (self):
    return (len (self.deque) == 0)

  def size (self):
    return len (self.deque)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def wasVisited (self):
    return self.visited

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex already exists in the graph
  def hasVertex (self, label):
    allVert = len (self.Vertices)
    for i in range (allVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # given a label get the index of a vertex
  def getIndex (self, label):
    allVert = len (self.Vertices)
    for i in range (allVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
    for i in range(len(self.Vertices)):
      if self.Vertices[i].label == fromVertexLabel:
        fromID = i
        break

    for j in range(len(self.Vertices)):
      if self.Vertices[j].label == toVertexLabel:
        toID = j
        break

    if self.adjMat[fromID][toID] > 0:
      return self.adjMat[fromID][toID]

    else:
      return -1

  # Reset visited flag in the vertices class
  def unvisit_all(self):
    num_vert = len (self.Vertices)
    for i in range (num_vert):
      (self.Vertices[i]).visited = False

  # get a list of immediate neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, vertexLabel):
    neighbors = []
    vtex = -1
    for i in range(len(self.Vertices)):
      if (self.Vertices[i].label == vertexLabel):
        vtex = i
        break

    if (vtex == -1):
      return neighbors

    for j in range(len(self.Vertices)):
      if (self.adjMat[vtex][j] != 0):
        neighbors.append(j)

    return neighbors

  # get a copy of the list of vertices
  def getVertices (self):
    vertList = []
    for i in range (len(self.Vertices)):
      vertList.append(self.Vertices[i].label)

    return vertList

  # delete an edge from the adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel):
    start = self.getIndex(fromVertexLabel)
    finish = self.getIndex(toVertexLabel)
    self.adjMat[start][finish] = 0
    self.adjMat[finish][start]= 0


  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def deleteVertex (self, vertexLabel):
    vIdx = self.getIndex(vertexLabel)
    num_vert = len(self.Vertices)

    # Delete the column
    for i in range(num_vert):
      for j in range(vIdx, num_vert - 1):
        self.adjMat[i][j] = self.adjMat[i][j + 1]
      self.adjMat[i].pop()

    # Delete the row
    self.adjMat.pop(vIdx)

    for vertex in self.Vertices:
      if vertex.label == vertexLabel:
        self.Vertices.remove(vertex)

  # add a Vertex with a given label to the graph
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex(label))

      # add a new column in the adjacency matrix for the new Vertex
      num_vert = len(self.Vertices)
      for i in range (num_vert - 1):
        (self.adjMat[i]).append (0)

      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (num_vert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v
  def getAdjUnvisitedVertex (self, v):
    num_vert = len (self.Vertices)
    for i in range (num_vert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # do the depth first search in a graph
  def dfs (self, v):
    dfs_list = []
    # create a Stack
    theStack = Stack()

    # mark vertex v as visited and push on the stack
    (self.Vertices[v]).visited = True
    dfs_list.append(self.Vertices[v].label)
    theStack.push (v)

    # vist other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        dfs_list.append(self.Vertices[u].label)
        theStack.push(u)
    # the stack is empty let us reset the flags
    self.unvisit_all()
    return dfs_list

  # do breadth first search in a graph
  def bfs (self, v):
    bfs_list = []
    # create a Queue
    theQueue = Queue ()

    (self.Vertices[v]).visited = True
    bfs_list.append(self.Vertices[v].label)
    theQueue.enqueue(v)

    while (not theQueue.isEmpty()):
      v1 = theQueue.dequeue()
      v2 = self.getAdjUnvisitedVertex(v1)
      while (v2 != -1):
        (self.Vertices[v2]).visited = True
        bfs_list.append(self.Vertices[v2].label)
        theQueue.enqueue(v2)
        v2 = self.getAdjUnvisitedVertex(v1)

    self.unvisit_all()
    return bfs_list

  def linksTo(self, fromVert, toVert):
    if self.adjMat[fromVert][toVert] > 0:
      return self.adjMat[fromVert][toVert]
    else:
      return -1


  # determine if a directed graph has a cycle
  def hasCycle (self):
    theStack = Stack()

    # Check each vertex to see if it has a cycle
    for i in range(len(self.Vertices)):
        self.Vertices[i].visited = True
        theStack.push(i)
        # Once empty, all vertices have been visited
        while (not theStack.isEmpty()):
          # Check if current shares edge with starting vertex
          if (self.linksTo(theStack.peek(), i) != -1):
             return True
          # get an adjacent unvisited vertex
          u = self.getAdjUnvisitedVertex (theStack.peek())
          if (u == -1):
            u = theStack.pop()
          else:
            (self.Vertices[u]).visited = True
            theStack.push(u)

        # reset the flags and check next vertex
        self.unvisit_all()
    return False
    
  def noUnvistedPredecessor (self, v):
    nVert = len(self.Vertices)
    for i in range(nVert):
      if (self.adjMat[i][v] != 0) and (not self.Vertices[i].wasVisited()):
        return False
    return True

  # return a list of vertices after a topological sort
  def toposort (self):
    nVert = len(self.Vertices)
    topo_list = []
    theDeque = Deque()            # Double Ended Queue
    # If the graph has a cycle, topo sort not possible
    if self.hasCycle():
        return None
    # Put any vertex with no predecessor into the deque
    for i in range(nVert):
        no_predecessor = True
        for j in range (nVert):
          if (self.adjMat[j][i] != 0):
              no_predecessor = False
              break
        if (no_predecessor):
            self.Vertices[i].visited = True
            topo_list.append(self.Vertices[i].label)
            theDeque.append(i)

    while (not theDeque.isEmpty()):
      v1 = theDeque.pop()
      v2 = self.getAdjUnvisitedVertex(v1)
      # If the vertex has an unvisited predecessor, place
      # it in the front of the deque
      if (not self.noUnvistedPredecessor(v2)):
          theDeque.appendLeft(v1)
      else:
          while (v2 != -1):
            # Check the new vertex
            if (self.noUnvistedPredecessor(v2)):
                (self.Vertices[v2]).visited = True
                topo_list.append(self.Vertices[v2].label)
                theDeque.append(v2)
                v2 = self.getAdjUnvisitedVertex(v1)
            else:
              theDeque.appendLeft(v2)

              break

    self.unvisit_all()
    return topo_list

def main():
  # create a Graph object
  cities = Graph()

  # open file for reading
  with open ("topo.txt", "r") as inFile:

      # read the Vertices
      numVertices = int ((inFile.readline()).strip())
      print (numVertices)

      for i in range (numVertices):
        city = (inFile.readline()).strip()
        print (city)
        cities.addVertex (city)

      # read the edges
      numEdges = int ((inFile.readline()).strip())
      print (numEdges)

      for i in range (numEdges):
        edge = (inFile.readline()).strip()
        print (edge)
        edge = edge.split()
        start = cities.getIndex(edge[0])
        finish = cities.getIndex(edge[1])
        #weight = int (edge[2])

        cities.addDirectedEdge (start, finish)

  # print the adjacency matrix
  print ("\nAdjacency Matrix:\n")
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities.adjMat[i][j], end = ' ')
    print ()
  print ()

#  The commented out code lines are tests from Graph.py
  # read the starting vertex for dfs and bfs
  #startVertex = (inFile.readline()).strip()
  #line = (inFile.readline()).strip().split()
  #city1 = line[0]
  #city2 = line[1]
  #print ('Start Label:', startVertex)

  # get the index of the start Vertex
  #startIndex = cities.getIndex (startVertex)
  #print ('Start Index:', startIndex)

  # Test getIndex
  print ('\nTest getIndex')
  print ('x Index:', cities.getIndex('x'))
  print ('Expected: 11\n')
  print ('o Index:', cities.getIndex('o'))
  print ('Expected: 2\n')

  # test depth first search
#  print('\nTest DFS')
#  print ("Depth First Search from " + startVertex + ':\n')
#  print('\nDFS Lable List\n', cities.dfs (startIndex))
#  print()

  # test breadth first search
#  print('Test BFS')
#  print ("Breadth First Search From " + startVertex + ':\n')
#  print('\nBFS Lable List\n', cities.bfs (startIndex))
#  print()

  # Test getEdgeWeight
  print('Test getEdgeWeight 1')
  print('Edge Weight to o to n:', cities.getEdgeWeight("o","n"))
  print ('Expected Output: -1 (no edge exists)\n')

#  print('Test getEdgeWeight 2')
  print("Edge Weight n to o:", cities.getEdgeWeight("n","o"))
  print ('Expected Output: 1 (edge exists)\n')

  # Test getNeighbors
#  print ('Test getNeighbors')
#  neighbors = cities.getNeighbors("Kansas City")
#  print("Neighbors to Kansas City:", neighbors)
#  neighbor_labels = []
#  for idx in neighbors:
#    neighbor_labels.append(cities.Vertices[idx].label)
#  print ('Neighbor labels:', neighbor_labels)
#  print ('Expected Output: [Los Angeles, Denver, Chicago, New York, Atlanta, Dallas]\n')

  # Test getVertices
  print ('Test getVertices')
  verticesCopy = cities.getVertices()
  print("Vertices:", verticesCopy)
  print ("Expected: ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']\n")

  # test deletion of an edge
#  print("\nTest deleteEdge")
#  print("Delete:", city1, 'to', city2)
#  cities.deleteEdge(city1, city2)
#  print("\nNew Adjacency Matrix:\n")
#  num_vert = len (cities.adjMat)
#  for i in range (num_vert):
#    for j in range (num_vert):
#      print (cities.adjMat[i][j], end = " ")
#    print()
#  print ()

  # test deletion of a vertex
#  print("\nTest deleteVertex")
#  print("Delete:", city1)
#  cities.deleteVertex(city1)
#  print("\nNew List of Cities:\n")
#  for vert in cities.Vertices:
#    print(vert.label)
#  print("\nNew Adjacency Matrix:\n")
#  num_vert = len (cities.adjMat)
#  for i in range (num_vert):
#    for j in range (num_vert):
#      print (cities.adjMat[i][j], end = " ")
#    print()
#  print ()

  # test if a directed graph has a cycle
  print ("Has cycle:", cities.hasCycle())
  print ()

  # test topological sort
  print ("TopoSort:", cities.toposort())


if __name__ == "__main__":
  main()
