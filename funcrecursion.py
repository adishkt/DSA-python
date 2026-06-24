#functional recursion
#sum of n natural numbers using recursion
#parameterized recursion
def func(sum,i,n):
    if i>n:
        print("Sum of first",n,"natural numbers is:",sum)
        return
    func(sum+i,i+1,n)
func(0,1,10)

#functional recursion
def func1(n):
    if n==1:
        return 1
    return n+func1(n-1)
print(func1(10))
    