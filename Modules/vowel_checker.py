def vowels(a):
	flag = False
	for i in a:
		print(i)
		if i in ['a', 'e', 'i', 'o', 'u']:
			flag = True
			break
	return flag