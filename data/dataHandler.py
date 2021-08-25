#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################
#                               #
#   ----     SAVED      ----    #
#   ----     DATA       ----    #
#                               #
#################################

import os
import pathlib
from configparser import ConfigParser
import tkinter as tk
import shutil

# -------------------------------------- #
#      General                           #
# -------------------------------------- #

title = "RoarCalc"
version = 2
subversion = 2
subsubversion = 1

gitPath = "https://github.com/TheChangeOfView/RoarCalc"
gitReleasePath = "https://api.github.com/repos/TheChangeOfView/RoarCalc/releases"

completeVersion = str(version) + "." + str(subversion) + "." + str(subsubversion)
titleVersion = title + " " + completeVersion

updaterMaxAttempts = 20

# -------------------------------------- #
#      Language Variables                #
# -------------------------------------- #

langFiles = {}

dict_lang = {
    "lang_general_width"                                : "Width",
    "lang_general_height"                               : "Height",
    "lang_general_depth"                                : "Depth",
    "lang_general_length"                               : "Length",
    "lang_general_count"                                : "Count",
    "lang_general_type"                                 : "Type",
    "lang_general_override"                             : "Enable Override",
    "lang_general_position"                             : "Pos.",
    "lang_general_no"                                   : "No",
    "lang_general_yes"                                  : "Yes",
    "lang_general_none"                                 : "- - -",
    "lang_general_with"                                 : "With",
    "lang_general_without"                              : "Without",
    "lang_general_ID"                                   : "ID",
    "lang_general_name"                                 : "Name",
    "lang_frmGeneralInfo"                               : "General Info",
    "lang_genInfo_orderID"                              : "Order ID",
    "lang_genInfo_date"                                 : "Date",
    "lang_genInfo_pto"                                  : "Push-To-Open",
    "lang_genInfo_specials"                             : "Specials",
    "lang_frmMeasure"                                   : "Measurements",
    "lang_frmColor"                                     : "Colorcode",
    "lang_color_aluminum"                               : "Aluminum",
    "lang_color_unicolor"                               : "Unicolor",
    "lang_color_wood"                                   : "Wooden Replication",
    "lang_color_material"                               : "Material Replication",
    "lang_frmCorpusInfo"                                : "Corpus Info",
    "lang_corInfo_light"                                : "Light",
    "lang_corInfo_indLight"                             : "Indirect Light",
    "lang_corInfo_door"                                 : "Doors Amount",
    "lang_corInfo_shelf"                                : "Shelfs Amount",
    "lang_corInfo_overhangUpper"                        : "Overhang Upper",
    "lang_corInfo_overhangLower"                        : "Overhang Lower",
    "lang_frmExtra"                                     : "Extra Spaces",
    "lang_extra_measure"                                : "Width / Height",
    "lang_extra_covered"                                : "Covered",
    "lang_frmCorpusMeasure"                             : "Corpus Measurements",
    "lang_frmGlassMeasure"                              : "Glass / Mirror Measurements",
    "lang_frmPackaging"                                 : "Packaging",
    "lang_frmInfo"                                      : "Info",
    "lang_button_calc"                                  : "Calculate",
    "lang_button_reset"                                 : "Reset",
    "lang_button_create"                                : "Create PDF",
    "lang_button_load"                                  : "Load RC-File",
    "lang_button_settings"                              : "Settings",
    "lang_button_quit"                                  : "Quit",
    "lang_button_save"                                  : "Save",
    "lang_button_close"                                 : "Close",
    "lang_button_update"                                : "Check for updates",
    "lang_button_updateStart"                           : "Install update",
    "lang_button_github"                                : "View on GitHub",
    "lang_frmPrgInfo"                                   : "Program Info",
    "lang_prgInfo_contact"                              : "Contact Us",
    "lang_prgInfo_git"                                  : "Find us on GitHub",
    "lang_frmFileHandling"                              : "File Handling",
    "lang_fileHandling_saveDir"                         : "Save File at:",
    "lang_fileHandling_calculate"                       : "Calculate before creating PDF",
    "lang_fileHandling_RCFile"                          : "Save RC-File of project",
    "lang_fileHandling_openPDF"                         : "Open PDF after creation",
    "lang_fileHandling_printPDF"                        : "Print PDF after creation",
    "lang_fileHandling_files"                           : "Open Libaryfiles Folder",
    "lang_frmMatPresets"                                : "Material Thickness (in mm)",
    "lang_matPresets_packaging"                         : "Packaging",
    "lang_matPresets_wood"                              : "Wood",
    "lang_matPresets_aluminum"                          : "Aluminum",
    "lang_matPresets_LEDFrontal"                        : "Frontal LED Profile",
    "lang_matPresets_LEDInternal"                       : "Internal LED Profile",
    "lang_frmOther"                                     : "Other",
    "lang_other_autoUpdate"                             : "Auto-updatesearch",
    "lang_other_language"                               : "Language",
    "lang_other_info"                                   : "Restart to change language",
    "lang_frmUpdateInfo"                                : "Update Info",
    "lang_updateInfo_statusNone"                    	: "Could not check for updates",
    "lang_updateInfo_statusTrue"                    	: "New build available!",
    "lang_updateInfo_statusFalse"                   	: "You got the latest build!",
    "lang_updateInfo_versionUsed"                   	: "Current build:",
    "lang_updateInfo_versionLatest"                 	: "Latest build:",
    "lang_frmChangelog"                                 : "Changelog",
    "lang_changlog_false"                               : "No Changelog found!",
    "lang_frmUpdateSettings"                            : "Settings",
    "lang_updateSettings_experimental"                  : "Use experimental Builds",
    "lang_updateSettings_exportConfig"                  : "Export configurations to new version",
    "lang_updateSettings_exportDatabase"                : "Export database to new version",
    "lang_updateSettings_shortcut"                      : "Create desktop-shortcut after installation",
    "lang_msg_rcoverride"                               : "An associated RC-File already exists.\nDo you want to replace it?",
    "lang_msg_pdfoverride"                              : "An associated PDF-File already exists.\nDo you want to replace it?",
    "lang_msg_doorAmountInvalid"                        : "Calculating more then four doors is leading to misscalculations in most cases! Do you wish to calculate anyway?",
    "lang_data_corInfo_light_warm"                      : "Warm",
    "lang_data_corInfo_light_neutral"                   : "Neutral",
    "lang_data_corInfo_light_cct"                       : "CCT",
    "lang_data_corInfo_light_rgb"                       : "RGB",
    "lang_data_corpusMeasure_type_ground"               : "Ground",
    "lang_data_corpusMeasure_type_side"                 : "Side",
    "lang_data_corpusMeasure_type_middleground"         : "Middleground",
    "lang_data_corpusMeasure_type_middleside"           : "Middleside",
    "lang_data_corpusMeasure_type_MF_ground"            : "MF Ground",
    "lang_data_corpusMeasure_type_MF_side"              : "MF Side",
    "lang_data_corpusMeasure_type_backwall"             : "Backwall",
    "lang_data_corpusMeasure_type_ground_short"         : "G",
    "lang_data_corpusMeasure_type_side_short"           : "S",
    "lang_data_corpusMeasure_type_middleground_short"   : "MG",
    "lang_data_corpusMeasure_type_middleside_short"     : "MS",
    "lang_data_corpusMeasure_type_MF_ground_short"      : "MF G",
    "lang_data_corpusMeasure_type_MF_side_short"        : "MF S",
    "lang_data_corpusMeasure_type_backwall_short"       : "BW",
    "lang_data_extra_type_1vert"                        : "1 sided vertical",
    "lang_data_extra_type_2vert"                        : "2 sided vertical",
    "lang_data_extra_type_1hori"                        : "1 sided horizontal",
    "lang_data_genInfo_specials_LEDfrontal"             : "LED Frontal",
    "lang_data_genInfo_specials_LEDinternal"            : "LED Internal",
    "lang_data_genInfo_type_surface"                    : "SU",
    "lang_data_genInfo_type_concealed"                  : "CO",
    "lang_data_genInfo_type_concealedMF"                : "COMF",
    "lang_data_glassMeasure_type_mirror3"               : "3mm Mirror",
    "lang_data_glassMeasure_type_mirror6"               : "6mm Mirror",
    "lang_data_glassMeasure_type_glass6"                : "6mm Glass",
    "lang_error_calculation"                            : "Calculation Error:",
    "lang_error_inputs"                                 : "Missing requirements or invalid input",
    "lang_calc_success"                                 : "Calculation successed!",
    "lang_calc_failed"                                  : "Calculation failed!",
    "lang_creation_success"                             : "File creation successed!",
    "lang_creation_failed"                              : "File creation failed!",
    "lang_update_info"                                  : "RoarCalc will now install the latest version and restart automatically!\nThis Process can take a while!\n\nDo you want to continue?",
    "lang_textbox_info"                                 : "The info-text is longer then the PDF can handle properly to fit inside the frame! Do you still wish to continue?",
    "lang_menu_file"                                    : "File",
    "lang_menu_reset"                                   : "Reset",
    "lang_menu_open"                                    : "Open..",
    "lang_menu_save"                                    : "Save",
    "lang_menu_saveas"                                  : "Save as..",
    "lang_menu_quit"                                    : "Quit",
    "lang_menu_edit"                                    : "Edit",
    "lang_menu_calculate"                               : "Calculate",
    "lang_menu_create"                                  : "Create PDF",
    "lang_menu_opensave"                                : "Open Save Directory",
    "lang_menu_settings"                                : "Settings",
    "lang_menu_help"                                    : "Help",
    "lang_menu_github"                                  : "View on GitHub",
    "lang_menu_updates"                                 : "Check for updates"
}

