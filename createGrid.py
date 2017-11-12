from tkinter import *
from random import *

cellSize = 3  # Grid Size Set
cellWidth = { 3 : 40, 4 : 30, 5 : 24 }
cellHeight = { 3 : 20, 4 : 15, 5 : 12 }

class mainGrid(Frame):

    def __init__(self, cellSize):
        Frame.__init__(self)
        
        self.cellSize = cellSize
        self.puzzle = [[i*self.cellSize + j for j in range(self.cellSize)] for i in range(self.cellSize)]
        self.complete = self.puzzle
        self.grid()
        self.master.title('Sliding Puzzle Game') #Game Title
        self.master.resizable(0, 0) #Disable Resizeable
        self.master.configure()
        # self.puzzle_setting()  # 사이즈에 맞는 퍼즐 받아오기
        self.gridCell = []
        self.initGrid()
        self.gameStart()
        self.mainloop()

    def gameStart(self):
        self.newCell()

    def initGrid(self):
        mainGrid = Frame(self, bg='black')
        mainGrid.grid(row = 0, column = 1)
        for i in range(self.cellSize):
            gridRow = []
            for j in range(self.cellSize):
                cell = Frame(mainGrid, bg = 'white')
                cell.grid(row = i, column = j, padx = 5, pady = 5)
                t = Label(master = cell, text=self.puzzle[i][j], bg='white', font = 'Helvetica -8', width=cellWidth[self.cellSize], height=cellHeight[self.cellSize], relief = 'solid')
                t.bind("<Button-1>", self.puzzle_change(i, j))
                t.grid()
                gridRow.append(t)

            self.gridCell.append(gridRow)

    def makeCell(self): #Make Cell
        self.newMatrix = []
        for i in range(self.cellSize):
            self.newMatrix.append([0] * self.cellSize)
        return self.newMatrix

    #image upload 구현하기.
    def newCell(self) :
        self.matrix = self.makeCell()

    def puzzle_change(self, i, j):  # i, j의 전후좌우에 빈칸이 있으면 자리 옮기기
        if i == 0:  # 퍼즐 위쪽
            if j == 0: # 퍼즐 왼쪽 위
                if self.puzzle[i][j+1] == 0:
                    self.change(i, j, i, j+1)
                elif self.puzzle[i+1][j] == 0:
                    self.change(i, j, i+1, j)
            elif j == self.cellSize:  # 퍼즐 오른쪽 위
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
        elif i == self.cellSize:  # 퍼즐 아래쪽
            if j == 0: # 퍼즐 왼쪽 아래
                if self.puzzle[i][j+1] == 0:
                    self.change(i, j, i, j+1)
                elif self.puzzle[i-1][j] == 0:
                    self.change(i, j, i-1, j)
            elif j == self.cellSize:  # 퍼즐 오른쪽 아래
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
                    self.change(i, j, i+1, j)
        elif j == 0:  # 퍼즐 왼쪽
            if self.puzzle[i-1][j] == 0:
                self.change(i, j, i-1, j)
            elif self.puzzle[i+1][j] == 0:
                self.change(i, j, i+1, j)
            elif self.puzzle[i][j+1] == 0:
                self.change(i, j, i, j+1)
        elif j == cellSize:  # 퍼즐 오른쪽
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
                self.gridCell[i][j].configure(image=self.cropped_puzzle[self.puzzle[i][j]])
        if self.puzzle == self.complete:
            print("Clear!")

    def change(self, x1, y1, x2, y2):  # 바꿀 퍼즐 위치 받아서 서로 바꾸기
        temp = self.puzzle[x1][y1]
        self.puzzle[x1][y1] = self.puzzle[x2][y2]
        self.puzzle[x2][y2] = temp

    def cropped_puzzle(self, orizinal_puzzle):  # 원본 사진을 받아와서 오리기
        self.cropped_puzzle = crop(orizinal_puzzle)
