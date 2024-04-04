import sys

n = int(sys.stdin.readline().strip())

intCount = 0

for _ in range(n):
    strInput = sys.stdin.readline().strip()
    if strInput.count('.') == 1:
        left, right = strInput.split('.')
        if 0 < len(left) and len(left) <= 8 and 0 < len(right) and len(right) <= 3:
            intCount += 1

print(intCount)
