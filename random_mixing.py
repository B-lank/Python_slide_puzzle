import random


def mix(puzzle, difficulty):
    for _ in range(100000):
        i = random.randint(0, difficulty-1)
        j = random.randint(0, difficulty-1)
        if i == 0:  # 퍼즐 위쪽
            if j == 0:  # 퍼즐 왼쪽 위
                if puzzle[i][j + 1] == 0:
                    change(puzzle, i, j, i, j + 1)
                elif puzzle[i + 1][j] == 0:
                    change(puzzle, i, j, i + 1, j)
            elif j == difficulty-1:  # 퍼즐 오른쪽 위
                if puzzle[i][j - 1] == 0:
                    change(puzzle, i, j, i, j - 1)
                elif puzzle[i + 1][j] == 0:
                    change(puzzle, i, j, i + 1, j)
            else:
                if puzzle[i][j - 1] == 0:
                    change(puzzle, i, j, i, j - 1)
                elif puzzle[i][j + 1] == 0:
                    change(puzzle, i, j, i, j + 1)
                elif puzzle[i + 1][j] == 0:
                    change(puzzle, i, j, i + 1, j)
        elif i == difficulty-1:  # 퍼즐 아래쪽
            if j == 0:  # 퍼즐 왼쪽 아래
                if puzzle[i][j + 1] == 0:
                    change(puzzle, i, j, i, j + 1)
                elif puzzle[i - 1][j] == 0:
                    change(puzzle, i, j, i - 1, j)
            elif j == difficulty-1:  # 퍼즐 오른쪽 아래
                if puzzle[i][j - 1] == 0:
                    change(puzzle, i, j, i, j - 1)
                elif puzzle[i - 1][j] == 0:
                    change(puzzle, i, j, i - 1, j)
            else:
                if puzzle[i][j - 1] == 0:
                    change(puzzle, i, j, i, j - 1)
                elif puzzle[i][j + 1] == 0:
                    change(puzzle, i, j, i, j + 1)
                elif puzzle[i - 1][j] == 0:
                    change(puzzle, i, j, i - 1, j)
        elif j == 0:  # 퍼즐 왼쪽
            if puzzle[i - 1][j] == 0:
                change(puzzle, i, j, i - 1, j)
            elif puzzle[i+1][j] == 0:
                change(puzzle, i, j, i+1, j)
            elif puzzle[i][j + 1] == 0:
                change(puzzle, i, j, i, j + 1)
        elif j == difficulty-1:  # 퍼즐 오른쪽
            if puzzle[i - 1][j] == 0:
                change(puzzle, i, j, i - 1, j)
            elif puzzle[i + 1][j] == 0:
                change(puzzle, i, j, i + 1, j)
            elif puzzle[i][j - 1] == 0:
                change(puzzle, i, j, i, j - 1)
        else:
            if puzzle[i-1][j] == 0:
                change(puzzle, i, j, i - 1, j)
            elif puzzle[i+1][j] == 0:
                change(puzzle, i, j, i+1, j)
            elif puzzle[i][j - 1] == 0:
                change(puzzle, i, j, i, j - 1)
            elif puzzle[i][j + 1] == 0:
                change(puzzle, i, j, i, j + 1)


def change(puzzle, x1, y1, x2, y2):  # 바꿀 퍼즐 위치 받아서 서로 바꾸기
    temp = puzzle[x1][y1]
    puzzle[x1][y1] = puzzle[x2][y2]
    puzzle[x2][y2] = temp

    # list1 = ['matrix[column][row]=matrix[column][row+1]', 'matrix[column][row]=matrix[column+1][row]']
    # list2 = ['matrix[column][row]=matrix[column-1][row]', 'matrix[column][row]=matrix[column][row+1]']
    # list3 = ['matrix[column][row]=matrix[column][row-1]', 'matrix[column][row]=matrix[column+1][row]']
    # list4 = ['matrix[column][row]=matrix[column-1][row]', 'matrix[column][row]=matrix[column][row-1]']
    # list5 = ['matrix[column][row]=matrix[column+1][row]', 'matrix[column][row]=matrix[column-1][row]']
    #
    # if column==0 and row==0:
    #      random.choice(list1)
    # elif column==0 and row==2:
    #      random.choice(list2)
    # elif column == 2 and row == 0:
    #      random.choice(list3)
    # elif column == 2 and row == 2:
    #      random.choice(list4)
    # else:
    #      random.choice(list5)