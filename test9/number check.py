z=input()
s=[]
for i in z :
  if i.isnumeric() :
    s.append(i)
if s==[] :
  print()
else :
  for i in s :
    print(i,end="")
