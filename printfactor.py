
#Brute force method to find factors of a number
n=int(input("Enter a number: "))
num=n
result=[]
for i in range(1,num+1):
    if num%i==0:
        result.append(i)
print("Factors of",n,"are:",result)

#better solution
result1=[]
for i in range(1,num//2+1):
    if num%i==0:
        result1.append(i)
result1.append(num)
print("Factors of",n,"are:",result1)

#optimal solution
from math import sqrt
result2=[]
for i in range(1,int(sqrt(num))+1):
    if num%i==0:
        result2.append(i)
        if num//i != i:
            result2.append(num//i)
result2.sort()
print("Factors of",n,"are:",result2)

#1 ---- 36/1== 36
#2 ---- 36/2== 18
#3 ---- 36/3== 12
#4 ---- 36/4== 9
#6 ---- 36/6== 6
#this is the optimal solution because we are only iterating till the square root of the number and we are also checking for the pair factor.