# -------------------------------------- #
#      Tooltip Variables                 #
# -------------------------------------- #

dict_tooltips = {
    "tool_error"  :     "ERROR",

    # general info
    "tool_genInfo_orderID"          :     "The given order identification number of your project",
    "tool_genInfo_date"             :     "The creation date stamp (will take the set date of the running OS)",
    "tool_genInfo_type"             :     "The way the corpus is mounted on the wall (SU = Surface, CO = Concealed, COMF = Concealed with mounting frame)",
    "tool_genInfo_pto"              :     "Enable if your project has Push-To-Open doors",
    "tool_genInfo_specials"         :     "Changes the calculation to special kinds of corpus",

    # measure
    "tool_measure_width"            :     "The main width in mm of the corpus",
    "tool_measure_height"           :     "The main height in mm of the corpus",
    "tool_measure_depth"            :     "The main depth in mm of the corpus",

    # corpus info
    "tool_corInfo_light"            :     "Set the light color",
    "tool_corInfo_indLight"         :     "Enable if your project has indirect light",
    "tool_corInfo_doors"            :     "The amount of doors",
    "tool_corInfo_shelfs"           :     "The amount of shelfs per section",
    "tool_corInfo_overhangUpper"    :     "The overhang in mm on the top-end",
    "tool_corInfo_overhangLower"    :     "The overhang in mm on the lower-end",

    # extra space
    "tool_extra_type"               :     "Add extra sections",
    "tool_extra_measure"            :     "The given space for the sections",
    "tool_extra_covered"            :     "Enable if the extra sections are covered with mirrors",

    # color
    "tool_color_select"             :     "Select the color your project should have",
    "tool_color_showSelected"       :     "Shows the selected color",
    
    # corpus measurement
    "tool_corpusMeasurement"        :     "The measurements of the given board",

    # glass measurements
    "tool_glassMeasurement"         :     "The measurements of the given glass / mirror",

    # packaging
    "tool_packaging_width"          :     "The width in mm of the packaging",
    "tool_packaging_height"         :     "The height in mm of the packaging",
    "tool_packaging_depth"          :     "The depth in mm of the packaging",

    # buttons
    "tool_buttons_calc"             :     "Calculate measurements",
    "tool_buttons_reset"            :     "Reset all inputs and measurements",
    "tool_buttons_create"           :     "Create PDF-File (Also if enabled: calculate beforehand, open PDF-file afterwards, print PDF-file and create RC-file)",
    "tool_buttons_load"             :     "Load an saved RC-File",
    "tool_buttons_settings"         :     "Open the settings-menu",
    "tool_buttons_quit"             :     "Quit the Application",

    # other
    "tool_other_override"           :     "Enable override measurements (sections with enabled override, will not be overriden by calculation)",

    # text box
    "tool_textbox"                  :     "Add custom info text to display in the PDF-File"
}

