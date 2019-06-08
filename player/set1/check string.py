y,z=input().split()
m=len(y)
cnt=0
for j in range(0,m,1):
	if y[j]!=z[j]:
		cnt+=1
if cnt==a1:
	print("yes")
else:
	print("no")
