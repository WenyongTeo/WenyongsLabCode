'''
<1000 no installment pay full
>=1000 either pay 6 months interest 5%, 12 months interest 10%
add interest then monthly
'''

def loan():
    pay= float(input('Enter amount$ '))
    if pay > 1000:
        installment= float(input('Enter installment here 0, 6 or 12 '))
        if installment == 0:
            print(f"Please pay {pay:.2f}. No installment")
        elif installment == 6:
            interest6 = pay*(5/100)
            monthly= (pay+interest6)/6
            print(f'6 months installment is ${monthly:.2f} per month')
        elif installment == 12:
            interest12 = pay * (10/100)
            monthly = (pay + interest12)/12
            print(f'12 months installment is ${monthly:.2f} per month')
        else:
            print("wrong wrong")
    else:
        print(f'Please pay {pay:.2f} no installment plan.')

loan()