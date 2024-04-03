import sys

intLength = 64
intSum = 0
intCount = 0

intX = int(sys.stdin.readline().strip())

while(not intSum == intX):
    if intX - intSum >= intLength:
        intSum += intLength
        intCount += 1
    
    intLength //= 2
    
    print(intX, intSum, intLength, intCount)

print(intCount)