nums=[[5,20,3],[7,-10,9],[1,-52,6]]
print(nums)

#iteration
#i-row j-column
rows=len(nums)
cols=len(nums[0])
for i in range(0,rows):
    for j in range(0,cols):
        print(nums[i][j],end=" ")
    print()
        
        
#print upper triangle 
print("upper triangle")
for i in range(0,rows):
    for j in range(0,cols):
        if j>=i:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()
            
#print lower triangle 
print("lower triangle")
for i in range(0,rows):
    for j in range(0,cols):
        if i>=j:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()

#print diagonal triangle 
print("Diagonal")
for i in range(0,rows):
    for j in range(0,cols):
        if i==j:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()
    
    
#transpose
print("Transpose")
result=[[0]*rows for _ in range(cols)]
for i in range(0,rows):
    for j in range(0,cols):
        result[j][i]=nums[i][j]
print(result)