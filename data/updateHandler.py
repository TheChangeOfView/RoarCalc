#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data import dataHandler

import requests
import os
import pathlib
import zipfile
import shutil
from configparser import ConfigParser
import time
from swinlnk.swinlnk import SWinLnk

# -------------------------------------------------------------------- #

def continueUpdate():

    update = ConfigParser()

    update.read(dataHandler.fPth_update)

    currentbuild = int(str(dataHandler.version) + str(dataHandler.subversion) + str(dataHandler.subsubversion))

    if currentbuild == int(update["update"]["newversion"]):

        updateState = deinstallOldRelease(update["update"]["oldpath"])

        if dataHandler.updaterShortcut == True:

            createShortcut()

        return updateState

    else:

        return False

def getReleases():

    response = requests.get(dataHandler.gitReleasePath)

    releasesList = list()

    releaseLatest = None
    releaseExperimental = None

    i = 0
    final = None

    while final == None and i < dataHandler.updaterMaxAttempts:

        try:

            release = response.json()[i]

            if release["prerelease"] == True:

                if releaseExperimental == None:
                    releaseExperimental = release

            else:

                if releaseLatest == None:
                    releaseLatest = release
                    final = True

            i += 1
        
        except IndexError:

            final = False

    return releaseLatest, releaseExperimental

def getChangelog(build):

    buildVersionList = str(build["tag_name"]).split(".")
    buildVersion = buildVersionList[0] + "_" + buildVersionList[1] + "_" + buildVersionList[2]

    changelogName = "changelog_" + buildVersion + ".txt"

    changelogPath = os.path.join(dataHandler.fold_tmp, changelogName)

    if os.path.isfile(changelogPath) == True:

        return changelogPath

    else:

        i = 0
        final = None

        while final == None and i < dataHandler.updaterMaxAttempts:

            try:

                fileName = build["assets"][i]["name"]

                if fileName == "changelog.txt":

                    dataHandler.createTmpFolder()

                    response = requests.get(build["assets"][i]["browser_download_url"], allow_redirects = True)

                    dlFile = open(changelogPath, "wb").write(response.content)

                    return changelogPath

                i += 1

            except IndexError:

                return None

def downloadRelease(build):

    updaterPath = os.path.join(dataHandler.fold_tmp, "update.zip")

    i = 0
    final = None

    while final == None and i < dataHandler.updaterMaxAttempts:

        try:

            extensionList = str(build["assets"][i]["name"]).split(".")

            extension = extensionList[len(extensionList) - 1]

            if extension == "zip":

                dataHandler.createTmpFolder()

                response = requests.get(build["assets"][i]["browser_download_url"], allow_redirects = True)

                dlFile = open(updaterPath, "wb").write(response.content)

                return updaterPath

            i += 1

        except IndexError:

            return None

def installRelease(zipPath, build):

    buildVersion = str(build["tag_name"]).replace(".", "_")

    # unpack release
    folderPath = unpackRelease(zipPath)

    # move files
    dirList = os.listdir(folderPath)
    srcPath = os.path.abspath(os.path.join(folderPath, dirList[0]))
    dstPath = pathlib.Path(os.path.abspath(folderPath)).parent.parent.parent

    movePath = shutil.move(srcPath, dstPath)

    # create Update.ini
    iniPath = os.path.join(movePath, "update.ini")
    curdir = os.path.abspath(os.curdir)
    newbuild = int(buildVersion.replace("_", ""))

    createUpdateINI(iniPath, curdir, newbuild)

    time.sleep(5)

    # move config and database
    if dataHandler.updaterExportConfig == True and dataHandler.configIsCompatible == True:

        src = os.path.join(os.path.abspath(os.curdir), "files", "config.ini")
        dst = os.path.join(movePath, "files", "config.ini")
        os.remove(dst)
        shutil.copy(src, dst)

    if dataHandler.updaterExportDatabase == True and dataHandler.databaseIsCompatible == True:

        src = os.path.join(os.path.abspath(os.curdir), "files", "database")
        dst = os.path.join(movePath, "files", "database")
        shutil.rmtree(dst)
        shutil.copytree(src, dst)

    return os.path.join(movePath, "RoarCalc.exe")

def deinstallOldRelease(path):

    time.sleep(3)

    try:

        shutil.rmtree(path)

    except PermissionError:

        return "permError"

    return True

def unpackRelease(zipPath):

    extractPath = os.path.join(pathlib.Path(zipPath).parent, "update")

    with zipfile.ZipFile(zipPath, "r") as update_zip:

        update_zip.extractall(extractPath)

    return extractPath

def createUpdateINI(iniPath, curdir, build):

    update = ConfigParser()

    update["update"] = {

        "oldpath" : curdir,
        "newversion" : build

    }

    with open(iniPath, "w") as updatefile:

        update.write(updatefile)

def createShortcut():

    desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")

    lnkPath = os.path.join(desktop, "RoarCalc.lnk")

    if os.path.islink(lnkPath) == True:

        os.remove(lnkPath)

    exePath = os.path.join(dataHandler.rootDir, "RoarCalc.exe")
    scrPath = os.path.join(desktop, "rc_scr.ps1")
    
    swl = SWinLnk()

    swl.create_lnk(exePath, lnkPath)
