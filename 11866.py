import sys

k, n = map(int,sys.stdin.readline().strip().split())

listJosephus = [i for i in range(1, k + 1)]

print("<", end='')
intCur = n - 1
print(listJosephus.pop(intCur), end='')

while(not len(listJosephus) == 0):
    intCur += n - 1
    intCur %= len(listJosephus)

    print(", " + str(listJosephus.pop(intCur)), end='')

print('>')