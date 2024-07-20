#swimming comp 1 winner
#z got selected mr x and mr y are frnds
#mr x -badminton and mr y -tabletennis
#badmintion sleection 1.height=140cm weigh=factors of 2  3.body fat<12%
#tennis  1.height=118 to 148cm  2.weight=factors(no.0f medals) 3.body fat<14%
#previous hist : z participated in 14 games out of which he has the sucess rate of 65%
#write a prgm whther x,y,z from india travel in same plane
z=True 
h1=int(input())
w1=int(input())
body_fat1=int(input())
if(h1>140 and w1%2==0 and body_fat1<12):
    print("x is selected")
    x=True
h2=int(input())
w2=int(input())
body_fat2=int(input())
#n=int(input())
if((h2>=118 and h2<=148) and w2%7==0 and body_fat2<14):
    print(" y is selected")
    y=True
if(x==True and y==True and z==True):
    print("ALL three ae tarvelling in same plane")
else:
    print("NO")



