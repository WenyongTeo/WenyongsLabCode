
def maina():
    chestSize = float(input('Enter Chest Measurement (cm): '))
    if chestSize < 80:
        print(f'Your T-Shirt size is 1\nChest Measurement lesser than {chestSize}, recommended size is 1')

    elif chestSize >= 80 and chestSize <= 88 :
        print(f'Your T-Shirt size is 2\nChest Measurement 80cm up to 88cm is size 2.')
    elif chestSize > 88 and chestSize <= 96:
        print(f'Your T-Shirt size is 3\nChest Measurement 89cm up to 96cm is size 3.')
    elif chestSize > 96 and chestSize <= 104:
        print(f'Your T-Shirt size is 4\nChest Measurement 97cm up to 104cm is size 4.')
    elif chestSize > 104 and chestSize <= 112:
        print(f'Your T-Shirt size is 5\nChest Measurement 105cm up to 112cm is size 5.')
    elif chestSize > 112 and chestSize <= 120:
        print(f'Your T-Shirt size is 6\nChest Measurement 113cm up to 120cm is size 6.')
    elif chestSize > 120 and chestSize < 128:
        print(f'Your T-Shirt size is 7\nChest Measurement 121cm up to 127cm is size 7.')
    else:
        print(f'Your T-Shirt size is 8\nFor chest measurement 128cm or more, recommended size is 8.')
maina()
