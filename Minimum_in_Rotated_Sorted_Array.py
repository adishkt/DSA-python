nums=[4,5,6,7,0,1,2]
#brute
n=len(nums)
mini=float("inf")
for i in range(0,n):
    mini=min(mini,nums[i])
print(mini)

#optimal
nums=[7,8,9,1,2,3,4]
n=len(nums)
low,high=0,n-1
minimum=float("inf")
while low<=high:
    mid=(low+high)//2
    if nums[mid]<nums[high]:
        minimum=min(minimum,nums[mid])
        high=mid-1
    else:
        minimum=min(minimum,nums[low])
        low=mid+1
print(minimum)
        



