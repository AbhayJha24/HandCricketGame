import tkinter

root = tkinter.Tk()

# GUI Logic

root.geometry("640x480")

root.minsize(640,480)

# Title

root.title("Hand Cricket Game")

# Label
h1 = tkinter.Label(text="Hello World")
h2 = tkinter.Label(text="Next Line")
h1.pack()
h2.pack()

# Images

bat = tkinter.PhotoImage(file="bat.png")
image = tkinter.Label(image=bat)
image.pack()

# This mainloop should remain at the end

root.mainloop()