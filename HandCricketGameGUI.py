import tkinter
from tkinter.constants import BOTH, FLAT, LEFT, RIGHT, X

root = tkinter.Tk()

# GUI Window Box Geometry Info

root.geometry("1200x900")

root.minsize(640,480)
root.maxsize(1200,900)

# Title

root.title("Hand Cricket Game")

# Images

newGame = tkinter.PhotoImage(file="ngBtn.png")
quit = tkinter.PhotoImage(file="quitBtn.png")

batBallImg = tkinter.PhotoImage(file="bat.png")
backgroundImage = tkinter.Label(root,image=batBallImg)
backgroundImage.place(x=0,y=0,relwidth=1,relheight=1)

# Frames, Labels & Buttons

titleBar = tkinter.Frame(root, borderwidth=2, relief=FLAT)
titleBar.pack(fill=X)

topNav = tkinter.Frame(root, background="#cccccc", borderwidth=2, relief=FLAT)
topNav.pack(fill=X)

h1 = tkinter.Label(titleBar ,text="Hand Cricket Game", font=("Ink Free", 20, "bold"), background="#bbbbbb")
b1 = tkinter.Button(topNav, image= newGame, relief=FLAT, highlightthickness=0, borderwidth=0, background="#cccccc")
b2 =  tkinter.Button(topNav, image= quit, command=root.destroy, relief=FLAT, highlightthickness=0, borderwidth=0, background="#cccccc")
h1.pack()
b1.pack(side=LEFT, padx=12)
b2.pack(side=RIGHT, padx=12)

# This mainloop should remain at the end

root.mainloop()