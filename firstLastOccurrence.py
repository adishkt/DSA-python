nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]
target=3
#brute
first=-1
last=-1
n=len(nums)
for i in range(0,n):
    if nums[i]==target:
        if first==-1:
            first=i
        last=i
print(first,last)


#optimal
def lowerBound(nums,target):
    n=len(nums)
    lb=-1
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return lb

def upperBound(nums,target):
    n=len(nums)
    ub=n
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            ub=mid
            high=mid-1
        else:
            low=mid+1
    return ub

lb=lowerBound(nums,target)
if lb==-1:
    print(-1,-1)
ub=upperBound(nums,target)
print(lb,ub-1)


        
