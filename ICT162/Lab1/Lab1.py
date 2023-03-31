'''#Q1
class Person:
    def __init__(self,gender,name,lastName):
        self._gender = gender
        self._name = name
        self._lastName = lastName

    @property
    def name(self): return self._name

    @property
    def lastName(self): return self._lastName

    @property
    def gender(self): return self._gender

    @name.setter
    def name(self,newName): self._name = newName
    def getFullName(self):
        salute = "Mr"
        if self._gender == "F":
            salute = "Ms"
        return  f'{salute}. {self._lastName} {self._name}'
    def getInitials(self):
        return f'{self._name[0]}. {self._lastName}'

    def __str__(self):
        txt = "Male"
        if self._gender == "F":
            text = "Female"
        return f'Name: {self._name} {self._lastName} Gender: {txt}'

def q1():
    p = Person("M","Joe","Lee")
    print(p)
    p2 = Person("M","Amy","Tan")
    print(p2)

    print(p.getFullName())
    print(p2.getInitials())
q1()

'''
import math

'''class Rectange:
    def __init__(self,length,width):
        self._length = length
        self._width = width

    @property
    def length(self): return self._length
    @property
    def width(self): return self._width
    def __str__(self):
        return f'Length: {self._length:.1f} Width: {self._width:.1f}' +\
            f'Area: {self.getArea():.1f} Perimeter: {self.getPerimeter():.1f}'

    @length.setter
    def length(self, newLength): self._length = newLength
    @width.setter
    def width(self, newWidth): self._width = newWidth
    def getArea(self):
        return self._length * self._width

    def getPerimeter(self):
        return (self._length + self._width)*2

    def increaseSize(self,deltaLen,deltawd):
        self._length+=deltaLen
        self._width+=deltawd
    def isBigger(self,otherRect):
        #Accepts another rect obj, otherRect
        #compares area of this rect with other rect, otherRect
        #returns True if this area is bigger; else returns False
        if self.getArea() >otherRect.getArea():
            return True
        else:
            return False

def q2():
    r = Rectange(2,5)
    print(r)
    r.increaseSize(0.5,0.7)
    print(r)
    r2 = Rectange(2,3)
    print(r2)
    if r.isBigger(r2):
        print('r is bigger')
    else:
        print('r is smaller')
q2()
'''
'''import math
class Point:
        #2 atr x(float) y(float
        #property (getter) for x and y
        #setter for x and y
        #mutator method: move()
        #accessor: distanceTo() and quadrant()
        #__str__
        def __init__(self,x=0,y=0):
                self._x = x
                self._y = y
        def __str__(self):
                return f"X is: {self._x}, Y is: {self._y}"
        @property
        def x(self): return self._x
        @property
        def y(self): return self._y

        @x.setter
        def x(self,newX): self._x = newX
        @y.setter
        def y(self, newY): self._y = newY

        def move(self,dx,dy): #mutator
                self._x+=dx
                self._y+=dy

        def distanceTo(self,otherPoint):
                #compute and return the dist from this point to otherPoint
                xd= (self._x-otherPoint._x)**2
                yd = (self._y - otherPoint._y)**2
                return math.sqrt(xd+yd)

        def quadrant(self):
                #return the sector(0 to 4) this point is located
                if self._x>0 and self._y>0:
                        d=1
                elif self._x>0 and self._y<0:
                        d=2
                elif self._x <0 and self._y<0:
                        d=3
                elif self._x <0 and self._y>0:
                        d=4
                else:
                        d=0

def q3():
        p = Point(1.5,1.2)
        print(p)
        p2= Point()
        print(p2)
        print(f'Distance between p and p2 is {p.distanceTo(p2):.2f}')
        print(f'p is in quadrant {p.quadrant()}')
        print(f'p2 is in quadrant {p.quadrant()}')
q3()'''

'''class BankAcct:
        def __init__(self,accountid,pin,balance):
                self._accountid = accountid
                self._balance= balance
                self._pin= pin
        def __str__(self):
                return  f'ID:{self._accountid} Balance: ${self._balance:.2f} '
        @property
        def accountid(self): return self._accountid
        @property
        def pin(self): return self._pin
        @property
        def balance(self): return self._balance

        @balance.setter
        def balance(self,newAmt): self._balance = newAmt
        def changePin(self,oldPin,newPin):
                if oldPin==self._pin:
                        self._pin=newPin
                        return True
                else:
                        return False
        def deposit(self,amt):
                self._balance+=amt
        def withdraw(self,amt):
                if amt<=self._balance:
                        self._balance-=amt
                        return True
                else:
                        return False
        def transferTo(self,otherAcct,amt):
                #accetps other bankacct obj, otheracct and an amt to transfer
                #attempt to transfer from this to otherAcct the amt value
                #return True if succ, otherwise return False
                if self.withdraw(amt):
                        otherAcct.deposit(amt)
                        return True
                else:
                        return False
def q4():
        ba = BankAcct("all",123,100)
        print(ba)
        ba2 = BankAcct("b22",456,200)
        print(ba2)
        ba.deposit(11)
        ba2.withdraw(55)
        print(ba)
        print(ba2)
        if ba.transferTo(ba2,22):
                print("Successful Transfer")
        else:
                print("You brokey bitch")
        print(ba)
        print(ba2)
q4()'''

class ToDo:
        #models an event with to do task
        #2 attr, Event(str and Actions(list)
        #property method for event
        #mutator method: addToDo() and removeToDo()
        #__str__
        def __init__(self,event):
                self._event = event
                self._actions = []
        def __str__(self):
                txt = f"Event {self._event}\n"
                for i, a in enumerate(self._actions):
                        txt+=f'{i+1}.{a}\n'
                return txt


        @property
        def event(self): return self._event
        @property
        def actions(self): return self._actions
        @event.setter
        def event(self,newEvent): self._event = newEvent
        def actions(self,newActions): self._actions = newActions

        def addToDo(self,Task):
                self._actions.append(Task)

        def removeToDo(self,index):
                if 1<=index<=len(self._actions):
                        self._actions.pop(index-1)
                        return True
                else:
                        return False

def q5():
        e = ToDo("Traveling")
        print(e)
        e.addToDo("Bring Passport")
        e.addToDo("Bring money")
        e.addToDo("Bring Meds")
        print(e)
q5()