#별,동그라미,네모,세모
testCase = int(input())
for tc in range(testCase):
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	aLen = a[0]
	a = a[1:]
	bLen = b[0]
	b = b[1:]

	aNum = []
	bNum = []
	for i in range(1,5):
		aNum.append(a.count(i))
		bNum.append(b.count(i))
	for i in range(3,-1,-1):
		if aNum[i] > bNum[i]:
			print('A')
			break
		elif aNum[i] < bNum[i]:
			print('B')
			break
	else:
		print('D')
	

