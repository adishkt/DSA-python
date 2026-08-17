nums=[2,4,6,7,9,11,18,9]
target=9
#iterative soln
def binarySearch(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
        
print(binarySearch(nums,target))  

#Recursive
def recBinarySearch(nums,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]<target:
        return recBinarySearch(nums,mid+1,high,target)      
    else:
        return recBinarySearch(nums,low,mid-1,target)

low=0
n=len(nums)
high=n-1
target=9
print(recBinarySearch(nums,low,high,target))
    