def backtrack(ind,total):
    if total==k:
        return 1
    elif total > k :
        return 0
    if ind>=len(nums):
        return 0
    sum=total+nums[ind]
    pick=backtrack(ind+1,sum)
    sum=total
    not_pick=backtrack(ind+1,sum)
    return not_pick+pick
        
    
    
 
nums=[5,9,4]
k=9
result=[]
print(backtrack(0,0))