1.Identify the Nature of a Number

n = int(input())

if n > 0:
    print("POSITIVE")
elif n < 0:
    print("NEGATIVE")
else:
    print("ZERO")

2.Explore Math Functions
import math

num = float(input())
n = int(input())
base = int(input())
power = int(input())

print(math.floor(num))
print(math.ceil(num))
print(round(num))
print(int(math.sqrt(n)))
print(base ** power)

3.Smallest of Four Numbers
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(min(a,b,c,d))

4.Truncate to Two Decimal Places
num = float(input())
truncated = int(num * 100) / 100
print(f"{truncated:.2f}")

5.Find Second Maximum Number
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("No second max")
elif a >= b and a >= c:
    if b >= c:
        print(b)
    else:
        print(c)
elif b >= a and b >= c:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if a >= b:
        print(a)
    else:
        print(b)
6.Triangle Angle Validation
A = int(input())
B = int(input())
C = int(input())

if A + B + C == 180 and A > 0 and B > 0 and C > 0:
    print("VALID")

    if A == B == C:
        print("EQUILATERAL")
    elif A == B or B == C or A == C:
        print("ISOSCELES")
    else:
        print("SCALENE")
else:
    print("NOT VALID")
    print()
7.Number to Word
n = int(input())

if n == 0:
    print("zero")
elif n == 1:
    print("one")
elif n == 2:
    print("two")
elif n == 3:
    print("three")
elif n == 4:
    print("four")
elif n == 5:
    print("five")
elif n == 6:
    print("six")
elif n == 7:
    print("seven")
elif n == 8:
    print("eight")
else:
    print("nine")

8.Vowel or Consonant
ch = input().strip()

if ch in "aeiouAEIOU":
    print("vowel")
else:
    print("consonant")

9.Leap Year Checker
year = int(input())

if year % 400 == 0:
    print("yes")
elif year % 100 == 0:
    print("no")
elif year % 4 == 0:
    print("yes")
else:
    print("no")

10.Fun Grade Calculator
marks = [int(input()) for _ in range(5)]
average = sum(marks) / 5

if average >= 90:
    print("Excellent!")
elif average >= 80:
    print("Great Job!")
elif average >= 70:
    print("Good Effort!")
elif average >= 50:
    print("Keep Trying!")
else:
    print("Better Luck Next Time!")

11.Train Berth Type Finder
n = int(input())

if n % 8 == 1 or n % 8 == 4:
    print("Lower Berth")
elif n % 8 == 2 or n % 8 == 5:
    print("Middle Berth")
elif n % 8 == 3 or n % 8 == 6:
    print("Upper Berth")
elif n % 8 == 7:
    print("Side Lower Berth")
else:
    print("Side Upper Berth")

12.Electricity Bill Calculator
units = float(input())

if units <= 50:
    bill = units * 1
elif units <= 150:
    bill = (50 * 1) + (units - 50) * 2
elif units <= 250:
    bill = (50 * 1) + (100 * 2) + (units - 150) * 3
else:
    bill = (50 * 1) + (100 * 2) + (100 * 3) + (units - 250) * 4

if bill > 150:
    bill = bill + (bill * 0.20)

print(bill)

13.Electricity Bill Calculator
units = float(input())

if units <= 50:
    bill = units * 1
elif units <= 150:
    bill = (50 * 1) + (units - 50) * 2
elif units <= 250:
    bill = (50 * 1) + (100 * 2) + (units - 150) * 3
else:
    bill = (50 * 1) + (100 * 2) + (100 * 3) + (units - 250) * 4

if bill > 150:
    bill = bill + (bill * 0.20)

print(bill)

14.Train Fare Calculator
age = int(input())
distance = int(input())

fare = distance * 5

if age < 12:
    fare = fare * 0.5
elif age >= 60:
    fare = fare * 0.75

print(fare)

15.Average Marks Calculator
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

avg = (a + b + c + d + e) / 5

if avg.is_integer():
    print(int(avg))
else:
    print(f"{avg:.2f}")

16.
Fun Character Case Converter
ch = input()

if ch.islower() and ch.isalpha():
    print(ch.upper())
elif ch.isupper() and ch.isalpha():
    print(ch.lower())
else:
    print("abcd theriyatha?")
