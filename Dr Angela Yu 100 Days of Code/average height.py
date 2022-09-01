def main():
    studentHeights = input("Input a list of student heights ").split()
    students = len(studentHeights)+1
    total = 0
    for i in studentHeights:
        x = int(i)
        total += x
    avg = round(total/students)
    print(avg)

main()