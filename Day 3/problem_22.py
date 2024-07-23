n=int(input())
ori=n
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(ori==rev):
    print("Panlindrome")
else:
    print("Not a palindrome")