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
<<<<<<< HEAD
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
