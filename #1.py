with open('names.txt', 'r+') as file:
	names_contents = file.read()

	names = names_contents.replace('"', '').lower().split(',')
	result = 0
	lists = []
	for i, name in enumerate(names):
		sum_local = 0
		for char in name:
			num = ord(char) - (ord('a') - 1)
			sum_local += num
			#print(char, num, sum_local)
		result += sum_local * (i + 1)
	print(result)
