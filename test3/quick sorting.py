n1=int(input())
l1=[int(x) for x in input().split()]
l1.sort()
for i in range(n1) :
  print(l1[i],end=" ")
