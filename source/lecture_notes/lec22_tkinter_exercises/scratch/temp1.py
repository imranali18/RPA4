import tkinter

# The controller.
def click():
    x = counter.get()
    if x < 2:
        x += 1
    else:
        x *= x
    counter.set(x)

if __name__ == '__main__':
    window = tkinter.Tk()
    
    # The model.
    counter = tkinter.IntVar()
    counter.set(0)

    # The views.
    frame = tkinter.Frame(window)
    frame.pack()

    button = tkinter.Button(frame, text='Click', command=click, 
                            font=('Courier', 24, 'bold italic'))
    button.pack()
    
    label = tkinter.Label(frame, textvariable=counter,
                          font=('Courier', 36, 'bold italic'),
                          bg = 'green', fg='black')
    label.pack()
    
    # Start the machinery!
    window.mainloop()
