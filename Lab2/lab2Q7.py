#(Make use of isdigit() and isalpha() function)
# length of the NRIC is 9
# # is a letter that can be "S", "T", "F" or "G"
# followed by 7 digits
# @ is any reference letter A to Z or a to z
#Write a program that inputs a NRIC number and displays whether a NRIC is valid.
# Display “Valid NRIC” or, if it is invalid, one of the following error messages:
#Length must be exactly 9
# The first letter must be S, T, F or G
# Must consist of 7 digits
# Reference letter must be A to Z or a to z

def nric():
    n=input('Enter NRIC: ')
    i = 9

    if len(n) > i:
        print('Must be exactly 9')

    elif n[1:8].isdigit():
        print('Valid')

    elif n[1:8].isalpha():
        print('Must have 7 digit')

    elif n[0] in ['S', 'T', 'F', 'G']:
        print('Valid')

    else:
        print("invalid")

nric()



