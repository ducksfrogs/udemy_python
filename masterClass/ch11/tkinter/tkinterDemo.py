try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)


mainWindow = tkinter.Tk()
mainWindow.title("Hello world")
mainWindow.geometry('640x480+8+400')
mainWindow.mainloop()