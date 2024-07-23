lst=list(map(int,input().split()))
arr=[]
for i in range(len(lst)-1,-1,-1):
    arr.append(lst[i])
print(arr)