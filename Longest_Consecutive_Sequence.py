nums=[1,99,101,98,2,5,3,100,1,1]
#brute
n=len(nums)
count=0
max_count=0
for i in range(0,n):
    num=nums[i]
    count=1
    while num+1 in nums:
        count+=1
        num=num+1
    max_count=max(max_count,count)
print(max_count)

#better solution
nums.sort()
last_smaller=float("-inf")
count=0
longest=0
for i in range(0,n):
    num=nums[i]
    if num-1 == last_smaller:
        count+=1
        last_smaller=num
    elif num!=last_smaller:
        count=1
        last_smaller=num
    longest=max(longest,count)
print(longest)

#optimal
nums=[1,99,101,98,2,5,3,100,1,1]
my_set=set()
for i in range(0,n):
    my_set.add(nums[i])
longest=0
for num in my_set:
    if num-1 not in my_set:
        x=num
        count=1
        while x+1 in my_set:
            count+=1
            x+=1
        longest=max(longest,count)
print(longest)
     