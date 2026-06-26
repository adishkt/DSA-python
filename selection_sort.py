
def selection_sort(nums):
    n=len(nums)
    for i in range(0,n):
        mid=i
        for j in range(i+1,n):
            if nums[mid]>nums[j]:
                mid=j
        nums[i],nums[mid]=nums[mid],nums[i]
    return nums

nums=[5,7,8,4,1,6,9,2]
print(selection_sort(nums))