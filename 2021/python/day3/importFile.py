def importFile(inFile):
    inFileList = []
    for x in open(inFile,"r").readlines():
        inFileList.append(x.strip())
    return inFileList
