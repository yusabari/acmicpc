import sys

n, m = map(int,sys.stdin.readline().strip().split())

fix = [[1, 0], [0, 1], [-1, 0], [0, -1]]
listTomato = []
listTravel = []
intCount = 0

for i in range(m):
    listInput = list(map(int,sys.stdin.readline().strip().split()))
    listTomato.append(listInput)
    for j in range(n):
        if listInput[j] == 1:
            listTravel.append([i, j])

while listTravel:
    listNext = []
    for x, y in listTravel:
        for xf, yf in fix:
            fixed_x = x if x + xf >= m or x + xf == -1 else x + xf
            fixed_y = y if y + yf >= n or y + yf == -1 else y + yf
            if listTomato[fixed_x][fixed_y] == 0:
                listTomato[fixed_x][fixed_y] = 1
                listNext.append([fixed_x, fixed_y])
    
    listTravel = listNext
    intCount += 1

for tomatoes in listTomato:
    if 0 in tomatoes:
        print(-1)
        exit()

print(intCount - 1)