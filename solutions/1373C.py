kk=int(input())
while(kk):
	li=list(input())
	q=w=0
	kk-=1
	for i in range(len(li)):
		if li[i]=="+":
			q+=1
		else:
			q-=1
		if(q<0):
			w+=i+1
			q+=1
	print(w+len(li))