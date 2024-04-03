import sys
import math

dictInfSeq = {}

def getInfSequence(n, p, q):
    if n == 0:
        return 1
    else:
        x, y = math.floor(n/p), math.floor(n/q)
        xval, yval = 0, 0

        if not x in dictInfSeq:
            dictInfSeq[x] = getInfSequence(x, p, q)
        
        if not y in dictInfSeq:
            dictInfSeq[y] = getInfSequence(y, p, q)
        
        return dictInfSeq[x] + dictInfSeq[y]

n, p, q = map(int,sys.stdin.readline().strip().split())

print(getInfSequence(n, p, q))