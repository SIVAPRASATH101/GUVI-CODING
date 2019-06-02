y,z=input().split()
y=int(y)
z=int(z)
if y>z :
  s=z
else :
  s=y
hcf1=1
for i in range(1,s+1) :
  if i%y==0 and i%z==0 :
    hcf1=i
print(hcf1)
