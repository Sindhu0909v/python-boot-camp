#1.append
#2.pop
#3.sort
#4.print gm or print len of the list
lst=list(map(int,input().split(",")))
print("Enter your choice ...\n 1 For Append \n 2 for Pop \n 3 for Sort\n  4 for length of the lis")
ch=int(input())
if(ch==1):
    print("enter the element")
    ele=int(input())
    lst.append(ele)
    print(lst)
elif(ch==2):
    lst.pop()
    print(lst)
elif(ch==3):
    lst.sort()
    print(lst)
elif(ch==4):
    length=len(lst)
    print("length of the list is",length)
else:
    print("enter a valid input")
