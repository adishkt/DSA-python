#recursion using parameter

def func(x,n):
    if n==0:
        return
    print(x)
    func(x,n-1)
func(5,3)

print("---------------------------------------------------")

#print 1 to n using recursion
def funct(n,count):
    if n==0:
        return
    print(count)
    count+=1
    funct(n-1,count)
funct(10,1)
 
#other way
def funct2(i,n):
    if i>n:
        return
    print(i)
    i+=1
    funct2(i,n)
funct2(11,20)