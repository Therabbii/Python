print("      ", end='')
for header in range(1, 11):
    print(f"{header:2}", end='  ')
print()
print("     " + ("--- " * 10))

for multiplicand in range(1, 11):
    print(f"{multiplicand:2} | ", end='')
    for multiplier in range(1, 11):
        result = multiplicand * multiplier
        print(f"{result:2}", end='  ')
    print()