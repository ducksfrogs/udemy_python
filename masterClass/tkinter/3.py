try:
    import tkinter
except ImportError:
    import Tkinter as tkinter



mainWindow = tkinter.Tk()


mainWindow.title("Hello world")
mainWindow.geometry('640x480+8+400')

label = tkinter.Label(mainWindow, text="Hellow world")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')

rightrFrame = tkinter.Frame(mainWindow)
rightrFrame.pack(side='right', anchor='n', expand=True)
button1 = tkinter.Button(rightrFrame, text='Button1')
button2 = tkinter.Button(rightrFrame, text='Button2')
button3 = tkinter.Button(rightrFrame, text='Button3')
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainWindow.mainloop()