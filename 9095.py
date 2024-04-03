import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    n = int(sys.stdin.readline().strip())
    
    if n == 1:
        print(1)
        continue
    elif n == 2:
        print(2)
        continue
    elif n == 3:
        print(4)
        continue
    else:
        listTravel = [[1], [2], [3]]
        listDone = []

        while listTravel:
            listNext = []
            for T in listTravel:
                intSum = sum(T)
                if intSum == n:
                    listDone.append(T)
                    continue
                if intSum < n:
                    listNext.append(T + [1])
                if intSum + 1 < n:
                    listNext.append(T + [2])
                if intSum + 2 < n:
                    listNext.append(T + [3])
            
            listTravel = listNext.copy()
        
        print(len(listDone))