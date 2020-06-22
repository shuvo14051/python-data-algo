def seq_search(arr, item):
	pos = 0
	found = False
	
	while pos < len(arr) and not found:
		if arr[pos] == item:
			found = True
			
		else:
			pos = pos + 1
			
	return found
	
	
arr = [1,23,4,5,6]
result = seq_search(arr, 75)
print(result)