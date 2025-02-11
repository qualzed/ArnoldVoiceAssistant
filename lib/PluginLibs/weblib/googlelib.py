import webview

def Google(Name, Ask):
    webview.create_window(Name, f'https://www.google.com/search?q={Ask}')
    webview.start()