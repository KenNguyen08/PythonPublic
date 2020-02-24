from tkinter import *
import tkinter.messagebox

mainWindow = Tk()
mainWindow.geometry('600x350')
mainWindow.title("Tic tac toe in Python")

moveList =[['-'for j in range(3)]for i in range(3)]
xturn = 1
oturn = 0

leftFrame = Frame(mainWindow, width = 350, height = 350, bg='red')
leftFrame.grid(rowspan  = 2, column=0)

topRightFrame = Frame (mainWindow, width = 250, height = 100, bg = 'pink')
topRightFrame.grid(row = 0, column = 1)

buttomRightFrame = Frame (mainWindow, width = 250, height = 250, bg ='blue')
buttomRightFrame.grid(row = 1, column = 1)

gameName = Label(topRightFrame, text='Tic Tac Toe', font='Times 20 bold' )
gameName.pack()



scoreMessageX = Label(buttomRightFrame, text='Score Of X: 0', font='Times 20 bold')
scoreMessageX.grid(row = 0, column = 0)
scoreMessageY = Label(buttomRightFrame, text='Score Of O: 0', font='Times 20 bold')
scoreMessageY.grid(row = 1, column = 0)

def reloadmoveList():
    for i in range(3):
        for k in range(3): 
            moveList[i][k] = '-'

scoreA = 0
scoreB = 0

def setScoreMessage(win):
    global scoreA, scoreB
    if win == 'X':
        scoreA = scoreA + 1
        message = 'Score Of X: ' + str(scoreA)
        print('set message time')
        scoreMessageX.configure(text=message) 
    else:
        scoreB = scoreB + 1
        message = 'Score Of O: ' + str(scoreB)
        scoreMessageY.configure(text=message)   

def movement(rows, columns, button):
    global xturn, oturn
    if xturn == 1:
        moveList[rows][columns] = 'X'
        button['text'] = "X"
        if checkResult() == 1:
            tkinter.messagebox.showinfo('Result: ', 'X win')
            reloadmoveList()
            loadButton()
            setScoreMessage('X')
        
        xturn=0
        oturn=1 
        button.configure(state=DISABLED)
    elif oturn == 1:
        moveList[rows][columns] = 'O'
        button['text'] = "O"
        if checkResult() == 1:
            tkinter.messagebox.showinfo('Result: ', 'O win')
            reloadmoveList()
            loadButton()
            setScoreMessage('O')
        else:
            if checkDraw() == 1:
                tkinter.messagebox.showinfo('Result: ', 'Draw')
                reloadmoveList()
                loadButton()
        xturn=1
        oturn=0
        button.configure(state=DISABLED) 

def checkResult():
    index = 1
    while index == 1: 
        if checkHorizontal() == 1:
            print('horizontal result')
            return 1
        elif checkVertical() == 1:
            print('vertical result')
            return 1
        elif checkCross() == 1:
            print('Cross result')
            return 1
        else:
            return 0

def checkHorizontal():
    global xturn, oturn
    checkValue = ' '
    result = 0
    if xturn == 1: 
        checkValue = 'X'
    else:
        checkValue = 'O'
    print('Checkvalue: ',checkValue)
    print('MoveList: ', moveList)
    f = 0
    for i in range (3):
        if i != f:
            result = 0
        for k in range (3):
            f = i
            if moveList[i][k] == checkValue:
                result = result + 1
                if result == 3:
                    return 1
            else:
                result = 0

        print('result ', result)
    return 0

def checkVertical():
    global xturn, oturn
    checkValue = ' '
    result = 0
    if xturn == 1: 
        checkValue = 'X'
    else:
        checkValue = 'O'
    print('Checkvalue: ',checkValue)
    print('MoveList: ', moveList)
    f = 0
    for i in range (3):
        if i != f:
            result =0
        for k in range (3):
            f = i
            if moveList[k][i] == checkValue:
                result = result + 1
                if result == 3:
                    return 1
            else:
                result = 0

        print('result ', result)
    return 0

def checkCross():
    global xturn, oturn
    checkValue = ' '
    result = 0
    if xturn == 1: 
        checkValue = 'X'
    else:
        checkValue = 'O'
    for i in range(3):
        if moveList[i][i] == checkValue:
            result= result + 1
            if result == 3:
                return 1
        else:
            result = 0
    f = 3         
    for k in range(3):
        f = f -1
        if moveList[k][f] == checkValue:
            result = result + 1  
            if result == 3:
                return 1
        else:
            result = 0

    return 0

def checkDraw():
    emptySpot = '-'
    a = 0
    for i in range(3):
        for k in range(3): 
            if moveList[i][k] != emptySpot:
                a = a +1
    print('value of a ', a)            
    if a == 9 and checkResult() == 0:
        return 1
    return 0

def loadButton():
    button1 = Button(leftFrame, text=' ', font='Times 20 bold', bg='brown', fg='white', height=3, width=6, command=lambda : movement(0,0,button1))
    button1.grid(row=0, column=0)

    button2 = Button(leftFrame, text=' ', font='Times 20 bold', bg='brown', fg='white', height=3, width=6, command=lambda : movement(0,1,button2))
    button2.grid(row=0, column=1)

    button3 = Button(leftFrame, text=' ', font='Times 20 bold', bg='brown', fg='white', height=3, width=6, command=lambda : movement(0,2,button3))
    button3.grid(row=0, column=2)

    button4 = Button(leftFrame, text=' ', font='Times 20 bold', bg='brown', fg='white', height=3, width=6, command=lambda : movement(1,0,button4))
    button4.grid(row=1, column=0)

    button5 = Button(leftFrame, text=' ', font='Times 20 bold', bg='brown', fg='white', height=3, width=6, command=lambda : movement(1,1,button5))
    button5.grid(row=1, column=1)

    button6 = Button(leftFrame, text=' ', font='Times 20 bold', bg='brown', fg='white', height=3, width=6,  command=lambda : movement(1,2,button6))
    button6.grid(row=1, column=2)

    button7 = Button(leftFrame, text=' ', font='Times 20 bold', bg='brown', fg='white', height=3, width=6,  command=lambda : movement(2,0,button7))
    button7.grid(row=2, column=0)

    button8 = Button(leftFrame, text=' ', font='Times 20 bold', bg='brown', fg='white', height=3, width=6,  command=lambda : movement(2,1,button8))
    button8.grid(row=2, column=1)

    button9 = Button(leftFrame, text=' ', font='Times 20 bold', bg='brown', fg='white', height=3, width=6,  command=lambda : movement(2,2,button9))
    button9.grid(row=2, column=2)

loadButton()
mainWindow.mainloop()