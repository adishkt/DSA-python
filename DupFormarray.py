#Remove Duplicates from a Sorted Array 
#brute force approach
nums=[1,1,1,2,3,4,4,7,9,9,9,10]
n=len(nums)
freq_map={}
for i in range(0,n):
    freq_map[nums[i]]=0
j=0
for k in freq_map:
    nums[j]=k
    j+=1
print(j)

#optimal solution
num=[1,1,1,2,3,4,4,7,9,9,9,10]
q=len(num)
if q==1:
    print(1)
i=0
j=i+1
while j<q:
    if num[j]!=num[i]:
        i+=1
        num[i],num[j]=num[j],num[i]
    j+=1
print(i+1)