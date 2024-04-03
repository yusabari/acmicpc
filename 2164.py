import sys
from collections import deque

n = int(sys.stdin.readline().strip())

dequeCards = deque([i for i in range(1, n + 1)])

while (not len(dequeCards) == 1):
    dequeCards.popleft()
    dequeCards.append(dequeCards.popleft())

print(dequeCards[0])