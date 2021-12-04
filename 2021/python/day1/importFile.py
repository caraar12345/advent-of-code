def importFile(inFile):
    inFileList = []
    for x in open(inFile,"r").readlines():
        inFileList.append(int(x.strip()))
    return inFileList
