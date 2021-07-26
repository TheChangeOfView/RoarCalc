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
from tkinter import messagebox as tkmsg
import shutil

# -------------------------------------- #
#      General                           #
# -------------------------------------- #

title = "RoarCalc"
version = 2
subversion = 1
subsubversion = 0
configIsCompatible = True
databaseIsCompatible = True

gitPath = "https://github.com/TheChangeOfView/RoarCalc"
gitReleasePath = "https://api.github.com/repos/TheChangeOfView/RoarCalc/releases"

completeVersion = str(version) + "." + str(subversion) + "." + str(subsubversion)
titleVersion = title + " " + completeVersion

updaterMaxAttempts = 20

# -------------------------------------- #
#      Language Variables                #
# -------------------------------------- #

lang_general_width = "Width"
lang_general_height = "Height"
lang_general_depth = "Depth"
lang_general_length = "Length"
lang_general_count = "Count"
lang_general_type = "Type"
lang_general_override = "Enable Override"
lang_general_position = "Pos."
lang_general_no = "No"
lang_general_yes = "Yes"
lang_general_none = "- - -"
lang_general_with = "With"
lang_general_without = "Without"
lang_general_ID = "ID"
lang_general_name = "Name"

lang_frmGeneralInfo = "General Info"
lang_genInfo_orderID = "Order ID"
lang_genInfo_date = "Date"
lang_genInfo_pto = "Push-To-Open"
lang_genInfo_specials = "Specials"

lang_frmMeasure = "Measurements"

lang_frmColor = "Colorcode"
lang_color_aluminum = "Aluminum"
lang_color_unicolor = "Unicolor"
lang_color_wood = "Wooden Replication"
lang_color_material = "Material Replication"

lang_frmCorpusInfo = "Corpus Info"
lang_corInfo_light = "Light"
lang_corInfo_indLight = "Indirect Light"
lang_corInfo_door = "Doors Amount"
lang_corInfo_shelf = "Shelfs Amount"
lang_corInfo_overhangUpper = "Overhang Upper"
lang_corInfo_overhangLower = "Overhang Lower"

lang_frmExtra = "Extra Spaces"
lang_extra_measure = "Width / Height"
lang_extra_covered = "Covered"

lang_frmCorpusMeasure = "Corpus Measurements"

lang_frmGlassMeasure = "Glass / Mirror Measurements"

lang_frmPackaging = "Packaging"

lang_frmInfo = "Info"

lang_button_calc = "Calculate"
lang_button_reset = "Reset"
lang_button_create = "Create PDF"
lang_button_load = "Load RC-File"
lang_button_settings = "Settings"
lang_button_quit = "Quit"
lang_button_save = "Save"
lang_button_close = "Close"
lang_button_update = "Check for updates"
lang_button_updateStart = "Install update"
lang_button_github = "View on GitHub"

lang_frmPrgInfo = "Program Info"
lang_prgInfo_contact = "Contact Us"
lang_prgInfo_git = "Find us on GitHub"

lang_frmFileHandling = "File Handling"
lang_fileHandling_saveDir = "Save File at:"
lang_fileHandling_calculate = "Calculate before creating PDF"
lang_fileHandling_RCFile = "Save RC-File of project"
lang_fileHandling_openPDF = "Open PDF after creation"
lang_fileHandling_printPDF = "Print PDF after creation"
lang_fileHandling_files = "Open Libaryfiles Folder"

lang_frmMatPresets = "Material Thickness (in mm)"
lang_matPresets_packaging = "Packaging"
lang_matPresets_wood = "Wood"
lang_matPresets_aluminum = "Aluminum"
lang_matPresets_LEDFrontal = "Frontal LED Profile"
lang_matPresets_LEDInternal = "Internal LED Profile"

lang_frmOther = "Other"
lang_other_autoUpdate = "Auto-updatesearch"
lang_other_language = "Language file directory"
lang_other_info = "Restart to change language"

lang_frmUpdateInfo = "Update Info"
lang_updateInfo_statusNone = "Could not check for updates"
lang_updateInfo_statusTrue = "New build available!"
lang_updateInfo_statusFalse = "You got the latest build!"
lang_updateInfo_versionUsed = "Current build:"
lang_updateInfo_versionLatest = "Latest build:"

