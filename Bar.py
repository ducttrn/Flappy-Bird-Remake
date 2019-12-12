#Phong Nguyen, Yurock Heo, Bill Tran
#12/6/2019
#Final Project COM110

from graphics import *
from time import *

class Bars:
    
    """This class creates a pair of rectangular bars which bases on
        the bottom bar. Users will input the center point of the
        bottom bar, its width, height, and also a constant for the gap between
        the mid points of 2 bars"""
    
    def __init__(self, win,centerPt, width, height,const):

        """ Creates 2 rectangles representing bars"""

        #Locating the coordinates of the bottom bar
        self.xmin = centerPt.getX() - width/2 
        self.xmax = centerPt.getX() + width/2
        self.ymin = centerPt.getY() - height/2
        self.ymax = centerPt.getY() + height/2
        
        p1 = Point(self.xmin, self.ymax)
        p2 = Point(self.xmax, self.ymin)

        p3 = Point(self.xmin, self.ymax + const)
        p4 = Point(self.xmax, self.ymin + const)

        self.line = Line(Point(self.xmin,self.ymax-10),Point(self.xmax-0.5,self.ymax-10))
        self.line1 = Line(Point(self.xmin,self.ymax+50),Point(self.xmax-0.5,self.ymax+50))
        self.rect = Rectangle(p1,p2)
        self.rect_1 = Rectangle(p3,p4)
        self.rect.setFill("green")
        self.rect_1.setFill("green")
        self.rect.draw(win)
        self.rect_1.draw(win)
        self.rect.setWidth(6)
        self.rect_1.setWidth(6)
        self.line.draw(win)
        self.line.setWidth(4)
        self.line1.draw(win)
        self.line1.setWidth(4)
                
    def move(self,x,y):

        """ This method moves the 2 bars simultaneously"""
        
        self.rect.move(x,y)
        self.rect_1.move(x,y)
        self.line.move(x,y)
        self.line1.move(x,y)
        
    def undraw(self):

        """ This method undraws the bars """
        
        self.rect.undraw()
        self.rect_1.undraw()
        self.line.undraw()
        self.line1.undraw()
