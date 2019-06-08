y,z=input().split()
y=int(y)
z=int(z)
cnt=0
for i in range(y,z+1) :
  f=0
  for j in range(2,i+1) :
    if i%j==0 :
      f=f+1
  if f==1 :
    cnt+=1
print(cnt)
