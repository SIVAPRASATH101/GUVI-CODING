s=input()
c=0
t=0
for i in s :
  if i.isalpha() :
    c=c+1
  if i.isnumeric() :
    t=t+1
if c>0 and t>0 :
  print("Yes")
else :
  print("No")
