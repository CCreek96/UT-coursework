#  File: Train.py

#  Description: Drawing a train using turtle graphics package

import turtle, math 

def draw_line (ttl, x1, y1, x2, y2):
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

def draw_rect (ttl, x, y, x_side_len, y_side_len):
  ttl.penup()
  ttl.goto (x, y)
  ttl.pendown()
  for i in range (2):
    ttl.forward (x_side_len)
    ttl.left (90)
    for j in range (1):
    	ttl.forward(y_side_len)
    ttl.left (90)


def draw_wheels(ttl, x, y, larger_r, smaller_r, num):
	
	change_size = 0
	
	for i in range (num):
		if (change_size == 1):
			larger_r -= 10
		inc = turtle.Turtle()
		inc.speed(0)
		inc.penup()
		inc.goto(x, y + larger_r - smaller_r)

		inc.color('red')
		ttl.color('red')
		
		ttl.penup()
		ttl.setheading(0)
		
		ttl.goto(x, y)
		ttl.pendown()
		ttl.circle(larger_r)
		ttl.penup()

		spoke_angle = 5
		for r in range(2):
			for q in range(9):
				inc.goto(x, y + larger_r - smaller_r)
				inc.pendown()
				inc.circle(smaller_r, q * 45)
				ttl.goto(x, y + smaller_r)
				ttl.pendown()
				ttl.circle(larger_r - smaller_r, spoke_angle)
				ttl.goto(inc.position())
				inc.penup()
				ttl.penup()
				spoke_angle += 45
				inc.setheading(0)
				ttl.setheading(0)
			spoke_angle = -5
		x += 250
		change_size += 1
		ttl.ht()
		inc.ht()

def main ():

	turtle.title ("I Like Trains")
	turtle.setup (800, 800, 0, 0)

	ttl = turtle.Turtle()
	ttl.pensize(2.3)
	ttl.speed(60)

	# Draw three wheels
	ttl.color("red")
	draw_wheels(ttl, -275, -200, 60, 9, 3)

	# Draw train tracks
	ttl.color("black")
	draw_line (ttl, -400, -200, 400, -200)
	draw_line (ttl, -400, -210, 400, -210)
	x_coord = -370
	for i in range (13):
		draw_rect(ttl, x_coord, -214, 20, 4)
		x_coord += 60

	# Draw cabin
	ttl.color("blue")
	draw_line(ttl, -370, 180, -370, -130)
	ttl.left(90)
	draw_line(ttl, -370, -130, -345, -130)
	ttl.setpos(-205, -130)
	ttl.pd()
	ttl.circle(70, 180)
	draw_line(ttl, -205, -130, -170, -130)
	ttl.left(90)
	draw_line(ttl, -170, -130, -170, 180)
	ttl.left(90)
	draw_rect (ttl, -350, 160, -100, -65)
	draw_rect (ttl, -260, 160, -100, -65)
	ttl.color ("grey")
	ttl.begin_fill()
	draw_rect (ttl, -350, 160, -100, -65)
	draw_rect (ttl, -260, 160, -100, -65)
	ttl.end_fill()
	ttl.color("blue")
	draw_rect (ttl, -350, 160, -100, -65)
	draw_rect (ttl, -260, 160, -100, -65)

	# Draw the top of cabin
	draw_line(ttl, -170, 180, -390, 180)
	ttl.left(270)
	draw_line (ttl, -390, 180, -390, 190)
	ttl.left(270)
	draw_line (ttl, -390, 190, -150, 190)
	ttl.left(270)
	draw_line (ttl, -150, 190, -150, 180)
	ttl.left(270)
	draw_line (ttl, -150, 180, -170, 180)

	# Draw engine
	ttl.left(90)
	draw_line (ttl, -170, 180, -170, 110)
	ttl.left(90)
	draw_line (ttl, -170, 110, 320, 110)
	draw_rect (ttl, 50, 110, -30, -80)
	draw_rect (ttl, 35, 140, -20, -50)
	draw_line (ttl, 160, 110, 140, 170)
	draw_line (ttl, 140, 170, 200, 170) #
	draw_line (ttl, 140, 170, 150, 195)
	draw_line (ttl, 150, 195, 190, 195)
	draw_line (ttl, 190, 195, 200, 170)
	draw_line (ttl, 200, 170, 185, 110)
	ttl.left(270)
	draw_line (ttl, 320, 110, 320, -130)
	ttl.left(270)
	draw_line (ttl, 320, -130, 285, -130)
	ttl.setpos(285, -130)
	ttl.pd()
	ttl.circle(60, 180)
	draw_line (ttl, 165, -130, 35, -130)
	ttl.setpos(-85, -130)
	ttl.pd()
	ttl.circle(60, -180)
	draw_line (ttl, -85, -130, -170, -130)
	draw_rect (ttl, -40, 110, -80, 15)
	draw_rect (ttl, 180, 110, -80, 15)
	draw_rect (ttl, -170, 30, -15, -490)

	# Draw dots along the lines
	# Horizontal
	x_pos = -163
	for i in range (29):
		ttl.pu()
		ttl.goto(x_pos, 22)
		ttl.dot(10, "black")
		x_pos += 17
	# Left vertical
	y_pos = 103
	for i in range (5):
		ttl.pu()
		ttl.goto(-48, y_pos)
		ttl.dot(10, "black")
		y_pos -= 16
	# Right vertical
	y_pos = 103
	for i in range (5):
		ttl.pu()
		ttl.goto(172, y_pos)
		ttl.dot(10, "black")
		y_pos -= 16

	# Draw front pieces
	draw_rect (ttl, 320, 80, -140, -20)
	draw_rect (ttl, 340, 60, -100, -15)
	draw_line (ttl, 320, -100, 355, -100)
	draw_line (ttl, 355, -100, 380, -160)
	draw_line (ttl, 380, -160, 320, -160)
	draw_line (ttl, 320, -160, 320, -100)

	turtle.done ()

main ()
