#!/usr/bin/python
import os, zipfile
import glob

zipPath = r"/Users/gianluca/Desktop/Change scrolling trackpad windows 10.PNG.zip"
baseFolderPath = "/Users/gianluca/Desktop/test/"
nationalNumber1 = None
nationalNumber2 = None


# def buildPaths():

def getFolderNames(basePath):
    pathList = glob.glob(basePath + "*")
    nationalNumberList = []

    for x in pathList:
        nationalNumberList.append(x.replace(basePath, ""))

    return nationalNumberList

def unzip(zipPath, extractPath):
    with zipfile.ZipFile(zipPath, 'r') as zip_ref:
        zip_ref.extractall(extractPath)

    print(zipPath + " ---> UNZIPPED \n")

    if os.path.exists(extractPath + "__MACOSX"):
        os.rmdir(extractPath + "__MACOSX")

def getFileNames(path):
    return glob.glob(path + "*")


def compareFileName(nationalNumber1, nationalNumber2, fileNameList, basePath):
    print("National number 1: " + nationalNumber1 + " - National number 2: " + nationalNumber2)

    for file in fileNameList:
        if nationalNumber1 not in file:
            if nationalNumber2 not in file:
                if ".zip" not in file:
                    print(file.replace(basePath, "") + ": " + " not ok")
            else:
                print(file.replace(basePath, "") + ": " + " ok")
        else:
            print(file.replace(basePath, "") + ": " + " ok")

    print("-----------")

def removeUnzippedFiles(path):
    filesToRemove = getFileNames(path + "*")

    for file in filesToRemove:
        if ".pdf" in file:
            os.remove(file)

    print(path + " ---> CLEANED \n")

print("          ")
print("          ")
print("          ")
getFolderNames("/Users/gianluca/Desktop/test/")
unzip("/Users/gianluca/Desktop/test/11111/test.zip", "/Users/gianluca/Desktop/test/11111/")
fileNames = getFileNames("/Users/gianluca/Desktop/test/11111/")
compareFileName("22222", "33333", fileNames, "/Users/gianluca/Desktop/test/")
removeUnzippedFiles("/Users/gianluca/Desktop/test/11111/")
