import sys

strInput = sys.stdin.readline().strip()
lenInput = len(strInput)
lenHalfInput = int(lenInput / 2)
lenQuarterInput = int(lenHalfInput / 2)

for i in range(lenHalfInput + 1):
    if not strInput[i] == strInput[lenInput - 1 - i]:
        print("IPSELENTI")
        exit()

for i in range(lenQuarterInput + 1):
    if not strInput[i] == strInput[lenHalfInput - 1 - i]:
        print("IPSELENTI")
        exit()

print("AKARAKA")