'''
import time
import tkinter
window = tkinter.Tk()
window.mainloop()
print('Anybody home?')
'''

'''
window = tkinter.Tk()
label = tkinter.Label(window, text='First label.')
label.pack()
label.config(text='Second label.')
window.mainloop()
'''

'''
import tkinter
window = tkinter.Tk()
data = tkinter.StringVar()
data.set('Data to display')
label = tkinter.Label(window, textvariable=data)
label.pack()
window.mainloop()
'''

'''
import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
first = tkinter.Label(frame, text='First label')
first.pack()
second = tkinter.Label(frame, text='Second label')
second.pack()
third = tkinter.Label(frame, text='Third label')
third.pack()
window.mainloop()
'''

'''
import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
frame2 = tkinter.Frame(window, borderwidth=14, relief=tkinter.RIDGE)
frame2.pack()
first = tkinter.Label(frame, text='First label')
first.pack()
second = tkinter.Label(frame2, text='Second label')
second.pack()
third = tkinter.Label(frame2, text='Third label')
third.pack()
window.mainloop()
'''


import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
var = tkinter.StringVar()
var.set('Good morning')
# label = tkinter.Label(frame, textvariable=var)
# label.pack()
entry = tkinter.Entry(frame, textvariable=var)
entry.pack()
window.mainloop()

print('*'*15 + '\n')
print('label value:', var.get() )
