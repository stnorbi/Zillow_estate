import os

ICONPATH=os.path.dirname(__file__).replace("utils","icons")+"/"

def getIcon(fileName):
    fileList=os.listdir(ICONPATH)

    if fileName in fileList:
        return ICONPATH + fileName
