'''
Q4.
For example : NRIC No.(with official reference) = S7928964G

Step 1:
  Multiply each digit by the following weights.
    NRIC No. : 7  9  2  8  9  6  4
    Weights :  2  7  6  5  4  3  2
    Products: 14 63 12 40 36 18  8

  Make use of a tuple for the weights:
    weight = (2, 7, 6, 5, 4, 3, 2)

Step 2:
  Sum the products of each digit x weight.
  Sum : 14 + 63 + 12 + 40 + 36 + 18 + 8 = 191   ==> only S, F series
  for T and G series, add 4 to sum

Step 3:
  Find the remainder when the sum is divided by 11.
  Sum/11: 17 remainder 4

Step 4:
  Take 11 – remainder to get the check digit.
  Check digit : 11 – 4 = 7

Step 5:
  Look up the following table to get the official reference.
  Official Reference : G
  Conversion: (* A B C D E F G H I Z  J )
        Table  0 1 2 3 4 5 6 7 8 9 10 11
'''
def nricRefCheck(nric):
    weight = (2,7,6,5,4,3,2)
    reference = ('*','A','B','C','D','E','F','G','H','I','Z','J')
    # processing, implement the above alogorithm
    # step 1 & 2
    total = 0
    for i in range(1,8):
        product = int(nric[i]) * weight[i-1]
        total = total + product

    if nric[0] in "TG":
        total = total + 4

    # step 3 & 4
    checkDigit = 11 - (total % 11)
    #print(checkDigit)

    # step 5
    #return (referenece[checkDigit] == nric[-1].upper())
    if reference[checkDigit] == nric[-1].upper():
        return True
    else:
        return False

def lab4Q4():
    nric = input('Enter NRIC: ').upper()

    # positive testing
    if len(nric) == 9:
        if nric[0] in 'STFG':
            if nric[1:8].isdigit():  # pos 1 to 7, exclude 8
                if nric[8].isalpha() and nricRefCheck(nric):
                    print("Valid NRIC")
                else:
                    print('Reference letter is invalid')
            else:
                print('Must consist of 7 digits')
        else:
            print('The first letter must be S, T, F or G')
    else:
        print('Length must be exactly 9')

lab4Q4()
