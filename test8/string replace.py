z=input()
l1=list(z)
l2=len(l1)//2
if len(l1)%2!=0:
	l1[l2]="*"
else:
	l1[l2]="*"
	l1[l2-1]="*"
for i in l1:
    print(i,end='')
