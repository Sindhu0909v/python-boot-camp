n=int(input())
r=n**0.5
c=0
if n==1:
    print("not a prime number")
elif n==2:
    print("prime")
for i in range(2,int(r+1)):
    if(n%i==0):
        c=1
        break
if c==0:
    print("prime number")
else:
    print("not a prime number")