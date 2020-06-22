def bubble_sort(arr):
	for n in range(len(arr)-1, 0, -1):
		for k in range(n):
			if arr[k] > arr[k+1]:
				#its a python style swaping
				arr[k], arr[k+1] = arr[k+1],arr[k]
				
	return arr
	
	
arr = [4,6,1,3,0]
result = bubble_sort(arr)
print(result)