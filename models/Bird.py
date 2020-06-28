# Phong Nguyen, Yurock Heo, Bill Tran
# 12/6/2019

from libs.graphics import *
from time import *


class Bird:
    """ This class creates a bird object """

    def __init__(self, x, y, win):

        """ User input the center point where
            the bird image will be imported"""

        self.Bird = Image(Point(x, y), "icon.gif")
        self.leftBottomPt = Point(x, y)
        self.leftTopPt = Point(x, y + 10)
        self.rightBottomPt = Point(x + 10, y)
        self.rightTopPt = Point(x + 10, y + 10)
        self.window = win
        self.Bird.draw(win)

    def fly(self):

        """This method simulates the movement of the bird
        basing on the user's mouseclick. If there is no mouse click, the
        bird moves downward. If there is a mouse click, the bird
        moves upward"""

        click = self.window.checkMouse()
        if not click:
            self.Bird.move(0, -10)
            sleep(0.01)
        else:
            self.Bird.move(0, 10)
            sleep(0.01)
