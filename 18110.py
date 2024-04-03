import sys

n = int(sys.stdin.readline().strip())


def anotherRound(n):
    if (n - int(n)) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

if not n == 0:
    intCut = anotherRound(n * 0.15)
    listComment = []

    for i in range(n):
        listComment.append(int(sys.stdin.readline().strip()))

    listComment.sort()

    intSum = anotherRound(sum(listComment[intCut:n - intCut]) / (n - intCut * 2))

    print(intSum)

else:
    print(0)