# -------------------------------------- #
#      Settings                          #
# -------------------------------------- #

dict_config = {
    "savedir"                   : "",
    "calculatebeforecreate"     : True,
    "creatercfile"              : True,
    "openpdf"                   : True,
    "printpdf"                  : False,
    "packingmatthickness"       : 100,
    "woodenthickness"           : 19,
    "aluminumthickness"         : 16,
    "ledthicknessfrontal"       : 13,
    "ledthicknessinternal"      : 9,
    "activelang"                : "Program Standart",
    "woodensubtraction"         : 2.5,
    "aluminumsubtraction"       : 10.0
}

dict_updateConfig = {
    "autoaskupdate"             : True,
    "updaterexperimentalbuilds" : False,
    "updaterexportconfig"       : True,
    "updaterexportdatabase"     : True,
    "updatershortcut"           : True
}

# -------------------------------------- #
#      File Pathes                       #
# -------------------------------------- #

# general Info
rootDir = pathlib.Path(os.path.abspath(os.path.realpath(__file__))).parent.parent

# get parent of directory if programm is started as executable
rootFile = os.path.split(rootDir)
if rootFile[len(rootFile) - 1] == "library.zip":
    rootDir = pathlib.Path(rootDir).parent

filesDir = os.path.join(rootDir, "files")
langDir = os.path.join(rootDir, "lang")
imgDir = os.path.join(filesDir, "img")
databaseDir = os.path.join(filesDir, "database")
tmpDir = os.path.join(rootDir, "tmp")

