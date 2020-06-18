#!/usr/bin/python
import glob
import os
import sys
import zipfile

# Global Variables
OS = sys.platform
basePath = "<path you want to check>"


def getFolderNames(basePath):

    nationalNumberList = []
    nationalNumberList = os.listdir(basePath)

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

    return os.listdir(path)


def compareFileName(nationalNumber, fileNameList, clientPath):
    valid = False

    for file in fileNameList:
        if ".zip" not in file:

            if ".xlsx" not in file:

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
            os.remove(path + nationalNumber + "/" + file)

    print("   " + path + nationalNumber + "/" + " ---> CLEANED")

folders = getFolderNames(basePath)

for client in folders:
    nationalNumber = client
    clientPath = basePath + nationalNumber + "/"

    print("#" + nationalNumber)
    unzip(basePath, nationalNumber)
    fileNames = getFileNames(clientPath)  # check glob here for \\ instead of //
    compareFileName(nationalNumber, fileNames, clientPath)
    removeUnzippedFiles(basePath, nationalNumber)
    print("-------------------------------")
