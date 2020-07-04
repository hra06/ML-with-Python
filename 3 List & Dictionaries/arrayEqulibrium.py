# Find and return the equilibrium index of an array. Equilibrium index of an array is an index i such that the sum of elements at indices less than i is equal to the sum of elements at indices greater than i.
# Element at index i is not included in either part.
# If more than one equilibrium index is present, you need to return the first one. And return -1 if no equilibrium index is present.


def equilibriumIndex(arr):
    n = len(arr)
    rightSum = 0
    leftSum = 0
    
    # Sum of all elements 
    for i in range(n):
        rightSum += arr[i]
    for i in range(n):
        rightSum -= arr[i]
        if leftSum == rightSum:
            return i
        leftSum += arr[i]
    return -1

# Main
n = int(input())
arr = [int(i) for i in input().strip().split()]
print(equilibriumIndex(arr))
            