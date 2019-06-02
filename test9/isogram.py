z=input()
cnt=0
for i in z :
  if z.count(i)>1 :
    cnt+=1
if cnt==0 :
  print("Yes")
else :
  print("No")
