def rec_binary_search(arr, item):
	if len(arr) == 0:
		return False
	else:
		mid = len(arr) // 2
		
		if arr[mid] == item:
			return True
		else:
			if item < arr[mid]:
				return rec_binary_search(arr[:mid], item)
			else:
				return rec_binary_search(arr[mid+1:], item)


arr = [1,2,3,45,6]
result = rec_binary_search(arr, 6)
print(result)