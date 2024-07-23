''' find the missing number in an array
sequence of number ..find the missing no'''
n=int(input())
lst=list(map(int,input().split()))
sum=(n*(n+1)//2)
sum2=0
for i in range(0,len(lst)):
    sum2+=lst[i]
print(sum-sum2)

