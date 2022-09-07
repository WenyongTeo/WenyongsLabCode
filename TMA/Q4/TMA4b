def readSeatingPlan(filename): #get the file name, put it into a dictionary
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

def showSeatingPlan(seatingPlan): #get the dictionary, put A as key seats as value. List in dict method
   for k,v in seatingPlan.items():
       for seats in v:
           x = '   '.join(v)
       print(k, x)
   for i in range(1,len(v)+1):
       print(end=' ')
       print(f'{i:02d}', end=' ')
   return seatingPlan

def menuOption(): #formatting the menu
    count = 1
    print("Main Menu - FR Productions")
    print('==========================')
    with open('FR_Productions.txt', 'r') as file: #open production file
        for data in file:
            (movieName, movieDate) = data.rstrip('\n,.txt').split('-') #strp the \n and .txt after the '-'
            movieDay = movieDate[6:8] #get DD
            movieMonth = movieDate[4:6] #get MM
            movieYear = movieDate[0:4] #get YY
            movieHour = movieDate[8:10] #get HH
            movieMinute = movieDate[10:12] #get MM
            print(f'{count}. {movieName} @ {movieYear}-{movieMonth}-{movieDay} {movieHour}:{movieMinute}') #format it
            count += 1
    print("X. Exit")
    option = input("Enter Selection: ")
    return option #return my input

def subMenuBc0809(seatingPlan):
    while True:
        showSeatingPlan(seatingPlan)
        print('\nSub-Menu\n=====\n1. Book seats\n2. Cancel Bookings\nX. Back to Main Menu')
        subOption = input('Enter option_: ') #choose 1234 or Xx
        if subOption == '1':
            selectedSeats = []
            bookInput = input('Enter seats to book: ').upper()  #input A1,B1
            selectedSeats = bookInput.split(',')                #input becomes [A1,B1]
            abortSelection = False                              #checker
            for booking in selectedSeats:
                bookRow = booking[0]              #key A,B,C,D...
                bookColumn = int(booking[1:])-1   #Value, 1,2,3...17
                availableSeats = (seatingPlan[booking[0]][bookColumn])
                if availableSeats == "X":         #check if its X
                    print(f'Exception! {booking} has been booked!')
                    abortSelection = True         #go next
                    print('Booking aborted')
                elif availableSeats == '#':       #check if its #
                    print(f'{booking} is blocked!')
                    abortSelection = True         #go next

            for booking in selectedSeats:
                if abortSelection is False:       #after both above are checked and are True, will come here
                    bookRow = booking[0]              #ABCD
                    bookColumn = int(booking[1:]) - 1 #1...17
                    availableSeats = (seatingPlan[booking[0]][bookColumn]) #A1...
                    if availableSeats == 'O': #if its O
                        seatingPlan[bookRow][bookColumn] = 'X' #change it to X
                        print(f'{booking} has been booked Successfuly!\n')
                        with open('Bad Citizen-202209081930.txt', 'w') as f:
                            for rowCode in sorted(seatingPlan.keys()):
                                f.write(rowCode + ',' + ''.join(seatingPlan[rowCode]) + '\n')

        elif subOption == '2':
            selectedSeats = []
            bookInput = input('Enter seats to cancel: ').upper()
            selectedSeats = bookInput.split(',')
            abortSelection = False
            for booking in selectedSeats:
                bookRow = booking[0]
                bookColumn = int(booking[1:]) - 1
                availableSeats = (seatingPlan[booking[0]][bookColumn])
                if availableSeats == "O": #will abort if not booked
                    print(f'Exception! {booking} is not booked!')
                    abortSelection = True
                    print('Canceling aborted')
                elif availableSeats == '#':
                    print(f'{booking} is blocked!')
                    abortSelection = True

            for booking in selectedSeats:
                if abortSelection is False:
                    bookRow = booking[0]
                    bookColumn = int(booking[1:]) - 1
                    availableSeats = (seatingPlan[booking[0]][bookColumn])
                    if availableSeats == 'X': #if X
                        seatingPlan[bookRow][bookColumn] = 'O' #change it to O
                        print(f'{booking} has been cancelled Successfuly!\n')
                        with open('Bad Citizen-202209081930.txt', 'w') as f:
                            for rowCode in sorted(seatingPlan.keys()):
                                f.write(rowCode + ',' + ''.join(seatingPlan[rowCode]) + '\n')
        elif subOption in 'xX':
            return False

