print("tic tac toe game.")

def draw_board(draw_list):
    print("tec tac teo game")
    print("\t~~~~~~~~~~~~~~~~~~")
    print("\t||", draw_list[0] , "||" ,  draw_list[1] , "||", draw_list[2] , "||")
    print("\t~~~~~~~~~~~~~~~~~~")
    print("\t||", draw_list[3] , "||" , draw_list[4] , "||", draw_list[5] , "||")
    print("\t~~~~~~~~~~~~~~~~~~")
    print("\t||", draw_list[6] , "||" , draw_list[7] , "||", draw_list[8] , "||")
    print("\t~~~~~~~~~~~~~~~~~~")

def get_player_input(player_char, char_list):
    while True:
        player_move = int(input(player_char + ": enter your spot by the numbers from 1 to 9 : "))
        if player_move > 0 and player_move < 10:
            if char_list[player_move - 1] == "_":
                return player_move
            else:
                print("this spot already chosen , try again.")

        else:
            print("this is not in the board, try again.")

def place_player_char(player_char , player_move , char_list):
    char_list[player_move - 1] = player_char


def winner(pC , cL):
        return (( cL[0] == pC and cL[1] == pC and cL[2] == pC) or
            ( cL[3] == pC and cL[4] == pC and cL[5] == pC) or
            ( cL[6] == pC and cL[7] == pC and cL[8] == pC) or
            ( cL[0] == pC and cL[3] == pC and cL[6] == pC) or
            ( cL[1] == pC and cL[4] == pC and cL[7] == pC) or
            ( cL[2] == pC and cL[5] == pC and cL[8] == pC) or 
            ( cL[0] == pC and cL[4] == pC and cL[8] == pC) or 
            ( cL[2] == pC and cL[4] == pC and cL[6] == pC))

player1 = "x"
player2 = "o"
c_list = ["_"]*9
n_list = ["1","2","3","4","5","6","7","8","9"]

draw_board(n_list)
draw_board(c_list)
while True:
    #player1 turn 
    move = get_player_input(player1, c_list)
    place_player_char(player1,move, c_list)
    if winner(player1, c_list):
        print("player1 is the winner.")
        break

    elif "_" not in c_list:
        print("the game was tie!")
        break
    draw_board(n_list)
    draw_board(c_list)
    
    #player2 turn
    move2 = get_player_input(player2, c_list)
    place_player_char(player2, move2, c_list)
    if winner(player2, c_list):
        print("player2 is the winner.")
        break
    elif "_" not in c_list:
        print("the game was tie!")
        break

    draw_board(n_list)
    draw_board(c_list)