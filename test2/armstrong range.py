no,m=input().split()
no=int(no)
m=int(m)
for i in range(no+1,m) :
  sum=0
  p=i
  while p>0 :
    t=p%10
    sum=sum+t**3
    p=p//10
  if sum==i :
    print(sum,end=" ")
