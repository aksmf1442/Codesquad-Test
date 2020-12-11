def rotateU(cube, di):
    pass

def rotateR(cube, di):
    pass

def rotateL(cube, di):
    pass

def rotateB(cube, di):
    pass

# cube의 현재 상태를 나타내는 함수
def stateCube(cube, di):
    print()
    if di != di.upper():
        print(di.upper())    
    else:
        print(di)
    [print(" ".join(i)) for i in cube]
    print()

# direction을 확인하는 함수
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
