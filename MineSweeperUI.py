import numpy
import random
from colorama import Fore
from tkinter import *
from tkinter.font import Font

bg = 'black'
fg = 'white'
pad = 5
FontFamily = 'Comic Sans MS'

class Cell:
    def __init__(self,Value,IfFind,IfMarkedAsBomb):
        self.Value = Value
        self.IfFind = IfFind
        self.IfMarkedAsBomb = IfMarkedAsBomb

def FormatDatabaseToStart():
    global Board,BoardUI
    Board=numpy.array([Cell(0,False,False) for i in range(100)])
    BoardUI = []

def CellClicked(ButtonNumber):
    AskMovePositionUI(ButtonNumber)
    UIUpdater()

def UI():
    global BoardUI

    def ButtonEvent(ButtonNumber):
        CellClicked(ButtonNumber)

    global mainroot
    mainroot = Tk(className='MineSweeper')
    BigPageFont = Font(mainroot,family=FontFamily,size=15)
    ShortPageFont = Font(mainroot,family=FontFamily,size=11)

    mainroot.config(bg=bg)

    Label(mainroot,text='Enjoy it !',pady=pad,bg=bg,fg=fg,font=BigPageFont).grid(column=0,row=0,columnspan=10)
    Label(mainroot,text='Designed by Hesam',pady=pad,bg=bg,fg=fg,font=ShortPageFont).grid(column=0,row=11,columnspan=10,sticky='W')


    def ButtonGen(i,j):
        Button(mainroot)
        BoardUI.append(Button(mainroot,text='     ',command=lambda : ButtonEvent(int(f'{i}{j}')),font=ShortPageFont,bg=bg,fg=fg,width=4))
        BoardUI[-1].grid(column=j,row=i+1,sticky='E,W')

    for i in range(10):
        for j in range(10):
            ButtonGen(i,j)

def UIUpdater():
    for i in range(len(BoardUI)):
        if Board[i].IfMarkedAsBomb:
            ValueToSet = '💣'
            BoardUI[i].config(bg='red')
        elif Board[i].IfFind:
            ValueToSet = str(Board[i].Value)
        else:
            ValueToSet = ''
        BoardUI[i].config(text=ValueToSet)



def AskMovePositionUI(UserMoveNumber):
    root = Tk(className='MineSweeper')
    BigPageFont = Font(root,family=FontFamily,size=15)
    ShortPageFont = Font(root,family=FontFamily,size=11)

    root.config(bg=bg)

    def ButtonEvent(Position):
        root.destroy()
        PlayerMoveIfLost(UserMoveNumber,Position)

    Label(root,text='Please enter your move position ...',bg=bg,fg=fg,padx=pad,pady=pad,font=BigPageFont).grid(column=0,row=0,columnspan=2)
    Button(root,text='Empty shortcut=E',bg=bg,fg=fg,padx=pad,pady=pad,font=ShortPageFont,command=lambda : ButtonEvent(True)).grid(column=0,row=1)
    Button(root,text='Bomb shortcut=B',bg=bg,fg=fg,padx=pad,pady=pad,font=ShortPageFont,command=lambda : ButtonEvent(False)).grid(column=1,row=1)
    # Label(root,text='Designed by Hesam',pady=pad,bg=bg,fg=fg,font=ShortPageFont).grid(column=0,row=2,columnspan=2,sticky='W')
    root.bind('<e>',lambda event : ButtonEvent(True))
    root.bind('<b>',lambda event : ButtonEvent(False))
    root.focus_force()


def AskThemeUI():
    root = Tk(className='MineSweeper')
    BigPageFont = Font(root,family=FontFamily,size=15)
    ShortPageFont = Font(root,family=FontFamily,size=11)

    root.config(bg=bg)

    def ButtonEvent(Position):
        global bg,fg
        root.destroy()
        if Position:
            bg = 'black'
            fg = 'white'
        else:
            bg = 'white'
            fg = 'black'
        ControllerUI()            

    Label(root,text='Please choose a theme ...',bg=bg,fg=fg,padx=pad,pady=pad,font=BigPageFont).grid(column=0,row=0,columnspan=2)
    Button(root,text='Dark mode shortcut=D',bg=bg,fg=fg,padx=pad,pady=pad,font=ShortPageFont,command=lambda : ButtonEvent(True)).grid(column=0,row=1)
    Button(root,text='Light mode shortcut=L',bg=bg,fg=fg,padx=pad,pady=pad,font=ShortPageFont,command=lambda : ButtonEvent(False)).grid(column=1,row=1)
    # Label(root,text='Designed by Hesam',pady=pad,bg=bg,fg=fg,font=ShortPageFont).grid(column=0,row=2,columnspan=2,sticky='W')
    root.bind('<d>',lambda event : ButtonEvent(True))
    root.bind('<l>',lambda event : ButtonEvent(False))
    root.mainloop()


