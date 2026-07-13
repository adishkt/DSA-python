#mysolution for it
nums=[1,0,2,4,3,0,0,3,5,1]
n=len(nums)
for i in range(0,n):
    for j in range(i+1,n):
     if nums[i]==0:
        nums[i],nums[j]=nums[j],nums[i]
print(nums)

#brute force solution
nums=[1,0,2,4,3,0,0,3,5,1]
n=len(nums)
temp=[]
for i in range(0,n):
   if nums[i]!=0:
      temp.append(nums[i])
nz=len(temp)
for i in range(0,nz):
   nums[i]=temp[i]
for i in range(nz,n):
   nums[i]=0
print(nums)

#optimal solution
nums=[1,0,2,4,3,0,0,3,5,1]
if len(nums)==1:
   print(nums)
i=0
while i<len(nums):
   if nums[i]==0:
      break
   i+=1
if i==len(nums):
   print(nums)
j=i+1
while j<len(nums):
   if nums[j]!=0:
      nums[i],nums[j]=nums[j],nums[i]
      i+=1
   j+=1
print(nums)
      
   
