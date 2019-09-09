#  File: Geom.py

#  Description: Creating and testing class objects for a point on a cartesian plane, a circle, and a rectangle.


import math

class Point (object):
  # constructor 
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  def __str__ (self):
    return '(' + str(self.x) + ", " + str(self.y) + ")"

  # test for equality
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c intersects this circle (non-zero area of overlap)
  def does_intersect (self, c):
    distance = self.center.dist (c.center)
    return (distance < (self.radius + c.radius))

  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  def circle_circumscribes (self, r):
    x = (r.ul.x + r.lr.x) / 2
    y = (r.ul.y + r.lr.y) / 2
    center = Point (x, y)
    radius = center.dist (r.ul)
    new_circle = Circle (round(radius, 2), x, y)
    return new_circle

  # string representation of a circle
  def __str__ (self):
    return "(" + str(self.center.x) + ", " + str(self.center.y) + ")" + ":" + str(self.radius) 

  # test for equality of radius
  def __eq__ (self, other):
    tol = 1.0e-16
    return (abs (self.radius - other.radius) < tol)

class Rectangle (object):
  # constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # determine length of Rectangle (distance along the x axis)
  def length (self):
    return abs(self.ul.x - self.lr.x)

  # determine width of Rectangle (distance along the y axis)
  def width (self):
    return abs(self.ul.y - self.lr.y)

  # determine the perimeter
  def perimeter (self):
    return (2 * (self.length())) + (2 * (self.width()))

  # determine the area
  def area (self):
    return (self.length() * self.width())

  # determine if a point is strictly inside the Rectangle
  def point_inside (self, p):
   return (p.x > float(self.ul.x) and p.x < float(self.lr.x) and p.y < float(self.ul.y) and p.y > float(self.lr.y))
    
  # determine if another Rectangle is strictly inside this Rectangle
  def rectangle_inside (self, r):
    if (self.ul.y < r.lr.y):
      return False
    if (self.ul.x > r.lr.x):
      return False
    if (self.lr.y > r.ul.y):
      return False
    if (self.lr.x < r.ul.x):
      return False
    else: 
      return True

  # determine if two Rectangles overlap (non-zero area of overlap)
  def does_intersect (self, other):
    if float(self.lr.x) < float(other.ul.x) or float(self.ul.y) < float(other.lr.y) or float(self.ul.x) > float(other.lr.x) or float(self.lr.y) > float(other.ul.y):
      return False
    else:
      return True

  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  def rect_circumscribe (self, c):
    ul_x = c.center.x - c.radius
    ul_y = c.center.y + c.radius
    lr_x = c.center.x + c.radius
    lr_y = c.center.y - c.radius

    new_rect = Rectangle (ul_x,ul_y,lr_x,lr_y)
    return new_rect

  # give string representation of a rectangle
  def __str__ (self):
    return "(" + str(self.ul.x) + ", " + str(self.ul.y) + ")" + " : " + "(" + str(self.lr.x) + ", " + str(self.lr.y) + ")"

  # determine if two rectangles have the same length and width
  def __eq__ (self, other):
    tol = 1.0e-16
    return (abs((self.ul.x - self.lr.x) - (other.ul.x - other.lr.x)) < tol and (abs((self.ul.y - self.lr.y) - (other.ul.y - other.lr.y) < tol)))

def main():
  points = []
  # open the file geom.txt
  with open ("./geom.txt","r") as in_file:
    for line in in_file:
      line = line.rstrip().split()
      points.append(line)

    
  # create Point objects P and Q
  pointP = Point (float(points[0][0]),float(points[0][1]))
  pointQ = Point (float(points[1][0]),float(points[1][1]))

  # find the distance between the points P and Q
  print ("Coordinates of P:", pointP)
  print ("Coordinates of Q:", pointQ)
  print ("Distance between P and Q:", round(pointQ.dist(pointP),2))

  # create two Circle objects C and D
  circleC = Circle (float(points[2][2]), float(points[2][0]), float(points[2][1]))
  circleD = Circle (float(points[3][2]), float(points[3][0]), float(points[3][1]))

  # print C and D
  print ("Circle C:", circleC)
  print ("Circle D:", circleD)

  # compute the circumference of C
  print ("Circumference of C:", round(circleC.circumference(), 2))

  # compute the area of D
  print ("Area of D:", round(circleD.area(), 2))

  # determine if P is strictly inside C
  if (circleC.point_inside(pointP)):
    print ("P is inside C")
  else:
    print ("P is not inside C")

  # determine if C is strictly inside D
  if (circleD.circle_inside(circleC)):
    print ("C is inside D")
  else:
    print ("C is not inside D")

  # determine if C and D intersect (non zero area of intersection)
  if (circleC.does_intersect(circleD)):
    print ("C does intersect D")
  else:
    print ("C does not intersect D")

  # determine if C and D are equal (have the same radius)
  if (circleC == circleD):
    print ("C is equal to D")
  else:
    print ("C is not equal to D")

  # create two rectangle objects G and H
  rectangleG = Rectangle (float(points[4][0]),float(points[4][1]), float(points[4][2]),float(points[4][3]))
  rectangleH = Rectangle (float(points[5][0]),float(points[5][1]), float(points[5][2]),float(points[5][3]))

  # print the two rectangles G and H
  print ("Rectangle G:", rectangleG)
  print ("Rectangle H:", rectangleH)

  # determine the length of G (distance along x axis)
  print ("Length of G:", rectangleG.length())

  # determine the width of H (distance along y axis)
  print ("Width of H:", rectangleH.width())

  # determine the perimeter of G
  print ("Perimeter of G:", rectangleG.perimeter())

  # determine the area of H
  print ("Area of H:", rectangleH.area())

  # determine if point P is strictly inside rectangle G
  if (rectangleG.point_inside(pointP)):
    print ("P is inside G")
  else:
    print ("P is not inside G")

  # determine if rectangle G is strictly inside rectangle H
  if (rectangleH.rectangle_inside(rectangleG)):
    print ("G is inside H")
  else:
    print ("G is not inside H")

  # determine if rectangles G and H overlap (non-zero area of overlap)
  if (rectangleG.does_intersect(rectangleH)):
    print ("G does overlap H")
  else:
    print ("G does not overlap H")
  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
  new_circle = circleD.circle_circumscribes(rectangleG)
  print ("Circle that circumscribes G:", new_circle)

  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle
  new_rect = rectangleG.rect_circumscribe(circleD)
  print ("Rectangle that circumscribes D:", new_rect)

  # determine if the two rectangles have the same length and width
  if (rectangleG == rectangleH):
    print ("Rectangle G is equal to H")
  else:
    print ("Rectangle G is not equal to H")

main()
