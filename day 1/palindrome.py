n = int(input())
a = n
rev = 0
while a > 0:
    rem = a % 10
    rev = (rev * 10) + rem
    a = a // 10
if(rev==n): 
    print("Palindrome")
else:
    print("Not a palindrome")
