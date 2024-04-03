import sys

strInput = sys.stdin.readline().strip()

def isSpecial(string):
    length = len(string)
    if length == 1:
        return True
    elif length == 2:
        if string == "01":
            return True
        else:
            return False
    else:
        exit()

isSpecial("01")