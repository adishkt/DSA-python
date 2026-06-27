nums=[55,32,-97,99,3,67]
#method 1
largest=nums[0]
n=len(nums)
for i in range(0,n):
    largest=max(largest,nums[i])
print(largest)

#method 2
largest1=float("-inf")
q=len(nums)
for i in range(0,q):
    largest1=max(largest1,nums[i])
print(largest1)
