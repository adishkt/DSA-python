nums=[55,32,97,-55,45,32,88,21]
#Brute force way
nums1=nums
nums1.sort()
n=len(nums)
print(nums1[n-2])

#better solution
largest=float("-inf")
s_largest=float("-inf")
for i in range(0,n):
    largest=max(largest,nums[i])
for i in range(0,n):
    if nums[i]>s_largest and nums[i]!=largest:
        s_largest=nums[i]
print(s_largest)

#optimal solution
l=float("-inf")
sl=float("-inf")
for i in range(0,n):
    if nums[i]>l:
        sl=l
        l=nums[i]
    elif nums[i]>sl and nums[i]!=l:
        sl=nums[i]
print(sl)
