import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

stringInput = sys.stdin.readline().strip()
intCount = 0

i = 0

while(i < m - n * 2):
    if stringInput[i] == 'I':
        intOICount = 0

        for j in range(i + 1, m - 1, 2):
            if stringInput[j] == 'O' and stringInput[j + 1] == 'I':
                intOICount += 1
            else:
                i = j
                break
        else:
            i = j
        if intOICount >= n:
            intCount += intOICount - n + 1
    else:
        i += 1

print(intCount)