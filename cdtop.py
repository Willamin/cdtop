import os

current = os.getcwd()
while True:
    current = os.path.normpath(current+"/..")
    if os.path.basename(current) == "Documents":
        print current
        break
    if os.path.basename(current) == "":
        print "."
        break
