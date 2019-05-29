n=int(input())
l=[int(x) for x in input().split()]
l.sort()
for i in range(n) :
  print(l[i],end=" ")
