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
   return seatingPlan

def menuOption():
    count = 1
    print("Main Menu - FR Productions")
    print('==========================')
    with open('FR_Productions.txt', 'r') as file:
        for data in file:
            (movieName, movieDate) = data.rstrip('\n,.txt').split('-')
            movieDay = movieDate[6:8]
            movieMonth = movieDate[4:6]
            movieYear = movieDate[0:4]
            movieHour = movieDate[8:10]
            movieMinute = movieDate[10:12]
            print(f'{count}. {movieName} @ {movieYear}-{movieMonth}-{movieDay} {movieHour}:{movieMinute}')
            count += 1
    print("X. Exit")
    option = input("Enter Selection: ")
    return option

def subMenuBc0809(seatingPlan):
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
                bookColumn = int(booking[1:])-1
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
                        with open('Bad Citizen-202209081930.txt', 'w') as f:
                            for rowCode in sorted(seatingPlan.keys()):
                                f.write(rowCode + ',' + ''.join(seatingPlan[rowCode]) + '\n')

        elif subOption == '2':
            selectedSeats = []
            bookInput = input('Enter seats to book: ').upper()
            selectedSeats = bookInput.split(',')
            abortSelection = False
            for booking in selectedSeats:
                bookRow = booking[0]
                bookColumn = int(booking[1:]) - 1
                availableSeats = (seatingPlan[booking[0]][bookColumn])
                if availableSeats == "O":
                    print(f'Exception! {booking} is not booked!')
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
                    if availableSeats == 'X':
                        seatingPlan[bookRow][bookColumn] = 'O'
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
            bookInput = input('Enter seats to book: ').upper()
            selectedSeats = bookInput.split(',')
            abortSelection = False
            for booking in selectedSeats:
                bookRow = booking[0]
                bookColumn = int(booking[1:]) - 1
                availableSeats = (seatingPlan[booking[0]][bookColumn])
                if availableSeats == "O":
                    print(f'Exception! {booking} is not booked!')
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
            bookInput = input('Enter seats to book: ').upper()
            selectedSeats = bookInput.split(',')
            abortSelection = False
            for booking in selectedSeats:
                bookRow = booking[0]
                bookColumn = int(booking[1:]) - 1
                availableSeats = (seatingPlan[booking[0]][bookColumn])
                if availableSeats == "O":
                    print(f'Exception! {booking} is not booked!')
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
            bookInput = input('Enter seats to book: ').upper()
            selectedSeats = bookInput.split(',')
            abortSelection = False
            for booking in selectedSeats:
                bookRow = booking[0]
                bookColumn = int(booking[1:]) - 1
                availableSeats = (seatingPlan[booking[0]][bookColumn])
                if availableSeats == "O":
                    print(f'Exception! {booking} is not booked!')
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
                    if availableSeats == 'X':
                        seatingPlan[bookRow][bookColumn] = 'O'
                        print(f'{booking} has been cancelled Successfuly!\n')
                        with open('Monkey Goes East-202209091430.txt', 'w') as f:
                            for rowCode in sorted(seatingPlan.keys()):
                                f.write(rowCode + ',' + ''.join(seatingPlan[rowCode]) + '\n')
        elif subOption in 'xX':
            return False

def tma4b():
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