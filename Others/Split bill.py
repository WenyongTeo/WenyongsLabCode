def main():
    sum = 0
    while True:
        quantity = int(input("Enter quantity: "))
        if quantity == -1:
            break
        unit = float(input('Enter unit price: '))
        subTotal = quantity*unit
        print(f'Subtotal is ${subTotal:.2f}')
        sum += subTotal
    gst = sum*0.07
    final= sum+gst
    print(f'Total price is ${sum:.2f}')
    print(f'GST is {gst:.2f}')
    print(f'Please pay ${final}')

main()