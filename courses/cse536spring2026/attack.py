import sys
import time

while True:
    try:
        with open(sys.argv[1], "r") as f:
            printed = 0
            while True:
                f.seek(0)
                content = f.read()
                numlines = content.count('\n') 
                if numlines > printed:
                    listoflines = content.split('\n')
                    for i in range(printed, numlines):
                        linetoprint = listoflines[i].replace('\n', '')
                        if len(linetoprint) > 0 or i < (numlines - 1):
                            print(linetoprint, end="")
                            print("\\n\n", end="")
                        else:
                            numlines -= 1
                    printed = numlines
                time.sleep(1)
    except:
        pass


