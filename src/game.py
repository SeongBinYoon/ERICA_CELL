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
        game()
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


def rbook() :    
    question = ['한 여성이 좀비들에게 둘러 쌓여 있는 것 같다. 여성을 구할 지, 그냥 지나쳐 갈 지 고민하는 나. 나의 선택은? \n 1. 여성을 구한다 2. 그냥 지나간다\n',
                '어두운 밤, 식량이 부족하다는 것을 깨달았다. 마트에 가서 식량을 챙겨올까, 아니면 안전한 낮에 다른 곳을 찾아볼까? \n 1. 지금 식량을 챙겨온다 2. 그냥 지나친다\n',
                '근처까지만 태워달라고 부탁하는 식은땀을 흘리는 남자. 남자를 태워줘야 할까? \n 1. 태워준다 2. 거절한다\n',
                '귀여운 강아지를 발견했다. 나는 차를 세우고 강아지를 데려올 지 말 지 고민한다. 나의 선택은?\n 1. 데려온다 2. 그냥 지나친다\n',
                '산을 넘어가다 꽤 깨끗한 계곡을 발견했다. 씻지 않은 지 오래되어 찝찝하고 냄새가 나는데….잠깐만 물이라도 묻힐까?\n 1. 씻는다 2. 그냥 지나친다\n',
                '공기가 맑은 산 속을 통과하는 길. 몸이 찌뿌둥한데, 차를 잠깐 세워두고 스트레칭을 할까?\n 1.스트레칭을 한다 2. 그냥 간다\n',
                '차의 기름을 아끼기 위해 히터를 틀지 않고 가는 나.\n그런데 점점 더 추워지는 게, 기온이 영하로 떨어진 것 같다.\n이대로 가다간 동사할지도 모르겠다. 아까 찾아보니 차에 라이터가 있긴 한데….\n 1. 히터를 튼다 2. 원시적인 방법으로 불을 피워 몸을 녹인다\n ',
                '도로와 멀지 않은 곳에서 찾은 컨테이너 집. 집을 둘러보니 초코바 하나가 보인다. 먹을까?\n 1.초코바를 먹는다 2. 그냥 두고 간다\n',
                '야심한 밤, 전조등을 켜고 서행 운전을 하던 중, 한 남자가 히치하이킹 핸드사인을 보내온다.\n좀비는 아닌 것 같다. 그의 앞에 차량을 세우고 창문을 연다.\n그 순간 문을 열더니 총을 들이댄다. 무장한 강도는 차에서 내려 모든 것을 내놓으라고 한다.\n 1. 맞서 싸운다 2. 그냥 치고 지나친다',
                '고속도로를 달리던 중, 갑자기 배에서 신호가 온다. 위급한 상황이다.\n그런데 조금만 더 가면 휴게소가 나올 것 같다. 어떡하지?\n 1. 지금 내려서 해결한다 2. 휴게소 화장실에서 해결한다\n',
                '길가에 돈이 흩뿌려져 있다. 전부 5만원권이다. 자낳괴인 나는 일단 속도를 줄이고 살펴보기로 했다.\n“조금 분위기가 섬뜩하긴 한데 이 때 아니면 언제 저런 큰 돈을 만져보겠어?”\n 1.줍는다 2. 그냥 지나친다',
                '어린 아이가 길가에서 울고 있다. 길을 잃은 것 같다. 도와줄까?\n 1.도와준다 2. 그냥 지나간다\n',
                '앗. 기름이 거의 떨어져간다.\n마침 시야에 s사 주유소와 g사 주유소가 보인다.\n두 곳 다 인기척은 없는 듯 하다.\n 1.s사 2. g사\n']

    answer = ['1',
              '1',
              '2',
              '2',
              '2',
              '1',
              '1',
              '2',
              '2',
              '1',
              '2',
              '2',
              '1']

    answerp = ['차에 구비해둔 무기를 이용해 좀비를 물리쳤다. 여자는 감사인사를 하고는 치료용품을 나누어 준 후, 사라졌다.\n',
              '혹시 모르니 그나마 안전한 낮에 찾아보자. 다음날, 나는 무사히 식량을 찾고 다시 길을 떠났다.\n',
              '상태가 안 좋은 것을 보니, 감염자일 확률이 높은 것 같다. 마음에 걸리지만 일단 지나치자.\n',
              '뉴스에서 동물도 바이러스를 옮길 수 있는 매체가 된다고 했던 것 같다. 만일을 대비해 지나치자.\n',
              '이 상황에서 씻는건 사치이다. 하루빨리 선착장에 도착해야 한다.\n',
              '아니야... 느낌이 좋지 않아. 너무 주위가 조용한 것도 섬찟하다. 이제 조금만 가면 안전지대니 조금만 참자.\n',
              '“지금의 내 건강이 더 중요해!” 히터를 튼다. 따뜻하다. 나른한 느낌이 들며 기분이 좋아진다.\n',
              '유통기한이 지났을지도 몰라... 그냥 두고 가자.\n',
              '강도가 방심한 틈을 타 기어를 후진에 넣고 밟았다.\n강도는 중심을 잃고 넘어졌고, 나는 재빨리 기어를 바꾸어 강도에게로 돌진했다.\n외마디 비명과 함께 차가 흔들렸다. 분명 방금의 총소리로 ‘그들’이 모여들 것이다.\n나는 빠르게 차를 몰아 그 곳을 벗어났다.\n',
              '사람이 늘 북새통인 휴게소는 분명 난리가 났을 것이고, 도시와 다를 것 없을 것이다.\n차라리 갓길 옆 풀숲이 나을 것 같다. 차를 멈춰 세워 볼일을 해결했다.\n고속도로는 원래 사람의 통행이 적은 곳이라 다행이었다.\n',
              '지금이 어떤 상황인지 나는 잘 알고 있다.\n평소라면 돈에 환장해 막 주우러 다녔을 테지만, 지금 이 세상은 돈 따위 휴지조각일 뿐이다.\n미련이 남지 않게 속력을 더 내었다.\n',
              '험난한 세상에서 아이를 지나치기엔 너무 안타까웠지만 혹시 모를 상황이 있기에 속력을 더 내었다.\n차량은 선착장을 향해 달린다.\n',
              '다행히 아무도 기름을 훔쳐가지 않은 조용한 주유소였다. 무사히 차량에 주유를 마치고 다시 선착장을 향해 엑셀을 밟았다.\n']

    wrong = ['여성이 좀비로 변해 차를 향해 돌진한다. 미니게임을 통해 그 장소를 벗어나야 살아 남을 수 있다.\n',
             '다음 날, 작은 마트를 발견하여 식량을 챙기러 들어간 순간 물품창고에 숨어있던 좀비가 나타났다. 미니게임을 통해 마트에 걸려있는 망치를 이용해 좀비를 죽여야만 살아남을 수 있다.\n',
             '갑자기 남자가 좀비로 변했다. 미니게임을 통해 좀비를 방망이로 죽여야 당신은 살아남을 수 있다.\n',
             '좀비바이러스 보균자인 강아지에게 물리면 당신은 좀비가 된다. 미니게임을 통해 강아지를 잡아 차 밖으로 내쫓아야 살아남을 수 있다.\n',
             '개운하게 몸을 씻고 난 뒤 다시 출발하는데 뭔가 몸이 이상했다.\n가렵고 점점 붉게 변하더니 고통스러웠다. 분명 계곡물에 뭔가가 있었을 것이다.\n치료를 하기 위해서는 미니게임을 통해 치료키트를 얻어야 한다. \n',
             '갑자기 다리에 쥐가 나 절벽에서 떨어졌다. 미니게임을 통해 나뭇가지를 잡고 올라가야만 한다.\n',  
             '“마침 차에 버릴만한 쓰레기들이 있는데 잘 타겠다.”\n나는 잠시 차에서 내린 후 쓰레기를 한데 모아 불을 붙였다. 따뜻하다.\n그러나 불을 보고 몰려든 ‘그들’에게 공격당하고 말았다.\n치료를 하기 위해서는 미니게임을 통해 치료키트를 얻어야 한다.\n',
             '격렬한 복통과 함께 식중독에 걸렸다. 미니게임을 통해 약통에 있는 식중독약을 복용해야 살아남을 수 있다.\n',
             '강도와 나 사이에 몸싸움이 벌어졌고, 나는 차에서 굴러떨어졌다.\n큰 소리와 함께 나는 눈앞이 희미해졌다.\n치료를 하기 위해서는 미니게임을 통해 치료키트를 얻어야 한다.\n',
             '급할수록 돌아가라고 했다. 차량은 휴게소로 진입했고, 차를 주차했다. 화장실에 들어가 볼일을 보았다.\n그 때, 발자국 소리가 난다. 사람인가…? 불규칙한 발자국 소리.\n칸막이 위에서 그들이 내려다보고 있었다.\n탈출하기 위해서는 미니게임을 통해 생존능력을 얻어야 한다.\n',
             '차를 멈춰세우고 주변을 살폈다. 도랑에 현금수송차량이 쳐박혀 있었다. 분명 싣고 가던 지폐들임에 틀림없었다.\n“이 세상이 바로 세워지면 난 부자다..!”\n나는 5만원권을 주머니에 구겨넣고 차에 올라탔다. 시동을 건 순간 뒤로 그림자가 드리운다.\n“누구... 으아악!”\n살아남기 위해서는 미니게임을 통해 생존능력을 얻어야 한다.\n',
             '차를 멈춰세우고 내렸다. 아이를 불러보았지만 미동이 없다.\n“얘, 괜찮니?”\n순간, 아이가 뻗은 내 손을 물었다. 생존자가 아니었다. 울음소리는 환청인가..\n치료를 하기 위해서는 미니게임을 통해 치료키트를 얻어야 한다.\n',
             '주유를 시도했지만 기름이 한 칸도 채워지지 않는다. 누군가 싸그리 훔쳐간 듯 하다.\n그 때, 큰 소리가 났고, 나는 그대로 쓰러졌다. 눈 앞이 희미해져 가는 가운데 사람들의 말소리가 들린다.\n“좋아..포식하겠군. 옮겨.”\n탈출을 하기 위해서는 미니게임을 통해 탈출키트를 얻어야 한다. \n']

    randombook = []
    for i in range(len(question)):
        randombook.append({'question' : question[i] , 'answer' : answer[i] , 'answerp' : answerp[i], 'wrong' : wrong[i]})
    random.shuffle(randombook)
    return randombook

