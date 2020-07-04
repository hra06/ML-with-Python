# Print the following pattern for n number of rows
    # For eg. N = 5

    # 1        1
    # 12      21
    # 123    321
    # 1234  4321
    # 1234554321


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
  