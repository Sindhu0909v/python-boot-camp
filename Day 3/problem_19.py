'''reverse of a number -method -1 '''
n=int(input())
rev=0
while(n>0):
    d=n%10
    rev=(rev)*10+d
    n=n//10
print(rev)