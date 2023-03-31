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