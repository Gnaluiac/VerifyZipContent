#!/usr/bin/python
import os, zipfile
import glob

def getFolderNames(basePath):
    pathList = glob.glob(basePath + "*")
    nationalNumberList = []

    for x in pathList:
        nationalNumberList.append(x.replace(basePath, ""))

    return nationalNumberList

def unzip(basePath, nationalNumber):
    zipPath = basePath + nationalNumber + "/" + nationalNumber + "_Appendix.zip"
    extractPath = basePath + nationalNumber + "/"

    with zipfile.ZipFile(zipPath, 'r') as zip_ref:
        zip_ref.extractall(extractPath)

    print("   " + zipPath + " ---> UNZIPPED")

    if os.path.exists(extractPath + "__MACOSX"):
        os.rmdir(extractPath + "__MACOSX")

def getFileNames(path):
    return glob.glob(path + "*")


def compareFileName(nationalNumber, fileNameList, clientPath):
    valid = False

    for file in fileNameList:
        if ".zip" not in file:
            file = file.replace(clientPath, "")

            if nationalNumber in file:
                valid = True
                print("   VERIFIED - VALID")
                break

    if not valid:
        print("   VERIFIED - ERROR")


def removeUnzippedFiles(path, nationalNumber):
    filesToRemove = getFileNames(path + nationalNumber + "/")

    for file in filesToRemove:
        if ".pdf" in file:
            os.remove(file)

    print("   " + path + nationalNumber + "/" + " ---> CLEANED")



basePath = "/Users/gianluca/Desktop/test/"

folders = getFolderNames(basePath)

for client in folders:
    nationalNumber = client
    clientPath = basePath + nationalNumber + "/"

    print("#" + nationalNumber)
    unzip(basePath, nationalNumber)
    fileNames = getFileNames(clientPath)
    compareFileName(nationalNumber, fileNames, clientPath)
    removeUnzippedFiles(basePath, nationalNumber)
    print("-------------------------------")