import sys
import math

dictInfSeq = {}

def getInfSequence(n, p, q, x, y):
    if n == 0:
        return 1
    else:
        a, b = math.floor(n/p) - x, math.floor(n/q) - y
        aval, yval = 0, 0

        if a < 0:
            a = 0
        if not a in dictInfSeq:
            dictInfSeq[a] = getInfSequence(a, p, q, x, y)
    
        if b < 0:
            b = 0
        if not b in dictInfSeq:
            dictInfSeq[b] = getInfSequence(b, p, q, x, y)
        
        return dictInfSeq[a] + dictInfSeq[b]

n, p, q, x, y = map(int,sys.stdin.readline().strip().split())

print(getInfSequence(n, p, q, x, y))