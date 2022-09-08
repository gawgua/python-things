"""
Compare 2 folder of music and check if is there an equivalant size on the other folder
Extract same .pck for old and new version to check

Usage:
    py audioDiff.py <old music folder> <new music folder>
"""

from os import listdir, mkdir, stat
from shutil import copy2
from sys import argv
import re

oldFolder = argv[1].strip("\\").strip("/") #make the path consistant
newFolder = argv[2].strip("\\").strip("/")
oldFiles = listdir(oldFolder)
newFiles = listdir(newFolder)

maxIndex = 31 #highest Music.pck is 31
mkdir('./diff/')
for i in range(0, maxIndex + 1):
    old = {}
    new = {}
    removeList = []
    pattern = re.compile(f'Music{i}($|\D)')

    #add old file + size to dict
    old_CheckingFiles = list(filter(pattern.match, oldFiles))
    for file in old_CheckingFiles:
        size = str(stat(f'{oldFolder}/{file}').st_size)
        old[size] = file

    #add new file + size to dict
    new_CheckingFiles = list(filter(pattern.match, newFiles))
    for file in new_CheckingFiles:
        size = str(stat(f'{newFolder}/{file}').st_size)
        new[size] = file

    #check if is new a equal size file in old 
    for size in new:
        if size not in old:
            copy2(f'{newFolder}/{new[size]}', f'./diff/{new[size]}')
            print(f'{new[size]}: {round(int(size) / 1024/1024, 2)}MB')