lang_frmChangelog = "Changelog"
lang_changlog_false = "No Changelog found!"

lang_frmUpdateSettings = "Settings"
lang_updateSettings_experimental = "Use experimental Builds"
lang_updateSettings_exportConfig = "Export configurations to new version"
lang_updateSettings_exportDatabase = "Export database to new version"
lang_updateSettings_shortcut = "Create desktop-shortcut after installation"

lang_msg_rcoverride = "An associated RC-File already exists.\nDo you want to replace it?"
lang_msg_pdfoverride = "An associated PDF-File already exists.\nDo you want to replace it?"
lang_msg_doorAmountInvalid = "Calculating more then four doors is leading to misscalculations in most cases! Do you wish to calculate anyway?"

lang_data_corInfo_light_warm = "Warm"
lang_data_corInfo_light_neutral = "Neutral"
lang_data_corInfo_light_cct = "CCT"
lang_data_corInfo_light_rgb = "RGB"

lang_data_corpusMeasure_type_ground = "Ground"
lang_data_corpusMeasure_type_side = "Side"
lang_data_corpusMeasure_type_middleground = "Middleground"
lang_data_corpusMeasure_type_middleside = "Middleside"
lang_data_corpusMeasure_type_MF_ground = "MF Ground"
lang_data_corpusMeasure_type_MF_side = "MF Side"
lang_data_corpusMeasure_type_backwall = "Backwall"

lang_data_corpusMeasure_type_ground_short = "G"
lang_data_corpusMeasure_type_side_short = "S"
lang_data_corpusMeasure_type_middleground_short = "MG"
lang_data_corpusMeasure_type_middleside_short = "MS"
lang_data_corpusMeasure_type_MF_ground_short = "MF G"
lang_data_corpusMeasure_type_MF_side_short = "MF S"
lang_data_corpusMeasure_type_backwall_short = "BW"

lang_data_extra_type_1vert = "1 sided vertical"
lang_data_extra_type_2vert = "2 sided vertical"
lang_data_extra_type_1hori = "1 sided horizontal"

lang_data_genInfo_specials_LEDfrontal = "LED Frontal"
lang_data_genInfo_specials_LEDinternal = "LED Internal"

lang_data_genInfo_type_surface = "SU"
lang_data_genInfo_type_concealed = "CO"
lang_data_genInfo_type_concealedMF = "COMF"

lang_data_glassMeasure_type_mirror3 = "3mm Mirror"
lang_data_glassMeasure_type_mirror6 = "6mm Mirror"
lang_data_glassMeasure_type_glass6 = "6mm Glass"

lang_error_calculation = "Calculation Error:"
lang_error_inputs = "Missing requirements or invalid input"

lang_calc_success = "Calculation successed!"
lang_calc_failed = "Calculation failed!"
lang_creation_success = "File creation successed!"
lang_creation_failed = "File creation failed!"

lang_update_info = "RoarCalc will now install the latest version and restart automatically!\nThis Process can take a while!\n\nDo you want to continue?"

# -------------------------------------- #
#      Tooltip Variables                 #
# -------------------------------------- #

dict_tooltips = {
    0  :     "ERROR",

    # general info
    1  :     "The given order identification number of your project",
    2  :     "The creation date stamp (will take the set date of the running OS)",
    3  :     "The way the corpus is mounted on the wall (SU = Surface, CO = Concealed, COMF = Concealed with mounting frame)",
    4  :     "Enable if your project has Push-To-Open doors",
    5  :     "Changes the calculation to special kinds of corpus",

    # measure
    6  :     "The main width in mm of the corpus",
    7  :     "The main height in mm of the corpus",
    8  :     "The main depth in mm of the corpus",

    # corpus info
    9  :     "Set the light color",
    10 :     "Enable if your project has indirect light",
    11 :     "The amount of doors",
    12 :     "The amount of shelfs per section",
    13 :     "The overhang in mm on the top-end",
    14 :     "The overhang in mm on the lower-end",

    # extra space
    15 :     "Add extra sections",
    16 :     "The given space for the sections",
    17 :     "Enable if the extra sections are covered with mirrors",

    # color
    18 :     "Select the color your project should have",
    19 :     "Shows the selected color",
    
    # corpus measurement
    20 :     "The measurements of the given board",

    # glass measurements
    21 :     "The measurements of the given glass / mirror",

    # packaging
    22 :     "The width in mm of the packaging",
    23 :     "The height in mm of the packaging",
    24 :     "The depth in mm of the packaging",

    # buttons
    25 :     "Calculate measurements",
    26 :     "Reset all inputs and measurements",
    27 :     "Create PDF-File (Also if enabled: calculate beforehand, open PDF-file afterwards, print PDF-file and create RC-file)",
    28 :     "Load an saved RC-File",
    29 :     "Open the settings-menu",
    30 :     "Quit the Application",

    # other
    31 :     "Enable override measurements (sections with enabled override, will not be overriden by calculation)",

    # text box
    32 :     "Add custom info text to display in the PDF-File"
}

