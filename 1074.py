import sys

def countZ(n, r, c):
    p = n - 1

    if n == 1:
        return r * 2 + c
    else:
        if r < 2 ** p and c < 2 ** p:
            return countZ(p, r, c) 
        elif r >= 2 ** p and c >= 2 ** p:
            return (4 ** p) * 3 + countZ(p, r - 2 ** p, c - 2 ** p)
        elif r >= 2 ** p:
            return (4 ** p) * 2 + countZ(p, r - 2 ** p, c)
        elif c >= 2 ** p:
            return 4 ** p + countZ(p, r, c - 2 ** p)

        
n, r, c = map(int,sys.stdin.readline().strip().split())
print(countZ(n, r, c))