import sys

n = int(sys.stdin.readline().strip())
listATM = list(map(int,sys.stdin.readline().strip().split()))

listATM.sort()
intSum = 0

while listATM:
    intSum += sum(listATM)
    listATM.pop()

print(intSum)