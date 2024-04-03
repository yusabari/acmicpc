import sys

while True:
    listTriangle = list(map(int,sys.stdin.readline().strip().split()))
    if max(listTriangle) == 0:
        break
    else:
        listTriangle.sort()
        
        if listTriangle[0] ** 2 + listTriangle[1] ** 2 == listTriangle[2] ** 2:
            print("right")
        else:
            print("wrong")
