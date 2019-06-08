y,z=input().split()
m=len(y)
cnt=0
for j in range(0,m,1):
	if s[j]!=t[j]:
		cnt+=1
if cnt==1:
	print("yes")
else:
	print("no")
