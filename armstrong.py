n=int(input("Enter a number: "))
nod=len(str(n))
total=0
num=n
while num>0:
    last=num%10
    total=total+(last**nod)
    num=num//10
if total==n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")