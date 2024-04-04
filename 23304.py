import sys
import math

def isAKARAKA(strIn):
    lenInput = len(strIn)
    if lenInput == 1:
        return True
    else:
        lenHalfInput = math.floor(lenInput / 2)

        for i in range(lenHalfInput + 1):
            if not strIn[i] == strIn[lenInput - 1 - i]:
                return False
        
        return isAKARAKA(strIn[0:lenHalfInput])


strInput = sys.stdin.readline().strip()

if isAKARAKA(strInput):
    print("AKARAKA")
else:
    print("IPSELENTI")