fPth_imageAluminum = os.path.join(imgDir,"img_color_aluminum.png")
fPth_imageUnicolor = os.path.join(imgDir, "img_color_unicolor.png")
fPth_imageWood = os.path.join(imgDir, "img_color_wood.png")
fPth_imageMaterial = os.path.join(imgDir, "img_color_material.png")

fPth_codesAluminum = os.path.join(databaseDir, "data_colorcodes_aluminum.txt")
fPth_codesUnicolor = os.path.join(databaseDir, "data_colorcodes_unicolor.txt")
fPth_codesWood = os.path.join(databaseDir, "data_colorcodes_wood.txt")
fPth_codesMaterial = os.path.join(databaseDir, "data_colorcodes_material.txt")

fPth_logo = os.path.join(imgDir, "ico_logo.ico")
fPth_logoImg = os.path.join(imgDir, "img_logo.png")

fPth_config = os.path.join(filesDir, "config.ini")

fPth_formOrig = os.path.join(filesDir, "form_blank.pdf")
fPth_formOvrl = os.path.join(rootDir, "form_overlay.pdf")
fPth_output = os.path.join(rootDir, "output.pdf")

fPth_fnt_NormalTTF = os.path.join(rootDir, "Vera.ttf")
fPth_fnt_BoldTTF = os.path.join(rootDir, "VeraBd.ttf")

fPth_update = os.path.join(rootDir, "update.ini")

fnt_Normal = "Vera"
fnt_NormalTTF = "Vera.ttf"
fnt_Bold = "Vera-Bold"
fnt_BoldTTF = "VeraBd.ttf"

# -------------------------------------- #
#      Functions                         #
# -------------------------------------- #

# --- initial routine ---

