import sys

n = int(sys.stdin.readline().strip())
listWord = []
intCount = 0

for i in range(n):
    listWord.append(sys.stdin.readline().strip())

listWord.sort()

for i in range(n):
    for j in range(n):
        if not i == j:
            if listWord[j].startswith(listWord[i]):
                listWord[i] = ''

for word in listWord:
    if not word == '':
        intCount += 1

print(intCount)