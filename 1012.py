import sys

fix = [[1, 0], [0, 1], [-1, 0], [0, -1]]
T = int(sys.stdin.readline())

for _ in range(T):
    _, _, k = map(int,sys.stdin.readline().strip().split())
    listCabbages = []

    for _ in range(k):
        listCabbages.append(list(map(int,sys.stdin.readline().strip().split())))

    listTravel = []
    listVisited = []
    intCount = 0

    while len(listCabbages) > 0:
        if listTravel == []:
            listTravel.append(listCabbages[0])
            intCount += 1
        listTemp = []

        for x, y in listTravel:
            listCabbages.remove([x, y])
            for xf, yf in fix:
                current = [x + xf, y + yf]
                if current in listCabbages and not current in listTemp:
                    listTemp.append(current)
            
            listTravel = listTemp
    
    print(intCount)