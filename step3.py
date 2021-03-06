import copy, time, datetime, random

# 큐브의 한 면을 270도로 회전
def rotate270(cube):
    n = len(cube)
    candidate = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            candidate[n-1-y][x] = cube[x][y]
    return candidate

# 큐브의 한 면을 90도로 회전
def rotate90(cube):
    n = len(cube)
    candidate = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            candidate[y][n-1-x] = cube[x][y]
    return candidate

# U or U' 회전함수
def rotateU(cube, d):
    candidate = copy.deepcopy(cube)
    x, y = [2,3,4,1], [4,1,2,3]

    if d == "U":
        for idx in range(4):
            candidate[idx+1][0] = cube[x[idx]][0]
        candidate[0] = rotate90(cube[0])
    else:
        for idx in range(4):
            candidate[idx+1][0] = cube[y[idx]][0]
        candidate[0] = rotate270(cube[0])

    return candidate

# D or D 회전함수
def rotateD(cube, d):
    candidate = copy.deepcopy(cube)
    x, y =[2,3,4,1], [4,1,2,3]

    if d == "D":
        for idx in range(4):
            candidate[idx+1][2] = cube[y[idx]][2]
        candidate[5] = rotate90(cube[5])
    else:
        for idx in range(4):
            candidate[idx+1][2] = cube[x[idx]][2]
        candidate[5] = rotate270(cube[5])
    return candidate

# F or F' 회전함수 (3,5), (1,0) 연결할 때 반대로 넣어야해서 3-i-1을 사용
def rotateF(cube, d):
    candidate = copy.deepcopy(cube)
    if d == "F":
        for i in range(3):
            candidate[0][2][3-i-1] = cube[1][i][2]
            candidate[3][i][0] = cube[0][2][i]
            candidate[5][0][3-i-1] = cube[3][i][0]
            candidate[1][i][2] = cube[5][0][i]
        candidate[2] = rotate90(cube[2])
    else:
        for i in range(3):
            candidate[0][2][i] = cube[3][i][0]
            candidate[3][3-i-1][0] = cube[5][0][i]
            candidate[5][0][i] = cube[1][i][2]
            candidate[1][3-i-1][2] = cube[0][2][i]
        candidate[2] = rotate270(cube[2])
    return candidate

# B or B' 회전함수 (3,5), (1,0) 연결할 때 반대로 넣어야해서 3-i-1을 사용
def rotateB(cube, d):
    candidate = copy.deepcopy(cube)
    if d == "B":
        for i in range(3):
            candidate[0][0][i] = cube[3][i][2]
            candidate[3][3-i-1][2] = cube[5][2][i]
            candidate[5][2][i] = cube[1][i][0]
            candidate[1][3-i-1][0] = cube[0][0][i]
        candidate[4] = rotate90(cube[4])
    else:
        for i in range(3):
            candidate[0][0][3-i-1] = cube[1][i][0]
            candidate[3][i][2] = cube[0][0][i]
            candidate[5][2][3-i-1] = cube[3][i][2]
            candidate[1][i][0] = cube[5][2][i]
        candidate[4] = rotate270(cube[4])
            
    return candidate    

# R or R' 회전함수 (0,4), (4,5) 연결할 때 반대로 넣어야해서 3-i-1을 사용
def rotateR(cube, d):
    candidate = copy.deepcopy(cube)
    if d == "R":
        for i in range(3):
            candidate[0][i][2] = cube[2][i][2]
            candidate[4][3-i-1][0] = cube[0][i][2]
            candidate[5][3-i-1][2] = cube[4][i][0]
            candidate[2][i][2] = cube[5][i][2]
        candidate[3] = rotate90(cube[3])
    else:
        for i in range(3):
            candidate[0][3-i-1][2] = cube[4][i][0]
            candidate[4][3-i-1][0] = cube[5][i][2]
            candidate[5][i][2] = cube[2][i][2]
            candidate[2][i][2] = cube[0][i][2]
        candidate[3] = rotate270(cube[3])
    return candidate

# L or L' 회전함수 (0,4), (4,5) 연결할 때 반대로 넣어야해서 3-i-1을 사용
def rotateL(cube, d):
    candidate = copy.deepcopy(cube)
    if d == "L":
        for i in range(3):
            candidate[0][3-i-1][0] = cube[4][i][2]
            candidate[2][i][0] = cube[0][i][0]
            candidate[5][i][0] = cube[2][i][0]
            candidate[4][3-i-1][2] = cube[5][i][0]
        candidate[1] = rotate90(cube[1])
    else:
        for i in range(3):
            candidate[0][i][0] = cube[2][i][0]
            candidate[2][i][0] = cube[5][i][0]
            candidate[5][3-i-1][0] = cube[4][i][2]
            candidate[4][3-i-1][2] = cube[0][i][0]
        candidate[1] = rotate270(cube[1])
    return candidate

# direction출력 함수
def printDirection(cube, di):
    if di != di.upper():
        print("\n",di.upper()+"'")    
    else:
        print("\n",di)
    stateCube(cube)

