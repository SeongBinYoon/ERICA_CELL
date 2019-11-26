input("")
print("Welcome To Our Cell Game!")
print("Press ANY KEY To Start Game!")
input("")
board = [["■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■"],
         ["■                            ■"],
         ["■                            ■"],
         ["■                            ■"],
         ["■                            ■"],
         ["■                            ■"],
         ["■                            ■"],
         ["■                            ■"],
         ["■                            ■"],
         ["■                            ■"],
         ["■                            ■"],
         ["■                            ■"],
         ["■                            ■"],
         ["■                            ■"],
         ["■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■"]]

def show_board(board):
    for row in board:
        s = ''
        for col in row:
            s += str(col)
            s += ' '
        print(s)

show_board(board)
