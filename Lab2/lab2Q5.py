#if else
#==========================================================
#| Data       |  Rate                                     |
#| up to 2gb  |  $5flat                                   |
#| above 2gb  |  $5 + $1 for every 100MB or part thereof  |
#==========================================================

import math
def rate():
    dataUsed= float(input('Amount of data used: '))


    if dataUsed > 2:
        dataUsedInMb = ((dataUsed * 1000)-2000)/100
        rate= (math.ceil(dataUsedInMb))+ 5
        print(f'Charge is {rate:.2f}')

    else:
        print('$5')

rate()

#