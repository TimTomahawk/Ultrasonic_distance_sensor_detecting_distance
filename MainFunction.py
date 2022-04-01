import os
import GUIWithImports
from tempFileExtraction import extracting#Extracting values from temp file
binNumber = extracting(0)#Values in temp file assigned at its appropiate position
xPosition = extracting(1)
yPosition = extracting(2)
os.remove("TempFile.txt")
print("Bin Number: " + str(binNumber))
print("Position X: " + str(xPosition) + " cm")
print("Position Y: " + str (yPosition) + " cm")
        
