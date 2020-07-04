# For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. That is, you need to print in the order followed for every iteration:
# a. First row(left to right)
# b. Last column(top to bottom)
# c. Last row(right to left)
# d. First column(bottom to top)



s = input().strip().split(" ")
n = int(s[0])
m = int(s[1])
k = [ [ int(s[i*m+j+2]) for j in range(m)]for i in range(n)]
b = [ [False for i in range(m)] for i in range(n)]
isRow = True
isRowFirst = True
isColumnLast = True
rowNum = 0
colNum = m-1
for i in range(n+m):
    if isRow:
      #  print(" * ", end="")
        isRow = False
        num=0
        if isRowFirst :
            isRowFirst = False
            num = rowNum
            nnn = 0
            for j in k[num]:
                if b[num][nnn]:
             #       print(b[num][nnn],end=" ")
             #       print("c"+str(nnn),end="")
                    nnn+=1
                    continue
              #  print("@",end="")
                b[num][nnn]=True
                print(k[num][nnn], end = " ")
                nnn+=1
            
        else:
            isRowFirst = True
            num = n-rowNum-1
            rowNum+=1
            for j in range(m-1,-1,-1):
                if b[num][j]:
                    continue
                b[num][j] = True
                print(k[num][j], end = " ")     
    else:
        isRow = True
        num = 0
        if isColumnLast:
            isColumnLast = False
            num=colNum
            for j in range(0,n):
                if num>=m:
                  continue
                if num<0:
                  continue
                if b[j][num]:
                    continue
                b[j][num]=True
                print(k[j][num], end = " ")
        else:
            isColumnLast = True
            num=m-colNum-1
            colNum-=1
            for j in range(n-1,-1,-1):              
                if num>=m:
                  continue
                if b[j][num]:
                    continue
                b[j][num]=True
                print(k[j][num], end = " ")
