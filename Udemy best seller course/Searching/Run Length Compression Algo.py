def compress(s):
	r = ""
	length = len(s)
	
	if length == 0:
		return ""
		
	if length == 1:
		return s + "1"
		
	i = 1
	count = 1
	
	while i < length:
		
		if s[i] == s[i-1]:
			count += 1
			
		else:
			r = r + s[i-1] + str(count)
			count = 1
		#	print(r)
			
		i += 1
		
	r = r + s[i-1] + str(count)
	
	return r

com = compress('aaabc')
print(com)