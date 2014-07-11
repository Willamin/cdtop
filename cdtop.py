import os
import sys

if len(sys.argv) <= 1:
    check = "~"
else:
    check = sys.argv[1]
current = os.getcwd()
while True:
    current = os.path.normpath(current+"/..")
    if os.path.basename(current) == check:
        print current
        break
    if os.path.basename(current) == "":
        sys.stderr.write("No parent found\n")
        break
