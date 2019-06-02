z=[int(x) for x in input().split()]
for i in range(0,len(z),2) :
  s=abs(z[i]-z[i+1])
  print(s)
