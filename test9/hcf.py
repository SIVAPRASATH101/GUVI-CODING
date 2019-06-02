y,z=input().split()
y=int(y)
z=int(z)
if y>z :
  s=z
else :
  s=y
for i in range(1,s+1) :
  if i%y==0 and i%z==0 :
    hcf=i
print(hcf)
