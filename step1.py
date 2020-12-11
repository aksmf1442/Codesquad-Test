# direction이 l일때 함수
def rotateL(word, n, length):
    candidate = ["" for _ in range(length)]
    for i in range(length):
        idx = (i+n)%length
        candidate[i] = word[idx]
    return "".join(candidate)

# direction이 r일때 함수
def rotateR(word, n, length):
    candidate = ["" for _ in range(length)]
    for i in range(length):
        idx = (i-n)%length
        candidate[i] = word[idx]
    return "".join(candidate)

# direction이 l인지 r인지 확인하고 l이면 lDirection에서 r이면 rDirection에서 값 가져오기
def checkDirection(word, n, direction, length):
    if direction == "L":
        return rotateL(word, n, length)
    elif direction == "R":
        return rotateR(word, n, length)
    else:
        return "잘못된 입력입니다."

def main():
    # 입력받기
    word, n, direction = input("> ").split()
    # 에러처리
    try:
        n, direction = int(n), direction.upper()
    except:
        return "잘못된 입력입니다."
    length = len(word)

    # direction이 L혹은 R이 아니라면 에러처리
    if "L" != direction and "R" != direction:
        word = "잘못된 입력입니다."
    # n이 0이 아닌것들만 checkDirection함수를 통해 word값 다시 받아오기 0이라면 원모습 그대로 출력
    elif n != 0:
        word = checkDirection(word, n, direction, length)
    return word

if __name__ == "__main__":
	print(main())