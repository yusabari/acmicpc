import sys

strInput = sys.stdin.readline().strip()
dictCard = {
    'P':set(),
    'K':set(),
    'H':set(),
    'T':set()
}

for i in range(0, len(strInput), 3):
    strCard = strInput[i:i+3]
    for chrFirst in dictCard.keys():
        if strCard.startswith(chrFirst):
            if strCard in dictCard[chrFirst]:
                print("GRESKA")
                exit()
            dictCard[chrFirst].add(strCard)

for j in dictCard.keys():
    print(13 - len(dictCard[j]), end=" ")