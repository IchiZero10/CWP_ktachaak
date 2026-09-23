def checkmate(board: str):
    # find king and turn to list
    king_x, king_y = -1, -1
    arr = [i.strip() for i in board.splitlines()]
    board_size = len(arr)
    king_counter = sum(i.count("K") for i in arr)
    if any(len(row) != board_size for row in arr):
        print("Board is not square")
        return
    if not king_counter:
        print("King not found")
        return
    elif king_counter > 1:
        print("Multiple King Found")
        return

    for i, j in enumerate(arr):
        finder = j.find("K")
        if finder != -1:
            king_y = i
            king_x = finder
            break
    # case Pawn
    # X.X
    # .P.
    if king_y + 1 < board_size and (
        (king_x - 1 >= 0 and arr[king_y + 1][king_x - 1] == "P")
        or (king_x + 1 < board_size and arr[king_y + 1][king_x + 1] == "P")
    ):
        print("Success")
        return
    # horizontal and vertical (Queen and Rook)
    for i in range(board_size):
        if arr[i][king_x] in "QR" or arr[king_y][i] in "QR":
            print("Success")
            return
    # diagonal
    for i in range(board_size):
        if i + king_y - king_x < board_size:
            if arr[i][i + king_y - king_x] in "QB":
                print("Success")
                return

        if -i + king_y + king_x < board_size:
            if arr[i][-i + king_y + king_x] in "QB":
                print("Success")
                return
    print("Failed")
