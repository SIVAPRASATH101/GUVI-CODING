z=list(input())
for i in range(0,len(z)-1,2) :
  z[i],z[i+1]=z[i+1],z[i]
for i in z :
  print(i,end="")