def initRoutine():

    missing = checkFiles()

    if missing != None:

        root = tk.Tk()
        root.withdraw()

        tk.messagebox.showerror(title = titleVersion, message = "Fatal Error: Missing: " + missing)

        root.destroy()

        return False

    else:

        if checkConfigINI() == False:

            root = tk.Tk()
            root.withdraw()

            tk.messagebox.showerror(title = titleVersion, message = "Error: config file is corrupted! Settings has been reseted to standart!")
            
            root.destroy()
            
            writeConfigINI()

        else:

            readConfigINI()

        getLanguageFiles()

        if getActiveLanguageAndCheck() == False:

            root = tk.Tk()
            root.withdraw()

            tk.messagebox.showerror(title = titleVersion, message = "Error: language file is corrupted! Used Language has been reseted to standart!")

            root.destroy()

        return True

def checkFiles():

    missing = None

    allDir = [
        filesDir,
        imgDir,
        databaseDir
    ]

    for i in allDir:
        
        if os.path.isdir(i) == False:

            dirPath = os.path.split(i)
            dirName = dirPath[len(dirPath) - 1]

            missing = dirName

            break

    if missing != None: # skip if already failed

        allFiles = [
            fPth_imageAluminum,
            fPth_imageUnicolor,
            fPth_imageWood,
            fPth_imageMaterial,
            fPth_codesAluminum,
            fPth_codesUnicolor,
            fPth_codesWood,
            fPth_codesMaterial,
            fPth_logo,
            fPth_logoImg,
            fPth_config,
            fPth_formOrig,
            fPth_fnt_NormalTTF,
            fPth_fnt_BoldTTF
        ]

        for i in allFiles:
            
            if os.path.isfile(i) == False:

                filePath = os.path.split(i)
                fileName = filePath[len(filePath) - 1]

                missing = fileName

                break

    return missing

# --- language

def getLanguageFiles():

    if os.path.isdir(langDir) == False:

        return False

    fileList = os.listdir(langDir)

    for file in fileList:

        fileSplit = file.split(".")

        if fileSplit[len(fileSplit) - 1] == "rcl":

            filePath = os.path.join(langDir, file)

            try:

                lang = ConfigParser()

                lang.read(filePath, "UTF-8")

                info = lang["info"]

                langName = info["langName"].replace('"',"")

                langFiles[langName] = file

            except KeyError:

                pass

def getActiveLanguageAndCheck():

    global dict_config

    if dict_config["activelang"] != "Program Standart":

        try:

            langFile = os.path.join(langDir, langFiles[dict_config["activelang"]])

            if checkLangFile(langFile) == False:

                dict_config["activelang"] = "Program Standart"

                writeConfigINI()

                return False

            readLangFile(langFile)

            return True

        except KeyError:

            dict_config["activelang"] = "Program Standart"

            writeConfigINI()

            return False

def checkLangFile(langFile):

    lang = ConfigParser()

    lang.read(langFile)

    for entry in dict_lang:

        if entry not in lang["language"]:

            return False

    for entry in dict_tooltips:

        if entry not in lang["tooltip"]:

            return False

    return True

def readLangFile(langFile):

    lang = ConfigParser()
    lang.optionxform = str

    lang.read(langFile, "UTF-8")

    # language section

    for entry in lang["language"]:

        dict_lang[entry] = lang["language"][entry].replace('"', "")

    # tooltip section

    for entry in lang["tooltip"]:

        dict_tooltips[entry] = lang["tooltip"][entry].replace('"', "")

# --- config ---

def checkConfigINI():

    # create ini if none exists

    if os.path.isfile(fPth_config) == False:

        writeConfigINI()
        return

    # else check

    config = ConfigParser()

    config.read(fPth_config)

    for entry in dict_config:

        if entry not in config["presets"]:

            return False

    for entry in dict_updateConfig:

        if entry not in config["updater"]:

            return False

    return True

