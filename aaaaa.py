import win32gui

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

if __name__ == "__main__":
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)

    for i in top_windows:
        #'''
        if i[1] != "":
            print(i)
    
        #'''
        #'''
        if "inprivate" in i[1].lower():
            print(i)
            win32gui.ShowWindow(i[0],5)
            win32gui.SetForegroundWindow(i[0])
            break
        #'''