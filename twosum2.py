def map(num,target):
	list1=[]
	for i in range(len(num)):
		for j in range(i+1,len(num)):
			if (i!=j and num[i]+num[j]==target):
				list1+=i,j
				print(list1)
num=[1,2,3,4]
target=6

map(num,target)
