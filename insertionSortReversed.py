A = [3,1,5,6,1,7,8,2,3,8,6]

for j in range(1,len(A)):
    key = A[j]
    i = j-1
    while i >= 0 and A[i] < key:
        A[i+1] = A[i]
        i=i-1
    A[i+1] = key

print(A)