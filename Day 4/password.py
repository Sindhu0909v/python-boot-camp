'''password verifier.mr x is trying to create a new password.These are the required condtions for creating a new password.These are 
1.minimum length is 8 and max lenght is 15
2. only @ and / is must in  a password
3. no spaces are allowed 
4. only alpha num are allowed
you are supposed to print weak if the length is exact 8 ,medium if tthe length is between 8-12 and strong if the lenght is between 12 to 15'''
str1=input()
l=len(str1)
if(l>=8 and l<=15):
    a="@/"
    for i in str1:
        if(i==a[0] or i==a[1]):      
           str1=True
    else:
        print(" Please follow instructions..")
    if(str1.isalpha()):
        str1=True
    else:
        print("please follow instruction...")
    if(str==" "):
        print("please folow the instructions")
if(l==8):
    print("weak")
elif(l==12):
    print("medium")
else:
    print("strong")