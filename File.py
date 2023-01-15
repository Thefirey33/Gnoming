import psutil
from tkinter.messagebox import *
from pynput.keyboard import *
AlreadyDone=False
import os
os.system("start chrome.exe")
while True:
 for s in psutil.process_iter(None,None):
    Pr = psutil.Process(s.pid)
    if Pr.name().__contains__("chrome"):
        print(Pr.name())
        import time
        time.sleep(5)
        import os
        if not Pr.is_running(): AlreadyDone = False
        if Pr.is_running() and not AlreadyDone:
         C = Controller()
         C.press(Key.cmd)
         C.press("m")
         C.release(Key.cmd)
         C.release("m")
         os.system("start chrome.exe https://www.youtube.com/watch?v=1FFBsX5C61Q")
         AlreadyDone=True
         time.sleep(12)
         C.tap(Key.space)
         showwarning("get rolled","HAHA")
         import winsound
         winsound.PlaySound("crow",winsound.SND_ASYNC)
         showwarning("get rolled","GNOMED")
         os.system("taskkill /im "+Pr.name() +" /f")
         import sys
         sys.exit()