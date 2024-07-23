'''sort elements --first half in ascending order and sec half in descending'''
lst=list(map(int,input().split()))
lst2=[]
for i in range(0,len(lst)//2):
    if(lst[i]<lst[i+1]):
        lst2.append(i)
        

    