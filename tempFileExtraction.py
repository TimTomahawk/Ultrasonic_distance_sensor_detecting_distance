def extracting(a):
    coordinateValue = []
    dataTxtSelected = open("TempFile.txt", "r")
    for line in dataTxtSelected:
            coordinateValue.append(int(line))
    return coordinateValue[a]
