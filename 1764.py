import sys

n, m = map(int,sys.stdin.readline().strip().split())

dictName = dict()

for _ in range(n):
    strName = sys.stdin.readline().strip()
    dictName[strName] = 1

for _ in range(m):
    strName = sys.stdin.readline().strip()
    if strName in dictName:
        dictName[strName] += 1
    else:
        dictName[strName] = 1

listName = [key for key, value in dictName.items() if value == 2]
listName.sort()

print(len(listName))

for name in listName:
    print(name)