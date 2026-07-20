nums=[5,10,-3,-1,-10,6]
#brute
n=len(nums)
pos=[]
neg=[]
for i in range(0,n):
    if nums[i]>0:
        pos.append(nums[i])
    else:
        neg.append(nums[i])
for i in range(0,len(pos)):
    nums[2*i]=pos[i]
    nums[(2*i)+1]=neg[i]
print(nums)
        
#optimal
num=[5,10,-3,-1,-10,6] 
q=len(num)
result=[0]*n
p,n=0,1
for i in range(0,q):
    if num[i]>=0:
        result[p]=num[i]
        p+=2
    else:
        result[n]=num[i]
        n+=2
print(result)
    
        