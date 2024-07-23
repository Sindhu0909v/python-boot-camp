a=int(input())
b=int(input())
c=a*b
while b!=0:
    a,b=b,a%b
    gcd=a
print("GCD",gcd)
lcm=c//gcd
print(lcm)