def func(ind,total,subset):
    if total==target:
        result.append(subset.copy())
        return
    elif total>target:
        return
    if ind>=len(nums):
        return
    subset.append(nums[ind])
    sum=total+nums[ind]
    func(ind+1,sum,subset)
    e=subset.pop()
    sum=sum-e
    func(ind+1,sum,subset) 
result=[]
target=9
nums=[5,9,4]
func(0,0,[])
print(result)