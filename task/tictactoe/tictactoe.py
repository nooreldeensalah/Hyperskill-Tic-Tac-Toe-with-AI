from random import randint

mapping_dict = {
    "1 1": "32",
    "2 1": "34",
    "3 1": "36",
    "1 2": "22",
    "2 2": "24",
    "3 2": "26",
    "1 3": "12",
    "2 3": "14",
    "3 3": "16",
    "0": "12",
    "1": "14",
    "2": "16",
    "3": "22",
    "4": "24",
    "5": "26",
    "6": "32",
    "7": "34",
    "8": "36",
}


def print_matrix(matrix_arg):
    copy_matrix = matrix_arg[:]
    for i in range(1, 4):
        copy_matrix[i] = "".join(copy_matrix[i])
    for line in copy_matrix:
        print(line)


def obtain_state():
    for symbol in ["X", "O"]:
        if (
            any(row.count(symbol) == 3 for row in all_rows)
            or (
                first_row[2] == symbol
                and second_row[4] == symbol
                and third_row[6] == symbol
            )
            or (
                first_row[6] == symbol
                and second_row[4] == symbol
                and third_row[2] == symbol
            )
            or any(all([row[i] == symbol for row in all_rows]) for i in range(2, 7, 2))
        ):
            print(f"{symbol} wins")
            return f"{symbol} wins"
    if all(row.count(" ") == 4 for row in all_rows):
        print("Draw")
        return "Draw"
    else:
        return "Game not finished"


