for i in range(5):
    for j in range(5):
       if(i==2 or j==2 or (i%2!=0 and j%2!=0)):
            print("*",end=" ")
       else:
           print(" ")
    print()