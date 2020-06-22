"""
def uni_char(s):
	return len(set(s)) == len(s)

result = uni_char('avbbnkg')
print(result)
"""
def uni_char(s):
	chars = set()
	for letter in s:
		if letter in chars:
			return False
		else:
			chars.add(letter)
	return True
	
result = uni_char('avbnkg')
if result == True:
	print('All the characterc in the given string are different.')
else:
	print('All the characterc in the given string are not different.')
