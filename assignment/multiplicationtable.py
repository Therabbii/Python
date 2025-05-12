print ('\t\t\t\tMultiplication Table')
print ('\t\t\t\t====================')
for header in range(1,10):
	print('\t', header, end= '')
print('\n   '+ ('-------'*11))

for multiplier in range(1,10):
	print(f'{multiplier:2} |', end='')
	for multiplicand in range(1,10):
		result = multiplier * multiplicand
		print(f'{result:8}' , end='')
	print()