import sys

n, m = map(int,sys.stdin.readline().strip().split())
wb = ['W', 'B']
listBoard = []
listDiff = []

for i in range(n):
    listBoard.append(sys.stdin.readline().strip())

for k in range(n - 7):
    for l in range(m - 7):
        for even in range(2):
            intDiff = 0
            for i in range(8):
                start = i + even
                for j in range(8):
                    if not wb[(j + start) % 2] == listBoard[i + k][j + l]:
                        intDiff += 1
            listDiff.append(intDiff)

print(min(listDiff))