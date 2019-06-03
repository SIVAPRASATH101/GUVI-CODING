y,z=input().split()
l=[int(x) for x in input().split()]
cnt=0
for i in l :
  if i%2!=0 :
    cnt=cnt+1
  if cnt==int(z) :
    print(i)
    break
