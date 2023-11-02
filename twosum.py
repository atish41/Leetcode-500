#two sum
num=[1,2,3,4,5]
target=9
list1=[]
for i in range(len(num)):
	for j in range(i+1,len(num)):
		if (i!=j and num[i]+num[j]==target):
			list1.append(i)
			list1.append(j)
			print(list1)
	