# Day3 miniproject - smart daily utility calculator
print("🔥 Welcome to Smart Daily Utility Calculator🔥")
#input numbers
a=float(input("Enter a number :"))
b=float(input("Enter b number :"))
#Operations
print("/Results:")
print(f"Addition:{a}+{b}={a+b}")
print(f"Substraction:{a}-{b}={a-b}")
print(f"Multiplication:{a}*{b}={a*b}")
print(f"Division:{a}/{b}={a/b}")
print(f"Floor Division:{a}//{b}={a//b}")
print(f"Modulus:{a} % {b}={a % b}")
print(f"Power:{a}**{b}={a**b}")
#Even/Odd
if a%2==0:
    print(f"{a} is Even")
else:
    print(f"{a} is Odd")
if b % 2==0:
    print(f"b is Even")
else:
    print(f"b is Odd")
#Chocolate Division Problem
chocolate=int(input("Enter no of Chocolates :"))
friends=int(input("Enter no of Friends :"))
left=chocolate%friends
print(f"Total no of Chocolates left :{left}")


