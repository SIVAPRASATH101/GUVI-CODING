z=int(input())
t=[int(x) for x in input().split()]
y=sorted(t)
for i in range(len(t)) :
  if t[i]!=y[i] :
    print(i)
    break
