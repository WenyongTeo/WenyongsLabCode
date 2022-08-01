def main():
    name, email = str(input('Enter your email: ')).split('@')
    print("name is:", name)
    print("Organisation is {0:<2s}".format(email))


main()
