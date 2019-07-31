def python_food():
    width = 80
    text = "Spam and eggs"
    left_mergin = (width - len(text)) //2
    print (" "*left_mergin, text)

def center_text(*args, sep=' ', end='\n', file=None, flush=False):
    text =""
    for arg in args:
        text += str(arg) + sep
    left_mergin = (80 - len(text)) //2
    print(" "* left_mergin, text, end=end, file=file, flush=flush)

with open('centerd', mode='w') as  centerd_file:

    center_text("spam and eggs", file=centerd_file)
    center_text("spam", "and", 12, file=centerd_file)
    center_text("spam and eggs  dddddd","momo", sep=":", file=centerd_file)
