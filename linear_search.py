nums=[5,3,9,8,1,6,4,-10,-100]
target=int(input("enter number to find : "))
for i in range(0,len(nums)):
    if nums[i]==target:
        print("index",i)
        break
else:
    print("not found")
