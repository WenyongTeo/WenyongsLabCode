'''
(while, sentinel loop) Write a program that simulates the point of sale at a supermarket checkout.
The program inputs the quantity and price of items and displays price, the subtotal.
Input ends when -1 is entered for quantity to indicate there is no more item to checkout.
The GST and the final price are then computed. For example,
Enter quantity: 2
Enter unit price: 1.5
Subtotal is $3.00
Enter quantity: 4
Enter unit price: 2.25
Subtotal is $9.00
Enter quantity: -1
Total price is $12.00
GST is $0.84
Please pay $12.84
'''
def main():
    sum = 0
    while True:
        quantity = int(input("Enter quantity: "))
        if quantity == -1: #real world, qty <= 0
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


