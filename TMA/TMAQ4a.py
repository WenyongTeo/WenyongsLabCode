#dynamically setup seating arrangements
#allow FR admin to perform
#booking and cancellation of seats.

#Each performance has its own seating plan. write
#use file to store,
#Movie name 'Bad Citizen' performing on 18-oct-2022 19:30
#file name will be bad citizen 202210181930.txt
#“Monkey Goes East”, performing on 8-Sep-2022 14:30
#file name file Monkey Goes East-202209081430.txt

#blocked seats are marked with #
#Booked sits X
#Empty sit O

#Monkey Goes East - 202209081430 - 08-Sept-2022 14:30
'''
A,OXXX#XXXX#XXOO
B,OOXX#XXXX#XXOO
C,OXXX#XXXO#OXXO
D,OOXX#XXXX#XXOO
E,OOOX#OXXO#XXOO
F,##XX#OXXX#XO##
'''

#i) write a function readSeatingPlan(filename)
#parameter is a string representing the file name that sitting plan is stored
#this functions read the file and store the seating plan in a dictionary
#dictionary should look like
#seatingPlan= {
#       'A':['O','X','X','X','#','X','X','X','X','#','X','X','O','O'],
#       'B':['O','O','X','X','#','X','X','X','X','#','X','X','O','O'],
#key is row labels eg A B C etc
#value is list of seat stautus
#seatingPlan[A][0] = O->Empty sit

def readSeatingPlan(filename):
    movieFile = {}
    with open(filename) as f:
        for row in f:
            (key,val)=row.split(',')
            seatingList = []
            for seats in val:
                seatingList.append(seats)
            seatingList = [x.strip("\n") for x in seatingList if not x.isspace() and x != ""]
            movieFile[(key)] = seatingList
    return movieFile
def showSeatingPlan(seatingPlan):
   for k,v in seatingPlan.items():
       for seats in v:
           x = '   '.join(v)
       print(k, x)
   for i in range(1,len(v)+1):
       print(end=' ')
       print(f'{i:02d}', end=' ')

def tma4a():
    filename= 'Monkey Goes East-202209081430.txt'
    seatingPlan = readSeatingPlan(filename)
    showSeats = showSeatingPlan(seatingPlan)

tma4a()