# -------------------------------------- #
#      Settings                          #
# -------------------------------------- #

saveDir = ""
calculateBeforeCreate = True
createRCFile = True
openPDF = True
printPDF = False
packingMatThickness = 100
woodenThickness = 19
aluminiumThickness = 16
LEDThicknessFrontal = 13
LEDThicknessInternal = 9
activeLang = ""

woodenSubtraction = 2.5
aluminiumSubtraction = 10

autoaskUpdate = True
updaterExperimentalBuilds = False
updaterExportConfig = True
updaterExportDatabase = True
updaterShortcut = True

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
imgDir = os.path.join(filesDir, "img")
databaseDir = os.path.join(filesDir, "database")

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

fold_tmp = "./tmp"

# -------------------------------------- #
#      Functions                         #
# -------------------------------------- #

def checkFiles():

    allDir = [
        filesDir,
        imgDir,
        databaseDir
    ]

    for i in allDir:
        
        if os.path.isdir(i) == False:

            dirPath = os.path.split(i)
            dirName = dirPath[len(dirPath) - 1]

            return False, dirName, True

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
            
            return False, fileName, False

    return True, None, None

def getLanguage():

    checkLanguage()

    if activeLang != "":

        readLangFile(activeLang)

def checkLanguage(onlyCheck = False):

    global activeLang

    if activeLang != "":

        if os.path.isfile(activeLang) == False:

            activeLang = ""

            if onlyCheck == False:

                writeConfigINI()

