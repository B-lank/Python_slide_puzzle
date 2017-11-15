from tkinter import *
import crop
import random_mixing
import ranking

cellSize = 3  # Grid Size Set

class mainGrid(Frame):

    def __init__(self, user_id, user_rank, user_high, cellSize):
        Frame.__init__(self)

        self.user_id = user_id
        self.user_rank = user_rank
        self.user_highest_score = user_high
        self.cellSize = cellSize
        self.score = cellSize * 100
        self.puzzle = [[i*self.cellSize + j for j in range(self.cellSize)] for i in range(self.cellSize)]
        self.complete = [[i*self.cellSize + j for j in range(self.cellSize)] for i in range(self.cellSize)]
        random_mixing.mix(self.puzzle, self.cellSize)
        self.grid()
        self.master.title('Sliding Puzzle Game')  # Game Title
        self.master.resizable(0, 0)  # Disable Resizeable
        self.master.configure(bg='white')
        self.configure(bg='white')
        self.cropped_puzzle()  # 사이즈에 맞는 퍼즐 받아오기
        self.gridCell = []
        self.initGrid()
        self.mainloop()

    def initGrid(self):
        originGrid = Frame(self, bg='white')
        originGrid.grid(row=0, column=0)
        for i in range(self.cellSize):
            for j in range(self.cellSize):
                self.origincell = Frame(originGrid, bg='white')
                self.origincell.grid(row=i, column=j, padx=5, pady=5)
                self.origin = Label(master=self.origincell, text="1", bg='white', image=self.cropped_puzzle[i * self.cellSize + j], font='Helvetica -7', relief='solid')
                self.origin.grid()

        middleGrid = Frame(self, bg='white')
        middleGrid.grid(row=0, column=1)
        txt = "ID : %s\nRank : %s\nHighest score : %s\n" % (self.user_id, self.user_rank, self.user_highest_score)
        label_information = Label(middleGrid, text=txt, font=("D2Coding", 20), bg='white')
        label_information.pack()
        self.present_score = StringVar()
        label_score = Label(middleGrid, textvariable=self.present_score, font=("D2Coding", 20), bg='white')
        self.present_score.set("Score : " + format(self.score))
        label_score.pack()
        self.finish = StringVar()
        label_finish = Label(middleGrid, textvariable=self.finish, font=("D2Coding", 15), bg='white')
        label_finish.pack()

        mainGrid = Frame(self, bg='white')
        mainGrid.grid(row = 0, column = 2)
        self.button_puzzle = []
        for i in range(self.cellSize):
            self.button_puzzle.append([])
            for j in range(self.cellSize):
                self.button_puzzle[i].append(Button(mainGrid, bg='white', font = 'Helvetica -8', relief = 'solid', command=lambda i=i, j=j:self.puzzle_change(i, j)))
                self.button_puzzle[i][j].grid(row = i, column = j, padx = 5, pady = 5)
        self.update_puzzle()

    def puzzle_change(self, i, j):  # i, j의 전후좌우에 빈칸이 있으면 자리 옮기기
        if i == 0:  # 퍼즐 위쪽
            if j == 0:  # 퍼즐 왼쪽 위
                if self.puzzle[i][j+1] == 0:
                    self.change(i, j, i, j+1)
                elif self.puzzle[i+1][j] == 0:
                    self.change(i, j, i+1, j)
            elif j == self.cellSize-1:  # 퍼즐 오른쪽 위
                if self.puzzle[i][j-1] == 0:
                    self.change(i, j, i, j-1)
                elif self.puzzle[i+1][j] == 0:
                    self.change(i, j, i+1, j)
            else:
                if self.puzzle[i][j-1] == 0:
                    self.change(i, j, i, j-1)
                elif self.puzzle[i][j+1] == 0:
                    self.change(i, j, i, j+1)
                elif self.puzzle[i+1][j] == 0:
                    self.change(i, j, i+1, j)
        elif i == self.cellSize-1:  # 퍼즐 아래쪽
            if j == 0:  # 퍼즐 왼쪽 아래
                if self.puzzle[i][j+1] == 0:
                    self.change(i, j, i, j+1)
                elif self.puzzle[i-1][j] == 0:
                    self.change(i, j, i-1, j)
            elif j == self.cellSize-1:  # 퍼즐 오른쪽 아래
                if self.puzzle[i][j-1] == 0:
                    self.change(i, j, i, j-1)
                elif self.puzzle[i-1][j] == 0:
                    self.change(i, j, i-1, j)
            else:
                if self.puzzle[i][j-1] == 0:
                    self.change(i, j, i, j-1)
                elif self.puzzle[i][j+1] == 0:
                    self.change(i, j, i, j+1)
                elif self.puzzle[i-1][j] == 0:
                    self.change(i, j, i-1, j)
        elif j == 0:  # 퍼즐 왼쪽
            if self.puzzle[i-1][j] == 0:
                self.change(i, j, i-1, j)
            elif self.puzzle[i+1][j] == 0:
                self.change(i, j, i+1, j)
            elif self.puzzle[i][j+1] == 0:
                self.change(i, j, i, j+1)
        elif j == cellSize-1:  # 퍼즐 오른쪽
            if self.puzzle[i-1][j] == 0:
                self.change(i, j, i-1, j)
            elif self.puzzle[i+1][j] == 0:
                self.change(i, j, i+1, j)
            elif self.puzzle[i][j-1] == 0:
                self.change(i, j, i, j-1)
        else:
            if self.puzzle[i-1][j] == 0:
                self.change(i, j, i-1, j)
            elif self.puzzle[i+1][j] == 0:
                self.change(i, j, i+1, j)
            elif self.puzzle[i][j-1] == 0:
                self.change(i, j, i, j-1)
            elif self.puzzle[i][j+1] == 0:
                self.change(i, j, i, j+1)
        self.update_puzzle()

    def update_puzzle(self):
        for i in range(self.cellSize):
            for j in range(self.cellSize):
                self.button_puzzle[i][j].configure(image=self.cropped_puzzle[self.puzzle[i][j]])
        if self.puzzle == self.complete:
            self.puzzle_complete()
            window_finish = Tk()
            self.finish.set("Clear!")
            ranking.set_rank(self.user_id, self.score)
        if self.score == 0:
            self.puzzle_complete()
            self.finish.set("Game Over")

    def puzzle_complete(self):
        for i in range(self.cellSize):
            for j in range(self.cellSize):
                self.button_puzzle[i][j].configure(state='disabled')

    def change(self, x1, y1, x2, y2):  # 바꿀 퍼즐 위치 받아서 서로 바꾸기
        temp = self.puzzle[x1][y1]
        self.puzzle[x1][y1] = self.puzzle[x2][y2]
        self.puzzle[x2][y2] = temp
        self.score -= 1
        self.present_score.set("Score : " + format(self.score))

    def cropped_puzzle(self):  # 원본 사진을 받아와서 오리기
        self.cropped_puzzle = crop.crop_image(self.cellSize)