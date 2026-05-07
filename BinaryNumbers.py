n = int(input().strip())
print(n)
binary = bin(n).split("0b")[1]
print(binary)
max_ones = 0
current = 0
for i in binary :
    if i == "1":
        current += 1
        max_ones =max(max_ones, current)
    else:
        current = 0
print(max_ones)

