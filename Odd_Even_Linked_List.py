#brute
values=[]
if head is None  or head.next is None:
    return head
temp=head
while temp and temp.next:
    values.append(temp.val)
    temp=temp.next.next 
temp=head.next 
while temp and temp.next:
    values.append(temp.val)
    temp=temp.next.next
temp=head 
index=0
while temp is not None:
    temp.val=values[index]
    index+=1
    temp=temp.next
return head



#optimal

if head is None  or head.next is None:
    return head
odd=head
even=head.next
even_head=even
while even.next is not None and even is not None:
    odd.next=odd.next.next 
    odd=odd.next 
    even.next=even.next.next 
    even=even.next 

odd.next=even_head
return head