i = 0
for i in range(2555):
	if chr(i).isdigit():
		print(chr(i), (i - ord('0')))