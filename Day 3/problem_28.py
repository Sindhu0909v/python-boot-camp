'''sum of sqaures of an even and odd digits in a number'''
n=int(input())
sum_even=0
sum_odd=0
while(n>0):
    d=n%10
    if(d%2==0):
        sum_even+=(d)**2
    else:
        sum_odd+=(d)**2
    n=n//10
print(sum_even)
print(sum_odd)