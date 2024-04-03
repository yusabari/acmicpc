import sys

strN = str(sys.stdin.readline().strip())
strNPrime = ""
strNPrimeDown = ""
intBrokenCount = int(sys.stdin.readline().strip())
setButton = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
setBroken = set(map(str,sys.stdin.readline().strip().split()))
setButton = setButton - setBroken
setIntButton = set(map(int,setButton))

i = 0

while(strN[i] in setButton and i <= len(strN)):
    strNPrime += strN[i]
    i += 1

if int(strN) > 100:
    if not max(setIntButton) < int(strN[i]):
        upper = 9
        for j in list(setIntButton)[::-1]:
            if j < int(strN[i]):
                break
            else:
                upper = j
        
        strNPrime += str(j)
        i += 1

    while (i < len(strN)):
        strMin = str(min(setIntButton))
        strNPrime += strMin
        i += 1

elif int(strN) < 100:
    if not min(setIntButton) > int(strN[i]):
        lower = 0
        for j in list(setIntButton):
            if j > int(strN[i]):
                break
            else:
                lower = j
        
        strNPrime += str(j)
        i += 1

    while (i < len(strN)):
        strMax = str(max(setIntButton))
        strNPrime += strMax
        i += 1
    

print(strNPrime)