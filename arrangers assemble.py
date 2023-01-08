import os, shutil

path = os.getcwd()
x = list(os.walk(path))

def isDir(path):
    return os.path.isdir(path)

def createDir(path):
    os.mkdir(path)

def isSubtitle(file):
    return file.endswith((".srt", ".vtt"))

def moveSubtitle(file, path):
    shutil.move(file, path)


for i in x[1:]: # starting 2nd index to check if it is a directory
    subFolder = i[0] + "/" + "Subtitles"
    if(os.path.exists(subFolder)):
        pass
    else:
        createDir(subFolder)
        for j in i[2:]:
            for k in j:
                if(isSubtitle(k)):
                    moveSubtitle(i[0] + "/" + k, subFolder)
