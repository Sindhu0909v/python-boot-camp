'''take a space sep i/p from user and print alt elements'''
lst=list(map(int,input().split()))
n=len(lst)
for i in range(0,n,2):
    print(lst[i])