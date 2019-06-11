# import
import random


# Print the TicTacToe board
def print_board(b):
    print(b[0], b[1], b[2], sep=" | ")
    print(b[3], b[4], b[5], sep=" | ")
    print(b[6], b[7], b[8], sep=" | ")
    print("--------------------------")


def choose_side(first):
    if first == 1:
        return 'X', 'O'
    else:
        return 'O', 'X'


def move(board, loc, l):
    if isinstance(board[loc], int):
        board[loc] = l
        return True
    else:
        return False


def comp_move(board, letter):
    cp_board = board.copy()

    # check if computer can win
    check = check_possible_win(cp_board, letter[1])
    if check != -1:
        move(board, check, letter[1])
        return

    # check if the player can win. If can then block.
    check = check_possible_win(cp_board, letter[0])
    if check != -1:
        move(board, check, letter[1])
        return

    # check if corners or middle are free. If not then move random.
    if isinstance(board[4], int):
        move(board, 4, letter[1])
        return
    elif isinstance(board[0], int):
        move(board, 0, letter[1])
        return
    elif isinstance(board[2], int):
        move(board, 2, letter[1])
        return
    elif isinstance(board[6], int):
        move(board, 6, letter[1])
        return
    elif isinstance(board[8], int):
        move(board, 8, letter[1])
        return
    else:
        rand = random.randint(0, 9)
        while not (move(board, rand, letter[1])):
            rand = random.randint(0, 9)
        return


def check_possible_win(b, l):
    for i in range(9):
        if isinstance(b[i], int):
            b[i] = l
            if check_win(b, l):
                return i
            b[i] = i + 1
    return -1


# b is board, l is letter
def check_win(b, l):
    return ((b[0] == b[1] == b[2] == l) or
            (b[3] == b[4] == b[5]) or
            (b[6] == b[7] == b[8]) or
            (b[0] == b[3] == b[6]) or
            (b[1] == b[4] == b[7]) or
            (b[2] == b[5] == b[8]) or
            (b[0] == b[4] == b[8]) or
            (b[2] == b[4] == b[6]))


if __name__ == '__main__':
    while True:
        turn_counter = 0
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print("Welcome to TicTacTOe:")
        choose = input("Press X to go first, O to go second, any to random.\n")
        letter = tuple()
        if choose.lower() == 'x':
            letter = ('X', 'O')
        elif choose.lower() == 'O':
            letter = ('O', 'X')
        else:
            letter = choose_side(random.randint(0, 1))

        turn = 0
        if letter[0].lower() == 'x':
            turn = 0
        else:
            turn = 1

        start = True
        while start:
            if turn_counter > 8:
                print("It's a tie!")
                break
            if turn == 0:
                print_board(board)
                loc = input("Choose move location\n")
                while not move(board, int(loc, 10) - 1, letter[0]):
                    print("Invalid move!")
                    print_board(board)
                    loc = input("Choose move location")
                if check_win(board, letter[0]):
                    print_board(board)
                    print("Player wins!")
                    break
                print_board(board)
                turn = 1
            else:
                comp_move(board, letter)
                if check_win(board, letter[1]):
                    print_board(board)
                    print("Computer wins!")
                    break
                print_board(board)
                turn = 0

            turn_counter += 1




