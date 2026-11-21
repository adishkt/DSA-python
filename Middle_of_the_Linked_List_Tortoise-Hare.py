#brute
n=0
temp=self.head
while temp is not None:
    n+=1
    temp=temp.next
temp=self.head
for i in range(0,n//2):
    temp=temp.next
return temp  

#optimal

slow=head
fast=head
while fast is not None and fast.next is not None:
    slow=slow.next
    fast = fast.next.next
return slow