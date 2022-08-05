#if else
#==========================================================
#| Data       |  Rate                                     |
#| up to 2gb  |  $5flat                                   |
#| above 2gb  |  $5 + $1 for every 100MB or part thereof  |
#==========================================================

def rate():
    dataUsed= float(input('Amount of data used: '))
    upTo2gb = float(5)

    if dataUsed < 2:
        print('Charge is $5')

    elif dataUsed > 2:
        print('The {}'.format(upTo2gb))

rate()
