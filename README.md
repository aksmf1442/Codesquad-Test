# Codesquad-Test
코드스쿼드 마스터즈 테스트 제출용

-----------------------
## Step1 단어 밀어내기 구현

### Step1 요구사항
1. 입력: 사용자로부터 단어 하나, 정수 숫자 하나( -100 <= N < 100) , L 또는 R을 입력받는다. L 또는 R은 대소문자 모두 입력 가능하다.
2. 주어진 단어를 L이면 주어진 숫자 갯수만큼 왼쪽으로, R이면 오른쪽으로 밀어낸다.
3. 밀려나간 단어는 반대쪽으로 채워진다. 
4. 컴파일 및 실행되지 않을 경우 불합격
5. 자기만의 기준으로 최대한 간결하게 코드를 작성한다.

### 입력 받는 값
word : 단어 입력 받음
n : -100 <= n <100의 값을 입력 받음
direction : L 혹은 R을 입력 받음(소문자도 가능)

### main()
1. word, n, direction을 입력받고, 편의상 direction을 upper()를 사용해서 소문자로 입력 받아도 대문자로 변경해준다.
2. n이 숫자가 아니고 n의 값이 -100이상 99이하가 아니며, direciton이 L이나 R이 아닌것을 에러처리 해준다.
3. 결과를 출력해줌.

### checkDirection()
1. direction이 L인지 R인지 확인함.
2. 확인한 direction이 L이면 rotateL()에서 R이면 rotateR()에서 값을 받아옴.

### rotateL()
1. word를 왼쪽으로 밀어줌.

### rotateR()
1. word를 오른쪽으로 밀어줌.
-----------------------
## Step2: 평면 큐브 구현하기

### Step2 요구사항
1. 처음 시작하면 초기 상태를 출력한다.
2. 간단한 프롬프트 (CLI에서 키보드 입력받기 전에 표시해주는 간단한 글자들 - 예: CUBE> )를 표시해 준다.
3. 한 번에 여러 문자를 입력받은 경우 순서대로 처리해서 매 과정을 화면에 출력한다.
4. 너무 크지 않은 함수 단위로 구현하려고 노력할 것
5. 전역변수의 사용을 자제할 것
6. 객체와 배열을 적절히 활용할 것

### 입력 받는 값
direction : 큐브 돌릴 방향을 1개이상 입력 받음.

### main()
1. 큐브의 초기상태를 출력해준다.
2. direction에 Q를 입력하기 전까지 계속 입력받을 수 있게 해준다.

### modifyDirection()
1. 구현하는데 있어서 편의를 위해 '가 포함된 문자를 소문자로 변경해준다.

### checkDirection()
1. 큐브 돌릴 방향을 확인해준다.

### stateCube()
1. cube의 현재 상태를 나타내준다.

### rotateU()
1. 방향을 확인하고 대문자 U라면 평면큐브에서 가장 윗줄을 왼쪽으로 한 칸 밀어준다.
2. 방향을 확인하고 소문자 u라면 평면큐브에서 가장 윗줄을 오른쪽으로 한 칸 밀어준다.

### rotateB()
1. 방향을 확인하고 대문자 B라면 평면큐브에서 가장 아랫줄을 오른쪽으로 한 칸 밀어준다.
2. 방향을 확인하고 소문자 b라면 평면큐브에서 가장 아랫줄을 쪽으로 한 칸 밀어준다.

### rotateR()
1. 방향을 확인하고 대문자 R이라면 평면큐브에서 가장 오른쪽 줄을 위쪽으로 한 칸 밀어준다.
2. 방향을 확인하고 소문자 b이라면 평면큐브에서 가장 오른쪽 줄을 아래로 한 칸 밀어준다.

### rotateL()
1. 방향을 확인하고 대문자 L이라면 평면큐브에서 가장 왼쪽 줄을 아래로 한 칸 밀어준다.
2. 방향을 확인하고 소문자 L이라면 평면큐브에서 가장 왼쪽 줄을 위쪽으로 한 칸 밀어준다.

-----------------------
## Step3: 루빅스 큐브 구현하기

### Step3 요구사항
1. 큐브는 W, B, G, Y, O, R의 6가지 색깔을 가지고 있다.
2. 입력: 각 조작법을 한 줄로 입력받는다.
3. 출력: 큐브의 6면을 펼친 상태로 출력한다.
4. Q를 입력받으면 프로그램을 종료하고, 조작 받은 명령의 갯수를 출력시킨다.
5. 가능한 한 커밋을 자주 하고 구현의 의미가 명확하게 전달되도록 커밋 메시지를 작성할 것
6. 함수나 메소드는 한 번에 한 가지 일을 하고 가능하면 20줄이 넘지 않도록 구현한다.
7. 함수나 메소드의 들여쓰기를 가능하면 적게(3단계까지만) 할 수 있도록 노력해 본다.


### 추가 구현 기능
1. 프로그램 종료 시 경과 시간 출력
2. 큐브의 무작위 섞기 기능
3. 모든 면을 맞추면 축하 메시지와 함께 프로그램을 자동 종료

# 초기 큐브 상태
         B B B
         B B B
         B B B

W W W    O O O    G G G    Y Y Y    
W W W    O O O    G G G    Y Y Y    
W W W    O O O    G G G    Y Y Y    

         R R R
         R R R
         R R R

-> B[0]:윗면, W[1]:왼쪽면, O[2]:앞쪽면, G[3]:오른쪽면, Y[4]:뒷쪽면, R[5]:아랫면