def AskUserLevel3IsHardestAnd1IsEasiestUI():
    root = Tk(className='MineSweeper')

    BigPageFont = Font(root,family=FontFamily,size=15)
    ShortPageFont = Font(root,family=FontFamily,size=11)

    root.config(bg=bg)


    def ButtonEvent(Level):
        global Return
        Return = Level
        root.destroy()

    Label(root,text='Welcome to our Minsweeper !',font=BigPageFont,bg=bg,fg=fg).grid(column=0,row=0,columnspan=3)
    Label(root,text='Choose a level ...',font=ShortPageFont,bg=bg,fg=fg).grid(column=0,row=1,columnspan=3)
    Button(root,text='Easy shortcut=1',font=ShortPageFont,padx=pad,pady=pad,bg=bg,fg=fg,command=lambda : ButtonEvent(1)).grid(column=0,row=2)
    Button(root,text='Medium shortcut=2',font=ShortPageFont,padx=pad,pady=pad,bg=bg,fg=fg,command=lambda : ButtonEvent(2)).grid(column=1,row=2)
    Button(root,text='Hard shortcut=3',font=ShortPageFont,padx=pad,pady=pad,bg=bg,fg=fg,command=lambda : ButtonEvent(3)).grid(column=2,row=2)
    for i in ['1','2','3']:
        root.bind(i,lambda event : ButtonEvent(int(event.char)))
    # Label(root,text='Designed by Hesam',pady=pad,bg=bg,fg=fg,font=ShortPageFont).grid(column=0,row=3)
    root.focus_force()
    root.mainloop()
    return Return

def WinUI():
    root = Tk(className='MineSweeper')
    BigPageFont = Font(root,family=FontFamily,size=15)
    ShortPageFont = Font(root,family=FontFamily,size=11)

    if bg == 'black':
        Ownbg = 'darkgreen'
        print('Went')
    else:
        Ownbg = 'lightgreen'

    Ownpad = 20

    root.config(bg=Ownbg)

    Label(root,text='Congrats',padx=Ownpad,pady=Ownpad,bg=Ownbg,fg=fg,font=BigPageFont).grid(column=0,row=0)
    Label(root,text='You won !',padx=Ownpad,pady=Ownpad,bg=Ownbg,fg=fg,font=BigPageFont).grid(column=0,row=1)
    Button(root,text='Do you want to win again ? ...',command=lambda : TryAgain(root),padx=pad,pady=pad,fg=fg,bg=bg,font=ShortPageFont).grid(column=0,row=2)
    root.mainloop()

def LooseUI():
    root = Tk(className='MineSweeper')
    BigPageFont = Font(root,family=FontFamily,size=15)
    ShortPageFont = Font(root,family=FontFamily,size=11)

    if bg == 'black':
        Ownbg = 'darkred'
        print('Went')
    else:
        Ownbg = 'crimson'

    Ownpad = 20

    root.config(bg=Ownbg)

    Label(root,text='Sorry',padx=Ownpad,pady=Ownpad,bg=Ownbg,fg=fg,font=BigPageFont).grid(column=0,row=0)
    Label(root,text='You lost !',padx=Ownpad,pady=Ownpad,bg=Ownbg,fg=fg,font=BigPageFont).grid(column=0,row=1)
    Button(root,text='This time you\'ll win ! Try it ...',command=lambda : TryAgain(root),padx=pad,pady=pad,fg=fg,bg=bg,font=ShortPageFont).grid(column=0,row=2)
    root.mainloop()

def TryAgain(TransmitterRoot):
    mainroot.destroy()
    TransmitterRoot.destroy()
    ControllerUI()






def RandomBombPlacer(Level):
    for i in range(10+Level*7):
    # for i in range(3):
        Board[random.randint(0,99)].Value='B'

def CheckCell(a,b,SearchFor):
    Board_Reshaped=Board.reshape(10,10)
    if a>-1 and b>-1 and a<10 and b<10:
        if Board_Reshaped[a][b].Value==SearchFor:
            return True

def CountAroundCells(Address,SearchFor):
    FNumber=Address//10
    SNumber=Address%10
    return [
        CheckCell(i,j,SearchFor) for i,j in [[FNumber+k,SNumber+m] for k,m in [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]]
    ].count(True)

def EmptyCellsNumberer():
    for i in range(len(Board)):
        if Board[i].Value=='B':
            continue
        else:
            Board[i].Value=CountAroundCells(i,'B')

def OpenZerosToStart():
    for i in range(100):
        if not Board[i].Value:
            Board[i].IfFind=True
            OpenArroundZerosToStart(i)

def OpenArroundZerosToStart(Address):
    FNumber=Address//10
    SNumber=Address%10
    for i,j in [[FNumber+k,SNumber+m] for k,m in [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]]:
        if i>-1 and j>-1 and i<10 and j<10:
            Board[int(str(i)+str(j))].IfFind=True

def PlayerMoveIfLost(UserMoveNumber,UserMovePosition):
    # UserMoveNumber=AskUserMoveNumber()-1
    if UserMovePosition:
        if Board[UserMoveNumber].Value=='B':
            # print(f'{Fore.RED}\n\nYou lost !\n\n{Fore.WHITE}')
            BoardUI[UserMoveNumber].config(text='✖',bg='red')
            for i in BoardUI:
                i.config(state=DISABLED)
            LooseUI()
        else:
            Board[UserMoveNumber].IfFind=True
            Board[UserMoveNumber].IfMarkedAsBomb=False
            UIUpdater()
    else:
        Board[UserMoveNumber].IfMarkedAsBomb=True
        UIUpdater()
    PageDisablerIfWon()

def PageDisablerIfWon():
    if IfBoardIsFull():
        # print(f'{Fore.GREEN}\n\nCongrats\nYou won !\n\n{Fore.WHITE}')
        for i in BoardUI:
            i.config(state=DISABLED)
        WinUI()

def IfBoardIsFull():
    if [i.Value=='B' or i.IfFind for i in Board].count(False)==0:
        return True




def ControllerUI():
    FormatDatabaseToStart()
    RandomBombPlacer(AskUserLevel3IsHardestAnd1IsEasiestUI())
    EmptyCellsNumberer()
    OpenZerosToStart()
    UI()
    UIUpdater()
    mainroot.mainloop()




AskThemeUI()
