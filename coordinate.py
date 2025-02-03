import time

import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")


while True:
    shell.SendKeys("W")
    print('нажал')
    time.sleep(2)
    time.sleep(2)