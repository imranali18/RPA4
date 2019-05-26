from tkinter import *

class MyApp(object):
    def __init__(self, parent):
        self.main_frame = Frame(parent)
        self.main_frame.pack()
        
        self.top_frame = Frame(self.main_frame)
        self.top_frame.pack(side=TOP)
        self.bottom_frame = Frame(self.main_frame)
        self.bottom_frame.pack(side=BOTTOM)
        
        self.button1 = Button(self.top_frame, text="Top 1")
        self.button1.pack(side=LEFT)
        self.button2 = Button(self.top_frame, text="Top 2")
        self.button2.pack(side=RIGHT)
        self.button3 = Button(self.bottom_frame, text="Bottom 1")
        self.button3.pack(side=LEFT)
        self.button4 = Button(self.bottom_frame, text="Bottom 2")
        self.button4.pack(side=RIGHT)

if __name__ == "__main__":
    root = Tk()
    myapp = MyApp(root)
    root.mainloop()
