def binary_search(arr, item):
	first = 0
	last = len(arr) - 1
	found = False
	
	while first <= last and not found:
		mid = ( first+last)//2
		
		if arr[mid] == item:
			found = True
		else:
			if item < arr[mid]:
				last = mid-1
			else:
				first = mid+1
	return found
		
		
arr = [1,2,2,3,4,4,5,6,7]
	
result = binary_search(arr, 7)
print(result)