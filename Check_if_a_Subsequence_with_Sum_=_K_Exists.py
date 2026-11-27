def backtrack(ind,total,subset):
    if total==k:
        result.append(subset.copy())
        return True
    elif total > k :
        return False
    if ind>=len(nums):
        return False
    subset.append(nums[ind])
    sum=total+nums[ind]
    pick=backtrack(ind+1,sum,subset)
    if pick==True:
        return True
    e=subset.pop()
    sum=total
    not_pick=backtrack(ind+1,sum,subset)
    return not_pick
        
    
    
 
nums=[5,9,4]
k=9
result=[]
print(backtrack(0,0,[]))