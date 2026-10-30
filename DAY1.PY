1.Input and Output Practice
a = int(input())
b = float(input())
c = input()
d = int(input())
e = float(input())

print(a)
print(b)
print(c)
print(d)
print(e)

2.Progressive Float Execution
import struct
a=float(input())
a = struct.unpack('f', struct.pack('f', a))[0]
print("%.5f"%a)
print("%.4f"%a)
print("%.3f"%a)
print("%.2f"%a)
print("%.1f"%a)
print("%.0f"%a)

3.Problem: Sum, Difference, Product, Division and Modulo.
A = int(input())
B = int(input())
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)

4.ASCII
n = int(input())
print(chr(n))

5.Update Counter
counter = int(input())
counter = counter + 5
counter = counter * 2
counter = counter - 3
print(counter)

6.ODD or EVEN
n = int(input())
result = "Even" if n % 2 == 0 else "Odd"
print(result)

7.Greatest Among Three Numbers

a = int(input())
b = int(input())
c = int(input())
#print(max(a,b,c))
if a>b and a>c:
  print(a)
elif b>c:
  print(b)
else:
  print(c)

8.Character Digit to Integer
char=input()
print(int(char))

9.Personalized Greeting
name = input()
print(f"Hi {name}, welcome to the programming class!")

1O.Calculate Total and Average Marks
name = input()
m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())
total = m1 + m2 + m3 + m4 + m5
average = total / 5
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks: {:.2f}".format(average))

11.Shape Area Calculation

a = int(input())
l = int(input())
b = int(input())
r = int(input())
B = int(input())
h = int(input())

square = a * a
rectangle = l * b
circle = 3.14 * r * r
triangle = 0.5 * B * h
print("Area of Square=", square, sep="")
print("Area of Rectangle=", rectangle, sep="")
print("Area of Circle=", format(circle, ".2f"), sep="")
print("Area of Triangle=", format(triangle, "g"), sep="")

12.Shape Perimeter Calculation Program

a = int(input())
l = int(input())
w = int(input())
r = int(input())
side1 = int(input())
side2 = int(input())
base = int(input())

square = 4 * a
rectangle = 2 * (l + w)
circle = 2 * 3.14 * r
triangle = side1 + side2 + base

print(square)
print(rectangle)
print(format(circle, ".2f"))
print(triangle)

13.Handling Mixed Inputs
n = int(input())
sentence = input()
print(n)
print(sentence)