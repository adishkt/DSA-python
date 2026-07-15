#Brute 
nums=[9,6,4,2,3,5,7,0,1]
n=len(nums)
for i in range(0,n+1):
    if i not in nums:
        print(i)
        break
    

#better solution

freq={}
for i in range(0,n+1):
    freq[i]=0
for num in nums:
    freq[num]=1
for k,v in freq.items():
    if v==0:
        print(k)
        break

#optimal solution
total_sum=(n*(n+1))//2
actual_sum=sum(nums)
print(total_sum-actual_sum)