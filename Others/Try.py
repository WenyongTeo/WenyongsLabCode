def main():

    n1=input('enter 1= ')
    n2=input('enter 2 ')
    n1, n2 = int(n1), int(n2)

    if n1==n2:
        print('same')
    elif n1>n2:
        print('n1 bigger')
    elif n1<n2:
        print('n2 bigger')
    else:
        print('idk')

    word=input('Enter word ')
    if word.upper() == word[::-1].upper():
        print('its the same')
    else:
        print('its not the same')

main()

