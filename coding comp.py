from graphics import *
import random, time
length = 600
height = 600
class Rec(object):
       """rectangle"""

       def __init__(self,sentX1,sentX2,sentY1,sentY2):
              self.x1 = sentX1
              self.x2 = sentX2
              self.y1 = sentY1
              self.y2 = sentY2
              self.index = len(recClass)

       def check(self,xval,yval):
              global which
              if xval > self.x1 and xval < self.x2:
                     if yval > self.y1 and yval < self.y2:
                            which = self.index
def start():
       global length,height,win
       win = GraphWin("College Planning App",length,height,autoflush = False)
       win.setBackground("blue4")
       txt = Text(Point(length/2,height/10),"Welcome to the College Planning App!")
       click = "click anywhere to continue"
       ex = Text(Point(length/2,height/4),click)
       explain = "This is an app designed for college students to make \n\n your \
stressful lives a little bit easier,\n\n and to make completing your work a little\
 more fun!"
       new = Text(Point(length/2,height/2),explain)
       things = [txt,ex,new]
       for thing in things:  
              if thing != ex:
                     thing.setFill("red")
              else:
                     thing.setStyle("bold")
                     thing.setFill("white")
              thing.setSize(25)
              thing.draw(win)
       mouse = True
       while mouse == True:
              mouse = win.getMouse()
       for thing in things:
              thing.undraw()
def actions():
       global reclist,textlist,recClass
       rlen = 150
       rhei = 60
       y1 = 160
       y2 = 320
       y3 = 480
       x1 = 80
       x2 = 380
       x3 = 230
       textlist = []
       r1 = rlen/2
       r2 = rhei/2

       textlist.append(Text(Point(x1+r1,y1+r2),"Add Item"))
       textlist.append(Text(Point(x2+r1,y1+r2),"Remove Item"))
       textlist.append(Text(Point(x1+r1,y2+r2),"Add Friends"))
       textlist.append(Text(Point(x2+r1,y2+r2),"Remove Friends"))
       textlist.append(Text(Point(x3+r1,y3+r2),"Home Page"))
       for j in textlist:
              j.setFill("black")
              j.setSize(20)

       reclist = []
       reclist.append(Rectangle(Point(x1,y1),Point(x1+rlen,y1+rhei)))
       reclist.append(Rectangle(Point(x2,y1),Point(x2+rlen,y1+rhei)))
       reclist.append(Rectangle(Point(x1,y2),Point(x1+rlen,y2+rhei)))
       reclist.append(Rectangle(Point(x2,y2),Point(x2+rlen,y2+rhei)))
       reclist.append(Rectangle(Point(x3,y3),Point(x3+rlen,y3+rhei)))
       recClass = []
       recClass.append(Rec(x1,x1+rlen,y1,y1+rhei))
       recClass.append(Rec(x2,x2+rlen,y1,y1+rhei))
       recClass.append(Rec(x1,x1+rlen,y2,y2+rhei))
       recClass.append(Rec(x2,x2+rlen,y2,y2+rhei))
       recClass.append(Rec(x3,x3+rlen,y3,y3+rhei))
       for i in range(5):
              reclist[i].setFill("red")
              reclist[i].draw(win)
              textlist[i].draw(win)
def removeact():
       global reclist
       global textlist
       for i in range(5):
              reclist[i].undraw()
              textlist[i].undraw()
def whichclick():
       global recClass,which
       which = None
       while which == None:
              click = win.getMouse()
              xval = click.getX()
              yval = click.getY()
              for rec in recClass:
                     rec.check(xval,yval)
              print(which)
              #gives the index of the square that was clicked
start()
update()
actions()
whichclick()
mouse = True
while mouse == True:
       mouse = win.getMouse()
removeact()