# 큐브회전함수
def checkDirection(di, cube, count, value):
    for _ in range(value):
        if di in ("U","u"):
            cube = rotateU(cube, di)
        elif di in ("D","d"):
            cube = rotateD(cube, di)
        elif di in ("F","f"):
            cube = rotateF(cube, di)
        elif di in ("B","b"):
            cube = rotateB(cube, di)
        elif di in ("R","r"):
            cube = rotateR(cube, di)
        elif di in ("L","l"):
            cube = rotateL(cube, di)
        else:
            print("{}는 없는 조작법입니다!".format(di))
            continue
        count +=1
        printDirection(cube, di)
    return cube, count

# 방향과 숫자 분류하는 함수
def classifyDirection(cube, direction, count):
    for d in direction:
        value = 1
        if len(d) != 1:
            d, value = d[0], int(d[1])
        cube, count = checkDirection(d, cube, count, value)
        if count >= 1 and checkCube(cube):
            return cube, count
    return cube, count

# Replace함수를 이용하여 direction을 구현하기 편하게 바꾸기
def modifyDirection(direction):
    direction = direction.replace("U'","u")
    direction = direction.replace("D'","d")
    direction = direction.replace("R'","r")
    direction = direction.replace("L'","l")
    direction = direction.replace("F'","f")
    direction = direction.replace("B'","b")
    return direction

# direction을 리스트로 변환
def filterDirection(direction):
    candidate = []
    string = ""
    lst = ["U","u","D","d","F","f","B","b","R","r","L","l"]
    for d in direction:
        if  d == "2" and string:
            candidate.append(string+d)
            string = ""
        elif d == "2" and not string:
            candidate.append(d)
        elif d in lst and not string:
            string += d
        elif d in lst and string:
            candidate.append(string)
            string = d
        else:
            candidate.append(d)
    if string:
        candidate.append(string)
    return candidate

# 랜덤으로 돌릴 때 큐브가 맞춰지면 스탑시키는 함수 (2차원 배열을 1차원배열로 바꿔서 set한 후 길이가 1이 아니면 false리턴)
def checkCube(cube):
    for i in range(6):
        if len(set(sum(cube[i], []))) != 1:
            return False
    return True

# 변환된 cube, count값을 받아오고 direction을 입력받는 함수 (Q 입력시 종료)
def selectInput(cube):
    count = 0
    while True:
        direction = input("CUBE> ").upper()
        if direction == "Q":
            return count
        # direction에서 '가 포함된 값을 소문자로 변환
        direction = modifyDirection(direction)
        # direction을 숫자포함해서 리스트 형태로 변환
        direction = filterDirection(direction)
        cube, count = classifyDirection(cube, direction, count)
        if count >= 1 and checkCube(cube):
            return count

# 방향중 하나를 랜덤으로 골라서 큐브를 돌려주는 함수
def randomInput(cube):
    count = 0
    lst = ["U","U2","U'","D","D2","D'","F","F2","F'","B","B2","B'","R","R2","R'","L","L2","L'"]
    while True:
        # lst에서 랜덤으로 값 하나 추출
        direction = random.choice(lst)
        # direction에서 '가 포함된 값을 소문자로 변환
        direction = modifyDirection(direction)
        # direction을 숫자포함해서 리스트 형태로 변환
        direction = filterDirection(direction)
        cube, count = classifyDirection(cube, direction, count)
        if checkCube(cube):
            return count

# 결과출력함수
def printResult(count, start):
    seconds = time.time()- start
    minutes = str(datetime.timedelta(seconds=seconds)).split(".")[0][2:]
    print("경과시간 : {}".format(minutes))
    print("조작갯수: {}".format(count))
    print("이용해주셔서 감사합니다.😆")

# 현재 큐브 상태 출력
def stateCube(cube):
    [print("\t",' '.join(i)) for i in cube[0]]
    print()

    for j in range(3):
        for idx in range(1, 5):
            print(' '.join(cube[idx][j]), end="    ")
        print()
    print()

    [print("\t",' '.join(i)) for i in cube[5]]
    print()    

# 무작위로 섞을건지 직접 섞을건지 고르는 함수
def chooseRandomInput(cube, start):
    random = input("-둘 중 하나를 입력해주세요- || 무작위 섞기 : 1, 직접 입력받고 섞기 : 2 -> ")
    # 큐브 초기 상태 출력
    stateCube(cube)
    
    if random == "1":
        count = randomInput(cube)
        printResult(count, start)
    elif random == "2":
        print("Q입력시 프로그램이 종료됩니다!")
        count = selectInput(cube)
        printResult(count, start)
    else:
        print("잘못된 입력입니다. 1 혹은 2를 다시 입력해주세요!")
        main()

# 메인함수
def main():
    # 시작 시간
    start = time.time()
    cube = [[] for _ in range(6)]
    # 초기값 : B[0] = 윗면, W[1] = 왼쪽면, O[2] = 앞면, G[3] = 오른쪽면, Y[4] = 뒷면, R[5] = 아랫면
    # cube에 값 넣기
    for _ in range(3):
        cube[0].append(['B','B','B'])    
        cube[1].append(['W','W','W'])
        cube[2].append(['O','O','O'])
        cube[3].append(['G','G','G'])
        cube[4].append(['Y','Y','Y'])
        cube[5].append(['R','R','R'])

    # 무작위로 섞을건지 직접 섞을건지 고르기
    chooseRandomInput(cube, start)


if __name__ == "__main__":
	main()