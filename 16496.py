import sys

n = int(sys.stdin.readline().strip())
listNum = list(map(int,sys.stdin.readline().strip().split()))
strAns = ''

for i in range(n - 1):
    for j in range(i + 1, n):
        sumij = int(str(listNum[i]) + str(listNum[j]))
        sumji = int(str(listNum[j]) + str(listNum[i]))

        if sumji > sumij:
            listNum[i], listNum[j] = listNum[j], listNum[i]

for ans in listNum:
    strAns += str(ans)

print(int(strAns))