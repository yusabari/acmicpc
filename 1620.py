import sys

n, m = map(int,sys.stdin.readline().strip().split())

dictPokemon = dict()

for i in range(1, n + 1):
    dictPokemon[i] = sys.stdin.readline().strip()

for _ in range(m):
    strInput = sys.stdin.readline().strip()
    if strInput.isdigit():
        print(dictPokemon[int(strInput)])
    else:
        for key, value in dictPokemon.items():
            if value == strInput:
                print(value)
                break