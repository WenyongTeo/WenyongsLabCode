import random
class Dice:
    '''models are real-world dice
    it has one attribute face value (int)
    it has methods: roll(), getValue()
    it has __str__()'''

    #constructor; needed to create objects
    def __init__(self): #must need this
        self._value = 1
    #accessor method and mutator methods
    #accessor method - returns an attribute value
    #mutator method - updates attribute value


    @property #special accesor method calls property method
    def value(self): return self._value

    def roll(self):
        #updates the top face value of the dice obj
        self._value = random.randint(1,6)

    def __str__(self): #and this
        '''This method returns a string representation of the objects attributes
        '''

        return f'Face value is {self._value}'

def demo():
    d= Dice() #class the constructor in Dice; __init__(self)
    print(d) #calls the __str__(self) and prints it
    print("d1: ", d.value) #calss the property method value(self)
    d.roll()
    print(d.value)
    d2 = Dice()
    print("d2: ",d2)

class Cashcard:
    '''Models a cash card
    it has:
    2 attribute: id(str) and balance(float)
    property methods for id and balance
    setter method for id
    mutator methods: deduct() and topUp()
    __str__()'''

    #constructor
    def __init__(self,id,amt):
        self._id = id
        self._amt = amt

    @property
    def id(self): return self._id
    @property
    def balance(self): return self._amt
    @id.setter #setter method is special mutator method
    def id(self,newId): self._id = newId

    def __str__(self):
        return f'ID: {self._id} Balance: ${self._amt:.2f}'

    def deduct(self,amt):
        '''attempts to deduct amt from balance'''
        if amt<=self._amt:
            self._amt -= amt
    def topUp(self,amt):
        self._amt += amt

def cc():
    c= Cashcard("b11 ",100)
    print(c)
    print(f'Balance is ${c.balance:.2f}')
    c.id= 'z01' #calls setter method
    print(c)

    c.topUp(11)
    print(c)
    c.deduct(45)
    print(c)
cc()