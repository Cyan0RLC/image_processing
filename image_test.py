import os
import sys

# test if command line argument (folder) was given
if len(sys.argv) < 3:
    print("please provide folder, common base-string of picture names, and gif name")
    sys.exit()

folder = sys.argv[1]
base = sys.argv[2]
name = sys.argv[3]

#go into specified folder
os.chdir(folder)

# use imagemagick to make the gif
os.system("convert -delay 10 -loop 0 " + str(base)+"*.png  " + str(name)+".gif")