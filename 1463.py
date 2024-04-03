import sys

n = int(sys.stdin.readline())

travel = [n]
visited = set()
count = 0

while not 1 in travel:
    current = set()
    for t in travel:
        visited.add(t)
        if t % 3 == 0 and not t % 3 in visited:
            current.add(t // 3)
        if t % 2 == 0 and not t % 2 in visited:
            current.add(t // 2)
        current.add(t - 1)

    travel = list(current)
    count += 1

print(count)