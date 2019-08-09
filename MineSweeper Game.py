# [Valid inputs : 1 to 9]  [Opened cells : 'O'] [Mine cell : 'X']

import pandas as pd
import sys
import random
import tkinter as tk

RowData = [[0,0,0,0,0],[0,1,2,3,0],[0,4,5,6,0],[0,7,8,9,0],[0,0,0,0,0]]
FakeMinefieldMatrix = pd.DataFrame(RowData)
MinefieldMatrix  = FakeMinefieldMatrix.loc[1:3,1:3]
BombMatrix = FakeMinefieldMatrix.loc[1:3,1:3]
print("Visual representation of the Minesweeper Game :")
print(MinefieldMatrix)

# Planting a Bomb using Random library
MineCell = random.randint(1, 9)
BombX = 0
while BombX <= 2:
    BombY = 0
    while BombY <= 2:
        if BombMatrix.iat[BombX,BombY] == MineCell:
            BombMatrix.iloc[BombX,BombY] = 'X'
        BombY = BombY + 1
    BombX = BombX + 1

def MainDef():
    
    try:
        OpenAcell = int(input("\nPlease guess any safe block from 1 to 9 options => "))
    except:
        print("\n==>> Not a valid input, Please enter only Integer numbers :")
        MainDef()
    if OpenAcell <= 0 or OpenAcell >= 10:
        print("\n==>> Wrong input, Please enter Integer number between 1 to 9 only :")
        MainDef()
    
    i,row,column,NotToOpen = 0,0,0,0
    while i <= 2:
        j = 0
        while j <= 2:
            if MinefieldMatrix.iat[i,j] == OpenAcell:
                if BombMatrix.iat[i,j] == 'X':
                    print(BombMatrix)
                    print("*** GAME OVER : Lose the Game, as you clicked on mine ***")
                    WindowLose()
                    sys.exit()
                else:
                    AdjacentCells(i,j)
            
            NotToOpen = NotToOpen + 1
            if NotToOpen == OpenAcell:
                AdjacentCells(i,j)
            j = j + 1
        i = i + 1
# Ending MainDef function

def AdjacentCells(row, column):
    
    if MinefieldMatrix.iat[row,column] == 'O':
        print("\n==>> Please choose other safe block, this cell is already marked as safe..")
        MainDef()
        
    i = 0
    while i <= 4:
        j = 0
        while j <= 4:
            if i == row+1 and j == column+1:
                FakeMinefieldMatrix.iloc[row+1,column+1] = FakeMinefieldMatrix.iloc[row+2,column+1] = FakeMinefieldMatrix.iloc[row+1,column+2] = FakeMinefieldMatrix.iloc[row,column+1] = FakeMinefieldMatrix.iloc[row+1,column] = 'O'
                x = 1
                while x <= 3:
                    y = 1
                    while y <= 3:
                        if FakeMinefieldMatrix.iloc[x,y] == 'O' and BombMatrix.iloc[x-1,y-1] != 'X':
                            MinefieldMatrix.iloc[x-1,y-1] = 'O'
                            BombMatrix.iloc[x-1,y-1] = 'O'
                        y = y + 1
                    x = x + 1
            j = j + 1
        i = i + 1

    print(MinefieldMatrix)
    
    a,count = 0,0
    while a <= 2:
        b = 0
        while b <= 2:
            if MinefieldMatrix.iloc[a,b] == 'O':
                count = count + 1
            b = b + 1
        a = a + 1
    if count == 8:
        print("*** GAME OVER : You've won the Game ***")
        WindowWin()
        sys.exit()
    else:
        MainDef()
# Ending AdjacentCells function

def WindowLose():
    root = tk.Tk()
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    root.geometry("+{}+{}".format(positionRight, positionDown))
    w = tk.Label(root, text="You Lose", fg='red', font=("Helvetica", 20))
    w.pack()
    root.mainloop()
    
def WindowWin():
    root = tk.Tk()
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    root.geometry("+{}+{}".format(positionRight, positionDown))
    w = tk.Label(root, text="You Win", fg='red', font=("Helvetica", 20))
    w.pack()
    root.mainloop()

MainDef() # Calling Main Function here to run the Game program