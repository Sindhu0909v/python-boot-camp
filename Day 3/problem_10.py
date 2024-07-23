'''find the element that is present in k+N  index .k  AND N are given by user '''
lst=list(map(int,input().split()))
k=int(input())
n=int(input())
length=len(lst)
if(length<(k+n)):
    print("Error")
else:
    for i in lst:
        a=(lst[k+n])
    print(a)