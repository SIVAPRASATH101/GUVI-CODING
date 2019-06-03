y,z=input().split()
l=[int(x) for x in input().split()]
cnt=0
while(cnt!=int(z)) :
  s=min(l)
  l.remove(s)
  cnt=cnt+1
print(s)
