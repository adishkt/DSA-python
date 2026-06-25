def rev(num,left,right):
    if left>=right:
        return num
    s=num[left]
    num[left]=num[right]
    num[right]=s
    return rev(num,left+1,right-1)

q=[5,7,3,2,6,1,5,9]
print(rev(q,0,7))

#other method
def rev(num,left,right):
    if left>=right:
        return num
    num[left],num[right]=num[right],num[left]
    return rev(num,left+1,right-1)

p=[5,7,3,2,6,1,5,9]
print(rev(p,0,7))
