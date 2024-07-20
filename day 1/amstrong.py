import math 
n=int(input())
ams=0
ori=n
c=0
while(n>0):
    n=n//10
    c+=1
n=ori
while(n>0):
    rem=n%10
    ams+=math.pow(rem,c)
    n=n//10
if(ori==ams):
    print("Amstrong12")
else:
    print("Not a amstrong")
    


    