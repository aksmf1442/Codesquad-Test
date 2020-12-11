def checkDirection(word, n, direction, length):
    pass

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