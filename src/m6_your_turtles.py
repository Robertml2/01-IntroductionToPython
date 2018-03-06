"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Madison Robertson.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg
window = rg.TurtleWindow()


rg.SimpleTurtle()

river = rg.SimpleTurtle()
rosie = rg.SimpleTurtle()
scum = rg.SimpleTurtle()
river.pen = rg.Pen('blue', 10)
rosie.pen = rg.Pen('red', 9)
scum.pen = rg.Pen('black', 8)
river.speed = 100000
scum.speed = 1000000
rosie.speed = 1000000

size = 50
for k in range(25):
    river.draw_regular_polygon(12, 50)
    rosie.draw_regular_polygon(12, 40)
    scum.draw_regular_polygon(11, 30)

    scum.pen_up()
    scum.right(90)
    scum.forward(40)
    scum.pen_down()

    scum.forward(40)
    scum.right(95)
    scum.forward(20)
    scum.left(43)
    scum.forward(25)

    river.pen_up()
    river.forward(25)
    river.pen_down()

    river.forward(40)
    river.right(30)
    river.forward(20)
    river.right(40)
    river.forward(60)

    rosie.right(100)
    rosie.forward(38)
    rosie.left(45)
    rosie.forward(20)

window.close_on_mouse_click()
