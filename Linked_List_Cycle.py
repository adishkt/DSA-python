#brute
temp=head
my_set=set()
while temp is not None:
    if temp in my_set:
        return True
    my_set.add(temp)
    temp=temp.next 
return False


#optimal
slow=head
fast=head
while fast is not None and fast.next is not None:
    slow=slow.next
    fast=fast.next.next 
    if slow==fast:
        return True
return False