def play_turn(player):
    global game_state
    if player["type"] == "user":
        while True:
            if game_state != "Game not finished":
                break
            user_move = input("Enter the coordinates: > ")
            if user_move == "exit":
                exit()
            if not all(
                element.isdigit() for element in user_move.split()
            ):  # Non-numerical input.
                print("You should enter numbers!")
                continue
            if not all(
                int(element) in range(1, 4) for element in user_move.split()
            ):  # Numbers are out of range
                print("Coordinates should be from 1 to 3!")
                continue
            row_user, col_user = int(mapping_dict[user_move][0]), int(
                mapping_dict[user_move][1]
            )
            if matrix[row_user][col_user].isalpha():  # Occupied Cell
                print("This cell is occupied! Choose another one!")
                continue
            matrix[row_user][col_user] = player["symbol"]
            print_matrix(matrix)
            game_state = obtain_state()
            break
    elif player["type"] == "medium":
        while True:
            if game_state != "Game not finished":
                break
            opponent_symbol = "X" if player["symbol"] == "O" else "O"
            row_altered = False
            for row in all_rows:
                if row.count(player["symbol"]) == 2 or row.count(opponent_symbol) == 2:
                    row_location = all_rows.index(row) + 1
                    col_location = None
                    col_location = [i for i in range(2, 7, 2) if not row[i].isalpha()]
                    if not col_location:
                        break
                    if not matrix[row_location][
                        col_location
                    ].isalpha():  # Occupied Cell
                        print(f'Making move level "{player["type"]}"')
                        matrix[row_location][col_location] = player["symbol"]
                        print_matrix(matrix)
                        game_state = obtain_state()
                        row_altered = True
            if row_altered:
                break
            if (
                first_row[2] == player["symbol"] and second_row[4] == player["symbol"]
            ) or (first_row[2] == opponent_symbol and second_row[4] == opponent_symbol):
                if not matrix[3][6].isalpha():  # Occupied Cell
                    print(f'Making move level "{player["type"]}"')
                    matrix[3][6] = player["symbol"]
                    print_matrix(matrix)
                    game_state = obtain_state()
                    break
            if (
                first_row[2] == player["symbol"] and third_row[6] == player["symbol"]
            ) or (first_row[2] == opponent_symbol and third_row[6] == opponent_symbol):
                if not matrix[2][4].isalpha():  # Occupied Cell
                    print(f'Making move level "{player["type"]}"')
                    matrix[2][4] = player["symbol"]
                    print_matrix(matrix)
                    game_state = obtain_state()
                    break
            if (
                second_row[4] == player["symbol"] and third_row[6] == player["symbol"]
            ) or (second_row[4] == opponent_symbol and third_row[6] == opponent_symbol):
                if not matrix[1][2].isalpha():  # Occupied Cell
                    print(f'Making move level "{player["type"]}"')
                    matrix[1][2] = player["symbol"]
                    print_matrix(matrix)
                    game_state = obtain_state()
                    break
            if (
                first_row[6] == player["symbol"] and second_row[4] == player["symbol"]
            ) or (first_row[6] == opponent_symbol and second_row[4] == opponent_symbol):
                if not matrix[3][2].isalpha():  # Occupied Cell
                    print(f'Making move level "{player["type"]}"')
                    matrix[3][2] = player["symbol"]
                    print_matrix(matrix)
                    game_state = obtain_state()
                    break
            if (
                first_row[6] == player["symbol"] and third_row[2] == player["symbol"]
            ) or (first_row[6] == opponent_symbol and third_row[2] == opponent_symbol):
                if not matrix[2][4].isalpha():  # Occupied Cell
                    print(f'Making move level "{player["type"]}"')
                    matrix[2][4] = player["symbol"]
                    print_matrix(matrix)
                    game_state = obtain_state()
                    break
            if (
                second_row[4] == player["symbol"] and third_row[2] == player["symbol"]
            ) or (second_row[4] == opponent_symbol and third_row[2] == opponent_symbol):
                if not matrix[1][6].isalpha():  # Occupied Cell
                    print(f'Making move level "{player["type"]}"')
                    matrix[1][6] = player["symbol"]
                    print_matrix(matrix)
                    game_state = obtain_state()
                    break
            columns = list(zip(first_row, second_row, third_row))
            columns = [columns[2], columns[4], columns[6]]
            column_altered = False
            for column in columns:
                if (
                    column.count(player["symbol"]) == 2
                    or column.count(opponent_symbol) == 2
                ):
                    column_location = columns.index(column) * 2 + 2
                    try:
                        row_location = column.index(" ") + 1
                    except ValueError:
                        continue
                    if not matrix[row_location][
                        column_location
                    ].isalpha():  # Occupied Cell
                        print(f'Making move level "{player["type"]}"')
                        matrix[row_location][column_location] = player["symbol"]
                        print_matrix(matrix)
                        game_state = obtain_state()
                        column_altered = True
            if column_altered:
                break
            computer_move = f"{randint(1, 3)} {randint(1, 3)}"
            row_computer, col_computer = int(mapping_dict[computer_move][0]), int(
                mapping_dict[computer_move][1]
            )
            if matrix[row_computer][col_computer].isalpha():  # Occupied Cell
                continue
            print(f'Making move level "{player["type"]}"')
            matrix[row_computer][col_computer] = player["symbol"]
            print_matrix(matrix)
            game_state = obtain_state()
            break
    elif player["type"] == "hard":
        if game_state == "Game not finished":
            opponent_symbol = "O" if player["symbol"] == "X" else "X"
            game_board = first_row[2:7:2] + second_row[2:7:2] + third_row[2:7:2]
            for index in range(len(game_board)):
                if not game_board[index].isalpha():
                    game_board[index] = index

            def winning(board, symbol):
                if (
                    (board[0] == symbol and board[1] == symbol and board[2] == symbol)
                    or (
                        board[3] == symbol and board[4] == symbol and board[5] == symbol
                    )
                    or (
                        board[6] == symbol and board[7] == symbol and board[8] == symbol
                    )
                    or (
                        board[0] == symbol and board[3] == symbol and board[6] == symbol
                    )
                    or (
                        board[1] == symbol and board[4] == symbol and board[7] == symbol
                    )
                    or (
                        board[2] == symbol and board[5] == symbol and board[8] == symbol
                    )
                    or (
                        board[0] == symbol and board[4] == symbol and board[8] == symbol
                    )
                    or (
                        board[2] == symbol and board[4] == symbol and board[6] == symbol
                    )
                ):
                    return True
                else:
                    return False

            def minimax(new_board, symbol):
                empty_indices = [
                    index
                    for index in range(len(new_board))
                    if not str(new_board[index]).isalpha()
                ]
                if winning(new_board, opponent_symbol):
                    return {"score": -10}
                elif winning(new_board, player["symbol"]):
                    return {"score": 10}
                elif not empty_indices:
                    return {"score": 0}
                moves = []
                for index in range(len(empty_indices)):
                    move = dict()
                    move["index"] = new_board[empty_indices[index]]
                    new_board[empty_indices[index]] = symbol
                    if symbol == player["symbol"]:
                        move["score"] = minimax(new_board, opponent_symbol)["score"]
                    else:
                        move["score"] = minimax(new_board, player["symbol"])["score"]
                    new_board[empty_indices[index]] = move["index"]
                    moves.append(move)
                if symbol == player["symbol"]:
                    best_score = float("-inf")
                    for ii in range(len(moves)):
                        if moves[ii]["score"] > best_score:
                            best_score = moves[ii]["score"]
                            best_move = ii
                else:
                    best_score = float("inf")
                    for ii in range(len(moves)):
                        if moves[ii]["score"] < best_score:
                            best_score = moves[ii]["score"]
                            best_move = ii
                return moves[best_move]

            move_index = str(minimax(game_board, player["symbol"])["index"])
            print(f'Making move level "{player["type"]}"')
            row_move, col_move = int(mapping_dict[move_index][0]), int(
                mapping_dict[move_index][1]
            )
            matrix[row_move][col_move] = player["symbol"]
            print_matrix(matrix)
            game_state = obtain_state()

    else:  # Easy
        while True:
            if game_state != "Game not finished":
                break
            computer_move = f"{randint(1, 3)} {randint(1, 3)}"
            row_computer, col_computer = int(mapping_dict[computer_move][0]), int(
                mapping_dict[computer_move][1]
            )
            if not matrix[row_computer][col_computer].isalpha():  # Occupied Cell
                print(f'Making move level "{player["type"]}"')
                matrix[row_computer][col_computer] = player["symbol"]
                print_matrix(matrix)
                game_state = obtain_state()
                break


while True:  # Validating input command
    input_command = input("Input command: >")
    if input_command == "exit":
        exit()
    if not input_command.startswith("start") or not len(input_command.split()) == 3:
        print("Bad parameters")
        continue
    empty_cells = " ".join("|   |")
    dashes = "---------"
    first_row = list(empty_cells)
    second_row = list(empty_cells)
    third_row = list(empty_cells)
    matrix = [dashes, first_row, second_row, third_row, dashes]
    all_rows = matrix[1:4]
    game_state = obtain_state()
    player_one = {"type": input_command.split()[1], "symbol": "X"}
    player_two = {"type": input_command.split()[2], "symbol": "O"}
    print_matrix(matrix)
    while game_state == "Game not finished":
        play_turn(player_one)
        play_turn(player_two)
