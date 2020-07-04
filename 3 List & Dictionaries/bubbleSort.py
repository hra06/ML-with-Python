l = [int(x) for x in  input().strip().split(" ")]
n = len(l)

for i in range(n -1):
	for j in range(0, n-1-i):
		if(l[j] > l[j+1]):
			t = l[j+1]
			l[j+1] = l[j]
			l[j] = t

print(l)