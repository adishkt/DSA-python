prices=[7,2,1,5,6,4,8]
#brute force
max_profit=0
n=len(prices)
for i in range(0,n):
    for j in range(i+1,n):
        if prices[j]>prices[i]:
            p=prices[j]-prices[i]
            max_profit=max(max_profit,p)
print(max_profit)

#optimal
max_pro=0
min_price=float("inf")
for i in range(0,n):
    min_price=min(min_price,prices[i])
    max_pro=max(max_pro,prices[i]-min_price)
print(max_pro)