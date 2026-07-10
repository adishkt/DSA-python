#Right Rotate an Array by K Places
nums=[3,9,5,6,7,2]
num=nums
n=len(nums)
k=int(input("Enter the value of k: "))
rotation=k%n
for _ in range(0,rotation):
    e=num.pop()
    num.insert(0,e)
print(num)

#better solution
numss=nums
q=len(numss)
k=k%q
numss[:]=numss[q-k:]+numss[:q-k]
print("better solution:", numss)

#optimal
def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
reverse(nums,n-k,n-1)
reverse(nums,0,n-k-1)
reverse(nums,0,n-1)
print("optimal solution:", nums)