# Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Selection Sort'.

n=int(input())
l=[int(x) for x in input().strip().split(" ")]
for i in range (0,n-1):
  minIndex=i
  for j in range(i+1,n):
    if(l[j]<l[minIndex]):
      minIndex=j
  l[i],l[minIndex]=l[minIndex],l[i]
for i in l:
  print(i,end=" ")
  
  