def readConfigINI():

    # create ini if none exists

    if os.path.isfile(fPth_config) == False:

        writeConfigINI()
        return

    # read ini

    global dict_config
    global dict_updateConfig

    dict_config.clear()
    dict_updateConfig.clear()

    config = ConfigParser()

    config.read(fPth_config)

    for section in config:

        for entry in config[section]:

            cont = config[section][entry]

            try:

                if cont[0] == "{":

                    out = int(cont[ 1 : (len(cont) - 1) ])

                elif cont[0] == "<":

                    out = bool(int(cont[ 1 : (len(cont) - 1) ]))

                elif cont[0] == "[":

                    out = float(cont[ 1 : (len(cont) - 1) ])

                else:

                    out = cont

            except IndexError:

                out = cont

            if section == "presets":

                dict_config[entry] = out

            elif section == "updater":

                dict_updateConfig[entry] = out

def writeConfigINI():

    config = ConfigParser()

    config["presets"] = {

        "packingmatthickness"   : "{" + str(dict_config["packingmatthickness"])        + "}",
        "woodenthickness"       : "{" + str(dict_config["woodenthickness"])            + "}",
        "aluminumthickness"     : "{" + str(dict_config["aluminumthickness"])          + "}",
        "ledthicknessfrontal"   : "{" + str(dict_config["ledthicknessfrontal"])        + "}",
        "ledthicknessinternal"  : "{" + str(dict_config["ledthicknessinternal"])       + "}",
        "savedir"               :       str(dict_config["savedir"])                         ,
        "calculatebeforecreate" : "<" + str(int(dict_config["calculatebeforecreate"])) + ">",
        "creatercfile"          : "<" + str(int(dict_config["creatercfile"]))          + ">",
        "openpdf"               : "<" + str(int(dict_config["openpdf"]))               + ">",
        "printpdf"              : "<" + str(int(dict_config["printpdf"]))              + ">",
        "activelang"            :       str(dict_config["activelang"])                      ,
        "woodensubtraction"     : "[" + str(dict_config["woodensubtraction"])          + "]",
        "aluminumsubtraction"   : "[" + str(dict_config["aluminumsubtraction"])        + "]"

    }

    config["updater"] = {

        "autoaskupdate"             : "<" + str(int(dict_updateConfig["autoaskupdate"]))             + ">",
        "updaterexperimentalbuilds" : "<" + str(int(dict_updateConfig["updaterexperimentalbuilds"])) + ">",
        "updaterexportconfig"       : "<" + str(int(dict_updateConfig["updaterexportconfig"]))       + ">",
        "updaterexportdatabase"     : "<" + str(int(dict_updateConfig["updaterexportdatabase"]))     + ">",
        "updatershortcut"           : "<" + str(int(dict_updateConfig["updatershortcut"]))           + ">"

    }

    with open(fPth_config, "w") as configfile:

        config.write(configfile)

# --- rc-file ---