def readLangFile(langFile):

    global lang_general_width
    global lang_general_height
    global lang_general_depth
    global lang_general_length
    global lang_general_count
    global lang_general_type
    global lang_general_override
    global lang_general_position
    global lang_general_no
    global lang_general_yes
    global lang_general_none
    global lang_general_with
    global lang_general_without
    global lang_general_ID
    global lang_general_name
    global lang_frmGeneralInfo
    global lang_genInfo_orderID
    global lang_genInfo_date
    global lang_genInfo_pto
    global lang_genInfo_specials
    global lang_frmColor
    global lang_color_aluminum
    global lang_color_unicolor
    global lang_color_wood
    global lang_color_material
    global lang_frmMeasure
    global lang_frmCorpusInfo
    global lang_corInfo_light
    global lang_corInfo_indLight
    global lang_corInfo_door
    global lang_corInfo_shelf
    global lang_corInfo_overhangUpper
    global lang_corInfo_overhangLower
    global lang_frmExtra
    global lang_extra_measure
    global lang_extra_covered
    global lang_frmCorpusMeasure
    global lang_frmGlassMeasure
    global lang_frmPackaging
    global lang_frmInfo
    global lang_button_calc
    global lang_button_reset
    global lang_button_create
    global lang_button_load
    global lang_button_settings
    global lang_button_quit
    global lang_button_save
    global lang_button_close
    global lang_button_update
    global lang_button_updateStart
    global lang_button_github
    global lang_frmPrgInfo
    global lang_prgInfo_contact
    global lang_prgInfo_git
    global lang_frmFileHandling
    global lang_fileHandling_saveDir
    global lang_fileHandling_calculate
    global lang_fileHandling_RCFile
    global lang_fileHandling_openPDF
    global lang_fileHandling_files
    global lang_frmMatPresets
    global lang_matPresets_packaging
    global lang_matPresets_wood
    global lang_matPresets_aluminum
    global lang_matPresets_LEDFrontal
    global lang_matPresets_LEDInternal
    global lang_frmOther
    global lang_other_autoUpdate
    global lang_other_language
    global lang_other_info
    global lang_frmUpdateInfo
    global lang_updateInfo_statusNone
    global lang_updateInfo_statusTrue
    global lang_updateInfo_statusFalse
    global lang_updateInfo_versionUsed
    global lang_updateInfo_versionLatest
    global lang_frmChangelog
    global lang_changlog_false
    global lang_frmUpdateSettings
    global lang_updateSettings_experimental
    global lang_updateSettings_exportConfig
    global lang_updateSettings_exportDatabase
    global lang_updateSettings_shortcut
    global lang_msg_rcoverride
    global lang_msg_pdfoverride
    global lang_msg_doorAmountInvalid
    global lang_data_corInfo_light_warm
    global lang_data_corInfo_light_neutral
    global lang_data_corInfo_light_cct
    global lang_data_corInfo_light_rgb
    global lang_data_corpusMeasure_type_ground
    global lang_data_corpusMeasure_type_side
    global lang_data_corpusMeasure_type_middleground
    global lang_data_corpusMeasure_type_middleside
    global lang_data_corpusMeasure_type_MF_ground
    global lang_data_corpusMeasure_type_MF_side
    global lang_data_corpusMeasure_type_backwall
    global lang_data_corpusMeasure_type_ground_short
    global lang_data_corpusMeasure_type_side_short
    global lang_data_corpusMeasure_type_middleground_short
    global lang_data_corpusMeasure_type_middleside_short
    global lang_data_corpusMeasure_type_MF_ground_short
    global lang_data_corpusMeasure_type_MF_side_short
    global lang_data_corpusMeasure_type_backwall_short
    global lang_data_extra_type_1vert
    global lang_data_extra_type_2vert
    global lang_data_extra_type_1hori
    global lang_data_genInfo_specials_LEDfrontal
    global lang_data_genInfo_specials_LEDinternal
    global lang_data_genInfo_type_surface
    global lang_data_genInfo_type_concealed
    global lang_data_genInfo_type_concealedMF
    global lang_data_glassMeasure_type_mirror3
    global lang_data_glassMeasure_type_mirror6
    global lang_data_glassMeasure_type_glass6
    global lang_error_calculation
    global lang_error_inputs
    global lang_calc_success
    global lang_calc_failed
    global lang_creation_success
    global lang_creation_failed
    global lang_update_info

    lang = ConfigParser()

    lang.read(langFile, "UTF-8")

    language = lang["language"]

    lang_general_width                              = language["lang_general_width"].replace('"', "")
    lang_general_height                             = language["lang_general_height"].replace('"', "")
    lang_general_depth                              = language["lang_general_depth"].replace('"', "")
    lang_general_length                             = language["lang_general_length"].replace('"', "")
    lang_general_count                              = language["lang_general_count"].replace('"', "")
    lang_general_type                               = language["lang_general_type"].replace('"', "")
    lang_general_override                           = language["lang_general_override"].replace('"', "")
    lang_general_position                           = language["lang_general_position"].replace('"', "")
    lang_general_no                                 = language["lang_general_no"].replace('"', "")
    lang_general_yes                                = language["lang_general_yes"].replace('"', "")
    lang_general_none                               = language["lang_general_none"].replace('"', "")
    lang_general_with                               = language["lang_general_with"].replace('"', "")
    lang_general_without                            = language["lang_general_without"].replace('"', "")
    lang_general_ID                                 = language["lang_general_ID"].replace('"', "")
    lang_general_name                               = language["lang_general_name"].replace('"', "")
    lang_frmGeneralInfo                             = language["lang_frmGeneralInfo"].replace('"', "")
    lang_genInfo_orderID                            = language["lang_genInfo_orderID"].replace('"', "")
    lang_genInfo_date                               = language["lang_genInfo_date"].replace('"', "")
    lang_genInfo_pto                                = language["lang_genInfo_pto"].replace('"', "")
    lang_genInfo_specials                           = language["lang_genInfo_specials"].replace('"', "")
    lang_frmMeasure                                 = language["lang_frmMeasure"].replace('"', "")
    lang_frmColor                                   = language["lang_frmColor"].replace('"', "")
    lang_color_aluminum                             = language["lang_color_aluminum"].replace('"', "")
    lang_color_unicolor                             = language["lang_color_unicolor"].replace('"', "")
    lang_color_wood                                 = language["lang_color_wood"].replace('"', "")
    lang_color_material                             = language["lang_color_material"].replace('"', "")
    lang_frmCorpusInfo                              = language["lang_frmCorpusInfo"].replace('"', "")
    lang_corInfo_light                              = language["lang_corInfo_light"].replace('"', "")
    lang_corInfo_indLight                           = language["lang_corInfo_indLight"].replace('"', "")
    lang_corInfo_door                               = language["lang_corInfo_door"].replace('"', "")
    lang_corInfo_shelf                              = language["lang_corInfo_shelf"].replace('"', "")
    lang_corInfo_overhangUpper                      = language["lang_corInfo_overhangUpper"].replace('"', "")
    lang_corInfo_overhangLower                      = language["lang_corInfo_overhangLower"].replace('"', "")
    lang_frmExtra                                   = language["lang_frmExtra"].replace('"', "")
    lang_extra_measure                              = language["lang_extra_measure"].replace('"', "")
    lang_extra_covered                              = language["lang_extra_covered"].replace('"', "")
    lang_frmCorpusMeasure                           = language["lang_frmCorpusMeasure"].replace('"', "")
    lang_frmGlassMeasure                            = language["lang_frmGlassMeasure"].replace('"', "")
    lang_frmPackaging                               = language["lang_frmPackaging"].replace('"', "")
    lang_frmInfo                                    = language["lang_frmInfo"].replace('"', "")
    lang_button_calc                                = language["lang_button_calc"].replace('"', "")
    lang_button_reset                               = language["lang_button_reset"].replace('"', "")
    lang_button_create                              = language["lang_button_create"].replace('"', "")
    lang_button_load                                = language["lang_button_load"].replace('"', "")
    lang_button_settings                            = language["lang_button_settings"].replace('"', "")
    lang_button_quit                                = language["lang_button_quit"].replace('"', "")
    lang_button_save                                = language["lang_button_save"].replace('"', "")
    lang_button_close                               = language["lang_button_close"].replace('"', "")
    lang_button_update                              = language["lang_button_update"].replace('"', "")
    lang_button_updateStart                         = language["lang_button_updateStart"].replace('"', "")
    lang_button_github                              = language["lang_button_github"].replace('"', "")
    lang_frmPrgInfo                                 = language["lang_frmPrgInfo"].replace('"', "")
    lang_prgInfo_contact                            = language["lang_prgInfo_contact"].replace('"', "")
    lang_prgInfo_git                                = language["lang_prgInfo_git"].replace('"', "")
    lang_frmFileHandling                            = language["lang_frmFileHandling"].replace('"', "")
    lang_fileHandling_saveDir                       = language["lang_fileHandling_saveDir"].replace('"', "")
    lang_fileHandling_calculate                     = language["lang_fileHandling_calculate"].replace('"', "")
    lang_fileHandling_RCFile                        = language["lang_fileHandling_RCFile"].replace('"', "")
    lang_fileHandling_openPDF                       = language["lang_fileHandling_openPDF"].replace('"', "")
    lang_fileHandling_files                         = language["lang_fileHandling_files"].replace('"', "")
    lang_frmMatPresets                              = language["lang_frmMatPresets"].replace('"', "")
    lang_matPresets_packaging                       = language["lang_matPresets_packaging"].replace('"', "")
    lang_matPresets_wood                            = language["lang_matPresets_wood"].replace('"', "")
    lang_matPresets_aluminum                        = language["lang_matPresets_aluminum"].replace('"', "")
    lang_matPresets_LEDFrontal                      = language["lang_matPresets_LEDFrontal"].replace('"', "")
    lang_matPresets_LEDInternal                     = language["lang_matPresets_LEDInternal"].replace('"', "")
    lang_frmOther                                   = language["lang_frmOther"].replace('"', "")
    lang_other_autoUpdate                           = language["lang_other_autoUpdate"].replace('"', "")
    lang_other_language                             = language["lang_other_language"].replace('"', "")
    lang_other_info                                 = language["lang_other_info"].replace('"', "")
    lang_frmUpdateInfo                              = language["lang_frmUpdateInfo"].replace('"', "")
    lang_updateInfo_statusNone                      = language["lang_updateInfo_statusNone"].replace('"', "")
    lang_updateInfo_statusTrue                      = language["lang_updateInfo_statusTrue"].replace('"', "")
    lang_updateInfo_statusFalse                     = language["lang_updateInfo_statusFalse"].replace('"', "")
    lang_updateInfo_versionUsed                     = language["lang_updateInfo_versionUsed"].replace('"', "")
    lang_updateInfo_versionLatest                   = language["lang_updateInfo_versionLatest"].replace('"', "")
    lang_frmChangelog                               = language["lang_frmChangelog"].replace('"', "")
    lang_changlog_false                             = language["lang_changlog_false"].replace('"', "")
    lang_frmUpdateSettings                          = language["lang_frmUpdateSettings"].replace('"', "")
    lang_updateSettings_experimental                = language["lang_updateSettings_experimental"].replace('"', "")
    lang_updateSettings_exportConfig                = language["lang_updateSettings_exportConfig"].replace('"', "")
    lang_updateSettings_exportDatabase              = language["lang_updateSettings_exportDatabase"].replace('"', "")
    lang_updateSettings_shortcut                    = language["lang_updateSettings_shortcut"].replace('"', "")
    lang_msg_rcoverride                             = language["lang_msg_rcoverride"].replace('"', "")
    lang_msg_pdfoverride                            = language["lang_msg_pdfoverride"].replace('"', "")
    lang_msg_doorAmountInvalid                      = language["lang_msg_doorAmountInvalid"].replace('"', "")
    lang_data_corInfo_light_warm                    = language["lang_data_corInfo_light_warm"].replace('"', "")
    lang_data_corInfo_light_neutral                 = language["lang_data_corInfo_light_neutral"].replace('"', "")
    lang_data_corInfo_light_cct                     = language["lang_data_corInfo_light_cct"].replace('"', "")
    lang_data_corInfo_light_rgb                     = language["lang_data_corInfo_light_rgb"].replace('"', "")
    lang_data_corpusMeasure_type_ground             = language["lang_data_corpusMeasure_type_ground"].replace('"', "")
    lang_data_corpusMeasure_type_side               = language["lang_data_corpusMeasure_type_side"].replace('"', "")
    lang_data_corpusMeasure_type_middleground       = language["lang_data_corpusMeasure_type_middleground"].replace('"', "")
    lang_data_corpusMeasure_type_middleside         = language["lang_data_corpusMeasure_type_middleside"].replace('"', "")
    lang_data_corpusMeasure_type_MF_ground          = language["lang_data_corpusMeasure_type_MF_ground"].replace('"', "")
    lang_data_corpusMeasure_type_MF_side            = language["lang_data_corpusMeasure_type_MF_side"].replace('"', "")
    lang_data_corpusMeasure_type_backwall           = language["lang_data_corpusMeasure_type_backwall"].replace('"', "")
    lang_data_corpusMeasure_type_ground_short       = language["lang_data_corpusMeasure_type_ground_short"].replace('"', "")
    lang_data_corpusMeasure_type_side_short         = language["lang_data_corpusMeasure_type_side_short"].replace('"', "")
    lang_data_corpusMeasure_type_middleground_short = language["lang_data_corpusMeasure_type_middleground_short"].replace('"', "")
    lang_data_corpusMeasure_type_middleside_short   = language["lang_data_corpusMeasure_type_middleside_short"].replace('"', "")
    lang_data_corpusMeasure_type_MF_ground_short    = language["lang_data_corpusMeasure_type_MF_ground_short"].replace('"', "")
    lang_data_corpusMeasure_type_MF_side_short      = language["lang_data_corpusMeasure_type_MF_side_short"].replace('"', "")
    lang_data_corpusMeasure_type_backwall_short     = language["lang_data_corpusMeasure_type_backwall_short"].replace('"', "")
    lang_data_extra_type_1vert                      = language["lang_data_extra_type_1vert"].replace('"', "")
    lang_data_extra_type_2vert                      = language["lang_data_extra_type_2vert"].replace('"', "")
    lang_data_extra_type_1hori                      = language["lang_data_extra_type_1hori"].replace('"', "")
    lang_data_genInfo_specials_LEDfrontal           = language["lang_data_genInfo_specials_LEDfrontal"].replace('"', "")
    lang_data_genInfo_specials_LEDinternal          = language["lang_data_genInfo_specials_LEDinternal"].replace('"', "")
    lang_data_genInfo_type_surface                  = language["lang_data_genInfo_type_surface"].replace('"', "")
    lang_data_genInfo_type_concealed                = language["lang_data_genInfo_type_concealed"].replace('"', "")
    lang_data_genInfo_type_concealedMF              = language["lang_data_genInfo_type_concealedMF"].replace('"', "")
    lang_data_glassMeasure_type_mirror3             = language["lang_data_glassMeasure_type_mirror3"].replace('"', "")
    lang_data_glassMeasure_type_mirror6             = language["lang_data_glassMeasure_type_mirror6"].replace('"', "")
    lang_data_glassMeasure_type_glass6              = language["lang_data_glassMeasure_type_glass6"].replace('"', "")
    lang_error_calculation                          = language["lang_error_calculation"].replace('"', "")
    lang_error_inputs                               = language["lang_error_inputs"].replace('"', "")
    lang_calc_success                               = language["lang_calc_success"].replace('"', "")
    lang_calc_failed                                = language["lang_calc_failed"].replace('"', "")
    lang_creation_success                           = language["lang_creation_success"].replace('"', "")
    lang_creation_failed                            = language["lang_creation_failed"].replace('"', "")
    lang_update_info                                = language["lang_update_info"].replace('"', "")

    global dict_tooltips

    tooltip = lang["tooltip"]

    newdict_tooltips = {
        0  :     "ERROR",
        1  :     tooltip["tool_genInfo_orderID"].replace('"', ""),
        2  :     tooltip["tool_genInfo_date"].replace('"', ""),
        3  :     tooltip["tool_genInfo_type"].replace('"', ""),
        4  :     tooltip["tool_genInfo_pto"].replace('"', ""),
        5  :     tooltip["tool_genInfo_specials"].replace('"', ""),
        6  :     tooltip["tool_measure_width"].replace('"', ""),
        7  :     tooltip["tool_measure_height"].replace('"', ""),
        8  :     tooltip["tool_measure_depth"].replace('"', ""),
        9  :     tooltip["tool_corInfo_light"].replace('"', ""),
        10 :     tooltip["tool_corInfo_indLight"].replace('"', ""),
        11 :     tooltip["tool_corInfo_doors"].replace('"', ""),
        12 :     tooltip["tool_corInfo_shelfs"].replace('"', ""),
        13 :     tooltip["tool_corInfo_overhangUpper"].replace('"', ""),
        14 :     tooltip["tool_corInfo_overhangLower"].replace('"', ""),
        15 :     tooltip["tool_extra_type"].replace('"', ""),
        16 :     tooltip["tool_extra_measure"].replace('"', ""),
        17 :     tooltip["tool_extra_covered"].replace('"', ""),
        18 :     tooltip["tool_color_select"].replace('"', ""),
        19 :     tooltip["tool_color_showSelected"].replace('"', ""),
        20 :     tooltip["tool_corpusMeasurement"].replace('"', ""),
        21 :     tooltip["tool_glassMeasurement"].replace('"', ""),
        22 :     tooltip["tool_packaging_width"].replace('"', ""),
        23 :     tooltip["tool_packaging_height"].replace('"', ""),
        24 :     tooltip["tool_packaging_depth"].replace('"', ""),
        25 :     tooltip["tool_buttons_calc"].replace('"', ""),
        26 :     tooltip["tool_buttons_reset"].replace('"', ""),
        27 :     tooltip["tool_buttons_create"].replace('"', ""),
        28 :     tooltip["tool_buttons_load"].replace('"', ""),
        29 :     tooltip["tool_buttons_settings"].replace('"', ""),
        30 :     tooltip["tool_buttons_quit"].replace('"', ""),
        31 :     tooltip["tool_other_override"].replace('"', ""),
        32 :     tooltip["tool_textbox"].replace('"', "")
    }

    dict_tooltips = dict_tooltips | newdict_tooltips

