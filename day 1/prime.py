import math
n=int(input())
if(n<=0):
    print("enter a positive number")
elif(n==1):
    print("neither a prime number or composite number")
else:
    for i in range (2,int(math.sqrt(n)+1)):
        if(n%i==0):
            a=False
        else:
            a=True
    if(a==True):
        print("prime")
    else: 
        print("not a prime")
            
