# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
yourname = name1.upper()
theirname = name2.upper()

t = yourname.count('T') + theirname.count('T')
r = yourname.count('R') + theirname.count('R')
u = yourname.count('U') + theirname.count('U')
e = yourname.count('E') + theirname.count('E')
l = yourname.count('L') + theirname.count('L')
o = yourname.count('O') + theirname.count('O')
v = yourname.count('V') + theirname.count('V')
e = yourname.count('E') + theirname.count('E')
totalTrue = t+r+u+e
totalLove = l+o+v+e
Lovescore = (totalTrue*10) + totalLove

if Lovescore < 10 or Lovescore > 90:
    print(f"Your score is {Lovescore}, you go together like coke and mentos.")
elif Lovescore >40 and Lovescore < 50:
    print(f"Your score is {Lovescore}, you are alright together.")
else:
    print(f'Your score is {Lovescore}')
