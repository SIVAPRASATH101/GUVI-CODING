n=int(input())
f=0
if n==1 :
  print("no")
else :
  for i in range(2,n//2) :
    if n%i==0 :
      f=f+1
  if f>0 :
    print("yes")
  else :
    print("no")
