# recursion = top down 
# memoization = storing the result of the function so that we can use it later
# Fib using recursion and memoization


def fib(num,dp):
    if num==0:
        return 0
    if num==1:
        return 1
    if dp[num]!=-1:
        return dp[num]
    dp[num]= fib(num-1,dp)+fib(num-2,dp)
    return dp[num]

N=5
dp=[-1]*(N+1)

print(fib(N,dp))


#tabulation bottom up
n=5
dpt=[-1]*(n+1)
dpt[1]=1
dpt[0]=0
for num in range(2,n+1):
    dpt[num]=dpt[num-1]+dpt[num-2]
print(dpt[n])

#tabulation space optimization
prev2=0
prev=1
for i in range(2,n+1):
    curr=prev2+prev
    prev2=prev
    prev=curr
print(prev)
