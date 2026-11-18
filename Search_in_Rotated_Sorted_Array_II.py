nums=[7,7,7,7,7,7,7,1,2,3,4,5,7,7]
target=int(input('enter number'))
n=len(nums)
low,high=0,n-1
while low<=high:
    mid=(low+high)//2
    if nums[mid]==target:
        print(True)
        break
    if nums[low]==nums[mid]==nums[high]:
        low+=1
        high-=1
        continue
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
print(False)