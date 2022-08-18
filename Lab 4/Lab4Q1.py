'''
File handling) The rainfall (in mm) for each day in a particular month is captured in a
file, rainfall.dat. Write a program to read the rainfall for each day, and display a
summary report as follows:
Rainfall Summary
Average rainfall 5.65mm
No of days with no rain 3 days
Highest rainfall recorded 20.6mm
Refer to the Appendix of this document for the content of rainfall.dat which you can
use to create the input file.
'''
def avg(rainfall):
    total =
    sum=
    print(f"Avgerage rainfall {sum}")
    return sum

def noRain(rainfall):
    for i in rainfall:
        if i == 0:
            i + 1
        print(f"No of days with no rain {i}")




def main():
    rainfall = open('rainfall.dat', 'r') #open/open modes
    for summary in rainfall:
        print('Rainfall Summary')
        avg(sum)
        noRain(i)



main()

