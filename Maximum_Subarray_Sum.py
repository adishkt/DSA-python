nums=[-2,1,-3,4,-1,2,1,-5,4]
#my solution
n=len(nums)
max_val=0
for i in range(0,n):
    sum=nums[i]
    for j in range(i+1,n):
        sum=sum+nums[j]
        max_val=max(max_val,sum)
print(max_val)

#brute
total=0
maxi=float("-inf")
for i in range(0,n):
    total=0
    for j in range(i,n):
        total=total+nums[j]
        maxi=max(maxi,total)
print(maxi)

#optimal
#Kadane alg

maxim=float("-inf")
total1=0
for i in range(0,n):
    total1=total1+nums[i]
    maxim=max(maxim,total1)
    if total1<0:
        total1=0
print(maxim)