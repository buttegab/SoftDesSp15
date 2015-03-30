from swampy.TurtleWorld import *

def draw_line(turtle, start_x,start_y, angle, line_length):
	""" draws a line in turtle world
		turtle: the turtle that will draw the line
		start_x: starting x coordinate in pixels for the line
		start_y: starting y ccoordinate in pixels for the lineangle" orientation of the line in degrees
		line_length: how long the line is
	"""
	turtle.x = start_x
	turtle.y = start_y
	turtle.heading = angle
	turtle.fd(line_length)
	turtle.lt(90)
	turtle.fd(line_length)
	turtle.lt(90)
	turtle.fd(line_length)
	turtle.lt(90)
	turtle.fd(line_length)
	turtle.lt(90)


def draw_polygon(turtle, start_x, start_y, sides, line_length):
	turtle.x = start_x
	turtle.y = start_y
	turtle.heading = 0
	turtle.fd(line_length)
	for i in range(1,sides):
		turtle.lt(120)
		turtle.fd(line_length)
	


world = TurtleWorld()
beth = Turtle()
beth.set_pen_color = 'red'
draw_polygon(beth, -100, -100, 5, 100)
wait_for_user()