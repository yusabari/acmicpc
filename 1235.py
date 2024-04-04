import sys

n = int(sys.stdin.readline().strip())
listStudent = []

for _ in range(n):
    listStudent.append(sys.stdin.readline().strip())

lenStudent = len(listStudent[0])

for i in range(lenStudent - 1, -1, -1):
    isDup = False
    setStudent = set()
    for student in listStudent:
        if student[i:lenStudent] in setStudent:
            isDup = True
            break
        else:
            setStudent.add(student[i:lenStudent])
    
    if not isDup:
        print(lenStudent - i)
        exit()