def subMenuBc0909(seatingPlan):
    while True:
        showSeatingPlan(seatingPlan)
        print('\nSub-Menu\n=====\n1. Book seats\n2. Cancel Bookings\nX. Back to Main Menu')
        subOption = input('Enter option_: ')
        if subOption == '1':
            selectedSeats = []
            bookInput = input('Enter seats to book: ').upper()
            selectedSeats = bookInput.split(',')
            abortSelection = False
            for booking in selectedSeats:
                bookRow = booking[0]
                bookColumn = int(booking[1:]) - 1
                availableSeats = (seatingPlan[booking[0]][bookColumn])
                if availableSeats == "X":
                    print(f'Exception! {booking} has been booked!')
                    abortSelection = True
                    print('Booking aborted')
                elif availableSeats == '#':
                    print(f'{booking} is blocked!')
                    abortSelection = True

            for booking in selectedSeats:
                if abortSelection is False:
                    bookRow = booking[0]
                    bookColumn = int(booking[1:]) - 1
                    availableSeats = (seatingPlan[booking[0]][bookColumn])
                    if availableSeats == 'O':
                        seatingPlan[bookRow][bookColumn] = 'X'
                        print(f'{booking} has been booked Successfuly!\n')
                        with open('Bad Citizen-202209091930.txt', 'w') as f:
                            for rowCode in sorted(seatingPlan.keys()):
                                f.write(rowCode + ',' + ''.join(seatingPlan[rowCode]) + '\n')

        elif subOption == '2':
            selectedSeats = []
            bookInput = input('Enter seats to Cancel: ').upper()
            selectedSeats = bookInput.split(',')
            abortSelection = False
            for booking in selectedSeats:
                bookRow = booking[0]
                bookColumn = int(booking[1:]) - 1
                availableSeats = (seatingPlan[booking[0]][bookColumn])
                if availableSeats == "O":
                    print(f'Exception! {booking} is not booked!')
                    abortSelection = True
                    print('Cancelling aborted')
                elif availableSeats == '#':
                    print(f'{booking} is blocked!')
                    abortSelection = True

            for booking in selectedSeats:
                if abortSelection is False:
                    bookRow = booking[0]
                    bookColumn = int(booking[1:]) - 1
                    availableSeats = (seatingPlan[booking[0]][bookColumn])
                    if availableSeats == 'X':
                        seatingPlan[bookRow][bookColumn] = 'O'
                        print(f'{booking} has been cancelled Successfuly!\n')
                        with open('Bad Citizen-202209091930.txt', 'w') as f:
                            for rowCode in sorted(seatingPlan.keys()):
                                f.write(rowCode + ',' + ''.join(seatingPlan[rowCode]) + '\n')
        elif subOption in 'xX':
            return False

def subMenuMge0809(seatingPlan):
    while True:
        showSeatingPlan(seatingPlan)
        print('\nSub-Menu\n=====\n1. Book seats\n2. Cancel Bookings\nX. Back to Main Menu')
        subOption = input('Enter option_: ')
        if subOption == '1':
            selectedSeats = []
            bookInput = input('Enter seats to book: ').upper()
            selectedSeats = bookInput.split(',')
            abortSelection = False
            for booking in selectedSeats:
                bookRow = booking[0]
                bookColumn = int(booking[1:]) - 1
                availableSeats = (seatingPlan[booking[0]][bookColumn])
                if availableSeats == "X":
                    print(f'Exception! {booking} has been booked!')
                    abortSelection = True
                    print('Booking aborted')
                elif availableSeats == '#':
                    print(f'{booking} is blocked!')
                    abortSelection = True

            for booking in selectedSeats:
                if abortSelection is False:
                    bookRow = booking[0]
                    bookColumn = int(booking[1:]) - 1
                    availableSeats = (seatingPlan[booking[0]][bookColumn])
                    if availableSeats == 'O':
                        seatingPlan[bookRow][bookColumn] = 'X'
                        print(f'{booking} has been booked Successfuly!\n')
                        with open('Monkey Goes East-202209081430.txt', 'w') as f:
                            for rowCode in sorted(seatingPlan.keys()):
                                f.write(rowCode + ',' + ''.join(seatingPlan[rowCode]) + '\n')

        elif subOption == '2':
            selectedSeats = []
            bookInput = input('Enter seats to Cancel: ').upper()
            selectedSeats = bookInput.split(',')
            abortSelection = False
            for booking in selectedSeats:
                bookRow = booking[0]
                bookColumn = int(booking[1:]) - 1
                availableSeats = (seatingPlan[booking[0]][bookColumn])
                if availableSeats == "O":
                    print(f'Exception! {booking} is not booked!')
                    abortSelection = True
                    print('Cancelling aborted')
                elif availableSeats == '#':
                    print(f'{booking} is blocked!')
                    abortSelection = True

            for booking in selectedSeats:
                if abortSelection is False:
                    bookRow = booking[0]
                    bookColumn = int(booking[1:]) - 1
                    availableSeats = (seatingPlan[booking[0]][bookColumn])
                    if availableSeats == 'X':
                        seatingPlan[bookRow][bookColumn] = 'O'
                        print(f'{booking} has been cancelled Successfuly!\n')
                        with open('Monkey Goes East-202209081430.txt', 'w') as f:
                            for rowCode in sorted(seatingPlan.keys()):
                                f.write(rowCode + ',' + ''.join(seatingPlan[rowCode]) + '\n')
        elif subOption in 'xX':
            return False

