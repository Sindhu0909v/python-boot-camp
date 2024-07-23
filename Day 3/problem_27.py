'''sum of sqaures in a number'''
n=int(input())
sum=0
while(n>0):
    d=n%10
    sum+=(d)**2
    n=n//10
print(sum)