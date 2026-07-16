#my solution
nums=[5,9,1,2,4,15,6,3]
target=14
n=len(nums)
for i in range(0,n):
    for j in range(i+1,n):
        if (nums[i]+nums[j]==target):
            print(i ,j)
            break
        else:
            j+=1
            

#brute
for i in range(0,n-1):
    for j in range(i+1,n):
        if (nums[i]+nums[j]==target):
            print(i ,j)
            break
        

#optimal
hash_map={}
for i in range(0,n):
    remaining=target-nums[i]
    if remaining in hash_map:
        print(hash_map[remaining],i)
    hash_map[nums[i]]=i