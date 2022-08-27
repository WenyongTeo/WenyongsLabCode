import math
def main():
    h = float(input('Enter height measurement (cm): '))
    c = float(input('Enter Chest Measurement (cm): '))
    waist = float(input('Enter waist measurement (cm): '))
    height = h//5
    chest = c//8
    if height < 31:
        heightSize = 1
    elif height == 31:
        heightSize = 2
    elif height == 32:
        heightSize = 3
    elif height == 33:
        heightSize = 4
    elif height == 34:
        heightSize = 5
    elif height == 35:
        heightSize = 6
    elif height == 36:
        heightSize = 7
    else:
        heightSize = 8
    if chest < 10:
        chestSize = 1
    elif chest == 10:
        chestSize = 2
    elif chest == 1:
        chestSize = 3
    elif chest == 12:
        chestSize = 4
    elif chest == 13:
        chestSize = 5
    elif chest == 14:
        chestSize = 6
    elif chest == 15:
        chestSize = 7
    else:
        chestSize = 8
    if waist < 70:
        waistSize = 1
    elif waist < 76:
        waistSize = 2
    elif waist < 84:
        waistSize = 3
    elif waist < 92:
        waistSize = 4
    elif waist < 100:
        waistSize = 5
    elif waist < 108:
        waistSize = 6
    elif waist < 116:
        waistSize = 7
    else:
        waistSize = 8
    if heightSize == chestSize == waistSize:
        shirt = "Best fit"
    elif heightSize == chestSize > waistSize or chestSize == waistSize > heightSize or heightSize == waistSize > chestSize:
        shirt = "Regular fit"
    elif (heightSize > chestSize and waistSize) or (chestSize > heightSize and waistSize) or (waistSize > heightSize and chestSize):
        shirt = "Relaxed fit"
    shirtList= [heightSize,chestSize,waistSize]
    fit= max(shirtList)
    print(f'Your size is {fit} {shirt}')

main()
'''

    HCW = (h,c,w)
    size1 = (0,0,0)
    size2 = (155,80,70)
    size3 = (160,88,76)
    size4 = (165,96,84)
    size5 = (170,104,92)
    size6 = (175,112,100)
    size7 = (180,120,108)
    size8 = (185,128,116)
'''