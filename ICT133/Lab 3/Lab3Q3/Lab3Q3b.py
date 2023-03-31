def main():
    while True:
        num= int(input('Enter number: '))
        if num == -1:
            print('No more baby')
            break
        for i in range(num):
            print(f'{i+1}x{num}={(i+1)*num}')
main()
