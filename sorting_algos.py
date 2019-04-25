A = [34,32,1,23,123,22]
len_arr = len(A)	
for i in range(1,len_arr):
	key = A[i]
	j = i-1
	while j >= 0 and A[j] > key:
		A[j+1] = A[j]
		j = j-1
	A[j+1] = key

print(A)