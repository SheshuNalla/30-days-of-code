import sys

n = int(sys.stdin.readline().strip())

phonebook = dict()

for i in range(n):
    entry = sys.stdin.readline().strip().split(" ")
    phonebook[entry[0]] = entry[1]

query = sys.stdin.readline().strip()
while query:
    phonenumber = phonebook.get(query)
    if phonenumber:
        print(query + "=" + phonenumber)
    else:
        print("Not found")
    query = sys.stdin.readline().strip()