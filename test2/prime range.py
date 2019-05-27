n,m=input().split()
n=int(n)
m=int(m)
for k in range(n+1,m) :
  f=0
  for i in range(2,k+1) :
    if k%i==0 :
      f=f+1
  if f==1 :
      print(k,end=" ")
