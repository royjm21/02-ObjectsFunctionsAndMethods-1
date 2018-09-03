"""
Practice DEFINING and CALLING
     FUNCTIONS

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Jeremy Roy.
"""  # TODOne: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
#
# TODOne: 2.
#   Allow this module to use the  rosegraphics.py  module by marking the
#     src
#   folder in this project as a "Sources Root", as follows:
#
#     In the Project window (to the left), right click on the src  folder,
#     then select  Mark Directory As  ~  Sources Root.
#
###############################################################################

import rosegraphics as rg
import math


def main():
    """
    TESTS the functions that you will write below.
    You write the tests per the _TODO_s below.
    """
    print(triangle(3, 4))
    print(theta_xi('silver', 10))

###############################################################################
#
# TODOne: 3a.  Define a function immediately blow this _TODO_.
#   It takes two arguments that denote, for a right triangle,
#   the lengths of the two sides adjacent to its right angle,
#   and it returns the length of the hypotenuse of that triangle.
#     HINT: Apply the Pythagorean theorem.
#
#   You may name the function and its parameters whatever you wish.


def triangle(a, b):
    return math.sqrt((a**2)+(b**2))

# TODOne: 3b.  In main, CALL your function and print the returned value,
#   to test whether you defined the function correctly.
#
###############################################################################


###############################################################################
#
# TODOne: 4a.  Define a function immediately below this _TODO_.
#   It takes two arguments:
#     -- a string that represents a color (e.g. 'red')
#     -- a positive integer that represents the thickness of a Pen.
#
#   The function:
#     -- Constructs a TurtleWindow.
#     -- Constructs two SimpleTurtles, where:
#        - one has a Pen whose color is "green" and has the GIVEN thickness
#        - the other has a Pen whose color is the GIVEN color
#            and whose thickness is 5
#     -- Makes the first (green) SimpleTurtle move FORWARD 100 pixels, and
#        makes the other SimpleTurtle move BACKWARD 100 pixels.
#
#   You may name the function and its parameters whatever you wish.
def theta_xi(color, thickness):
    window = rg.TurtleWindow()
    window.delay(20)
    hal = rg.SimpleTurtle()
    hal.pen = rg.Pen('green', thickness)
    paul = rg.SimpleTurtle()
    paul.pen = rg.Pen(color, 5)
    hal.forward(100)
    paul.backward(100)
    window.close_on_mouse_click()
# TODOne: 4b.  In main, CALL your function and print the returned value,
#   to test whether you defined the function correctly.
#
###############################################################################


###############################################################################
#
# TODOne: 5.
#   COMMIT-and-PUSH your work (after changing this TO-DO to DONE).
#
#   As a reminder, here is how you should do so:
#     1. Select   VCS   from the menu bar (above).
#     2. Choose  Commit  from the pull-down menu that appears.
#     3. In the  Commit Changes  window that pops up:
#          - HOVER over the  Commit  button
#              (in the lower-right corner of the window)
#          - CLICK on  Commit and Push.
#          - Select  Push  when asked.
#
#   COMMIT adds the changed work to the version control on your computer
#   and PUSH adds the changed work into your Github repository in the "cloud".
#
#    COMMIT-and-PUSH your work as often as you want, but at least for each
#    module after you have tested the module and believe that it is correct.
#
###############################################################################

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
