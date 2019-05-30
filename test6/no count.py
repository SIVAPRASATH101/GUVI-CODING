s,t=input().split()
l=[int(x) for x in input().split()]
s=int(s)
t=int(t)
c=0
for i in l :
  if i==t :
    c=c+1
print(c)
