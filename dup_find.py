import os, sys, hashlib, re

FileList = []
RootDir = r'C:\Users\greys_9wqm0ju\Desktop\root'
Direct = os.walk(str(RootDir))
for Path, Dirs, FileNames in Direct:
    for Item in FileNames:
        FilePath = os.path.join(Path, Item)
        FileList.append(FilePath)

print(FileList)