def subMenuMge0909(seatingPlan):
    while True:
        showSeatingPlan(seatingPlan)
        print('\nSub-Menu\n=====\n1. Book seats\n2. Cancel Bookings\nX. Back to Main Menu')
        subOption = input('Enter option_: ')
        if subOption == '1':
            selectedSeats = []
            bookInput = input('Enter seats to book: ').upper()
            selectedSeats = bookInput.split(',')
            abortSelection = False
            for booking in selectedSeats:
                bookRow = booking[0]
                bookColumn = int(booking[1:]) - 1
                availableSeats = (seatingPlan[booking[0]][bookColumn])
                if availableSeats == "X":
                    print(f'Exception! {booking} has been booked!')
                    abortSelection = True
                    print('Booking aborted')
                elif availableSeats == '#':
                    print(f'{booking} is blocked!')
                    abortSelection = True

            for booking in selectedSeats:
                if abortSelection is False:
                    bookRow = booking[0]
                    bookColumn = int(booking[1:]) - 1
                    availableSeats = (seatingPlan[booking[0]][bookColumn])
                    if availableSeats == 'O':
                        seatingPlan[bookRow][bookColumn] = 'X'
                        print(f'{booking} has been booked Successfuly!\n')
                        with open('Monkey Goes East-202209091430.txt', 'w') as f:
                            for rowCode in sorted(seatingPlan.keys()):
                                f.write(rowCode + ',' + ''.join(seatingPlan[rowCode]) + '\n')

        elif subOption == '2':
            selectedSeats = []
            bookInput = input('Enter seats to Cancel: ').upper()
            selectedSeats = bookInput.split(',')
            abortSelection = False
            for booking in selectedSeats:
                bookRow = booking[0]
                bookColumn = int(booking[1:]) - 1
                availableSeats = (seatingPlan[booking[0]][bookColumn])
                if availableSeats == "O":
                    print(f'Exception! {booking} is not booked!')
                    abortSelection = True
                    print('Cancelling aborted')
                elif availableSeats == '#':
                    print(f'{booking} is blocked!')
                    abortSelection = True

            for booking in selectedSeats:
                if abortSelection is False:
                    bookRow = booking[0]
                    bookColumn = int(booking[1:]) - 1
                    availableSeats = (seatingPlan[booking[0]][bookColumn])
                    if availableSeats == 'X':
                        seatingPlan[bookRow][bookColumn] = 'O'
                        print(f'{booking} has been cancelled Successfuly!\n')
                        with open('Monkey Goes East-202209091430.txt', 'w') as f:
                            for rowCode in sorted(seatingPlan.keys()):
                                f.write(rowCode + ',' + ''.join(seatingPlan[rowCode]) + '\n')
        elif subOption in 'xX':
            return False

def tma4b(): #traffic controller
    while True:
        option = menuOption()
        if option == '1':
            filename = 'Bad Citizen-202209081930.txt'
            print('Production: Bad Citizen\nPerformance datetime: 2022-09-08 19:30\nSeating plan:')
            seatingPlan = readSeatingPlan(filename)
            subMenuBc0809(seatingPlan)

        elif option == '2':
            filename = 'Bad Citizen-202209091930.txt'
            print('Production: Bad Citizen\nPerformance datetime: 2022-09-09 19:30\nSeating plan:')
            seatingPlan = readSeatingPlan(filename)
            subMenuBc0909(seatingPlan)

        elif option == '3':
            filename = 'Monkey Goes East-202209081430.txt'
            print('Production: Monkey Goes East\nPerformance datetime: 2022-09-08 14:30\nSeating plan:')
            seatingPlan = readSeatingPlan(filename)
            subMenuMge0809(seatingPlan)

        elif option == '4':
            filename = 'Monkey Goes East-202209091430.txt'
            print('Production: Monkey Goes East\nPerformance datetime: 2022-09-09 14:30\nSeating plan:')
            seatingPlan = readSeatingPlan(filename)
            subMenuMge0909(seatingPlan)
        elif option in 'xX':
            break

tma4b()