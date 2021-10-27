import tkinter
from tkinter.constants import BOTH, FLAT, X

root = tkinter.Tk()

# GUI Window Box Geometry Info

root.geometry("1200x900")

root.minsize(640,480)
root.maxsize(1200,900)

# Title

root.title("Hand Cricket Game")

# Frames & Labels

topNav = tkinter.Frame(root, background="#bbbbbb", borderwidth=2, relief=FLAT)
topNav.pack(fill=X)

h1 = tkinter.Label(topNav ,text="Hand Cricket Game", font=("Ink Free", 20, "bold"), background="#bbbbbb")
#h2 = tkinter.Label(text="Next Line")
h1.pack()
#h2.pack()

# Images

bat = tkinter.PhotoImage(file="bat.png")
image = tkinter.Label(image= bat)
image.pack(fill=BOTH)

# This mainloop should remain at the end

root.mainloop()