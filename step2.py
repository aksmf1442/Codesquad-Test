import copy

def rotateU(cube, di):
    candidate = copy.deepcopy(cube)
    length = len(cube)
    if di == "U":
        for i in range(length):
            idx = (i-1)%length
            candidate[0][idx] = cube[0][i]
    else:
        for i in range(length):
            idx = (i+1)%length
            candidate[0][idx] = cube[0][i]
    return candidate

def rotateB(cube, di):
    candidate = copy.deepcopy(cube)
    length = len(cube)
    if di == "B":
        for i in range(length):
            idx = (i+1)%length
            candidate[2][idx] = cube[2][i]
    else:
        for i in range(length):
            idx = (i-1)%length
            candidate[2][idx] = cube[2][i]
    return candidate

def rotateR(cube, di):
    candidate = copy.deepcopy(cube)
    length = len(cube)
    if di == "R":
        for i in range(length):
            idx = (i-1)%length
            candidate[idx][2] = cube[i][2]
    else:
        for i in range(length):
            idx = (i+1)%length
            candidate[idx][2] = cube[i][2]
    return candidate

def rotateL(cube, di):
    candidate = copy.deepcopy(cube)
    length = len(cube)
    if di == "L":
        for i in range(length):
            idx = (i+1)%length
            candidate[idx][0] = cube[i][0]
    else:
        for i in range(length):
            idx = (i-1)%length
            candidate[idx][0] = cube[i][0]
    return candidate

# cube의 현재 상태를 나타내는 함수
def stateCube(cube, di):
    print()
    if di != di.upper():
        print(di.upper())    
    else:
        print(di)
    [print(" ".join(i)) for i in cube]
    print()

# 큐브 돌릴 방향을 확인하는 함수
def checkDirection(direction, cube):
    for di in direction:
        if di in ("U","u"):
            cube = rotateU(cube, di)
        elif di in ("R","r"):
            cube = rotateR(cube, di)
        elif di in ("L","l"):
            cube = rotateL(cube, di)
        elif di in ("B","b"):
            cube = rotateB(cube, di)
        else:
            print("{}는 없는 조작법입니다.".format(di))

        stateCube(cube, di)
    return cube

        
# direction을 반복문으로 돌리기 쉽게 '포함한 대문자를 소문자로 변경
def modifyDirection(direction):
    direction = direction.replace("U'","u")
    direction = direction.replace("R'","r")
    direction = direction.replace("L'","l")
    direction = direction.replace("B'","b")
    return direction

def main():
    cube = [["R","R","W"],["G","C","W"],["G","B","B"]]
    [print(" ".join(i)) for i in cube]
    print()

    # direction에 Q를 입력하면 멈추는 while문
    while True:
        direction = input("CUBE> ").upper()
        if direction == "Q":
            break
        # direction에서 '가 포함된 값을 소문자로 변환
        direction = modifyDirection(direction)
        
        # 한줄로 적힌 dkrection을 하나씩 실행
        for d in direction:
            cube = checkDirection(d, cube)

    print("Bye~")

if __name__ == "__main__":
	main()
