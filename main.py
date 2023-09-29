from tkinter import *
import random

def Check(row,col):
    global player
    if buttons[row][col]['text'] == "" and check_ans() is False:
        if player == players[0]:
            buttons[row][col]["text"]=player
            print(buttons[row][col]["text"])
            if check_ans() is False:
                player=players[1]
                label.config(text=(players[1]+" turn"))
            elif check_ans() is True:
                label.config(text=(players[0]+" wins"))
            elif check_ans() == "Tie":
                label.config(text=player.upper() + "'" + " Tie")
        else:
            if player == players[1]:
                buttons[row][col]["text"] = player
                if check_ans() is False:
                    player = players[0]
                    label.config(text="'" + player.upper() + "'" + " Play Time")
                elif check_ans() is True:
                    label.config(text=player.upper() + "'" + " Won")
                elif check_ans() == "Tie":
                    label.config(text=player.upper() + "'" + " Tie")









def check_ans():
    for i in range(3):
        if buttons[i][0]["text"]==buttons[i][1]["text"]==buttons[i][2]["text"]!="":
            return True
    for j in range(3):
        if buttons[0][j]["text"] == buttons[1][j]["text"] == buttons[2][j]["text"] != "":
            return True
    if buttons[0][0]["text"]==buttons[1][1]["text"]==buttons[2][2]["text"]!="":
        return True
    if buttons[0][2]["text"]==buttons[1][1]["text"]==buttons[2][0]["text"]!="":
        return True
    elif emptyCheck() is False:
        return "Tie"
    else:
        return False

def emptyCheck():
    pass

def reset():
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text']=""

window =Tk()
window.title("TicTacToe")
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text="'"+player.upper()+"'"+" Play Time")
label.pack(side="top")
button =Button(text="reset",command=lambda :reset())
button.pack(side="top")
frame = Frame(window)
frame.pack()
for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(frame, text="",font=('consolas',40), width=5, height=2,command= lambda a=i,b=j: Check(a,b))
        buttons[i][j].grid(row=i,column=j)















window.mainloop()
