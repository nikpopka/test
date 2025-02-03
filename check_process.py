import psutil

for i in psutil.process_iter():
    try:
        if 'LOSTA' in i.cmdline()[0]:
            print(i.cmdline())

    except: pass