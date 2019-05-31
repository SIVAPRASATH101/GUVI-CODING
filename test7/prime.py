n=int(input())
fz=0
for i in range(2,n+1) :
  if n%i==0 :
    fz=fz+1
if fz==1 :
  print("yes")
else :
  print("no")
