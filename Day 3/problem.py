'''sum of even digits in a num'''
n=int(input())
sum=0
while n>0:
    d=n%10
    if(d%2==0):
        sum+=d
    n=n//10
print(sum)