'''replace the elements of the array with the avg of maxi and min element'''
lst=list(map(int,input().split()))
min=lst[0]
for i in range(0,len(lst)):
    if(min>lst[i]):
        min=lst[i]
max=lst[0]
for i in range(0,len(lst)):
    if(max<lst[i]):
        max=lst[i]
aver=(max+min)/2
for i in range(0,len(lst)):
    lst[i]=aver
print(lst)
''' 1.even or odd
    2.greatest of 3
    3. sum of all elements in an aray
    4. peak element in an array
    5. max elem in an array
    6. second max ele in an array
    7. reverse an array without using built in function
    8. sum of squares of a numbber
    9. sum of even or odd digit
    `10. palindrome
    11. fibonnaci series '''