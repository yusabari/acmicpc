import sys

def checkRepeatX(string, targetTime):
    for targetLength in range(1, len(string)): # 타겟 문자열의 크기 재기 
        listrepeatedString = []

        for i in range(0, len(string) - targetLength + 1):
            
            repeatString = string[i:i + targetLength]
            if repeatString in listrepeatedString:
                continue
            else:
                listrepeatedString.append(repeatString)

            intEqualCount = 0

            for j in range(0, len(string) - targetLength * targetTime + 1):
                boolEqual = True
                for k in range(targetLength * targetTime):
                    if not string[j + k] == repeatString[k % targetLength]:
                        boolEqual = False
                        break
                
                if boolEqual:
                    return False
                
            # if intEqualCount >= targetTime:
            #     print(intEqualCount, targetTime, targetLength, i, repeatString)
            #     return False
        
    return True
   


k, n, a = map(int,sys.stdin.readline().strip().split())

tupleAllowed = tuple(map(lambda x : chr(65 + x), range(0, n)))

listTarget = []

i = 0

while len(listTarget) < n:
    listTarget.append(0)
    while(not checkRepeatX(listTarget, k)):
        listTarget[len(listTarget) - 1] += 1

        while(max(listTarget) == a):
            indexMax = listTarget.index(a)
            if indexMax - 1 == -1:
                print(-1)
                exit()
            listTarget[indexMax] = 0
            listTarget[indexMax - 1] += 1

for i in listTarget:
    print(tupleAllowed[i],end='')