def ordered_seq_search(arr, item):
	"""
	Input array must be ordered or sorted!
	"""
	pos = 0
	found = False
	stopped = False
	
	while pos < len(arr) and not found and not stopped:
		if arr[pos] == item:
			found = True
			
		else:
			if arr[pos] > item:
				stopped = True
			else:
			    pos = pos + 1
			
	return found
	
	
arr = [1,2,3,4,5,6]
result = ordered_seq_search(arr, 5)
print(result)