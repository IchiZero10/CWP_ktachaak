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
    # find king x y

    for i, j in enumerate(arr):
        finder = j.find("K")
        if finder != -1:
            king_y = i
            king_x = finder
            break
    # case Pawn

    if king_y + 1 < board_size and (
        (king_x - 1 >= 0 and arr[king_y + 1][king_x - 1] == "P")
        or (king_x + 1 < board_size and arr[king_y + 1][king_x + 1] == "P")
    ):
        print("Success")
        return
    # case horizontal and vertical (QR)
    for i in range(board_size):
        if arr[i][king_x] in "QR":
            step = 1 if i < king_y else -1
            for j in range(i + step, king_y, step):
                if arr[j][king_x] != ".":
                    print("Failed")
                    return
            print("Success")
            return
        elif arr[king_y][i] in "QR":
            step = 1 if i < king_x else -1
            for j in range(i+step,king_x,step):
                if arr[king_y][j] != ".":
                    print("Failed")
                    return     
            print("Success")      
            return
    # case diagonal (QB)
    for i in range(board_size):
        y = i + king_x - king_y
        if 0 <= y < board_size:
            if arr[i][y] in "QB":
                pointer = [y, i]
                while pointer[0] != king_x or pointer[1] != king_y:
                    if arr[pointer[1] + 1][pointer[0] + 1] != ".":
                        print("Failed")
                        return
                    pointer[0] += 1
                    pointer[1] += 1
                print("Success")
                return

        y = -i + king_x + king_y
        if 0 <= y < board_size:
            if arr[i][y] in "QB":
                pointer = [y, i]
                while pointer[0] != king_x or pointer[1] != king_y:
                    if arr[pointer[1] - 1][pointer[0] - 1] != ".":
                        print("Failed")
                        return
                    pointer[0] -= 1
                    pointer[1] -= 1
                print("Success")
                return

    print("Failed")
