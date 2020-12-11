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

def main():
    # 입력받기
    word, n, direction = input("> ").split()
    # 에러처리
    try:
        n, direction = int(n), direction.upper()
    except:
        print("n의 값을 정수로 적어주세요(-100이상 99이하)")
        exit(0)
    length = len(word)

    # direction이 L혹은 R이 아니라면 에러처리
    if "L" != direction and "R" != direction:
        word = "direction값을 L혹은 R을 입력해주세요(소문자도 가능)"
    # n이 0이 아닌것들만 checkDirection함수를 통해 word값 다시 받아오기 0이라면 원모습 그대로 출력
    elif -100 <= n < 100:
        word = checkDirection(word, n, direction, length)
    else:
        word = "n의 값을 -100이상 99이하로 입력해주세요."
    
    print(word)

if __name__ == "__main__":
	main()