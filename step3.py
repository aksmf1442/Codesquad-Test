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