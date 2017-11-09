from tkinter import *
from random import *

cellSize = 3  # Grid Size Set
cellWidth = { 3 : 40, 4 : 30, 5 : 24 }
cellHeight = { 3 : 20, 4 : 15, 5 : 12 }

class mainGrid(Frame):

    def __init__(self, cellSize):
        Frame.__init__(self)
        
        self.cellSize = cellSize
        
        self.grid()
        self.master.title('Sliding Puzzle Game') #Game Title
        self.master.resizable(0, 0) #Disable Resizeable
        self.master.configure()
        self.gridCell = []
        self.initGrid()
        self.gameStart()
        self.mainloop()

    def gameStart(self):
        self.newCell()

    def initGrid(self):
        mainGrid = Frame(self, bg='white')
        mainGrid.grid(row = 0, column = 1)
        for i in range(self.cellSize):
            gridRow = []
            for j in range(self.cellSize):
                cell = Frame(mainGrid, bg = 'white')
                cell.grid(row = i, column = j, padx = 5, pady = 5)
                t = Label(master = cell, text="", bg='white', font = 'Helvetica -8', width=cellWidth[self.cellSize], height=cellHeight[self.cellSize], relief = 'solid')
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
