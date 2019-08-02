def python_food():
    width = 80
    text = "Spam and eggs"
    left_mergin = (width - len(text)) //2
    print (" "*left_mergin, text)

def center_text(*args, sep=' '):
    text =""
    for arg in args:
        text += str(arg) + sep
    left_mergin = (80 - len(text)) //2
    return  " "* left_mergin + text

s1 = center_text("momon")
print(s1)
print(center_text("spam and eggs"))
print(center_text("spam", "and", 12))
print(center_text("spam and eggs  dddddd","momo", sep=":"))

print(("=" +str(12*3)))
print(sorted(["b", "d", "c", "a"]))