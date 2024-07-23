'''find rev of a number '''
n=int(input())
rev=""
while(n>0):
    d=n%10
    rev=rev+str(d)
    n=n//10
print(int(rev))