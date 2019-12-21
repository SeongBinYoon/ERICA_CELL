import random

#숫자야구게임
def number_baseball():
    def get_random_number():
        return random.randrange(100, 1000)
    def is_digit(user_input_number):
        if user_input_number.isdigit() == True: 
            result = True
        else :
            result = False
        return result

    def is_between_100_and_999(user_input_number): 
        if (((user_input_number//100)<1) | ((user_input_number//1000)>=1)):
            result = False
        else:
            result = True
        return result 

    def is_duplicated_number(three_digit):
        temp1 = three_digit // 100
        temp2 = (three_digit - temp1 * 100) // 10
        temp3 = three_digit - temp1 * 100 - temp2 * 10

        if temp1 == temp2:
            result = True
        elif temp1 == temp3:
            result = True
        elif temp2 == temp3:
            result = True
        else:
            result = False
        return result

    def is_validated_number(user_input_number):
        valid_num = is_digit(user_input_number)
        temp = 0
        if valid_num == True:
            temp = int(user_input_number)
            if is_between_100_and_999(temp) == True:
                result = temp
                if is_duplicated_number(temp) == False:
                    temp = temp
                else:
                    print("0부터 9까지의 숫자를 한번씩만 사용해주세요.")
                    result = None

            else:
                print("조건에 맞게 숫자를 입력해주세요.")
                result = None
        else:
            print("은(는) 숫자가 아닙니다. 다시 입력해주세요.")
            result = None
        return result

    def get_not_duplicated_three_digit_number():
        result = None
        while 1:
            rnum = get_random_number()
            temp1 = rnum // 100
            temp2 = (rnum - temp1 * 100) // 10
            temp3 = rnum - temp1 * 100 - temp2 * 10
            if temp1 == temp2:
                result = None
            elif temp1 == temp3:
                result = None
            elif temp2 == temp3:
                result = None
            else:
                result = rnum
                break
        return result

    def get_strikes_or_ball(user_input_number, random_number):
        s = 0
        b = 0
        result = None
        if ((user_input_number == None)):                                       
            result = result 
        else:
            for i in range(0,3):
                for j in range(0,3):
                    if i == j:
                        if user_input_number[i] == random_number[j]:
                            s += 1
                    else:
                        if user_input_number[i] == random_number[j]:
                            b += 1
        s = str(s)
        b = str(b)
        result = ["strike = " +  s + ", ball = "+ b]
        result = ("".join(result))
        return '현 상황: ' + result

    def main():
        count = 1
        print("게임 성공시 당신에게 치료키트가 제공됩니다.")
        print("숫자맞추기 게임을 시작하겠습니다. 8회안에 못 맞출 시 실패입니다.")
        print()
        user_input = input("0부터 9까지의 숫자를 한 번씩만 사용하여 만든 세 자리 수를 입력해주세요. : ")
        random_number = str(get_not_duplicated_three_digit_number())
        valid_num = is_validated_number(user_input)
        str_valid_num = str(valid_num)
        if (valid_num == None):
            print("-the End-")
            return False
        else:
            print(get_strikes_or_ball(str_valid_num, random_number))
            while count != 8:                      
                new_user_input = input()
                new_valid_num = is_validated_number(new_user_input)
                new_str_valid_num = str(new_valid_num)
                get_strikes_or_ball(new_str_valid_num, random_number)
                result = get_strikes_or_ball(new_str_valid_num, random_number)
                print(result)
                count += 1
                if (new_str_valid_num == random_number):
                    print("숫자맞추기게임을 성공했습니다. 치료키트가 주어집니다.")
                    return True
                    break
            if count == 8:
                return False
        
    return main()


#스도쿠게임
def create_board(): #create_board() 함수 구현
    seed = [1,2,3,4,5,6]
    random.shuffle(seed)
    a = seed[0]
    b = seed[1]
    c = seed[2]
    d = seed[3]
    e = seed[4]
    f = seed[5]
    board = [[a, b, c, d, e, f], \
             [b, c, d, e, f ,a], \
             [c, d, e, f, a ,b], \
             [d, e, f, a ,b ,c], \
             [e, f, a, b, c, d], \
             [f, a, b, c, d, e]]
    return board

def transpose(board): #가로세로 바꾸기
    transposed = []
    for _ in range(len(board)):
        transposed.append([])
    count = 0
    for row in board:
        for column in row:
            transposed[count].append(column)
            count = count + 1
            if count >= len(row) :
                count = 0
    return transposed

def shuffle_ribbons(board) : 
    top_half = board[:2]
    random.shuffle(top_half)
    mid_half = board[2:4]
    random.shuffle(mid_half)
    bottom_half = board[4:]
    random.shuffle(bottom_half)
    return top_half + mid_half + bottom_half

def shuffle_ribbons_2(board) : 
    top_half = board[:3]
    random.shuffle(top_half)
    bottom_half = board[3:]
    random.shuffle(bottom_half)
    return top_half + bottom_half

def create_solution_board(): 
    board = create_board()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons_2(board)
    board = transpose(board)
    return board

def copy_board(board): 
    board_clone = []
    for row in board :
        row_clone = row[:]
        board_clone.append(row_clone)
    return board_clone

def get_level(): #레벨선택
    level = input("난이도 (상중하) 중에서 하나 선택하여 입력하세요: ")
    while level not in {"상", "중", "하"}:
         level = input("난이도 (상중하) 중에서 하나 선택하여 입력하세요: ")
    if level == "상":
        return 16
    elif level == "중":
        return 12
    elif level == "하":
        return 8

def make_holes(board,no_of_holes):
    holeset = []
    count = 0
    while count <= no_of_holes :
        i, j = random.randrange(0,5), random.randrange(0,5)
        if board[i][j] != 0 :
            board[i][j] = 0
            holeset.append((i,j))
            count += 1
    return (board, holeset)

def show_board(board): #퍼즐 게임보드 보여주기
    print()
    print('S','|','1','2','3','4','5','6')
    print('-','+','-','-','-','-','-','-')
    a = 1
    for row in board:
        print(a, '|', end=' ')
        for colunm in row :
            if colunm == 0 :
                print('.', end=' ')
            else :
                print(colunm, end=' ')
        a += 1
        print()

def get_integer(message,i,j): #수 입력받기
    number = input(message)
    while not (i <= int(number) <= j):
        number = input(message)
    return int(number)

def sudokmini_6(): 
    solution = create_solution_board()
    no_of_holes = get_level()
    puzzle = copy_board(solution)
    (puzzle,holeset) = make_holes(puzzle,no_of_holes)
    show_board(puzzle)
    while no_of_holes > 0:
        i = get_integer("가로줄번호(1~6): ",1,6) - 1
        j = get_integer("세로줄번호(1~6): ",1,6) - 1
        if (i,j) not in holeset:
            print("빈칸이 아닙니다.")
            continue
        sol = solution[i][j]
        n = get_integer("숫자(1~6): ",1,6)
        if n == sol:
            puzzle[i][j] = sol
            show_board(puzzle)
            holeset.remove((i,j))
            no_of_holes =  no_of_holes - 1
        else:
            print("답이 아닙니다. 치료키트를 얻지 못했으므로 당신은 사망했습니다.\n게임을 종료합니다.")
            exit(1)
    print("정답입니다. 치료키트가 제공됩니다.")

# 게임시작
def start():
    print("뉴스속보입니다. 현재 대한민국 전역에 일명 ‘좀비’ 바이러스라고 불리는 이상증세가 시민들 가운데서 급속도로 확산되고 있습니다.")
    print("긴급대피령이 내려진 상황에서 경찰과 군대는 진압을 시작하고 있지만,이미 감염자가 많이 퍼진 만큼 진압이 쉽지는 않아 보입니다.")
    print("국민 여러분께서는 집 밖 외출을 자제해 주시고, 기동대가 도착할 때까지 가까운 피난소 및 대피소에 몸을 숨겨주시기 바랍니다.")
    print("윤성빈 청와대 비상 대책 위원장에 의하면, 현재 안전 지역인 완도에서 이 사태의 해결책을 마련하고 있다는데요, 김현진 기자...")
    go_wando = input("게임을 시작하시겠습니까? 1 : 네 2 : 아니요 ")
    if go_wando == str(1):
        sudokmini_6()
    else:
        print("게임 종료")

def dice(): 
    dice = [1,2,3]
    random.shuffle(dice)
    return dice[0]
def fix():
    question = ['평소와 다른 tv소리에 불현듯 눈을 뜬 나.\n방금 들었던 내용이 꿈이길 바라며 채널을 돌린다. \n신호는 잡히지 않았고, 멀리서 폭발음과 함께 비명소리가 들리기 시작했다.\n나는 본능적으로 야구배트를 집어들었다.\n이 때, 이웃집에서 이상한 소리와 함께 누군가 집 문을 긁는다..\n“아, 아주머니 또 소음 때문에 괴롭히시려나. 나갈게요.”\n인터폰으로 밖을 본 순간 섬뜩한 기분이 들었다.\n 1. 문을 연다 2.문을 열지 않는다\n',
                '부엌의 식량을 확인했다.\n 며칠 못 버틸 것 같다.\n집을 나가 식량을 구해야 한다.\n 다행히 집 밖은 조용했고, 나갈 기회인 것 같다.\n대형마트로 갈까 아니면 편의점으로 갈까?\n1. 대형마트 2. 편의점\n',
                '이제 어떻게 해야 할지를 고민하다가, 뉴스에서 말한 안전 지역이 떠올랐다.\n나는 안전 지역인 완도로 향하기로 했다.\n어떤 수단을 이용하는 것이 가장 안전하고 빨리 도착할 수 있을까?\n 1. 버려진 차 2. 버려진 따릉이\n']

    answer = ['2',
              '2',
              '1']

    answerp = ['불안감은 적중했다. 분명 뉴스에 나온 그 증상이 틀림없었다.\n나는 조용히 문으로부터 떨어졌다.\n',
              '아무와도 마주치지 않고 편의점에 도착해 챙길 수 있는 모든 식량과 물품들을 챙겼다.\n',
              '버려진 차 답게 키가 그대로 꽂혀 있었다.\n“앗싸 개꿀~!키히히힛…!게헤헤헥…!”\n완도로 연결된 선착장을 향해 출발했다.\n']          

    wrong = ['아무 의심없이 문으로 다가가 문을 연다. \n야구 방망이를 휘둘렀지만 당신은 좀비로 변한 이웃집에게 공격당했다.\n치료를 하기 위해서는 미니게임을 통해 치료키트를 얻어야 한다.\n',
             '집 근처 마트로 들어가자마자 물렸다.\n치료를 하기 위해서는 미니게임을 통해 치료키트를 얻어야 한다.\n',
             '평소에도 잘 이용하고 있던 따릉이를 선택했다.\n그러나 얼마 가지 않아 좀비 떼를 마주쳤고, 그들은 내 예상보다 훨씬 빨랐다.\n이것이 바로 집단 근육인가…!\n결국 좀비 떼에게 잡혀버렸다.\n치료를 하기 위해서는 미니게임을 통해 치료키트를 얻어야 한다.\n']
    
    startbook = []
    for i in range(3):
        startbook.append({'question' : question[i] , 'answer' : answer[i] , 'answerp' : answerp[i] , 'wrong' : wrong[i]})
    return startbook

start()