### 입력 받는 값
random : 1 or 2를 입력받아서 1이면 랜덤으로 2면 직접 입력해서 큐브를 돌릴 수 있게 하는 변수
direction : 큐브를 어느 방향으로 돌릴지 입력

### main()
1. 초기의 큐브 값을 넣어주고 시작 시간을 기록해준다.

### chooseRandomInput()
1. random값을 입력 받고, 1이면 랜덤으로 큐브를 돌리고, 2면 direciton을 직접 입력하여 큐브를 돌릴 수 있게한다.
2. random값이 1이나 2가 아니라면 에러 처리해주고 다시 입력하게 해준다.

### stateCube()
1. 현재 큐브의 상태가 어떤지 확인 할 수 있게 한다.

### printResult()
1. 결과출력 함수이며, 시작할 때 저장해두었던 시간을 끝나는 시간과 비교해서 경과시간을 출력한다.
2. 큐브를 돌린 횟수를 출력해주고, 축하 메시지를 출력해준다.

### randomInput()
1. chooseInput함수에서 1을 입력받는다면 이곳으로 와서 랜덤으로 방향을 하나 뽑은 다음 큐브가 맞춰질때까지 돌아가게 한다.
2. 무작위가 조건이라서 그대로 구현하였지만 무작위로 큐브를 들리면 안 맞춰질 확률이 높아서 계속 돌아갈 수도 있다.

### selectInput()
1. chooseInput함수에서 2를 입력받는다면 이것으로 와서 direction변수값을 입력하고 그에 따라서 큐브를 돌릴 수 있게 한다.
2. Q를 입력 받거나 큐브가 맞춰지면 멈추고, 그렇지 않으면 계속 입력 받는다.

### checkCube()
1. 큐브를 한 면씩 확인하면서 한 면의 2차원 배열을 1차원 배열로 변환시키고 그 1차원 배열의 값이 모두 같으면 통과시킨다.
2. 통과하지 못하면 False를 리턴하고 통과하면 True를 리턴한다.

### filterDirection()
1. direction값을 리스트로 변환해준다.
2. 리스트로 변환하는 과정에서 큐브를 돌리는 기호에 없는 문자열이 있다면 리스트에 따로 리스트에 넣어주고 나중에 에러처리를 해준다.

### modifyDirection()
1. 구현하는데 있어 편의를 위해 '가 포함된 direction을 replace를 통해 소문자로 바꾼다.

### classifyDirection()
1. 방향과 숫자를 분류해서 문자뒤에 2가 붙어있다면 큐브를 두 번 돌아갈 수 있게 해준다.

### checkDirection()
1. direction 값에 따라서 rotate할 수 있게 해준다.
2. 큐브 돌리는 기호에 없는 문자열이라면 따로 에러 처리를 해준다.

### printDirection()
1. 지금 큐브를 돌리는 방향이 무엇인지를 출력해준다.

### rotateL()
1. direction값이 L이라면 큐브의 왼쪽을 시계방향으로 돌려준다.
2. direction값이 L'이라면 큐브의 왼쪽을 반시계방향으로 돌려준다.
3. 하지만 이 함수에서는 옆 모서리를 돌려주고 다른 함수에서 앞 면를 돌린다.

### rotateR()
1. direction값이 R이라면 큐브의 오른쪽을 시계방향으로 돌려준다.
2. direction값이 R'이라면 큐브의 오른쪽을 반시계방향으로 돌려준다.
3. 하지만 이 함수에서는 옆 모서리를 돌려주고 다른 함수에서 앞 면를 돌린다.

### rotateB()
1. direction값이 B이라면 큐브의 뒷쪽을 시계방향으로 돌려준다.
2. direction값이 B'이라면 큐브의 뒷쪽을 반시계방향으로 돌려준다.
3. 하지만 이 함수에서는 옆 모서리를 돌려주고 다른 함수에서 앞 면를 돌린다.

### rotateF()
1. direction값이 F이라면 큐브의 앞쪽을 시계방향으로 돌려준다.
2. direction값이 F'이라면 큐브의 앞쪽을 반시계방향으로 돌려준다.
3. 하지만 이 함수에서는 옆 모서리를 돌려주고 다른 함수에서 앞 면를 돌린다.

### rotateD()
1. direction값이 D이라면 큐브의 아래쪽을 시계방향으로 돌려준다.
2. direction값이 D'이라면 큐브의 아래쪽을 반시계방향으로 돌려준다.
3. 하지만 이 함수에서는 옆 모서리를 돌려주고 다른 함수에서 앞 면를 돌린다.

### rotateU()
1. direction값이 U이라면 큐브의 뒷쪽을 시계방향으로 돌려준다.
2. direction값이 U'이라면 큐브의 뒷쪽을 반시계방향으로 돌려준다.
3. 하지만 이 함수에서는 옆 모서리를 돌려주고 다른 함수에서 앞 면를 돌린다.

### rotate90()
1. 큐브의 앞쪽 면을 시계방향으로 돌려준다.

### rotate270()
1. 큐브의 앞쪽 면을 반시계방향으로 돌려준다.

## 기억하고 싶은 것
- vscode 터미널에서는 코드가 작동 되었는데 맥 터미널에서는 왜 안됬나? 
-> 바보같이 python으로 실행하려고 했었다. 다음부터는 python3로 작동하자.=

-----------------------