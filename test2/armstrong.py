no=int(input())
sum=0
p=no
while p>0 :
  t=p%10
  sum=sum+t**3
  p=p//10
if sum==no :
  print("yes")
else :
  print("no")
