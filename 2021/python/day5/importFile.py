def importFile(inFile):
    coordList = []
    for x in open(inFile,"r").readlines():
        combined = []
        splitGroups = x.split(" -> ")
        for group in splitGroups:
          group = group.split(",")
          for x in range(len(group)):
            group[x] = int(group[x].strip())
          combined.append(group)
        coordList.append(combined)
    return coordList
