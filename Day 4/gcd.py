'''gcd  of two num'''
a=int(input())
b=int(input())
while b!=0:
    a,b=b,a%b
print("GCD",a)