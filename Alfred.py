# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 11:20:46 2022

@author: csivley

Alfred: Folder Organizer
In the spirit of Belvedere, RIP
"""

#import stuff
import os
import shutil

#target variable names
source = "C:/Users/csivley/Documents"
destination = "C:/Users/csivley/Desktop/Alfred/"

pdfExt = [".pdf"]
pptExt = [".ppt", ".pptx"]
wordExt = [".doc",".docx"]
excelExt = [".xls", ".xlsx", ".csv"]
zipExt = [".zip", ".7z"]
exeExt = [".exe"]
imageExt = [".jpg", ".jpeg", ".png", ".gif", ".webm", ".tif", ".tiff"]
threeDimExt = [".stl", ".obj", ".g", "gcode"]
audioExt = [".wav", ".mp3"]
codeExt = [".c", ".cpp", ".m", ".py", ".mat"]
textExt = [".txt", ".log", ".xml"]
installExt = [".msi"]
videoExt = [".avi", ".mp4"]
circuitExt = [".diy"]
webExt = [".html", ".webp"]


logFilename = "AlfredLogOut.alfredlog"

files = os.listdir(source) #returns list of all files and directories in source
print(files)

#Functions
def log(arg):
    arg = str(arg)
    print(arg)
    with open(logFilename, 'a') as log:
        log.write(arg + "\n")


#########################################   MAIN LOOP

""" control flow:
    for each file, create a target string to select folder
    if the folder exists, try to copy it
    if there is an error, reflect the error and move on
    repeat until files are done.
    """
    
for file in files:
    ext = (os.path.splitext(file)[1]).lower() #returns extension of file
    target = ""
    if ext in pdfExt:
        target = destination + "PDF"
    elif ext in pptExt:
        target = destination + "Powerpoint"
    elif ext in wordExt:
        target = destination + "Word"
    elif ext in zipExt:
        target = destination + "Zip"
    elif ext in exeExt:
        target = destination + "Exe"
    elif ext in imageExt:
        target = destination + "Image"
    elif ext in threeDimExt:
        target = destination + "3D"
    elif ext in audioExt:
        target = destination + "Audio"
    elif ext in codeExt:
        target = destination + "Code"
    elif ext in textExt:
        target = destination + "Plaintext"
    elif ext in installExt:
        target = destination + "Installer"
    elif ext in videoExt:
        target = destination + "Video"
    elif ext in excelExt:
        target = destination + "Excel"
    elif ext in circuitExt:
        target = destination + "Circuits"
    elif ext in webExt:
        target = destination + "Web"
    else:
        target = None
    
    if target:
        log("Moving " + file + " to " + target)
        try:
            shutil.move((source + "\\" + file), target)
        except:
            log("Error in moving " + file)
    else:
        pass
