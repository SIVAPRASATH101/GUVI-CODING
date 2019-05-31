a1=input()
l=['0','1']
cnt=0
for i in a1 :
  if i not in l :
    cnt=1
if cnt>0 :
  print("no")
else :
  print("yes")
