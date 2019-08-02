def python_food():
    width = 80
    text: str ="spam and eggs"
    left_margin = (width - len(text))//2
    print(" "* left_margin, text)

def center_text(text):
    left_margin = (80 - len(text))//2
    print(" "* left_margin, text)

def center_text2(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text))//2
    print(" "* left_margin, text)


def center_text3(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text))//2
    print(" "* left_margin, text, end=end, file=file, flush=flush)

#center_text2("first'", "ceser", "ddd")
#center_text2("spam and dogs")
#center_text("spam spam spam")
#center_text(12)
center_text3("dddd", 12, "ddddgfdd", sep=":")
center_text3("dddd", 12, "ddddgfdd")
