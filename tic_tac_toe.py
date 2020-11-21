# DEFINE EMPTY BOARD
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# CHECK IF STILL GAME GOING
game_still_going = True

# CHECK WINNER
winner = None

# CHECK PLAYER
current_player = 'X'


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def play_game():
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(f"{winner} won!!!.")
    elif winner == None:
        print("Tie.")


def handle_turn(player):
    print(f"{player}'s turn!.")
    location = input("Enter the position from (1-9):")

    valid = False
    while not valid:
        while location not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            location = input("Choose valid position from (1-9)")
        location = int(location) - 1

        if board[location] == "-":
            valid = True
        else:
            print("You cannot go there")

    board[location] = player
    display_board()


def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return


def check_if_game_over():
    check_if_win()
    check_if_tie()
    return


def check_if_win():
    global winner
    # CHECK ROWS
    row_winner = check_rows()
    # CHECK COLUMNS
    column_winner = check_columns()
    # CHECK DIAGONALS
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    # SET UP GLOBAL VARIABLE
    global game_still_going
    # CHECK IF THE ROWS HAVE EQUAL VALUE AND NOT EMPTY
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # IF ANY ROW HAS A MATCH THAN FLAG IT AS A WIN
    if row_1 or row_2 or row_3:
        game_still_going = False

    # RETURN WINNER 'X' OR 'O'
    if row_1:
        return board[0]
    elif row_2:
        return board[4]
    elif row_3:
        return
    return


def check_columns():
    # SET UP GLOBAL VARIABLE
    global game_still_going
    # CHECK IF THE COLUMNS HAVE EQUAL VALUE AND NOT EMPTY
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # IF ANY column HAS A MATCH THAN FLAG IT AS A WIN
    if column_1 or column_2 or column_3:
        game_still_going = False

    # RETURN WINNER 'X' OR 'O'
    if column_1:
        return board[0]
    elif column_2:
        return board[4]
    elif column_3:
        return board[5]
    return


def check_diagonals():
    # SET UP GLOBAL VARIABLE
    global game_still_going
    # CHECK IF THE ROWS HAVE EQUAL VALUE AND NOT EMPTY
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    # IF ANY diagonal HAS A MATCH THAN FLAG IT AS A WIN
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # RETURN WINNER 'X' OR 'O'
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


play_game()
