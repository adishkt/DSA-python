#number hashing
#brute force

n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]

for num in m:
    count=0
    for x in n:
        if x==num:
            count +=1
    print(f"Frequency of {num} is: {count}")
print("---------------------------------------------------")
print("---------------------------------------------------")

#optimal solution
hash_list=[0]*11
for num in n:
    hash_list[num] +=1
for num in m:
    if num<1 or num>10:
        print(f"Frequency of {num} is: 0")
    else:
        print(f"Frequency of {num} is: {hash_list[num]}")

print("---------------------------------------------------")
print("---------------------------------------------------")

#using dictionary
freq_dist={}
for num in n:
    if num in freq_dist:
        freq_dist[num] +=1
    else:
        freq_dist[num] =1

for num in m:
    if num in freq_dist:
        print(f"Frequency of {num} is: {freq_dist[num]}")
    else:
        print(f"Frequency of {num} is: 0")

print("---------------------------------------------------")
print("---------------------------------------------------")

#character hashing brute force
s="azyxyyzaaaa"
q=["a","z","y","x"]
for char in q:
    count=0
    for c in s:
        if c==char:
            count +=1
    print(f"Frequency of {char} is: {count}")
print("---------------------------------------------------")
print("---------------------------------------------------")

#character hashing optimal
hash_list1=[0]*26
for char in s:
    ascii_val=ord(char)
    index = ascii_val-97
    hash_list1[index] +=1
for char in q:
    ascii_val=ord(char)
    index=ascii_val-97
    print(f"Frequency of {char} is: {hash_list1[index]}")