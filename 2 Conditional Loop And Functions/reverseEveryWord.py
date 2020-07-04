# Given a string S, reverse each word of a string individually. For eg. if a string is "abc def", reversed string should be "cba fed".


n=int(input())
k=2*n-2
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    for j in range(k):
        print(" ",end="")
    k=k-2
    for j in range(1,i+1):
        print(i,end="")
        i=i-1
    print()
  