from checkmate import checkmate
import sys, io


def main():
    board = """\
    .Q
    .K\
    """
    

    checkmate(board)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            try:
                # เปิดและอ่านไฟล์
                with open(i, "r", encoding="utf-8") as file:
                    content = file.read()
                    checkmate(content)
            except FileNotFoundError:
                print(f"File not found {i}")
    else:
        main()
