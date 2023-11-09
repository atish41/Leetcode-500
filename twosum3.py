class twosum:
	def __init__(self,num,target):
		self.num=num
		self.target=target
	def sum(self):
		for i in range(len(num)):
			for j in range(i+1,len(num)):
				if (i!=j and num[i]+num[j]==target):
					print(i,j)
num=[1,2,3,4,5]
target=8




add=twosum(num,target)
add.sum()