#sum of digits
n=int(input())
sum=0
while(n>0):
    d=n%10
    sum+=d
    n=n//10
print(sum)
