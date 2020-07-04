# For a given two-dimensional integer array/list of size (N x M), you need to find out which row or column has the largest sum(sum of all the elements in a row/column) amongst all the rows and columns.


s = input().strip().split(" ")
n = int(s[0])
m = int(s[1])
s = input().strip().split(" ")
k = [ [ int(s[i*m+j]) for j in range(m)]for i in range(n)]

index = 0
max = 0
type = True
#for rows:
ind = 0
for i in k:
    t = 0
    for j in i:
        t+=j
    if max<t :
        max = t
        index = ind
    ind+=1
for i in range(m):
    t = 0
    for f in k:
        t+=f[i]
    if max<t:
        type = False
        max = t
        index = i
if type:
    print("row", end = " ")
else :
    print("column", end = " ")
print(str(index)+" "+str(max))