def writeRCFile(filePath = None):

    from data import uiHandler

    if filePath != None:

        fPth_rcOutput = filePath

    else:

        rcfOut = None

        if dict_config["savedir"] == "":

            fileOut = os.path.join(os.curdir, "output")

            if os.path.isdir(fileOut) == False:

                os.mkdir(fileOut)

            rcfOut = os.path.join(fileOut, "rcf")

            if os.path.isdir(rcfOut) == False:

                os.mkdir(rcfOut)

        else:

            rcfOut = os.path.join(dict_config["savedir"], "rcf")

            if os.path.isdir(rcfOut) == False:

                os.mkdir(rcfOut)

        rcFileName = "project.rcf"

        if uiHandler.ety_genInfo_orderIDVar.get() != "":

            rcFileName = uiHandler.ety_genInfo_orderIDVar.get() + ".rcf"

        fPth_rcOutput = os.path.join(rcfOut, rcFileName)

        if os.path.isfile(fPth_rcOutput) == True:

            if tk.messagebox.askyesno(title = titleVersion, message = dict_lang["lang_msg_rcoverride"]) == False:

                return

    rcfiler = ConfigParser()

    rcfiler["general"] = {
        "orderid"       : uiHandler.ety_genInfo_orderIDVar.get(),
        "type"          : uiHandler.cbb_genInfo_type.current(),
        "pto"           : uiHandler.cbt_genInfo_ptoVar.get(),
        "specials"      : uiHandler.cbb_genInfo_specials.current(),
        "color"         : uiHandler.ety_color_selectedVar.get(),
        "colortype"     : uiHandler.lastSelectedListbox,
        "colorindex"    : uiHandler.lastSelectedListboxItem
    }

    rcfiler["measure"] = {
        "mainwidth"     : uiHandler.ety_measure_widthVar.get(),
        "mainheight"    : uiHandler.ety_measure_heightVar.get(),
        "maindepth"     : uiHandler.ety_measure_depthVar.get(),
    }

    rcfiler["corpus"] = {
        "light"         : uiHandler.cbb_corInfo_light.current(),
        "indlight"      : uiHandler.cbt_genInfo_ptoVar.get(),
        "doors"         : uiHandler.ety_corInfo_doorVar.get(),
        "shelfs"        : uiHandler.ety_corInfo_shelfVar.get(),
        "overUpper"     : uiHandler.ety_corInfo_overhangUpperVar.get(),
        "overLower"     : uiHandler.ety_corInfo_overhangLowerVar.get()
    }

    rcfiler["extra"] = {
        "type"          : uiHandler.cbb_extra_type.current(),
        "measure"       : uiHandler.ety_extra_measureVar.get(),
        "covered"       : uiHandler.cbt_extra_coveredVar.get()
    }

    rcfiler["corpusmeasure"] = {
        "p1length"      : uiHandler.ety_corpusMeasure_pos1lengthVar.get(),
        "p2length"      : uiHandler.ety_corpusMeasure_pos2lengthVar.get(),
        "p3length"      : uiHandler.ety_corpusMeasure_pos3lengthVar.get(),
        "p4length"      : uiHandler.ety_corpusMeasure_pos4lengthVar.get(),
        "p5length"      : uiHandler.ety_corpusMeasure_pos5lengthVar.get(),
        "p6length"      : uiHandler.ety_corpusMeasure_pos6lengthVar.get(),
        "p7length"      : uiHandler.ety_corpusMeasure_pos7lengthVar.get(),
        "p8length"      : uiHandler.ety_corpusMeasure_pos8lengthVar.get(),
        "p1width"       : uiHandler.ety_corpusMeasure_pos1widthVar.get(),
        "p2width"       : uiHandler.ety_corpusMeasure_pos2widthVar.get(),
        "p3width"       : uiHandler.ety_corpusMeasure_pos3widthVar.get(),
        "p4width"       : uiHandler.ety_corpusMeasure_pos4widthVar.get(),
        "p5width"       : uiHandler.ety_corpusMeasure_pos5widthVar.get(),
        "p6width"       : uiHandler.ety_corpusMeasure_pos6widthVar.get(),
        "p7width"       : uiHandler.ety_corpusMeasure_pos7widthVar.get(),
        "p8width"       : uiHandler.ety_corpusMeasure_pos8widthVar.get(),
        "p1count"       : uiHandler.ety_corpusMeasure_pos1countVar.get(),
        "p2count"       : uiHandler.ety_corpusMeasure_pos2countVar.get(),
        "p3count"       : uiHandler.ety_corpusMeasure_pos3countVar.get(),
        "p4count"       : uiHandler.ety_corpusMeasure_pos4countVar.get(),
        "p5count"       : uiHandler.ety_corpusMeasure_pos5countVar.get(),
        "p6count"       : uiHandler.ety_corpusMeasure_pos6countVar.get(),
        "p7count"       : uiHandler.ety_corpusMeasure_pos7countVar.get(),
        "p8count"       : uiHandler.ety_corpusMeasure_pos8countVar.get(),
        "p1type"        : uiHandler.cbb_corpusMeasure_pos1type.current(),
        "p2type"        : uiHandler.cbb_corpusMeasure_pos2type.current(),
        "p3type"        : uiHandler.cbb_corpusMeasure_pos3type.current(),
        "p4type"        : uiHandler.cbb_corpusMeasure_pos4type.current(),
        "p5type"        : uiHandler.cbb_corpusMeasure_pos5type.current(),
        "p6type"        : uiHandler.cbb_corpusMeasure_pos6type.current(),
        "p7type"        : uiHandler.cbb_corpusMeasure_pos7type.current(),
        "p8type"        : uiHandler.cbb_corpusMeasure_pos8type.current()
    }

    rcfiler["glassmeasure"] = {
        "p1length"      : uiHandler.ety_glassMeasure_pos1lengthVar.get(),
        "p2length"      : uiHandler.ety_glassMeasure_pos2lengthVar.get(),
        "p3length"      : uiHandler.ety_glassMeasure_pos3lengthVar.get(),
        "p4length"      : uiHandler.ety_glassMeasure_pos4lengthVar.get(),
        "p5length"      : uiHandler.ety_glassMeasure_pos5lengthVar.get(),
        "p6length"      : uiHandler.ety_glassMeasure_pos6lengthVar.get(),
        "p7length"      : uiHandler.ety_glassMeasure_pos7lengthVar.get(),
        "p8length"      : uiHandler.ety_glassMeasure_pos8lengthVar.get(),
        "p1width"       : uiHandler.ety_glassMeasure_pos1widthVar.get(),
        "p2width"       : uiHandler.ety_glassMeasure_pos2widthVar.get(),
        "p3width"       : uiHandler.ety_glassMeasure_pos3widthVar.get(),
        "p4width"       : uiHandler.ety_glassMeasure_pos4widthVar.get(),
        "p5width"       : uiHandler.ety_glassMeasure_pos5widthVar.get(),
        "p6width"       : uiHandler.ety_glassMeasure_pos6widthVar.get(),
        "p7width"       : uiHandler.ety_glassMeasure_pos7widthVar.get(),
        "p8width"       : uiHandler.ety_glassMeasure_pos8widthVar.get(),
        "p1count"       : uiHandler.ety_glassMeasure_pos1countVar.get(),
        "p2count"       : uiHandler.ety_glassMeasure_pos2countVar.get(),
        "p3count"       : uiHandler.ety_glassMeasure_pos3countVar.get(),
        "p4count"       : uiHandler.ety_glassMeasure_pos4countVar.get(),
        "p5count"       : uiHandler.ety_glassMeasure_pos5countVar.get(),
        "p6count"       : uiHandler.ety_glassMeasure_pos6countVar.get(),
        "p7count"       : uiHandler.ety_glassMeasure_pos7countVar.get(),
        "p8count"       : uiHandler.ety_glassMeasure_pos8countVar.get(),
        "p1type"        : uiHandler.cbb_glassMeasure_pos1type.current(),
        "p2type"        : uiHandler.cbb_glassMeasure_pos2type.current(),
        "p3type"        : uiHandler.cbb_glassMeasure_pos3type.current(),
        "p4type"        : uiHandler.cbb_glassMeasure_pos4type.current(),
        "p5type"        : uiHandler.cbb_glassMeasure_pos5type.current(),
        "p6type"        : uiHandler.cbb_glassMeasure_pos6type.current(),
        "p7type"        : uiHandler.cbb_glassMeasure_pos7type.current(),
        "p8type"        : uiHandler.cbb_glassMeasure_pos8type.current()
    }

    rcfiler["packaging"] = {
        "packwidth"     : uiHandler.ety_packaging_widthVar.get(),
        "packheight"    : uiHandler.ety_packaging_heightVar.get(),
        "packdepth"     : uiHandler.ety_packaging_depthVar.get()
    }

    with open(fPth_rcOutput, "w") as rcfile:

        rcfiler.write(rcfile)

    return True

# --- tmp-Folder ---

def createTmpFolder():

    if os.path.isdir(tmpDir) == False:

        os.mkdir(tmpDir)
        return True

    else:

        return False

def deleteTmpFolder():

    if os.path.isdir(tmpDir) == True:

        shutil.rmtree(tmpDir)
        return True

    else:

        return False