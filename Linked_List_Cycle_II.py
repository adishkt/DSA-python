#find cycle starting point in linked list

#brute
temp=head
my_set=set()
while temp is not None:
    if temp in my_set:
        return temp
    my_set.add(temp)
    temp=temp.next
return None


#optimal

slow=head
fast=head
while fast is not None and fast.next is not None:
    slow=slow.next 
    fast=fast.next.next 
    if slow==fast:
        slow=head
        while slow!=fast:
            slow=slow.next 
            fast=fast.next 
        return slow

return None

  
