nums=[11,15,20,1,4,5,6,8,9,10]
target=8
#brute 
n=len(nums)
for i in range(0,n):
    if nums[i]==target:
        print(i)
print(-1)


#optimal
nums=[17,18,20,1,3,4,5,7,8,10,11,13,14,16]
target=4
q=len(nums)
low,high=0,n-1
while low<=high:
    mid=(low+high)//2
    if nums[mid]==target:
        print(mid)
    if nums[mid]<=nums[high]:
        if nums[mid]<=target<=nums[high]:
            low=mid+1 
        else:
            high=mid-1
    else:
        if nums[low]<=target<=nums[mid]:
            high=mid-1
        else:
            low=mid+1
print(-1)