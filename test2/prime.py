n=int(input())
f=0
for i in range(2,n+1) :
  if n%i==0 :
    f=f+1
if f==1 :
  print("prime")
else :
  print("no")
