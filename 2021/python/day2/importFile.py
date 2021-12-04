def importFile(inFile):
    inFileList = []
    for x in open(inFile,"r").readlines():
        inFileList.append(x.split(" "))
        inFileList[-1][1] = int(inFileList[-1][1].strip())
    return inFileList
