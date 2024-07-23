n=int(input())
f=0
s=1
if(n<=0):
    print("enter a positive number")
else:
    print(f,s,end=" ")
    for i in range(2,n):
        t=f+s
        f=s
        s=t
        print(t,end=" ")
 
