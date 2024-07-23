'''print the ele in particular index -cyclic printing'''
lst=list(map(int,input().split()))
k=int(input())
ind=k%len(lst)
'''for i in range(0,ind):
    a=(lst[i])
print(a)'''
print(lst[ind])