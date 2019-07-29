try:
    import tkinter
except ImportError:
    import Tkinter as tkinter



mainWindow = tkinter.Tk()


mainWindow.title("Hello world")
mainWindow.geometry('640x480+8+400')

label = tkinter.Label(mainWindow, text="Hellow world")
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
#canvas.pack(side='left', fill=tkinter.X, expand=True)
canvas.pack(side='left', fill=tkinter.Y)
#canvas.pack(side='top', fill=tkinter.BOTH, expand=True)

button1 = tkinter.Button(mainWindow, text='Button1')
button2 = tkinter.Button(mainWindow, text='Button2')
button3 = tkinter.Button(mainWindow, text='Button3')
button1.pack(side='left', anchor='n')
button2.pack(side='left', anchor='s')
button3.pack(side='left')

mainWindow.mainloop()