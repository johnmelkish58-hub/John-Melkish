1.Count the number of digits
N = int(input())
print(len(str(abs(N))))

2.Sum of Even Digits
N = int(input())
total = 0

while N > 0:
    digit = N % 10
    if digit % 2 == 0:
        total += digit
    N //= 10

print(total)

3.Product of Digits
N = int(input())
product = 1

if N == 0:
    product = 0
else:
    N = abs(N)
    while N > 0:
        digit = N % 10
        product *= digit
        N //= 10

print(product)

4.Reverse a Number
N = int(input())
reverse = 0

while N > 0:
    digit = N % 10
    reverse = reverse * 10 + digit
    N //= 10

print(reverse)

5.Palindrome Number
N = int(input())
original = N
reverse = 0

while N > 0:
    digit = N % 10
    reverse = reverse * 10 + digit
    N //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

6.First Digit of a Number
N = int(input())

while N >= 10:
    N //= 10

print(N)

7.Count Zeros in a Number
n=int(input())
if n==0:
  print("1")
else:
  count=0
  while n>0:
    last=n%10
    if last==0:
      count=count+1
    n=n//10
  print(count)

8.Armstrong Number
N = int(input())
original = N
digits = len(str(N))
total = 0

while N > 0:
    digit = N % 10
    total += digit ** digits
    N //= 10

if total == original:
    print("Armstrong")
else:
    print("Not Armstrong")

9.Strong Number
import math
n=input()
s=0
for i in n:
  s+=math.factorial(int(i))
if s==int(n):
  print("Strong")
else:
  print("Not Strong")

10.Check Perfect Number
N = int(input())
total = 0

for i in range(1, N):
    if N % i == 0:
        total += i

if total == N:
    print("Perfect")
else:
    print("Not Perfect")

