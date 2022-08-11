#Write your code below this line 👇
#input() will get user input in console
#Then print() will print the word "Hello" and user input
print("Hello" + "!" + input("what is your name?  "))
print(len(input("What is your name? ")))

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
a = b
b = c


#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print(f"a:{a}")
print(f"b:{b}")

#1. Create a greeting for your program.
print("Hello!, today we will create your band based on the city you grew up with and the name of your pet!")
#2. Ask the user for the city that they grew up in.
city=input("Please enter the city you grew up in here!\n")

#3. Ask the user for the name of a pet.
pet=input("Please enter the name of your pet!\n")
#4. Combine the name of their city and pet and show them their band name.
print(f"The name of your band will be '{city} {pet}'")
print("The name of your ban will be " + city + " " + pet)
#5. Make sure the input cursor shows on a new line, see the example at:
#https://replit.com/@appbrewery/band-name-generator-end

#my style of coding learnt from SUSS
print("Band name Generator")
city,pet= input("Enter your city and pet here ").split(' ')
print(f'The name of your band will be {city} {pet}')