count=0
n=int(input("Enter a number: "))
num=n
num1=n
while num>0:
    count+=1
    num=num//10
print(count)

#logarithmic method
from math import *
def count_digits(num1):
    print(int(log10(num1)+1))
count_digits(num1)