def readConfigINI():

    if os.path.isfile(fPth_config) == False:

        writeConfigINI()
        return

    config = ConfigParser()

    config.read(fPth_config)

    presets = config["presets"]

    global packingMatThickness
    packingMatThickness = int(presets["packingmatthickness"])

    global woodenThickness
    woodenThickness = int(presets["woodenthickness"])

    global aluminiumThickness
    aluminiumThickness = int(presets["aluminiumthickness"])

    global LEDThicknessFrontal
    LEDThicknessFrontal = int(presets["ledthicknessfrontal"])

    global LEDThicknessInternal
    LEDThicknessInternal = int(presets["ledthicknessinternal"])

    global saveDir
    saveDir = presets["savedir"]

    global calculateBeforeCreate
    calculateBeforeCreate = bool(int(presets["calculatebeforecreate"]))

    global createRCFile
    createRCFile = bool(int(presets["creatercfile"]))

    global openPDF
    openPDF = bool(int(presets["openpdfaftercreation"]))

    global printPDF
    printPDF = bool(int(presets["printpdfaftercreation"]))

    global activeLang
    activeLang = presets["activelang"]

    updater = config["updater"]

    global autoaskUpdate
    autoaskUpdate = bool(int(updater["autoaskupdate"]))

    global updaterExperimentalBuilds
    updaterExperimentalBuilds = bool(int(updater["experimental"]))

    global updaterExportConfig
    updaterExportConfig = bool(int(updater["exportconfig"]))

    global updaterExportDatabase
    updaterExportDatabase = bool(int(updater["exportdatabase"]))

    global updaterShortcut
    updaterShortcut = bool(int(updater["shortcut"]))