def game():
    i = 1
    playtime = 0 # 주사위 굴린 횟수 저장하는 변수
    startcheck=0 #startbook 인덱스에 접근하기 위한 변수
    randomcheck=0 #randombook 인덱스에 접근하기 위한 변수
    print()
    print("좀비 게임을 시작한 당신, 20번째 칸보다 많이 가게 되면 완도에 있는 안전지대에 도착하게 됩니다.")
    randombook=rbook()
    while i <= 20 :
        print("당신은 현재 "+str(i)+"번째 칸에 있습니다. 반주사위를 굴리겠습니다.")
        a = dice()
        playtime+=1 # 주사위 굴린 횟수 ++
        i += a
        print('주사위 값 :',end='')
        print(a)
        print()

        startbook=fix()
        if playtime<=3:
            user_answer = input(startbook[startcheck]['question'])
            if user_answer == startbook[startcheck]['answer']:
                print(startbook[startcheck]['answerp'])
                startcheck+=1
                b=True
            else:
                print(startbook[startcheck]['wrong'])
                startcheck+=1
                b=False
        elif 4<=playtime<=20:
            user_answer = input(randombook[randomcheck]['question'])
            if user_answer == randombook[randomcheck]['answer']:
                print(randombook[randomcheck]['answerp'])
                randomcheck+=1
                b=True
            else:
                print(randombook[randomcheck]['wrong'])
                randomcheck+=1
                b=False

        if b == False:
            c = number_baseball() # 숫자야구게임과 스도쿠 랜덤 배정
            if c == False:
                break
    if i <= 20:
        print("당신은 사망했습니다.")
    else:
        print("당신은 20번째 칸을 넘어 안전지대에 도착했습니다.")
        print()
        print("당신은 완도에 있는 생존자 캠프에 도착했습니다. ")
        print("축하합니다. 게임을 이겼습니다.")


start()

