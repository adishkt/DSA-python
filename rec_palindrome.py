#recursion palindrome

#looping
s=str(input("enter the string :"))
left=0
right=len(s)-1
while left<right:
    if s[left] != s[right]:
        print(False)
        break
    left+=1
    right -= 1
else:
    print(True)

#recursion

def func(q,l,r):
    if l>=r:
        return True
    if s[left]!=s[right]:
        return False
    return func(s,l+1,r-1)
    
q=str(input("enter the string :"))
l=0
r=len(q)-1
print(func(q,l,r))