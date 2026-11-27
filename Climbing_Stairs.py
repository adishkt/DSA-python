def fun(index):
    if index==1 or index==0:
        return 1
    return fun(index-1)+fun(index-2)

print(fun(4))


#memorization
def fun(index,dp):
    if index==1 or index==0:
        return 1
    if dp[index]!=-1:
        return dp[index]
    dp[index]=fun(index-1,dp)+fun(index-2,dp)
    return dp[index]

n=5
dp=[-1]*(n+1)
print(fun(n,dp))


dpt=[-1]*(n+1)
dpt[1]=1
dpt[0]=1
for num in range(2,n+1):
    dpt[num]=dpt[num-1]+dpt[num-2]
print(dpt[n])


prev2=1
prev=1
for i in range(2,n+1):
    curr=prev2+prev
    prev2=prev
    prev=curr
print(prev)
