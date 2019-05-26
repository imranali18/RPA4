from tkinter import *

root = Tk()
main_frame = Frame(root, bg='green', borderwidth=7, relief='raised')
main_frame.pack()

top_frame = Frame(main_frame, bg='red', borderwidth=7, relief='raised')
top_frame.pack(side=TOP)

bottom_frame = Frame(main_frame, bg='red', borderwidth=7, relief='raised')
bottom_frame.pack(side=BOTTOM)

button1 = Button(top_frame, text="Top 1", bg='yellow')
button1.pack(side=LEFT)
button2 = Button(top_frame, text="Top 2", bg='blue')
button2.pack(side=RIGHT)

button3 = Button(bottom_frame, text="Bottom 1", bg='purple', borderwidth=7, relief='raised')
button3.pack(side=LEFT)
button4 = Button(bottom_frame, text="Bottom 2", bg='white')
button4.pack(side=RIGHT)

root.mainloop()