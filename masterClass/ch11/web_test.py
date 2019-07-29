import webbrowser

#webbrowser.open('https://www.python.jp/')

for i in range(10):
    print(i)


#chrome = webbrowser.get(using='google-chrome')
#chrome.open_new("https://www.python.org")

firefox = webbrowser.get(using='firefox')
firefox.open_new('https://www.python.org')
