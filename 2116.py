import sys

n = int(sys.stdin.readline().strip())
listDice = []
listSum = []

for i in range(n):
    a, b, c, d, e, f = map(int,sys.stdin.readline().strip().split())
    listDice.append([a, f, b, d, c, e])

for i in range(1, 7):
    intSum = 0
    x = i

    for dice_original in listDice:
        dice = dice_original.copy() # deepcopy
        indexX = dice.index(x) 
        
        if indexX % 2 == 0: #X even check
            even = 1
        else:
            even = -1
        
        # for Debug, Don't mind
        # print(x, indexX, dice[dice.index(x) + even], dice)

        xPrime = dice[dice.index(x) + even] # pair of x
        dice.pop(indexX)
        dice.pop(dice.index(xPrime))
        x = xPrime

        intSum += max(dice)

    listSum.append(intSum)

print(max(listSum))