def writeConfigINI():

    checkLanguage(True)

    config = ConfigParser()

    config["presets"] = {

        "packingmatthickness" : packingMatThickness,
        "woodenthickness" : woodenThickness,
        "aluminiumthickness" : aluminiumThickness,
        "ledthicknessfrontal" : LEDThicknessFrontal,
        "ledthicknessinternal" : LEDThicknessInternal,
        "savedir" : saveDir,
        "calculatebeforecreate" : int(calculateBeforeCreate),
        "creatercfile" : int(createRCFile),
        "openpdfaftercreation" : int(openPDF),
        "printpdfaftercreation" : int(printPDF),
        "activelang" : activeLang

    }

    config["updater"] = {

        "autoaskUpdate" : int(autoaskUpdate),
        "experimental" : int(updaterExperimentalBuilds),
        "exportConfig" : int(updaterExportConfig),
        "exportDatabase" : int(updaterExportDatabase),
        "shortcut" : int(updaterShortcut)

    }

    with open(fPth_config, "w") as configfile:

        config.write(configfile)

def writeRCFile():

    import uiHandler

    rcfOut = None

    if saveDir == "":

        fileOut = os.path.join(os.curdir, "output")

        if os.path.isdir(fileOut) == False:

            os.mkdir(fileOut)

        rcfOut = os.path.join(fileOut, "rcf")

        if os.path.isdir(rcfOut) == False:

            os.mkdir(rcfOut)

    else:

        rcfOut = os.path.join(saveDir, "rcf")

        if os.path.isdir(rcfOut) == False:

            os.mkdir(rcfOut)

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

    rcFileName = "project.rcf"

    if uiHandler.ety_genInfo_orderIDVar.get() != "":

        rcFileName = uiHandler.ety_genInfo_orderIDVar.get() + ".rcf"

    fPth_rcOutput = os.path.join(rcfOut, rcFileName)

    if os.path.isfile(fPth_rcOutput) == True:

        if tkmsg.askyesno(title = titleVersion, message = lang_msg_rcoverride) == False:

            return

    with open(fPth_rcOutput, "w") as rcfile:

        rcfiler.write(rcfile)

    return True

def createTmpFolder():

    if os.path.isdir(fold_tmp) == False:

        os.mkdir(fold_tmp)
        return True

    else:

        return False

def deleteTmpFolder():

    if os.path.isdir(fold_tmp) == True:

        shutil.rmtree(fold_tmp)
        return True

    else:

        return False