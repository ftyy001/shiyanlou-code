num=range(1,100)
count=0
for i in num:
	if (i % 7 !=0  and  i //10!=7 and i % 10!=7) :
		print(i)
		count=count+1
		if count % 6 ==0:
			print("\r\n")
	else:
		continue
