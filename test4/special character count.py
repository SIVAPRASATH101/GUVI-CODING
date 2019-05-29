str=input()
c=0
for i in str :
  if i.isnumeric()!=True :
    if i.isalpha()!=True :
      c=c+1
print(c)
