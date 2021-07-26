#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data import dataHandler, fileHandler, calcHandler, updateHandler

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as tkmsg
from tkinter import filedialog as tkfile
from subprocess import Popen, PIPE

from os.path import isdir, isfile, join
from os import curdir, startfile, remove

from PIL import Image, ImageTk

from math import floor

from datetime import date
import time

import webbrowser

title = dataHandler.titleVersion
lastSelectedListbox = None
lastSelectedListboxItem = None
root = None
ui_settings = None
ui_updater = None
ui_updateProcess = None

infoShown = False

# releases
releaseLatest = None
releaseExperimental = None

# -------------------------------------- #
#      Global Variables                  #
# -------------------------------------- #

# general info
lbl_genInfo_orderID = None
lbl_genInfo_type = None

ety_genInfo_orderIDVar = None
ety_genInfo_dateVar = None
cbb_genInfo_type = None
cbt_genInfo_ptoVar = None
cbb_genInfo_specials = None

# measures
lbl_measure_width = None
lbl_measure_height = None
lbl_measure_depth = None

ety_measure_widthVar = None
ety_measure_heightVar = None
ety_measure_depthVar = None

# color
ntb_colorcode = None
tvw_ntbColor_aluminum = None
tvw_ntbColor_unicolor = None
tvw_ntbColor_wooden = None
tvw_ntbColor_material = None
ety_color_selectedVar = None

codesAluminum = None
codesUnicolor = None
codesWooden = None
codesMaterial = None

tvw_ntbColor_aluminum_reversed = None
tvw_ntbColor_unicolor_reversed = None
tvw_ntbColor_wooden_reversed = None
tvw_ntbColor_material_reversed = None
tvw_ntbColor_aluminum_reversed_last = None
tvw_ntbColor_unicolor_reversed_last = None
tvw_ntbColor_wooden_reversed_last = None
tvw_ntbColor_material_reversed_last = None

# corpus info
lbl_corInfo_door = None
lbl_corInfo_shelf = None
lbl_corInfo_overhangUpper = None
lbl_corInfo_overhangLower = None

ety_corInfo_overhangUpper = None
ety_corInfo_overhangLower = None

cbb_corInfo_light = None
cbt_corInfo_indLightVar = None
ety_corInfo_doorVar = None
ety_corInfo_shelfVar = None
ety_corInfo_overhangUpperVar = None
ety_corInfo_overhangLowerVar = None

# extra space
lbl_extra_type = None
lbl_extra_measure = None
lbl_extra_covered = None

ety_extra_measure = None
cbt_extra_covered = None

cbb_extra_type = None
ety_extra_measureVar = None
cbt_extra_coveredVar = None

# corpus measurements
ety_corpusMeasure_pos1length = None
ety_corpusMeasure_pos2length = None
ety_corpusMeasure_pos3length = None
ety_corpusMeasure_pos4length = None
ety_corpusMeasure_pos5length = None
ety_corpusMeasure_pos6length = None
ety_corpusMeasure_pos7length = None
ety_corpusMeasure_pos8length = None
ety_corpusMeasure_pos1width = None
ety_corpusMeasure_pos2width = None
ety_corpusMeasure_pos3width = None
ety_corpusMeasure_pos4width = None
ety_corpusMeasure_pos5width = None
ety_corpusMeasure_pos6width = None
ety_corpusMeasure_pos7width = None
ety_corpusMeasure_pos8width = None
ety_corpusMeasure_pos1count = None
ety_corpusMeasure_pos2count = None
ety_corpusMeasure_pos3count = None
ety_corpusMeasure_pos4count = None
ety_corpusMeasure_pos5count = None
ety_corpusMeasure_pos6count = None
ety_corpusMeasure_pos7count = None
ety_corpusMeasure_pos8count = None

ety_corpusMeasure_pos1lengthVar = None
ety_corpusMeasure_pos2lengthVar = None
ety_corpusMeasure_pos3lengthVar = None
ety_corpusMeasure_pos4lengthVar = None
ety_corpusMeasure_pos5lengthVar = None
ety_corpusMeasure_pos6lengthVar = None
ety_corpusMeasure_pos7lengthVar = None
ety_corpusMeasure_pos8lengthVar = None
ety_corpusMeasure_pos1widthVar = None
ety_corpusMeasure_pos2widthVar = None
ety_corpusMeasure_pos3widthVar = None
ety_corpusMeasure_pos4widthVar = None
ety_corpusMeasure_pos5widthVar = None
ety_corpusMeasure_pos6widthVar = None
ety_corpusMeasure_pos7widthVar = None
ety_corpusMeasure_pos8widthVar = None
ety_corpusMeasure_pos1countVar = None
ety_corpusMeasure_pos2countVar = None
ety_corpusMeasure_pos3countVar = None
ety_corpusMeasure_pos4countVar = None
ety_corpusMeasure_pos5countVar = None
ety_corpusMeasure_pos6countVar = None
ety_corpusMeasure_pos7countVar = None
ety_corpusMeasure_pos8countVar = None
cbb_corpusMeasure_pos1type = None
cbb_corpusMeasure_pos2type = None
cbb_corpusMeasure_pos3type = None
cbb_corpusMeasure_pos4type = None
cbb_corpusMeasure_pos5type = None
cbb_corpusMeasure_pos6type = None
cbb_corpusMeasure_pos7type = None
cbb_corpusMeasure_pos8type = None
cbt_corpusMeasure_overrideVar = None

# glass measurements
ety_glassMeasure_pos1length = None
ety_glassMeasure_pos2length = None
ety_glassMeasure_pos3length = None
ety_glassMeasure_pos4length = None
ety_glassMeasure_pos5length = None
ety_glassMeasure_pos6length = None
ety_glassMeasure_pos7length = None
ety_glassMeasure_pos8length = None
ety_glassMeasure_pos1width = None
ety_glassMeasure_pos2width = None
ety_glassMeasure_pos3width = None
ety_glassMeasure_pos4width = None
ety_glassMeasure_pos5width = None
ety_glassMeasure_pos6width = None
ety_glassMeasure_pos7width = None
ety_glassMeasure_pos8width = None
ety_glassMeasure_pos1count = None
ety_glassMeasure_pos2count = None
ety_glassMeasure_pos3count = None
ety_glassMeasure_pos4count = None
ety_glassMeasure_pos5count = None
ety_glassMeasure_pos6count = None
ety_glassMeasure_pos7count = None
ety_glassMeasure_pos8count = None

ety_glassMeasure_pos1lengthVar = None
ety_glassMeasure_pos2lengthVar = None
ety_glassMeasure_pos3lengthVar = None
ety_glassMeasure_pos4lengthVar = None
ety_glassMeasure_pos5lengthVar = None
ety_glassMeasure_pos6lengthVar = None
ety_glassMeasure_pos7lengthVar = None
ety_glassMeasure_pos8lengthVar = None
ety_glassMeasure_pos1widthVar = None
ety_glassMeasure_pos2widthVar = None
ety_glassMeasure_pos3widthVar = None
ety_glassMeasure_pos4widthVar = None
ety_glassMeasure_pos5widthVar = None
ety_glassMeasure_pos6widthVar = None
ety_glassMeasure_pos7widthVar = None
ety_glassMeasure_pos8widthVar = None
ety_glassMeasure_pos1countVar = None
ety_glassMeasure_pos2countVar = None
ety_glassMeasure_pos3countVar = None
ety_glassMeasure_pos4countVar = None
ety_glassMeasure_pos5countVar = None
ety_glassMeasure_pos6countVar = None
ety_glassMeasure_pos7countVar = None
ety_glassMeasure_pos8countVar = None
cbb_glassMeasure_pos1type = None
cbb_glassMeasure_pos2type = None
cbb_glassMeasure_pos3type = None
cbb_glassMeasure_pos4type = None
cbb_glassMeasure_pos5type = None
cbb_glassMeasure_pos6type = None
cbb_glassMeasure_pos7type = None
cbb_glassMeasure_pos8type = None
cbt_glassMeasure_overrideVar = None

# packaging
ety_packaging_width = None
ety_packaging_height = None
ety_packaging_depth = None

ety_packaging_widthVar = None
ety_packaging_heightVar = None
ety_packaging_depthVar = None
cbt_packaging_overrideVar = None

# text info
txt_infoBox = None

# feedback
ety_general_feedback = None
ety_general_feedbackVar = None

# file handling
lbl_fileHandling_saveDir = None
ety_fileHandling_saveDirVar = None
cbt_fileHandling_calculateVar = None
cbt_fileHandling_RCFileVar = None
cbt_fileHandling_openPDFVar = None
cbt_fileHandling_printPDFVar = None

# material presets
ety_matPresets_packagingVar = None
ety_matPresets_woodVar = None
ety_matPresets_aluminumVar = None
ety_matPresets_LEDFrontalVar = None
ety_matPresets_LEDInternalVar = None

# other
cbt_other_autoUpdateVar = None
ety_other_languageVar = None

# updater info
lbl_updateInfo_state = None
ety_updateInfo_versionLatest = None
ety_updateInfo_versionUsedVar = None
ety_updateInfo_versionLatestVar = None

# changelog
txt_changelog = None

# updater settings
cbt_updateSettings_experimentalVar = None
cbt_updateSettings_exportConfigVar = None
cbt_updateSettings_exportDatabaseVar = None
cbt_updateSettings_createShortcutVar = None

# updater buttons
btn_startUpdate = None

# -------------------------------------- #
#      Functions                         #
# -------------------------------------- #

def createUI():

    dataHandler.deleteTmpFolder()

    global root
    root = tk.Tk()
    root.resizable(False, False)
    root.title(title)
    root.withdraw()
    root.iconbitmap(dataHandler.fPth_logo)

    style = ttk.Style(root)
    style.configure("Bold.TLabelframe.Label", font = ("vera", 8, "bold"))
    style.configure("Header.TLabel.Label", font = ("vera", 12, "bold"))
    style.configure("BoldUpdate.TLabel.Label", font = ("vera", 12, "bold"))
    style.configure("NormalUpdate.TLabel.Label", font = ("vera", 10, "bold"))

    app = mainUserInterface(master = root)
    app.mainloop()
        
class mainUserInterface(tk.Frame):

    def __init__(self, master=None):

        global ui_updater

        super().__init__(master)

        self.master = master

        self.createWidgets()
        self.fillTreeviewlists()
        self.fillCombobox()
        self.addTracing()
        self.updateDependencies()
        self.centerWindow()
        self.update()
        root.deiconify()

        self.pack

        # check if in update process
        if isfile(dataHandler.fPth_update) == True:

            runUpdateProcessInterface()
            updateState = updateHandler.continueUpdate()
            if updateState != False:

                closingUpdateProcessInterface()

                if updateState == "permError":

                    tkmsg.showwarning(title = dataHandler.titleVersion, message = "Due to permission denial, we could not remove all components of the old installation. To remove all components, please go to your installation directory and delete the left over parts by hand.")

                tkmsg.showinfo(title = dataHandler.titleVersion, message = "Sucessfully updated! Please enjoy!")

                remove(dataHandler.fPth_update)

        if dataHandler.autoaskUpdate == True:

            self.getLatestRelease()

    def createWidgets(self):

        self.update()

        # -------------------------------------- #
        #      Global Init                       #
        # -------------------------------------- #
        
        # general info
        global ety_genInfo_orderIDVar
        global ety_genInfo_dateVar
        global cbt_genInfo_ptoVar 

        # measure
        global ety_measure_widthVar
        global ety_measure_heightVar
        global ety_measure_depthVar

        # corpus info
        global cbt_corInfo_indLightVar 
        global ety_corInfo_doorVar 
        global ety_corInfo_shelfVar 
        global ety_corInfo_overhangUpperVar 
        global ety_corInfo_overhangLowerVar

        # color
        global ety_color_selectedVar

        # extra space
        global ety_extra_measureVar 
        global cbt_extra_coveredVar 

        # corpus measurements
        global ety_corpusMeasure_pos1lengthVar 
        global ety_corpusMeasure_pos2lengthVar 
        global ety_corpusMeasure_pos3lengthVar 
        global ety_corpusMeasure_pos4lengthVar 
        global ety_corpusMeasure_pos5lengthVar 
        global ety_corpusMeasure_pos6lengthVar 
        global ety_corpusMeasure_pos7lengthVar 
        global ety_corpusMeasure_pos8lengthVar 
        global ety_corpusMeasure_pos1widthVar 
        global ety_corpusMeasure_pos2widthVar 
        global ety_corpusMeasure_pos3widthVar 
        global ety_corpusMeasure_pos4widthVar 
        global ety_corpusMeasure_pos5widthVar 
        global ety_corpusMeasure_pos6widthVar 
        global ety_corpusMeasure_pos7widthVar 
        global ety_corpusMeasure_pos8widthVar 
        global ety_corpusMeasure_pos1countVar 
        global ety_corpusMeasure_pos2countVar 
        global ety_corpusMeasure_pos3countVar 
        global ety_corpusMeasure_pos4countVar 
        global ety_corpusMeasure_pos5countVar 
        global ety_corpusMeasure_pos6countVar 
        global ety_corpusMeasure_pos7countVar 
        global ety_corpusMeasure_pos8countVar 
        global cbt_corpusMeasure_overrideVar 

        # glass measurements
        global ety_glassMeasure_pos1lengthVar 
        global ety_glassMeasure_pos2lengthVar 
        global ety_glassMeasure_pos3lengthVar 
        global ety_glassMeasure_pos4lengthVar 
        global ety_glassMeasure_pos5lengthVar 
        global ety_glassMeasure_pos6lengthVar 
        global ety_glassMeasure_pos7lengthVar 
        global ety_glassMeasure_pos8lengthVar 
        global ety_glassMeasure_pos1widthVar 
        global ety_glassMeasure_pos2widthVar 
        global ety_glassMeasure_pos3widthVar 
        global ety_glassMeasure_pos4widthVar 
        global ety_glassMeasure_pos5widthVar 
        global ety_glassMeasure_pos6widthVar 
        global ety_glassMeasure_pos7widthVar 
        global ety_glassMeasure_pos8widthVar 
        global ety_glassMeasure_pos1countVar 
        global ety_glassMeasure_pos2countVar 
        global ety_glassMeasure_pos3countVar 
        global ety_glassMeasure_pos4countVar 
        global ety_glassMeasure_pos5countVar 
        global ety_glassMeasure_pos6countVar 
        global ety_glassMeasure_pos7countVar 
        global ety_glassMeasure_pos8countVar 
        global cbt_glassMeasure_overrideVar 

        # packaging
        global ety_packaging_widthVar 
        global ety_packaging_heightVar 
        global ety_packaging_depthVar 
        global cbt_packaging_overrideVar 

        # feedback
        global ety_general_feedback
        global ety_general_feedbackVar

        # file handling
        global ety_fileHandling_saveDirVar
        global cbt_fileHandling_calculateVar
        global cbt_fileHandling_RCFileVar
        global cbt_fileHandling_openPDFVar
        global cbt_fileHandling_printPDFVar

        # material presets
        global ety_matPresets_packagingVar
        global ety_matPresets_woodVar
        global ety_matPresets_aluminumVar
        global ety_matPresets_LEDFrontalVar
        global ety_matPresets_LEDInternalVar

        # other
        global cbt_other_autoUpdateVar
        global ety_other_languageVar

        # updater info
        global ety_updateInfo_versionUsedVar
        global ety_updateInfo_versionLatestVar

        # updater settings
        global cbt_updateSettings_experimentalVar
        global cbt_updateSettings_exportConfigVar
        global cbt_updateSettings_exportDatabaseVar
        global cbt_updateSettings_createShortcutVar

        # general info
        ety_genInfo_orderIDVar = tk.StringVar()
        ety_genInfo_dateVar = tk.StringVar()
        cbt_genInfo_ptoVar = tk.IntVar()

        # measure
        ety_measure_widthVar = tk.StringVar()
        ety_measure_heightVar = tk.StringVar()
        ety_measure_depthVar = tk.StringVar()

        # corpus info
        cbt_corInfo_indLightVar = tk.IntVar()
        ety_corInfo_doorVar = tk.StringVar()
        ety_corInfo_shelfVar = tk.StringVar()
        ety_corInfo_overhangUpperVar = tk.StringVar()
        ety_corInfo_overhangLowerVar = tk.StringVar()

        # color
        ety_color_selectedVar = tk.StringVar()

        # extra space
        ety_extra_measureVar = tk.StringVar()
        cbt_extra_coveredVar = tk.IntVar()

        # corpus measurements
        ety_corpusMeasure_pos1lengthVar = tk.StringVar()
        ety_corpusMeasure_pos2lengthVar = tk.StringVar()
        ety_corpusMeasure_pos3lengthVar = tk.StringVar()
        ety_corpusMeasure_pos4lengthVar = tk.StringVar()
        ety_corpusMeasure_pos5lengthVar = tk.StringVar()
        ety_corpusMeasure_pos6lengthVar = tk.StringVar()
        ety_corpusMeasure_pos7lengthVar = tk.StringVar()
        ety_corpusMeasure_pos8lengthVar = tk.StringVar()
        ety_corpusMeasure_pos1widthVar = tk.StringVar()
        ety_corpusMeasure_pos2widthVar = tk.StringVar()
        ety_corpusMeasure_pos3widthVar = tk.StringVar()
        ety_corpusMeasure_pos4widthVar = tk.StringVar()
        ety_corpusMeasure_pos5widthVar = tk.StringVar()
        ety_corpusMeasure_pos6widthVar = tk.StringVar()
        ety_corpusMeasure_pos7widthVar = tk.StringVar()
        ety_corpusMeasure_pos8widthVar = tk.StringVar()
        ety_corpusMeasure_pos1countVar = tk.StringVar()
        ety_corpusMeasure_pos2countVar = tk.StringVar()
        ety_corpusMeasure_pos3countVar = tk.StringVar()
        ety_corpusMeasure_pos4countVar = tk.StringVar()
        ety_corpusMeasure_pos5countVar = tk.StringVar()
        ety_corpusMeasure_pos6countVar = tk.StringVar()
        ety_corpusMeasure_pos7countVar = tk.StringVar()
        ety_corpusMeasure_pos8countVar = tk.StringVar()
        cbt_corpusMeasure_overrideVar = tk.IntVar()

        # glass measurements
        ety_glassMeasure_pos1lengthVar = tk.StringVar()
        ety_glassMeasure_pos2lengthVar = tk.StringVar()
        ety_glassMeasure_pos3lengthVar = tk.StringVar()
        ety_glassMeasure_pos4lengthVar = tk.StringVar()
        ety_glassMeasure_pos5lengthVar = tk.StringVar()
        ety_glassMeasure_pos6lengthVar = tk.StringVar()
        ety_glassMeasure_pos7lengthVar = tk.StringVar()
        ety_glassMeasure_pos8lengthVar = tk.StringVar()
        ety_glassMeasure_pos1widthVar = tk.StringVar()
        ety_glassMeasure_pos2widthVar = tk.StringVar()
        ety_glassMeasure_pos3widthVar = tk.StringVar()
        ety_glassMeasure_pos4widthVar = tk.StringVar()
        ety_glassMeasure_pos5widthVar = tk.StringVar()
        ety_glassMeasure_pos6widthVar = tk.StringVar()
        ety_glassMeasure_pos7widthVar = tk.StringVar()
        ety_glassMeasure_pos8widthVar = tk.StringVar()
        ety_glassMeasure_pos1countVar = tk.StringVar()
        ety_glassMeasure_pos2countVar = tk.StringVar()
        ety_glassMeasure_pos3countVar = tk.StringVar()
        ety_glassMeasure_pos4countVar = tk.StringVar()
        ety_glassMeasure_pos5countVar = tk.StringVar()
        ety_glassMeasure_pos6countVar = tk.StringVar()
        ety_glassMeasure_pos7countVar = tk.StringVar()
        ety_glassMeasure_pos8countVar = tk.StringVar()
        cbt_glassMeasure_overrideVar = tk.IntVar()

        # packaging
        ety_packaging_widthVar = tk.StringVar()
        ety_packaging_heightVar = tk.StringVar()
        ety_packaging_depthVar = tk.StringVar()
        cbt_packaging_overrideVar = tk.IntVar()

        # feedback
        ety_general_feedbackVar = tk.StringVar()

        # file handling
        ety_fileHandling_saveDirVar = tk.StringVar()
        cbt_fileHandling_calculateVar = tk.IntVar()
        cbt_fileHandling_RCFileVar = tk.IntVar()
        cbt_fileHandling_openPDFVar = tk.IntVar()
        cbt_fileHandling_printPDFVar = tk.IntVar()

        # material presets
        ety_matPresets_packagingVar = tk.StringVar()
        ety_matPresets_woodVar = tk.StringVar()
        ety_matPresets_aluminumVar = tk.StringVar()
        ety_matPresets_LEDFrontalVar = tk.StringVar()
        ety_matPresets_LEDInternalVar = tk.StringVar()

        # other
        cbt_other_autoUpdateVar = tk.IntVar()
        ety_other_languageVar = tk.StringVar()

        # updater info
        ety_updateInfo_versionUsedVar = tk.StringVar()
        ety_updateInfo_versionLatestVar = tk.StringVar()

        # updater settings
        cbt_updateSettings_experimentalVar = tk.IntVar()
        cbt_updateSettings_exportConfigVar = tk.IntVar()
        cbt_updateSettings_exportDatabaseVar = tk.IntVar()
        cbt_updateSettings_createShortcutVar = tk.IntVar()

        # -------------------------------------- #
        #      Shorts Legend                     #
        # -------------------------------------- #

        #   frm = Frame
        #   ntb = Notebook
        #   lbl = Label
        #   ety = Entry
        #   cbb = Combobox
        #   cbt = Checkbutton
        #   lbx = Listbox
        #   txt = Text
        #   tvw = Treeview
        #   spc = Spacer
        #   sep = Separator

        # -------------------------------------- #
        #      Frame Tree (outdated)             #
        # -------------------------------------- #

        # ROOT
        #   |->   frm_mainLeft
        #   |       |
        #   |       |->   frm_generalInfo
        #   |       |->   frm_corpusInfo
        #   |       |->   frm_color
        #   |       |->   frm_extraSpace
        #   |       |->   frm_packaging
        #   |
        #   |->   frm_masterMiddleRight
        #           |
        #           |->   frm_mainMiddle
        #           |->   frm_mainRight
        #           |->   frm_buttons

        frm_mainLeft = ttk.Frame()
        frm_mainLeft.grid(row = 0, column = 0, sticky = "n")

        frm_mainLeftLeft = ttk.Frame(master = frm_mainLeft)
        frm_mainLeftLeft.grid(row = 0, column = 0, sticky = "n")

        frm_mainLeftRight = ttk.Frame(master = frm_mainLeft)
        frm_mainLeftRight.grid(row = 0, column = 1, sticky = "n")

        frm_masterMiddleRight = ttk.Frame()
        frm_masterMiddleRight.grid(row = 0, column = 1, sticky = "n")

        frm_mainMiddle = ttk.Frame(master = frm_masterMiddleRight)
        frm_mainMiddle.grid(row = 0, column = 0, sticky = "n")

        frm_mainRight = ttk.Frame(master = frm_masterMiddleRight)
        frm_mainRight.grid(row = 0, column = 1, sticky = "n")

        frm_buttons = ttk.Frame(master = frm_masterMiddleRight)
        frm_buttons.grid(row = 1, column = 0, columnspan = 2)

        # -------------------------------------- #
        #      General Info                      #
        # -------------------------------------- #

        # globals

        global lbl_genInfo_orderID
        global lbl_genInfo_type

        global cbb_genInfo_type
        global cbb_genInfo_specials
        
        ety_genInfo_dateVar.set(date.today().strftime("%d/%m/%Y"))

        # frame
        frm_generalInfo = ttk.LabelFrame(master = frm_mainLeftLeft, text = dataHandler.lang_frmGeneralInfo, style = "Bold.TLabelframe")
        frm_generalInfo.grid(row = 0, column = 0, padx = 5, pady = 0)

        frm_generalInfo_widthSpacer = tk.Label(master = frm_generalInfo, width = 23, height = 0)
        frm_generalInfo_widthSpacer.grid(row = 0, column = 0, columnspan = 2)

        # label
        lbl_genInfo_orderID = ttk.Label(master = frm_generalInfo, text = dataHandler.lang_genInfo_orderID)
        lbl_genInfo_date = ttk.Label(master = frm_generalInfo, text = dataHandler.lang_genInfo_date)
        lbl_genInfo_type = ttk.Label(master = frm_generalInfo, text = dataHandler.lang_general_type)
        lbl_genInfo_pto = ttk.Label(master = frm_generalInfo, text = dataHandler.lang_genInfo_pto)
        lbl_genInfo_specials = ttk.Label(master = frm_generalInfo, text = dataHandler.lang_genInfo_specials)
        
        # input
        ety_genInfo_orderID = ttk.Entry(master = frm_generalInfo, width = 11, textvariable = ety_genInfo_orderIDVar, validate = "key", justify = "center")
        ety_genInfo_date = ttk.Entry(master = frm_generalInfo, width = 11, textvariable = ety_genInfo_dateVar, state = "disabled", justify = "center")
        cbb_genInfo_type = ttk.Combobox(master = frm_generalInfo, width = 8, state = "readonly")
        cbt_genInfo_pto = ttk.Checkbutton(master = frm_generalInfo, variable = cbt_genInfo_ptoVar)
        cbb_genInfo_specials = ttk.Combobox(master = frm_generalInfo, width = 8, state = "readonly")

        # entry validation
        ety_genInfo_orderID.configure(validatecommand = (ety_genInfo_orderID.register(self.validateEntryInput), "%P", "%d"))

        # label grid
        lbl_genInfo_orderID.grid(row = 0, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_genInfo_date.grid(row = 1, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_genInfo_type.grid(row = 2, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_genInfo_pto.grid(row = 3, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_genInfo_specials.grid(row = 4, column = 0, padx = 1, pady = 1, sticky = "w")

        # input grid
        ety_genInfo_orderID.grid(row = 0, column = 1, padx = 1, pady = 1, sticky = "e")
        ety_genInfo_date.grid(row = 1, column = 1, padx = 1, pady = 1, sticky = "e")
        cbb_genInfo_type.grid(row = 2, column = 1, padx = 1, pady = 1, sticky = "e")
        cbt_genInfo_pto.grid(row = 3, column = 1, padx = 1, pady = 1, sticky = "e")
        cbb_genInfo_specials.grid(row = 4, column = 1, padx = 1, pady = 1, sticky = "e")

        # -------------------------------------- #
        #      Measures                          #
        # -------------------------------------- #
        
        # globals
        global lbl_measure_width
        global lbl_measure_height
        global lbl_measure_depth

        # frame
        frm_measure = ttk.LabelFrame(master = frm_mainLeftLeft, text = dataHandler.lang_frmMeasure, style = "Bold.TLabelframe")
        frm_measure.grid(row = 1, column = 0, padx = 5, pady = 0)

        frm_measure_widthSpacer = tk.Label(master = frm_measure, width = 23, height = 0)
        frm_measure_widthSpacer.grid(row = 0, column = 0, columnspan = 2)

        # label
        lbl_measure_width = ttk.Label(master = frm_measure, text = dataHandler.lang_general_width)
        lbl_measure_height = ttk.Label(master = frm_measure, text = dataHandler.lang_general_height)
        lbl_measure_depth = ttk.Label(master = frm_measure, text = dataHandler.lang_general_depth)

        # input
        ety_measure_width = ttk.Entry(master = frm_measure, width = 11, textvariable = ety_measure_widthVar, validate = "key")
        ety_measure_height = ttk.Entry(master = frm_measure, width = 11, textvariable = ety_measure_heightVar, validate = "key")
        ety_measure_depth = ttk.Entry(master = frm_measure, width = 11, textvariable = ety_measure_depthVar, validate = "key")

        # entry validation
        ety_measure_width.configure(validatecommand = (ety_measure_width.register(self.validateEntryInput), "%P", "%d"))
        ety_measure_height.configure(validatecommand = (ety_measure_height.register(self.validateEntryInput), "%P", "%d"))
        ety_measure_depth.configure(validatecommand = (ety_measure_depth.register(self.validateEntryInput), "%P", "%d"))

        # label grid
        lbl_measure_width.grid(row = 0, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_measure_height.grid(row = 1, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_measure_depth.grid(row = 2, column = 0, padx = 1, pady = 1, sticky = "w")

        # entry grid
        ety_measure_width.grid(row = 0, column = 1, padx = 1, pady = 1, sticky = "e")
        ety_measure_height.grid(row = 1, column = 1, padx = 1, pady = 1, sticky = "e")
        ety_measure_depth.grid(row = 2, column = 1, padx = 1, pady = 1, sticky = "e")

        # -------------------------------------- #
        #      Corpus Info                       #
        # -------------------------------------- #

        # globals
        global lbl_corInfo_door
        global lbl_corInfo_shelf
        global lbl_corInfo_overhangUpper
        global lbl_corInfo_overhangLower
        
        global ety_corInfo_overhangUpper
        global ety_corInfo_overhangLower

        global cbb_corInfo_light

        # frame
        frm_corpusInfo = ttk.LabelFrame(master = frm_mainLeftRight, text = dataHandler.lang_frmCorpusInfo, style = "Bold.TLabelframe")
        frm_corpusInfo.grid(row = 0, column = 0, padx = 5, pady = 0)

        frm_corpusInfo_widthSpacer = tk.Label(master = frm_corpusInfo, width = 23, height = 0)
        frm_corpusInfo_widthSpacer.grid(row = 0, column = 0, columnspan = 2)

        # label
        lbl_corInfo_light = ttk.Label(master = frm_corpusInfo, text = dataHandler.lang_corInfo_light)
        lbl_corInfo_indLight = ttk.Label(master = frm_corpusInfo, text = dataHandler.lang_corInfo_indLight)
        lbl_corInfo_door = ttk.Label(master = frm_corpusInfo, text = dataHandler.lang_corInfo_door)
        lbl_corInfo_shelf = ttk.Label(master = frm_corpusInfo, text = dataHandler.lang_corInfo_shelf)
        lbl_corInfo_overhangUpper = ttk.Label(master = frm_corpusInfo, text = dataHandler.lang_corInfo_overhangUpper)
        lbl_corInfo_overhangLower = ttk.Label(master = frm_corpusInfo, text = dataHandler.lang_corInfo_overhangLower)

        # input
        cbb_corInfo_light = ttk.Combobox(master = frm_corpusInfo, width = 8, state = "readonly")
        cbt_corInfo_indLight = ttk.Checkbutton(master = frm_corpusInfo, variable = cbt_corInfo_indLightVar)
        ety_corInfo_door = ttk.Entry(master = frm_corpusInfo, width = 11, textvariable = ety_corInfo_doorVar, validate = "key")
        ety_corInfo_shelf = ttk.Entry(master = frm_corpusInfo, width = 11, textvariable = ety_corInfo_shelfVar, validate = "key")
        ety_corInfo_overhangUpper = ttk.Entry(master = frm_corpusInfo, width = 11, textvariable = ety_corInfo_overhangUpperVar, validate = "key")
        ety_corInfo_overhangLower = ttk.Entry(master = frm_corpusInfo, width = 11, textvariable = ety_corInfo_overhangLowerVar, validate = "key")

        # entry validation
        ety_corInfo_door.configure(validatecommand = (ety_corInfo_door.register(self.validateEntryInput), "%P", "%d"))
        ety_corInfo_shelf.configure(validatecommand = (ety_corInfo_shelf.register(self.validateEntryInput), "%P", "%d"))
        ety_corInfo_overhangUpper.configure(validatecommand = (ety_corInfo_overhangUpper.register(self.validateEntryInput), "%P", "%d"))
        ety_corInfo_overhangLower.configure(validatecommand = (ety_corInfo_overhangLower.register(self.validateEntryInput), "%P", "%d"))

        # label grid
        lbl_corInfo_light.grid(row = 0, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_corInfo_indLight.grid(row = 1, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_corInfo_door.grid(row = 2, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_corInfo_shelf.grid(row = 3, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_corInfo_overhangUpper.grid(row = 4, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_corInfo_overhangLower.grid(row = 5, column = 0, padx = 1, pady = 1, sticky = "w")

        # input grid
        cbb_corInfo_light.grid(row = 0, column = 1, padx = 1, pady = 1, sticky = "e")
        cbt_corInfo_indLight.grid(row = 1, column = 1, padx = 1, pady = 1, sticky = "e")
        ety_corInfo_door.grid(row = 2, column = 1, padx = 1, pady = 1, sticky = "e")
        ety_corInfo_shelf.grid(row = 3, column = 1, padx = 1, pady = 1, sticky = "e")
        ety_corInfo_overhangUpper.grid(row = 4, column = 1, padx = 1, pady = 1, sticky = "e")
        ety_corInfo_overhangLower.grid(row = 5, column = 1, padx = 1, pady = 1, sticky = "e")

        # -------------------------------------- #
        #      Extra Space                       #
        # -------------------------------------- #

        # globals
        global lbl_extra_type
        global lbl_extra_measure
        global lbl_extra_covered

        global ety_extra_measure
        global cbt_extra_covered

        global cbb_extra_type

        # frame
        frm_extraSpace = ttk.LabelFrame(master = frm_mainLeftRight, text = dataHandler.lang_frmExtra, style = "Bold.TLabelframe")
        frm_extraSpace.grid(row = 1, column = 0, padx = 5, pady = 0)

        frm_extraSpace_widthSpacer = tk.Label(master = frm_extraSpace, width = 23, height = 0)
        frm_extraSpace_widthSpacer.grid(row = 0, column = 0, columnspan = 2)

        # label
        lbl_extra_type = ttk.Label(master = frm_extraSpace, text = dataHandler.lang_general_type)
        lbl_extra_measure = ttk.Label(master = frm_extraSpace, text = dataHandler.lang_extra_measure)
        lbl_extra_covered = ttk.Label(master = frm_extraSpace, text = dataHandler.lang_extra_covered)

        # input
        cbb_extra_type = ttk.Combobox(master = frm_extraSpace, width = 8, state = "readonly")
        ety_extra_measure = ttk.Entry(master = frm_extraSpace, width = 11, textvariable = ety_extra_measureVar, validate = "key")
        cbt_extra_covered = ttk.Checkbutton(master = frm_extraSpace, variable = cbt_extra_coveredVar)

        cbb_extra_type.bind("<<ComboboxSelected>>", self.updateDependencies)

        # entry validation
        ety_extra_measure.configure(validatecommand = (ety_extra_measure.register(self.validateEntryInput), "%P", "%d"))

        # label grid
        lbl_extra_type.grid(row = 0, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_extra_measure.grid(row = 1, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_extra_covered.grid(row = 2, column = 0, padx = 1, pady = 1, sticky = "w")

        # input grid
        cbb_extra_type.grid(row = 0, column = 1, columnspan = 2, padx = 1, pady = 1, sticky = "e")
        ety_extra_measure.grid(row = 1, column = 1, padx = 1, pady = 1, sticky = "e")
        cbt_extra_covered.grid(row = 2, column = 1, padx = 1, pady = 1, sticky = "e")

        # -------------------------------------- #
        #      Color                             #
        # -------------------------------------- #

        # globals
        global ntb_colorcode
        global tvw_ntbColor_aluminum
        global tvw_ntbColor_unicolor
        global tvw_ntbColor_wooden
        global tvw_ntbColor_material

        global tvw_ntbColor_aluminum_reversed
        global tvw_ntbColor_unicolor_reversed
        global tvw_ntbColor_wooden_reversed
        global tvw_ntbColor_material_reversed

        # frame
        frm_color = ttk.LabelFrame(master = frm_mainLeft, text = dataHandler.lang_frmColor, style = "Bold.TLabelframe")
        frm_color.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 0)

        # icon binding
        ico_colorcode_aluminum = Image.open(dataHandler.fPth_imageAluminum)
        self.ptk_colorcode_aluminum = ImageTk.PhotoImage(ico_colorcode_aluminum)
        ico_colorcode_unicolor = Image.open(dataHandler.fPth_imageUnicolor)
        self.ptk_colorcode_unicolor = ImageTk.PhotoImage(ico_colorcode_unicolor)
        ico_colorcode_wood = Image.open(dataHandler.fPth_imageWood)
        self.ptk_colorcode_wood = ImageTk.PhotoImage(ico_colorcode_wood)
        ico_colorcode_material = Image.open(dataHandler.fPth_imageMaterial)
        self.ptk_colorcode_material = ImageTk.PhotoImage(ico_colorcode_material)

        # notebook
        ntb_colorcode = ttk.Notebook(master = frm_color)
        ntb_colorcode.grid(row = 0, column = 0, padx = 2, pady = 2)

        ntb_colorcode.bind("<<NotebookTabChanged>>", lambda event, notebook = ntb_colorcode: self.notebookTabChange(notebook))

        ntb_frmAluminum = ttk.Frame(master = ntb_colorcode)
        ntb_frmUnicolor = ttk.Frame(master = ntb_colorcode)
        ntb_frmWooden = ttk.Frame(master = ntb_colorcode)
        ntb_frmMaterial = ttk.Frame(master = ntb_colorcode)
        
        ntb_colorcode.add(ntb_frmAluminum, text = dataHandler.lang_color_aluminum, image = self.ptk_colorcode_aluminum, compound = tk.LEFT)
        ntb_colorcode.add(ntb_frmUnicolor, text = dataHandler.lang_color_unicolor, image = self.ptk_colorcode_unicolor, compound = tk.LEFT)
        ntb_colorcode.add(ntb_frmWooden, text = dataHandler.lang_color_wood, image = self.ptk_colorcode_wood, compound = tk.LEFT)
        ntb_colorcode.add(ntb_frmMaterial, text = dataHandler.lang_color_material, image = self.ptk_colorcode_material, compound = tk.LEFT)

        # input
        tvw_ntbColor_aluminum = ttk.Treeview(master = ntb_frmAluminum, columns = ("id", "name"), show = "headings", height = 12)
        tvw_ntbColor_aluminum.column("id", width = 75, stretch = False)
        tvw_ntbColor_aluminum.column("name", width = 245, stretch = False)
        tvw_ntbColor_aluminum.heading("id", text = dataHandler.lang_general_ID, \
            command = lambda treeview = tvw_ntbColor_aluminum, column = 0: self.treeviewSort(treeview, column))
        tvw_ntbColor_aluminum.heading("name", text = dataHandler.lang_general_name, \
            command = lambda treeview = tvw_ntbColor_aluminum, column = 1: self.treeviewSort(treeview, column))

        tvw_ntbColor_unicolor = ttk.Treeview(master = ntb_frmUnicolor, columns = ("id", "name"), show = "headings", height = 12)
        tvw_ntbColor_unicolor.column("id", width = 75, stretch = tk.NO)
        tvw_ntbColor_unicolor.column("name", width = 245, stretch = tk.NO)
        tvw_ntbColor_unicolor.heading("id", text = dataHandler.lang_general_ID, \
            command = lambda treeview = tvw_ntbColor_unicolor, column = 0: self.treeviewSort(treeview, column))
        tvw_ntbColor_unicolor.heading("name", text = dataHandler.lang_general_name, \
            command = lambda treeview = tvw_ntbColor_unicolor, column = 1: self.treeviewSort(treeview, column))

        tvw_ntbColor_wooden = ttk.Treeview(master = ntb_frmWooden, columns = ("id", "name"), show = "headings", height = 12)
        tvw_ntbColor_wooden.column("id", width = 75, stretch = tk.NO)
        tvw_ntbColor_wooden.column("name", width = 245, stretch = tk.NO)
        tvw_ntbColor_wooden.heading("id", text = dataHandler.lang_general_ID, \
            command = lambda treeview = tvw_ntbColor_wooden, column = 0: self.treeviewSort(treeview, column))
        tvw_ntbColor_wooden.heading("name", text = dataHandler.lang_general_name, \
            command = lambda treeview = tvw_ntbColor_wooden, column = 1: self.treeviewSort(treeview, column))

        tvw_ntbColor_material = ttk.Treeview(master = ntb_frmMaterial, columns = ("id", "name"), show = "headings", height = 12)
        tvw_ntbColor_material.column("id", width = 75, stretch = tk.NO)
        tvw_ntbColor_material.column("name", width = 245, stretch = tk.NO)
        tvw_ntbColor_material.heading("id", text = dataHandler.lang_general_ID, \
            command = lambda treeview = tvw_ntbColor_material, column = 0: self.treeviewSort(treeview, column))
        tvw_ntbColor_material.heading("name", text = dataHandler.lang_general_name, \
            command = lambda treeview = tvw_ntbColor_material, column = 1: self.treeviewSort(treeview, column))

        tvw_ntbColor_aluminum.bind("<<TreeviewSelect>>", lambda event, treeview = tvw_ntbColor_aluminum: self.treeviewChange(treeview))
        tvw_ntbColor_unicolor.bind("<<TreeviewSelect>>", lambda event, treeview = tvw_ntbColor_unicolor: self.treeviewChange(treeview))
        tvw_ntbColor_wooden.bind("<<TreeviewSelect>>", lambda event, treeview = tvw_ntbColor_wooden: self.treeviewChange(treeview))
        tvw_ntbColor_material.bind("<<TreeviewSelect>>", lambda event, treeview = tvw_ntbColor_material: self.treeviewChange(treeview))

        scr_ntbColor_aluminum = ttk.Scrollbar(master = ntb_frmAluminum, orient = tk.VERTICAL)
        scr_ntbColor_unicolor = ttk.Scrollbar(master = ntb_frmUnicolor, orient = tk.VERTICAL)
        scr_ntbColor_wooden = ttk.Scrollbar(master = ntb_frmWooden, orient = tk.VERTICAL)
        scr_ntbColor_material = ttk.Scrollbar(master = ntb_frmMaterial, orient = tk.VERTICAL)

        ety_color_selected = ttk.Entry(master = frm_color, textvariable = ety_color_selectedVar, state = "disabled")

        # input grid
        tvw_ntbColor_aluminum.grid(row = 0, column = 0, sticky = "we")
        tvw_ntbColor_unicolor.grid(row = 0, column = 0, sticky = "we")
        tvw_ntbColor_wooden.grid(row = 0, column = 0, sticky = "we")
        tvw_ntbColor_material.grid(row = 0, column = 0, sticky = "we")

        scr_ntbColor_aluminum.grid(row = 0, column = 1, sticky = "ns")
        scr_ntbColor_unicolor.grid(row = 0, column = 1, sticky = "ns")
        scr_ntbColor_wooden.grid(row = 0, column = 1, sticky = "ns")
        scr_ntbColor_material.grid(row = 0, column = 1, sticky = "ns")
        
        ety_color_selected.grid(row = 1, column = 0, padx = 1, pady = 1, sticky = "we")

        # scroll binding
        tvw_ntbColor_aluminum.configure(yscrollcommand = scr_ntbColor_aluminum.set)
        tvw_ntbColor_unicolor.configure(yscrollcommand = scr_ntbColor_unicolor.set)
        tvw_ntbColor_wooden.configure(yscrollcommand = scr_ntbColor_wooden.set)
        tvw_ntbColor_material.configure(yscrollcommand = scr_ntbColor_material.set)

        scr_ntbColor_aluminum.configure(command = tvw_ntbColor_aluminum.yview)
        scr_ntbColor_unicolor.configure(command = tvw_ntbColor_unicolor.yview)
        scr_ntbColor_wooden.configure(command = tvw_ntbColor_wooden.yview)
        scr_ntbColor_material.configure(command = tvw_ntbColor_material.yview)

        # -------------------------------------- #
        #      Corpus Measure                    #
        # -------------------------------------- #
    
        # globals
        global ety_corpusMeasure_pos1length
        global ety_corpusMeasure_pos2length
        global ety_corpusMeasure_pos3length
        global ety_corpusMeasure_pos4length
        global ety_corpusMeasure_pos5length
        global ety_corpusMeasure_pos6length
        global ety_corpusMeasure_pos7length
        global ety_corpusMeasure_pos8length
        global ety_corpusMeasure_pos1width
        global ety_corpusMeasure_pos2width
        global ety_corpusMeasure_pos3width
        global ety_corpusMeasure_pos4width
        global ety_corpusMeasure_pos5width
        global ety_corpusMeasure_pos6width
        global ety_corpusMeasure_pos7width
        global ety_corpusMeasure_pos8width
        global ety_corpusMeasure_pos1count
        global ety_corpusMeasure_pos2count
        global ety_corpusMeasure_pos3count
        global ety_corpusMeasure_pos4count
        global ety_corpusMeasure_pos5count
        global ety_corpusMeasure_pos6count
        global ety_corpusMeasure_pos7count
        global ety_corpusMeasure_pos8count

        global cbb_corpusMeasure_pos1type
        global cbb_corpusMeasure_pos2type
        global cbb_corpusMeasure_pos3type
        global cbb_corpusMeasure_pos4type
        global cbb_corpusMeasure_pos5type
        global cbb_corpusMeasure_pos6type
        global cbb_corpusMeasure_pos7type
        global cbb_corpusMeasure_pos8type

        # frame
        frm_corpusMeasure = ttk.LabelFrame(master = frm_mainMiddle, text = dataHandler.lang_frmCorpusMeasure, style = "Bold.TLabelframe")
        frm_corpusMeasure.grid(row = 0, column = 0, padx = 5, pady = (0, 2))

        # label
        lbl_corpusMeasure_position = ttk.Label(master = frm_corpusMeasure, text = dataHandler.lang_general_position)
        lbl_corpusMeasure_length = ttk.Label(master = frm_corpusMeasure, text = dataHandler.lang_general_length)
        lbl_corpusMeasure_width = ttk.Label(master = frm_corpusMeasure, text = dataHandler.lang_general_width)
        lbl_corpusMeasure_count = ttk.Label(master = frm_corpusMeasure, text = dataHandler.lang_general_count)
        lbl_corpusMeasure_type = ttk.Label(master = frm_corpusMeasure, text = dataHandler.lang_general_type)
        lbl_corpusMeasure_pos1 = ttk.Label(master = frm_corpusMeasure, text = "1")
        lbl_corpusMeasure_pos2 = ttk.Label(master = frm_corpusMeasure, text = "2")
        lbl_corpusMeasure_pos3 = ttk.Label(master = frm_corpusMeasure, text = "3")
        lbl_corpusMeasure_pos4 = ttk.Label(master = frm_corpusMeasure, text = "4")
        lbl_corpusMeasure_pos5 = ttk.Label(master = frm_corpusMeasure, text = "5")
        lbl_corpusMeasure_pos6 = ttk.Label(master = frm_corpusMeasure, text = "6")
        lbl_corpusMeasure_pos7 = ttk.Label(master = frm_corpusMeasure, text = "7")
        lbl_corpusMeasure_pos8 = ttk.Label(master = frm_corpusMeasure, text = "8")
        lbl_corpusMeasure_pos1separator = ttk.Label(master = frm_corpusMeasure, text = "x")
        lbl_corpusMeasure_pos2separator = ttk.Label(master = frm_corpusMeasure, text = "x")
        lbl_corpusMeasure_pos3separator = ttk.Label(master = frm_corpusMeasure, text = "x")
        lbl_corpusMeasure_pos4separator = ttk.Label(master = frm_corpusMeasure, text = "x")
        lbl_corpusMeasure_pos5separator = ttk.Label(master = frm_corpusMeasure, text = "x")
        lbl_corpusMeasure_pos6separator = ttk.Label(master = frm_corpusMeasure, text = "x")
        lbl_corpusMeasure_pos7separator = ttk.Label(master = frm_corpusMeasure, text = "x")
        lbl_corpusMeasure_pos8separator = ttk.Label(master = frm_corpusMeasure, text = "x")

        # input
        ety_corpusMeasure_pos1length = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos1lengthVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos2length = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos2lengthVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos3length = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos3lengthVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos4length = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos4lengthVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos5length = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos5lengthVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos6length = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos6lengthVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos7length = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos7lengthVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos8length = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos8lengthVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos1width = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos1widthVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos2width = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos2widthVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos3width = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos3widthVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos4width = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos4widthVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos5width = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos5widthVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos6width = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos6widthVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos7width = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos7widthVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos8width = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos8widthVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos1count = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos1countVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos2count = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos2countVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos3count = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos3countVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos4count = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos4countVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos5count = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos5countVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos6count = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos6countVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos7count = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos7countVar, validate = "key", justify = "center")
        ety_corpusMeasure_pos8count = ttk.Entry(master = frm_corpusMeasure, width = 8, textvariable = ety_corpusMeasure_pos8countVar, validate = "key", justify = "center")
        cbb_corpusMeasure_pos1type = ttk.Combobox(master = frm_corpusMeasure, width = 8, state = "readonly")
        cbb_corpusMeasure_pos2type = ttk.Combobox(master = frm_corpusMeasure, width = 8, state = "readonly")
        cbb_corpusMeasure_pos3type = ttk.Combobox(master = frm_corpusMeasure, width = 8, state = "readonly")
        cbb_corpusMeasure_pos4type = ttk.Combobox(master = frm_corpusMeasure, width = 8, state = "readonly")
        cbb_corpusMeasure_pos5type = ttk.Combobox(master = frm_corpusMeasure, width = 8, state = "readonly")
        cbb_corpusMeasure_pos6type = ttk.Combobox(master = frm_corpusMeasure, width = 8, state = "readonly")
        cbb_corpusMeasure_pos7type = ttk.Combobox(master = frm_corpusMeasure, width = 8, state = "readonly")
        cbb_corpusMeasure_pos8type = ttk.Combobox(master = frm_corpusMeasure, width = 8, state = "readonly")
        cbt_corpusMeasure_override = ttk.Checkbutton(master = frm_corpusMeasure, text = dataHandler.lang_general_override, variable = cbt_corpusMeasure_overrideVar, command = self.updateDependencies)

        # entry validation
        ety_corpusMeasure_pos1length.configure(validatecommand = (ety_corpusMeasure_pos1length.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos2length.configure(validatecommand = (ety_corpusMeasure_pos2length.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos3length.configure(validatecommand = (ety_corpusMeasure_pos3length.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos4length.configure(validatecommand = (ety_corpusMeasure_pos4length.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos5length.configure(validatecommand = (ety_corpusMeasure_pos5length.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos6length.configure(validatecommand = (ety_corpusMeasure_pos6length.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos7length.configure(validatecommand = (ety_corpusMeasure_pos7length.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos8length.configure(validatecommand = (ety_corpusMeasure_pos8length.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos1width.configure(validatecommand = (ety_corpusMeasure_pos1width.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos2width.configure(validatecommand = (ety_corpusMeasure_pos2width.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos3width.configure(validatecommand = (ety_corpusMeasure_pos3width.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos4width.configure(validatecommand = (ety_corpusMeasure_pos4width.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos5width.configure(validatecommand = (ety_corpusMeasure_pos5width.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos6width.configure(validatecommand = (ety_corpusMeasure_pos6width.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos7width.configure(validatecommand = (ety_corpusMeasure_pos7width.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos8width.configure(validatecommand = (ety_corpusMeasure_pos8width.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos1count.configure(validatecommand = (ety_corpusMeasure_pos1count.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos2count.configure(validatecommand = (ety_corpusMeasure_pos2count.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos3count.configure(validatecommand = (ety_corpusMeasure_pos3count.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos4count.configure(validatecommand = (ety_corpusMeasure_pos4count.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos5count.configure(validatecommand = (ety_corpusMeasure_pos5count.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos6count.configure(validatecommand = (ety_corpusMeasure_pos6count.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos7count.configure(validatecommand = (ety_corpusMeasure_pos7count.register(self.validateEntryInput), "%P", "%d"))
        ety_corpusMeasure_pos8count.configure(validatecommand = (ety_corpusMeasure_pos8count.register(self.validateEntryInput), "%P", "%d"))

        # label grid
        lbl_corpusMeasure_position.grid(row = 0, column = 0, padx = 1, pady = 1)
        lbl_corpusMeasure_length.grid(row = 0, column = 1, padx = 1, pady = 1)
        lbl_corpusMeasure_width.grid(row = 0, column = 3, padx = 1, pady = 1)
        lbl_corpusMeasure_count.grid(row = 0, column = 4, padx = 1, pady = 1)
        lbl_corpusMeasure_type.grid(row = 0, column = 5, padx = 1, pady = 1)
        lbl_corpusMeasure_pos1.grid(row = 1, column = 0, padx = 1, pady = 1)
        lbl_corpusMeasure_pos2.grid(row = 2, column = 0, padx = 1, pady = 1)
        lbl_corpusMeasure_pos3.grid(row = 3, column = 0, padx = 1, pady = 1)
        lbl_corpusMeasure_pos4.grid(row = 4, column = 0, padx = 1, pady = 1)
        lbl_corpusMeasure_pos5.grid(row = 5, column = 0, padx = 1, pady = 1)
        lbl_corpusMeasure_pos6.grid(row = 6, column = 0, padx = 1, pady = 1)
        lbl_corpusMeasure_pos7.grid(row = 7, column = 0, padx = 1, pady = 1)
        lbl_corpusMeasure_pos8.grid(row = 8, column = 0, padx = 1, pady = 1)
        lbl_corpusMeasure_pos1separator.grid(row = 1, column = 2, padx = 3, pady = 1)
        lbl_corpusMeasure_pos2separator.grid(row = 2, column = 2, padx = 3, pady = 1)
        lbl_corpusMeasure_pos3separator.grid(row = 3, column = 2, padx = 3, pady = 1)
        lbl_corpusMeasure_pos4separator.grid(row = 4, column = 2, padx = 3, pady = 1)
        lbl_corpusMeasure_pos5separator.grid(row = 5, column = 2, padx = 3, pady = 1)
        lbl_corpusMeasure_pos6separator.grid(row = 6, column = 2, padx = 3, pady = 1)
        lbl_corpusMeasure_pos7separator.grid(row = 7, column = 2, padx = 3, pady = 1)
        lbl_corpusMeasure_pos8separator.grid(row = 8, column = 2, padx = 3, pady = 1)

        # input grid
        ety_corpusMeasure_pos1length.grid(row = 1, column = 1, padx = 1, pady = 1)
        ety_corpusMeasure_pos2length.grid(row = 2, column = 1, padx = 1, pady = 1)
        ety_corpusMeasure_pos3length.grid(row = 3, column = 1, padx = 1, pady = 1)
        ety_corpusMeasure_pos4length.grid(row = 4, column = 1, padx = 1, pady = 1)
        ety_corpusMeasure_pos5length.grid(row = 5, column = 1, padx = 1, pady = 1)
        ety_corpusMeasure_pos6length.grid(row = 6, column = 1, padx = 1, pady = 1)
        ety_corpusMeasure_pos7length.grid(row = 7, column = 1, padx = 1, pady = 1)
        ety_corpusMeasure_pos8length.grid(row = 8, column = 1, padx = 1, pady = 1)
        ety_corpusMeasure_pos1width.grid(row = 1, column = 3, padx = 1, pady = 1)
        ety_corpusMeasure_pos2width.grid(row = 2, column = 3, padx = 1, pady = 1)
        ety_corpusMeasure_pos3width.grid(row = 3, column = 3, padx = 1, pady = 1)
        ety_corpusMeasure_pos4width.grid(row = 4, column = 3, padx = 1, pady = 1)
        ety_corpusMeasure_pos5width.grid(row = 5, column = 3, padx = 1, pady = 1)
        ety_corpusMeasure_pos6width.grid(row = 6, column = 3, padx = 1, pady = 1)
        ety_corpusMeasure_pos7width.grid(row = 7, column = 3, padx = 1, pady = 1)
        ety_corpusMeasure_pos8width.grid(row = 8, column = 3, padx = 1, pady = 1)
        ety_corpusMeasure_pos1count.grid(row = 1, column = 4, padx = 1, pady = 1)
        ety_corpusMeasure_pos2count.grid(row = 2, column = 4, padx = 1, pady = 1)
        ety_corpusMeasure_pos3count.grid(row = 3, column = 4, padx = 1, pady = 1)
        ety_corpusMeasure_pos4count.grid(row = 4, column = 4, padx = 1, pady = 1)
        ety_corpusMeasure_pos5count.grid(row = 5, column = 4, padx = 1, pady = 1)
        ety_corpusMeasure_pos6count.grid(row = 6, column = 4, padx = 1, pady = 1)
        ety_corpusMeasure_pos7count.grid(row = 7, column = 4, padx = 1, pady = 1)
        ety_corpusMeasure_pos8count.grid(row = 8, column = 4, padx = 1, pady = 1)
        cbb_corpusMeasure_pos1type.grid(row = 1, column = 5, padx = 1, pady = 1)
        cbb_corpusMeasure_pos2type.grid(row = 2, column = 5, padx = 1, pady = 1)
        cbb_corpusMeasure_pos3type.grid(row = 3, column = 5, padx = 1, pady = 1)
        cbb_corpusMeasure_pos4type.grid(row = 4, column = 5, padx = 1, pady = 1)
        cbb_corpusMeasure_pos5type.grid(row = 5, column = 5, padx = 1, pady = 1)
        cbb_corpusMeasure_pos6type.grid(row = 6, column = 5, padx = 1, pady = 1)
        cbb_corpusMeasure_pos7type.grid(row = 7, column = 5, padx = 1, pady = 1)
        cbb_corpusMeasure_pos8type.grid(row = 8, column = 5, padx = 1, pady = 1)
        cbt_corpusMeasure_override.grid(row = 9, column = 0, columnspan = 6, padx = 1, pady = 1, sticky = "w")

        # -------------------------------------- #
        #      Glass Measure                     #
        # -------------------------------------- #

        # globals
        global ety_glassMeasure_pos1length
        global ety_glassMeasure_pos2length
        global ety_glassMeasure_pos3length
        global ety_glassMeasure_pos4length
        global ety_glassMeasure_pos5length
        global ety_glassMeasure_pos6length
        global ety_glassMeasure_pos7length
        global ety_glassMeasure_pos8length
        global ety_glassMeasure_pos1width
        global ety_glassMeasure_pos2width
        global ety_glassMeasure_pos3width
        global ety_glassMeasure_pos4width
        global ety_glassMeasure_pos5width
        global ety_glassMeasure_pos6width
        global ety_glassMeasure_pos7width
        global ety_glassMeasure_pos8width
        global ety_glassMeasure_pos1count
        global ety_glassMeasure_pos2count
        global ety_glassMeasure_pos3count
        global ety_glassMeasure_pos4count
        global ety_glassMeasure_pos5count
        global ety_glassMeasure_pos6count
        global ety_glassMeasure_pos7count
        global ety_glassMeasure_pos8count

        global cbb_glassMeasure_pos1type
        global cbb_glassMeasure_pos2type
        global cbb_glassMeasure_pos3type
        global cbb_glassMeasure_pos4type
        global cbb_glassMeasure_pos5type
        global cbb_glassMeasure_pos6type
        global cbb_glassMeasure_pos7type
        global cbb_glassMeasure_pos8type

        # frame
        frm_glassMeasure = ttk.LabelFrame(master = frm_mainMiddle, text = dataHandler.lang_frmGlassMeasure, style = "Bold.TLabelframe")
        frm_glassMeasure.grid(row = 1, column = 0, padx = 5, pady = (0, 3))

        # label
        lbl_glassMeasure_position = ttk.Label(master = frm_glassMeasure, text = dataHandler.lang_general_position)
        lbl_glassMeasure_length = ttk.Label(master = frm_glassMeasure, text = dataHandler.lang_general_length)
        lbl_glassMeasure_width = ttk.Label(master = frm_glassMeasure, text = dataHandler.lang_general_width)
        lbl_glassMeasure_count = ttk.Label(master = frm_glassMeasure, text = dataHandler.lang_general_count)
        lbl_glassMeasure_type = ttk.Label(master = frm_glassMeasure, text = dataHandler.lang_general_type)
        lbl_glassMeasure_pos1 = ttk.Label(master = frm_glassMeasure, text = "1")
        lbl_glassMeasure_pos2 = ttk.Label(master = frm_glassMeasure, text = "2")
        lbl_glassMeasure_pos3 = ttk.Label(master = frm_glassMeasure, text = "3")
        lbl_glassMeasure_pos4 = ttk.Label(master = frm_glassMeasure, text = "4")
        lbl_glassMeasure_pos5 = ttk.Label(master = frm_glassMeasure, text = "5")
        lbl_glassMeasure_pos6 = ttk.Label(master = frm_glassMeasure, text = "6")
        lbl_glassMeasure_pos7 = ttk.Label(master = frm_glassMeasure, text = "7")
        lbl_glassMeasure_pos8 = ttk.Label(master = frm_glassMeasure, text = "8")
        lbl_glassMeasure_pos1separator = ttk.Label(master = frm_glassMeasure, text = "x")
        lbl_glassMeasure_pos2separator = ttk.Label(master = frm_glassMeasure, text = "x")
        lbl_glassMeasure_pos3separator = ttk.Label(master = frm_glassMeasure, text = "x")
        lbl_glassMeasure_pos4separator = ttk.Label(master = frm_glassMeasure, text = "x")
        lbl_glassMeasure_pos5separator = ttk.Label(master = frm_glassMeasure, text = "x")
        lbl_glassMeasure_pos6separator = ttk.Label(master = frm_glassMeasure, text = "x")
        lbl_glassMeasure_pos7separator = ttk.Label(master = frm_glassMeasure, text = "x")
        lbl_glassMeasure_pos8separator = ttk.Label(master = frm_glassMeasure, text = "x")

        # input
        ety_glassMeasure_pos1length = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos1lengthVar, validate = "key", justify = "center")
        ety_glassMeasure_pos2length = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos2lengthVar, validate = "key", justify = "center")
        ety_glassMeasure_pos3length = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos3lengthVar, validate = "key", justify = "center")
        ety_glassMeasure_pos4length = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos4lengthVar, validate = "key", justify = "center")
        ety_glassMeasure_pos5length = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos5lengthVar, validate = "key", justify = "center")
        ety_glassMeasure_pos6length = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos6lengthVar, validate = "key", justify = "center")
        ety_glassMeasure_pos7length = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos7lengthVar, validate = "key", justify = "center")
        ety_glassMeasure_pos8length = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos8lengthVar, validate = "key", justify = "center")
        ety_glassMeasure_pos1width = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos1widthVar, validate = "key", justify = "center")
        ety_glassMeasure_pos2width = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos2widthVar, validate = "key", justify = "center")
        ety_glassMeasure_pos3width = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos3widthVar, validate = "key", justify = "center")
        ety_glassMeasure_pos4width = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos4widthVar, validate = "key", justify = "center")
        ety_glassMeasure_pos5width = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos5widthVar, validate = "key", justify = "center")
        ety_glassMeasure_pos6width = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos6widthVar, validate = "key", justify = "center")
        ety_glassMeasure_pos7width = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos7widthVar, validate = "key", justify = "center")
        ety_glassMeasure_pos8width = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos8widthVar, validate = "key", justify = "center")
        ety_glassMeasure_pos1count = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos1countVar, validate = "key", justify = "center")
        ety_glassMeasure_pos2count = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos2countVar, validate = "key", justify = "center")
        ety_glassMeasure_pos3count = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos3countVar, validate = "key", justify = "center")
        ety_glassMeasure_pos4count = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos4countVar, validate = "key", justify = "center")
        ety_glassMeasure_pos5count = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos5countVar, validate = "key", justify = "center")
        ety_glassMeasure_pos6count = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos6countVar, validate = "key", justify = "center")
        ety_glassMeasure_pos7count = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos7countVar, validate = "key", justify = "center")
        ety_glassMeasure_pos8count = ttk.Entry(master = frm_glassMeasure, width = 8, textvariable = ety_glassMeasure_pos8countVar, validate = "key", justify = "center")
        cbb_glassMeasure_pos1type = ttk.Combobox(master = frm_glassMeasure, width = 8, state = "readonly")
        cbb_glassMeasure_pos2type = ttk.Combobox(master = frm_glassMeasure, width = 8, state = "readonly")
        cbb_glassMeasure_pos3type = ttk.Combobox(master = frm_glassMeasure, width = 8, state = "readonly")
        cbb_glassMeasure_pos4type = ttk.Combobox(master = frm_glassMeasure, width = 8, state = "readonly")
        cbb_glassMeasure_pos5type = ttk.Combobox(master = frm_glassMeasure, width = 8, state = "readonly")
        cbb_glassMeasure_pos6type = ttk.Combobox(master = frm_glassMeasure, width = 8, state = "readonly")
        cbb_glassMeasure_pos7type = ttk.Combobox(master = frm_glassMeasure, width = 8, state = "readonly")
        cbb_glassMeasure_pos8type = ttk.Combobox(master = frm_glassMeasure, width = 8, state = "readonly")
        cbt_glassMeasure_override = ttk.Checkbutton(master = frm_glassMeasure, text = dataHandler.lang_general_override, variable = cbt_glassMeasure_overrideVar, command = self.updateDependencies)
        
        # entry validation
        ety_glassMeasure_pos1length.configure(validatecommand = (ety_glassMeasure_pos1length.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos2length.configure(validatecommand = (ety_glassMeasure_pos2length.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos3length.configure(validatecommand = (ety_glassMeasure_pos3length.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos4length.configure(validatecommand = (ety_glassMeasure_pos4length.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos5length.configure(validatecommand = (ety_glassMeasure_pos5length.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos6length.configure(validatecommand = (ety_glassMeasure_pos6length.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos7length.configure(validatecommand = (ety_glassMeasure_pos7length.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos8length.configure(validatecommand = (ety_glassMeasure_pos8length.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos1width.configure(validatecommand = (ety_glassMeasure_pos1width.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos2width.configure(validatecommand = (ety_glassMeasure_pos2width.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos3width.configure(validatecommand = (ety_glassMeasure_pos3width.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos4width.configure(validatecommand = (ety_glassMeasure_pos4width.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos5width.configure(validatecommand = (ety_glassMeasure_pos5width.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos6width.configure(validatecommand = (ety_glassMeasure_pos6width.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos7width.configure(validatecommand = (ety_glassMeasure_pos7width.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos8width.configure(validatecommand = (ety_glassMeasure_pos8width.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos1count.configure(validatecommand = (ety_glassMeasure_pos1count.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos2count.configure(validatecommand = (ety_glassMeasure_pos2count.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos3count.configure(validatecommand = (ety_glassMeasure_pos3count.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos4count.configure(validatecommand = (ety_glassMeasure_pos4count.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos5count.configure(validatecommand = (ety_glassMeasure_pos5count.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos6count.configure(validatecommand = (ety_glassMeasure_pos6count.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos7count.configure(validatecommand = (ety_glassMeasure_pos7count.register(self.validateEntryInput), "%P", "%d"))
        ety_glassMeasure_pos8count.configure(validatecommand = (ety_glassMeasure_pos8count.register(self.validateEntryInput), "%P", "%d"))

        # label grid
        lbl_glassMeasure_position.grid(row = 0, column = 0, padx = 1, pady = 1)
        lbl_glassMeasure_length.grid(row = 0, column = 1, padx = 1, pady = 1)
        lbl_glassMeasure_width.grid(row = 0, column = 3, padx = 1, pady = 1)
        lbl_glassMeasure_count.grid(row = 0, column = 4, padx = 1, pady = 1)
        lbl_glassMeasure_type.grid(row = 0, column = 5, padx = 1, pady = 1)
        lbl_glassMeasure_pos1.grid(row = 1, column = 0, padx = 1, pady = 1)
        lbl_glassMeasure_pos2.grid(row = 2, column = 0, padx = 1, pady = 1)
        lbl_glassMeasure_pos3.grid(row = 3, column = 0, padx = 1, pady = 1)
        lbl_glassMeasure_pos4.grid(row = 4, column = 0, padx = 1, pady = 1)
        lbl_glassMeasure_pos5.grid(row = 5, column = 0, padx = 1, pady = 1)
        lbl_glassMeasure_pos6.grid(row = 6, column = 0, padx = 1, pady = 1)
        lbl_glassMeasure_pos7.grid(row = 7, column = 0, padx = 1, pady = 1)
        lbl_glassMeasure_pos8.grid(row = 8, column = 0, padx = 1, pady = 1)
        lbl_glassMeasure_pos1separator.grid(row = 1, column = 2, padx = 3, pady = 1)
        lbl_glassMeasure_pos2separator.grid(row = 2, column = 2, padx = 3, pady = 1)
        lbl_glassMeasure_pos3separator.grid(row = 3, column = 2, padx = 3, pady = 1)
        lbl_glassMeasure_pos4separator.grid(row = 4, column = 2, padx = 3, pady = 1)
        lbl_glassMeasure_pos5separator.grid(row = 5, column = 2, padx = 3, pady = 1)
        lbl_glassMeasure_pos6separator.grid(row = 6, column = 2, padx = 3, pady = 1)
        lbl_glassMeasure_pos7separator.grid(row = 7, column = 2, padx = 3, pady = 1)
        lbl_glassMeasure_pos8separator.grid(row = 8, column = 2, padx = 3, pady = 1)

        # input grid
        ety_glassMeasure_pos1length.grid(row = 1, column = 1, padx = 1, pady = 1)
        ety_glassMeasure_pos2length.grid(row = 2, column = 1, padx = 1, pady = 1)
        ety_glassMeasure_pos3length.grid(row = 3, column = 1, padx = 1, pady = 1)
        ety_glassMeasure_pos4length.grid(row = 4, column = 1, padx = 1, pady = 1)
        ety_glassMeasure_pos5length.grid(row = 5, column = 1, padx = 1, pady = 1)
        ety_glassMeasure_pos6length.grid(row = 6, column = 1, padx = 1, pady = 1)
        ety_glassMeasure_pos7length.grid(row = 7, column = 1, padx = 1, pady = 1)
        ety_glassMeasure_pos8length.grid(row = 8, column = 1, padx = 1, pady = 1)
        ety_glassMeasure_pos1width.grid(row = 1, column = 3, padx = 1, pady = 1)
        ety_glassMeasure_pos2width.grid(row = 2, column = 3, padx = 1, pady = 1)
        ety_glassMeasure_pos3width.grid(row = 3, column = 3, padx = 1, pady = 1)
        ety_glassMeasure_pos4width.grid(row = 4, column = 3, padx = 1, pady = 1)
        ety_glassMeasure_pos5width.grid(row = 5, column = 3, padx = 1, pady = 1)
        ety_glassMeasure_pos6width.grid(row = 6, column = 3, padx = 1, pady = 1)
        ety_glassMeasure_pos7width.grid(row = 7, column = 3, padx = 1, pady = 1)
        ety_glassMeasure_pos8width.grid(row = 8, column = 3, padx = 1, pady = 1)
        ety_glassMeasure_pos1count.grid(row = 1, column = 4, padx = 1, pady = 1)
        ety_glassMeasure_pos2count.grid(row = 2, column = 4, padx = 1, pady = 1)
        ety_glassMeasure_pos3count.grid(row = 3, column = 4, padx = 1, pady = 1)
        ety_glassMeasure_pos4count.grid(row = 4, column = 4, padx = 1, pady = 1)
        ety_glassMeasure_pos5count.grid(row = 5, column = 4, padx = 1, pady = 1)
        ety_glassMeasure_pos6count.grid(row = 6, column = 4, padx = 1, pady = 1)
        ety_glassMeasure_pos7count.grid(row = 7, column = 4, padx = 1, pady = 1)
        ety_glassMeasure_pos8count.grid(row = 8, column = 4, padx = 1, pady = 1)
        cbb_glassMeasure_pos1type.grid(row = 1, column = 5, padx = 1, pady = 1)
        cbb_glassMeasure_pos2type.grid(row = 2, column = 5, padx = 1, pady = 1)
        cbb_glassMeasure_pos3type.grid(row = 3, column = 5, padx = 1, pady = 1)
        cbb_glassMeasure_pos4type.grid(row = 4, column = 5, padx = 1, pady = 1)
        cbb_glassMeasure_pos5type.grid(row = 5, column = 5, padx = 1, pady = 1)
        cbb_glassMeasure_pos6type.grid(row = 6, column = 5, padx = 1, pady = 1)
        cbb_glassMeasure_pos7type.grid(row = 7, column = 5, padx = 1, pady = 1)
        cbb_glassMeasure_pos8type.grid(row = 8, column = 5, padx = 1, pady = 1)
        cbt_glassMeasure_override.grid(row = 9, column = 0, columnspan = 6, padx = 1, pady = 1, sticky = "w")

        # -------------------------------------- #
        #      Packaging                         #
        # -------------------------------------- #
        
        # globals
        global ety_packaging_width
        global ety_packaging_height
        global ety_packaging_depth

        # frame
        frm_packaging = ttk.LabelFrame(master = frm_mainMiddle, text = dataHandler.lang_frmPackaging, style = "Bold.TLabelframe")
        frm_packaging.grid(row = 3, column = 0, sticky = "we", padx = 5, pady = 2)

        # label
        lbl_packaging_width = ttk.Label(master = frm_packaging, text = dataHandler.lang_general_width)
        lbl_packaging_height = ttk.Label(master = frm_packaging, text = dataHandler.lang_general_height)
        lbl_packaging_depth = ttk.Label(master = frm_packaging, text = dataHandler.lang_general_depth)

        # input
        ety_packaging_width = ttk.Entry(master = frm_packaging, width = 14, textvariable = ety_packaging_widthVar, validate = "key", justify = "center")
        ety_packaging_height = ttk.Entry(master = frm_packaging, width = 14, textvariable = ety_packaging_heightVar, validate = "key", justify = "center")
        ety_packaging_depth = ttk.Entry(master = frm_packaging, width = 14, textvariable = ety_packaging_depthVar, validate = "key", justify = "center")
        cbt_packaging_override = ttk.Checkbutton(master = frm_packaging, text = dataHandler.lang_general_override, variable = cbt_packaging_overrideVar, command = self.updateDependencies)
                
        # entry validation
        ety_packaging_width.configure(validatecommand = (ety_packaging_width.register(self.validateEntryInput), "%P", "%d"))
        ety_packaging_height.configure(validatecommand = (ety_packaging_height.register(self.validateEntryInput), "%P", "%d"))
        ety_packaging_depth.configure(validatecommand = (ety_packaging_depth.register(self.validateEntryInput), "%P", "%d"))

        # label grid
        lbl_packaging_width.grid(row = 0, column = 0, padx = 1, pady = 1)
        lbl_packaging_height.grid(row = 0, column = 1, padx = 1, pady = 1)
        lbl_packaging_depth.grid(row = 0, column = 2, padx = 1, pady = 1)

        # input_grid
        ety_packaging_width.grid(row = 1, column = 0, padx = 2, pady = 1)
        ety_packaging_height.grid(row = 1, column = 1, padx = 3, pady = 1)
        ety_packaging_depth.grid(row = 1, column = 2, padx = 2, pady = 1)
        cbt_packaging_override.grid(row = 2, column = 0, columnspan = 3, padx = 1, pady = 1, sticky = "w")

        # -------------------------------------- #
        #      Info Box                          #
        # -------------------------------------- #

        # globals
        global txt_infoBox

        # frame
        frm_infoBox = ttk.LabelFrame(master = frm_mainRight, text = dataHandler.lang_frmInfo, style = "Bold.TLabelframe")
        frm_infoBox.grid(row = 0, column = 0, padx = 5, pady = 0)

        # input
        txt_infoBox = tk.Text(master = frm_infoBox, width = 22)

        # input grid
        txt_infoBox.grid(row = 0, column = 0, padx = 1, pady = 1)

        # -------------------------------------- #
        #      Buttons                           #
        # -------------------------------------- #

        # frame
        frm_buttons = ttk.Frame(master = frm_mainRight)
        frm_buttons.grid(row = 1, column = 0, pady = 5)

        # buttons
        btn_calculate = ttk.Button(master = frm_buttons, text = dataHandler.lang_button_calc, width = 29, command = self.btn_calculate_callback)
        btn_reset = ttk.Button(master = frm_buttons, text = dataHandler.lang_button_reset, width = 29, command = self.btn_reset_callback)
        btn_create = ttk.Button(master = frm_buttons, text = dataHandler.lang_button_create, width = 29, command = self.btn_create_callback)
        btn_load = ttk.Button(master = frm_buttons, text = dataHandler.lang_button_load, width = 29, command = self.btn_load_callback)
        btn_settings = ttk.Button(master = frm_buttons, text = dataHandler.lang_button_settings, width = 29, command = self.btn_settings_callback)
        btn_quit = ttk.Button(master = frm_buttons, text = dataHandler.lang_button_quit, width = 29, command = self.btn_quit_callback)

        # buttons grid
        btn_calculate.grid(row = 1, column = 0, padx = 1, pady = 1)
        btn_reset.grid(row = 2, column = 0, padx = 1, pady = 1)
        btn_create.grid(row = 3, column = 0, padx = 1, pady = 1)
        btn_load.grid(row = 4, column = 0, padx = 1, pady = 1)
        btn_settings.grid(row = 5, column = 0, padx = 1, pady = 1)
        btn_quit.grid(row = 6, column = 0, padx = 1, pady = 1)

        # -------------------------------------- #
        #      Feedback                          #
        # -------------------------------------- #

        global ety_general_feedback

        # input
        ety_general_feedback = ttk.Entry(textvariable = ety_general_feedbackVar, state = "disabled")

        # input grid
        ety_general_feedback.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = (0, 5), sticky = "we")
        
        # -------------------------------------- #
        #      Keybinding                        #
        # -------------------------------------- #

        cbt_genInfo_pto.bind("<Return>", lambda event, widget = cbt_genInfo_pto: self.cb_key_return(widget))
        cbt_corInfo_indLight.bind("<Return>", lambda event, widget = cbt_corInfo_indLight: self.cb_key_return(widget))
        cbt_extra_covered.bind("<Return>", lambda event, widget = cbt_extra_covered: self.cb_key_return(widget))
        cbt_corpusMeasure_override.bind("<Return>", lambda event, widget = cbt_corpusMeasure_override: self.cb_key_return(widget))
        cbt_glassMeasure_override.bind("<Return>", lambda event, widget = cbt_glassMeasure_override: self.cb_key_return(widget))
        cbt_packaging_override.bind("<Return>", lambda event, widget = cbt_packaging_override: self.cb_key_return(widget))

        # -------------------------------------- #
        #      Tooltip Bind                      #
        # -------------------------------------- #

        # general info

        lbl_genInfo_orderID.bind                ("<Enter>", lambda event, id = 1: self.tooltip(tooltipID = id))
        lbl_genInfo_date.bind                   ("<Enter>", lambda event, id = 2: self.tooltip(tooltipID = id))
        lbl_genInfo_type.bind                   ("<Enter>", lambda event, id = 3: self.tooltip(tooltipID = id))
        lbl_genInfo_pto.bind                    ("<Enter>", lambda event, id = 4: self.tooltip(tooltipID = id))
        lbl_genInfo_specials.bind               ("<Enter>", lambda event, id = 5: self.tooltip(tooltipID = id))
        
        ety_genInfo_orderID.bind                ("<Enter>", lambda event, id = 1: self.tooltip(tooltipID = id))
        ety_genInfo_date.bind                   ("<Enter>", lambda event, id = 2: self.tooltip(tooltipID = id))
        cbb_genInfo_type.bind                   ("<Enter>", lambda event, id = 3: self.tooltip(tooltipID = id))
        cbt_genInfo_pto.bind                    ("<Enter>", lambda event, id = 4: self.tooltip(tooltipID = id))
        cbb_genInfo_specials.bind               ("<Enter>", lambda event, id = 5: self.tooltip(tooltipID = id))

        lbl_genInfo_orderID.bind                ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_genInfo_date.bind                   ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_genInfo_type.bind                   ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_genInfo_pto.bind                    ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_genInfo_specials.bind               ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        
        ety_genInfo_orderID.bind                ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_genInfo_date.bind                   ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbb_genInfo_type.bind                   ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbt_genInfo_pto.bind                    ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbb_genInfo_specials.bind               ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        # measure

        lbl_measure_width.bind                  ("<Enter>", lambda event, id = 6: self.tooltip(tooltipID = id))
        lbl_measure_height.bind                 ("<Enter>", lambda event, id = 7: self.tooltip(tooltipID = id))
        lbl_measure_depth.bind                  ("<Enter>", lambda event, id = 8: self.tooltip(tooltipID = id))

        ety_measure_width.bind                  ("<Enter>", lambda event, id = 6: self.tooltip(tooltipID = id))
        ety_measure_height.bind                 ("<Enter>", lambda event, id = 7: self.tooltip(tooltipID = id))
        ety_measure_depth.bind                  ("<Enter>", lambda event, id = 8: self.tooltip(tooltipID = id))

        lbl_measure_width.bind                  ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_measure_height.bind                 ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_measure_depth.bind                  ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        ety_measure_width.bind                  ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_measure_height.bind                 ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_measure_depth.bind                  ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        # corpus info

        lbl_corInfo_light.bind                  ("<Enter>", lambda event, id = 9: self.tooltip(tooltipID = id))
        lbl_corInfo_indLight.bind               ("<Enter>", lambda event, id = 10: self.tooltip(tooltipID = id))
        lbl_corInfo_door.bind                   ("<Enter>", lambda event, id = 11: self.tooltip(tooltipID = id))
        lbl_corInfo_shelf.bind                  ("<Enter>", lambda event, id = 12: self.tooltip(tooltipID = id))
        lbl_corInfo_overhangUpper.bind          ("<Enter>", lambda event, id = 13: self.tooltip(tooltipID = id))
        lbl_corInfo_overhangLower.bind          ("<Enter>", lambda event, id = 14: self.tooltip(tooltipID = id))

        cbb_corInfo_light.bind                  ("<Enter>", lambda event, id = 9: self.tooltip(tooltipID = id))
        cbt_corInfo_indLight.bind               ("<Enter>", lambda event, id = 10: self.tooltip(tooltipID = id))
        ety_corInfo_door.bind                   ("<Enter>", lambda event, id = 11: self.tooltip(tooltipID = id))
        ety_corInfo_shelf.bind                  ("<Enter>", lambda event, id = 12: self.tooltip(tooltipID = id))
        ety_corInfo_overhangUpper.bind          ("<Enter>", lambda event, id = 13: self.tooltip(tooltipID = id))
        ety_corInfo_overhangLower.bind          ("<Enter>", lambda event, id = 14: self.tooltip(tooltipID = id))

        lbl_corInfo_light.bind                  ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corInfo_indLight.bind               ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corInfo_door.bind                   ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corInfo_shelf.bind                  ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corInfo_overhangUpper.bind          ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corInfo_overhangLower.bind          ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        cbb_corInfo_light.bind                  ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbt_corInfo_indLight.bind               ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corInfo_door.bind                   ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corInfo_shelf.bind                  ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corInfo_overhangUpper.bind          ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corInfo_overhangLower.bind          ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        # extra space

        lbl_extra_type.bind                     ("<Enter>", lambda event, id = 15: self.tooltip(tooltipID = id))
        lbl_extra_measure.bind                  ("<Enter>", lambda event, id = 16: self.tooltip(tooltipID = id))
        lbl_extra_covered.bind                  ("<Enter>", lambda event, id = 17: self.tooltip(tooltipID = id))

        cbb_extra_type.bind                     ("<Enter>", lambda event, id = 15: self.tooltip(tooltipID = id))
        ety_extra_measure.bind                  ("<Enter>", lambda event, id = 16: self.tooltip(tooltipID = id))
        cbt_extra_covered.bind                  ("<Enter>", lambda event, id = 17: self.tooltip(tooltipID = id))

        lbl_extra_type.bind                     ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_extra_measure.bind                  ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_extra_covered.bind                  ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        cbb_extra_type.bind                     ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_extra_measure.bind                  ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbt_extra_covered.bind                  ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        # color

        ntb_colorcode.bind                      ("<Enter>", lambda event, id = 18: self.tooltip(tooltipID = id))
        ety_color_selected.bind                 ("<Enter>", lambda event, id = 19: self.tooltip(tooltipID = id))

        ntb_colorcode.bind                      ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_color_selected.bind                 ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        # corpus measurements

        lbl_corpusMeasure_pos1.bind             ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        lbl_corpusMeasure_pos2.bind             ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        lbl_corpusMeasure_pos3.bind             ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        lbl_corpusMeasure_pos4.bind             ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        lbl_corpusMeasure_pos5.bind             ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        lbl_corpusMeasure_pos6.bind             ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        lbl_corpusMeasure_pos7.bind             ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        lbl_corpusMeasure_pos8.bind             ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))

        lbl_corpusMeasure_pos1separator.bind    ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        lbl_corpusMeasure_pos2separator.bind    ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        lbl_corpusMeasure_pos3separator.bind    ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        lbl_corpusMeasure_pos4separator.bind    ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        lbl_corpusMeasure_pos5separator.bind    ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        lbl_corpusMeasure_pos6separator.bind    ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        lbl_corpusMeasure_pos7separator.bind    ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        lbl_corpusMeasure_pos8separator.bind    ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))

        ety_corpusMeasure_pos1length.bind       ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos2length.bind       ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos3length.bind       ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos4length.bind       ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos5length.bind       ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos6length.bind       ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos7length.bind       ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos8length.bind       ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))

        ety_corpusMeasure_pos1width.bind        ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos2width.bind        ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos3width.bind        ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos4width.bind        ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos5width.bind        ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos6width.bind        ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos7width.bind        ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos8width.bind        ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))

        ety_corpusMeasure_pos1count.bind        ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos2count.bind        ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos3count.bind        ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos4count.bind        ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos5count.bind        ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos6count.bind        ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos7count.bind        ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        ety_corpusMeasure_pos8count.bind        ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))

        cbb_corpusMeasure_pos1type.bind         ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        cbb_corpusMeasure_pos2type.bind         ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        cbb_corpusMeasure_pos3type.bind         ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        cbb_corpusMeasure_pos4type.bind         ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        cbb_corpusMeasure_pos5type.bind         ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        cbb_corpusMeasure_pos6type.bind         ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        cbb_corpusMeasure_pos7type.bind         ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))
        cbb_corpusMeasure_pos8type.bind         ("<Enter>", lambda event, id = 20: self.tooltip(tooltipID = id))

        cbt_corpusMeasure_override.bind         ("<Enter>", lambda event, id = 31: self.tooltip(tooltipID = id))

        lbl_corpusMeasure_pos1.bind             ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corpusMeasure_pos2.bind             ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corpusMeasure_pos3.bind             ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corpusMeasure_pos4.bind             ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corpusMeasure_pos5.bind             ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corpusMeasure_pos6.bind             ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corpusMeasure_pos7.bind             ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corpusMeasure_pos8.bind             ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        lbl_corpusMeasure_pos1separator.bind    ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corpusMeasure_pos2separator.bind    ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corpusMeasure_pos3separator.bind    ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corpusMeasure_pos4separator.bind    ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corpusMeasure_pos5separator.bind    ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corpusMeasure_pos6separator.bind    ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corpusMeasure_pos7separator.bind    ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_corpusMeasure_pos8separator.bind    ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        ety_corpusMeasure_pos1length.bind       ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos2length.bind       ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos3length.bind       ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos4length.bind       ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos5length.bind       ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos6length.bind       ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos7length.bind       ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos8length.bind       ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        ety_corpusMeasure_pos1width.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos2width.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos3width.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos4width.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos5width.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos6width.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos7width.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos8width.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        ety_corpusMeasure_pos1count.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos2count.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos3count.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos4count.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos5count.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos6count.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos7count.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_corpusMeasure_pos8count.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        cbb_corpusMeasure_pos1type.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbb_corpusMeasure_pos2type.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbb_corpusMeasure_pos3type.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbb_corpusMeasure_pos4type.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbb_corpusMeasure_pos5type.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbb_corpusMeasure_pos6type.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbb_corpusMeasure_pos7type.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbb_corpusMeasure_pos8type.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        cbt_corpusMeasure_override.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        # glass measurements

        lbl_glassMeasure_pos1.bind              ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        lbl_glassMeasure_pos2.bind              ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        lbl_glassMeasure_pos3.bind              ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        lbl_glassMeasure_pos4.bind              ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        lbl_glassMeasure_pos5.bind              ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        lbl_glassMeasure_pos6.bind              ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        lbl_glassMeasure_pos7.bind              ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        lbl_glassMeasure_pos8.bind              ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))

        lbl_glassMeasure_pos1separator.bind     ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        lbl_glassMeasure_pos2separator.bind     ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        lbl_glassMeasure_pos3separator.bind     ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        lbl_glassMeasure_pos4separator.bind     ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        lbl_glassMeasure_pos5separator.bind     ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        lbl_glassMeasure_pos6separator.bind     ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        lbl_glassMeasure_pos7separator.bind     ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        lbl_glassMeasure_pos8separator.bind     ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))

        ety_glassMeasure_pos1length.bind        ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos2length.bind        ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos3length.bind        ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos4length.bind        ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos5length.bind        ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos6length.bind        ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos7length.bind        ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos8length.bind        ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))

        ety_glassMeasure_pos1width.bind         ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos2width.bind         ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos3width.bind         ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos4width.bind         ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos5width.bind         ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos6width.bind         ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos7width.bind         ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos8width.bind         ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))

        ety_glassMeasure_pos1count.bind         ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos2count.bind         ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos3count.bind         ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos4count.bind         ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos5count.bind         ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos6count.bind         ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos7count.bind         ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        ety_glassMeasure_pos8count.bind         ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))

        cbb_glassMeasure_pos1type.bind          ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        cbb_glassMeasure_pos2type.bind          ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        cbb_glassMeasure_pos3type.bind          ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        cbb_glassMeasure_pos4type.bind          ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        cbb_glassMeasure_pos5type.bind          ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        cbb_glassMeasure_pos6type.bind          ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        cbb_glassMeasure_pos7type.bind          ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))
        cbb_glassMeasure_pos8type.bind          ("<Enter>", lambda event, id = 21: self.tooltip(tooltipID = id))

        cbt_glassMeasure_override.bind          ("<Enter>", lambda event, id = 31: self.tooltip(tooltipID = id))

        lbl_glassMeasure_pos1.bind              ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_glassMeasure_pos2.bind              ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_glassMeasure_pos3.bind              ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_glassMeasure_pos4.bind              ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_glassMeasure_pos5.bind              ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_glassMeasure_pos6.bind              ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_glassMeasure_pos7.bind              ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_glassMeasure_pos8.bind              ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        lbl_glassMeasure_pos1separator.bind     ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_glassMeasure_pos2separator.bind     ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_glassMeasure_pos3separator.bind     ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_glassMeasure_pos4separator.bind     ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_glassMeasure_pos5separator.bind     ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_glassMeasure_pos6separator.bind     ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_glassMeasure_pos7separator.bind     ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_glassMeasure_pos8separator.bind     ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        ety_glassMeasure_pos1length.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos2length.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos3length.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos4length.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos5length.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos6length.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos7length.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos8length.bind        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        ety_glassMeasure_pos1width.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos2width.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos3width.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos4width.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos5width.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos6width.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos7width.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos8width.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        ety_glassMeasure_pos1count.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos2count.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos3count.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos4count.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos5count.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos6count.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos7count.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_glassMeasure_pos8count.bind         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        cbb_glassMeasure_pos1type.bind          ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbb_glassMeasure_pos2type.bind          ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbb_glassMeasure_pos3type.bind          ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbb_glassMeasure_pos4type.bind          ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbb_glassMeasure_pos5type.bind          ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbb_glassMeasure_pos6type.bind          ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbb_glassMeasure_pos7type.bind          ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        cbb_glassMeasure_pos8type.bind          ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        cbt_glassMeasure_override.bind          ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        # packaging

        lbl_packaging_width.bind                ("<Enter>", lambda event, id = 22: self.tooltip(tooltipID = id))
        lbl_packaging_height.bind               ("<Enter>", lambda event, id = 23: self.tooltip(tooltipID = id))
        lbl_packaging_depth.bind                ("<Enter>", lambda event, id = 24: self.tooltip(tooltipID = id))

        ety_packaging_width.bind                ("<Enter>", lambda event, id = 22: self.tooltip(tooltipID = id))
        ety_packaging_height.bind               ("<Enter>", lambda event, id = 23: self.tooltip(tooltipID = id))
        ety_packaging_depth.bind                ("<Enter>", lambda event, id = 24: self.tooltip(tooltipID = id))

        cbt_packaging_override.bind             ("<Enter>", lambda event, id = 31: self.tooltip(tooltipID = id))

        lbl_packaging_width.bind                ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_packaging_height.bind               ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        lbl_packaging_depth.bind                ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        ety_packaging_width.bind                ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_packaging_height.bind               ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        ety_packaging_depth.bind                ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        cbt_packaging_override.bind             ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        # text box

        txt_infoBox.bind                        ("<Enter>", lambda event, id = 32: self.tooltip(tooltipID = id))

        txt_infoBox.bind                        ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

        # buttons

        btn_calculate.bind                      ("<Enter>", lambda event, id = 25: self.tooltip(tooltipID = id))
        btn_reset.bind                          ("<Enter>", lambda event, id = 26: self.tooltip(tooltipID = id))
        btn_create.bind                         ("<Enter>", lambda event, id = 27: self.tooltip(tooltipID = id))
        btn_load.bind                           ("<Enter>", lambda event, id = 28: self.tooltip(tooltipID = id))
        btn_settings.bind                       ("<Enter>", lambda event, id = 29: self.tooltip(tooltipID = id))
        btn_quit.bind                           ("<Enter>", lambda event, id = 30: self.tooltip(tooltipID = id))

        btn_calculate.bind                      ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        btn_reset.bind                          ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        btn_create.bind                         ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        btn_load.bind                           ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        btn_settings.bind                       ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))
        btn_quit.bind                           ("<Leave>", lambda event, hide = True: self.tooltip(hideTooltip = hide))

    def btn_calculate_callback(self):

        if self.checkInputs() == False:

            return

        self.calcMeasures()

    def btn_reset_callback(self):

        self.resetDefault()

    def btn_create_callback(self):

        if dataHandler.calculateBeforeCreate == True:

            if self.checkInputs() == False:

                return

            if self.calcMeasures(True) == 1:

                return

        if dataHandler.createRCFile == True:

            dataHandler.writeRCFile()

        if fileHandler.createPDF() == True:

            self.showInfo(dataHandler.lang_creation_success)

        else:

            self.showInfo(dataHandler.lang_creation_failed, False)

    def btn_load_callback(self):

        loadFile = tkfile.askopenfilename(filetypes = [("RC-File", "*.rcf")])

        if loadFile ==  "":

            return

        from configparser import ConfigParser

        rcfiler = ConfigParser()

        rcfiler.read(loadFile)

        general = rcfiler["general"]

        ety_genInfo_orderIDVar.set(general["orderid"])
        cbb_genInfo_type.current(newindex = general["type"])
        cbt_genInfo_ptoVar.set(general["pto"])
        cbb_genInfo_specials.current(newindex = general["specials"])

        ntb_colorcode.select(general["colortype"])

        self.update()

        ety_color_selectedVar.set(general["color"])

        if general["colortype"] == "0":

            tvw_ntbColor_aluminum.selection_set(general["colorindex"])
            tvw_ntbColor_aluminum.see(general["colorindex"])

        elif general["colortype"] == "1":
            
            tvw_ntbColor_unicolor.selection_set(general["colorindex"])
            tvw_ntbColor_unicolor.see(general["colorindex"])

        elif general["colortype"] == "2":
            
            tvw_ntbColor_wooden.selection_set(general["colorindex"])
            tvw_ntbColor_wooden.see(general["colorindex"])

        elif general["colortype"] == "3":
            
            tvw_ntbColor_material.selection_set(general["colorindex"])
            tvw_ntbColor_material.see(general["colorindex"])

        lastSelectedListbox = int(general["colortype"])
        lastSelectedListboxItem = general["colorindex"]

        measure = rcfiler["measure"]

        ety_measure_widthVar.set(measure["mainwidth"])
        ety_measure_heightVar.set(measure["mainheight"])
        ety_measure_depthVar.set(measure["maindepth"])

        corpus = rcfiler["corpus"]

        cbb_corInfo_light.current(newindex = corpus["light"])
        cbt_genInfo_ptoVar.set(corpus["indlight"])
        ety_corInfo_doorVar.set(corpus["doors"])
        ety_corInfo_shelfVar.set(corpus["shelfs"])
        ety_corInfo_overhangUpperVar.set(corpus["overUpper"])
        ety_corInfo_overhangLowerVar.set(corpus["overLower"])

        extra = rcfiler["extra"]

        cbb_extra_type.current(newindex = extra["type"])
        ety_extra_measureVar.set(extra["measure"])
        cbt_extra_coveredVar.set(extra["covered"])

        corpusmeasure = rcfiler["corpusmeasure"]

        ety_corpusMeasure_pos1lengthVar.set(corpusmeasure["p1length"])
        ety_corpusMeasure_pos2lengthVar.set(corpusmeasure["p2length"])
        ety_corpusMeasure_pos3lengthVar.set(corpusmeasure["p3length"])
        ety_corpusMeasure_pos4lengthVar.set(corpusmeasure["p4length"])
        ety_corpusMeasure_pos5lengthVar.set(corpusmeasure["p5length"])
        ety_corpusMeasure_pos6lengthVar.set(corpusmeasure["p6length"])
        ety_corpusMeasure_pos7lengthVar.set(corpusmeasure["p7length"])
        ety_corpusMeasure_pos8lengthVar.set(corpusmeasure["p8length"])
        ety_corpusMeasure_pos1widthVar.set(corpusmeasure["p1width"])
        ety_corpusMeasure_pos2widthVar.set(corpusmeasure["p2width"])
        ety_corpusMeasure_pos3widthVar.set(corpusmeasure["p3width"])
        ety_corpusMeasure_pos4widthVar.set(corpusmeasure["p4width"])
        ety_corpusMeasure_pos5widthVar.set(corpusmeasure["p5width"])
        ety_corpusMeasure_pos6widthVar.set(corpusmeasure["p6width"])
        ety_corpusMeasure_pos7widthVar.set(corpusmeasure["p7width"])
        ety_corpusMeasure_pos8widthVar.set(corpusmeasure["p8width"])
        ety_corpusMeasure_pos1countVar.set(corpusmeasure["p1count"])
        ety_corpusMeasure_pos2countVar.set(corpusmeasure["p2count"])
        ety_corpusMeasure_pos3countVar.set(corpusmeasure["p3count"])
        ety_corpusMeasure_pos4countVar.set(corpusmeasure["p4count"])
        ety_corpusMeasure_pos5countVar.set(corpusmeasure["p5count"])
        ety_corpusMeasure_pos6countVar.set(corpusmeasure["p6count"])
        ety_corpusMeasure_pos7countVar.set(corpusmeasure["p7count"])
        ety_corpusMeasure_pos8countVar.set(corpusmeasure["p8count"])
        cbb_corpusMeasure_pos1type.current(newindex = corpusmeasure["p1type"])
        cbb_corpusMeasure_pos2type.current(newindex = corpusmeasure["p2type"])
        cbb_corpusMeasure_pos3type.current(newindex = corpusmeasure["p3type"])
        cbb_corpusMeasure_pos4type.current(newindex = corpusmeasure["p4type"])
        cbb_corpusMeasure_pos5type.current(newindex = corpusmeasure["p5type"])
        cbb_corpusMeasure_pos6type.current(newindex = corpusmeasure["p6type"])
        cbb_corpusMeasure_pos7type.current(newindex = corpusmeasure["p7type"])
        cbb_corpusMeasure_pos8type.current(newindex = corpusmeasure["p8type"])

        glassmeasure = rcfiler["glassmeasure"]

        ety_glassMeasure_pos1lengthVar.set(glassmeasure["p1length"])
        ety_glassMeasure_pos2lengthVar.set(glassmeasure["p2length"])
        ety_glassMeasure_pos3lengthVar.set(glassmeasure["p3length"])
        ety_glassMeasure_pos4lengthVar.set(glassmeasure["p4length"])
        ety_glassMeasure_pos5lengthVar.set(glassmeasure["p5length"])
        ety_glassMeasure_pos6lengthVar.set(glassmeasure["p6length"])
        ety_glassMeasure_pos7lengthVar.set(glassmeasure["p7length"])
        ety_glassMeasure_pos8lengthVar.set(glassmeasure["p8length"])
        ety_glassMeasure_pos1widthVar.set(glassmeasure["p1width"])
        ety_glassMeasure_pos2widthVar.set(glassmeasure["p2width"])
        ety_glassMeasure_pos3widthVar.set(glassmeasure["p3width"])
        ety_glassMeasure_pos4widthVar.set(glassmeasure["p4width"])
        ety_glassMeasure_pos5widthVar.set(glassmeasure["p5width"])
        ety_glassMeasure_pos6widthVar.set(glassmeasure["p6width"])
        ety_glassMeasure_pos7widthVar.set(glassmeasure["p7width"])
        ety_glassMeasure_pos8widthVar.set(glassmeasure["p8width"])
        ety_glassMeasure_pos1countVar.set(glassmeasure["p1count"])
        ety_glassMeasure_pos2countVar.set(glassmeasure["p2count"])
        ety_glassMeasure_pos3countVar.set(glassmeasure["p3count"])
        ety_glassMeasure_pos4countVar.set(glassmeasure["p4count"])
        ety_glassMeasure_pos5countVar.set(glassmeasure["p5count"])
        ety_glassMeasure_pos6countVar.set(glassmeasure["p6count"])
        ety_glassMeasure_pos7countVar.set(glassmeasure["p7count"])
        ety_glassMeasure_pos8countVar.set(glassmeasure["p8count"])
        cbb_glassMeasure_pos1type.current(newindex = glassmeasure["p1type"])
        cbb_glassMeasure_pos2type.current(newindex = glassmeasure["p2type"])
        cbb_glassMeasure_pos3type.current(newindex = glassmeasure["p3type"])
        cbb_glassMeasure_pos4type.current(newindex = glassmeasure["p4type"])
        cbb_glassMeasure_pos5type.current(newindex = glassmeasure["p5type"])
        cbb_glassMeasure_pos6type.current(newindex = glassmeasure["p6type"])
        cbb_glassMeasure_pos7type.current(newindex = glassmeasure["p7type"])
        cbb_glassMeasure_pos8type.current(newindex = glassmeasure["p8type"])

        packaging = rcfiler["packaging"]

        ety_packaging_widthVar.set(packaging["packwidth"])
        ety_packaging_heightVar.set(packaging["packheight"])
        ety_packaging_depthVar.set(packaging["packdepth"])

    def btn_settings_callback(self):

        runSettingsInterface()

    def btn_quit_callback(self):

        self.closeWindow()

    def calcMeasures(self, creationCalc = False):

        try:

            doorAmount = int(ety_corInfo_doorVar.get())

        except:

            pass

        if doorAmount >= 5:

            if creationCalc == True:

                feedback = tkmsg.askyesnocancel(title = dataHandler.titleVersion, message = dataHandler.lang_msg_doorAmountInvalid)

            else:

                feedback = tkmsg.askyesno(title = dataHandler.titleVersion, message = dataHandler.lang_msg_doorAmountInvalid)

            if feedback == False:

                return 0

            elif feedback == None:

                return 1

        self.resetDefault(True)

        if calcHandler.calculateCuttings(int(ety_measure_widthVar.get()), int(ety_measure_heightVar.get()), int(ety_measure_depthVar.get())) == True:

            self.showInfo(dataHandler.lang_calc_success)

        else:

            self.showInfo(dataHandler.lang_calc_failed, False)

    def notebookTabChange(self, notebook):
        
        global lastSelectedListbox

        tabList = notebook.tabs()

        for tab in tabList:

            notebook.tab(tab, compound = "image")
            notebook.tab(tab, sticky = "we")

        activeTab = notebook.select()
        notebook.tab(activeTab, compound = tk.LEFT)

        activeIndex = notebook.index(activeTab)

        if activeIndex == 0:

            childList = tvw_ntbColor_aluminum.get_children()
            tvw_ntbColor_aluminum.selection_set(childList[0])
            tvw_ntbColor_aluminum.see(childList[0])

        elif activeIndex == 1:

            childList = tvw_ntbColor_unicolor.get_children()
            tvw_ntbColor_unicolor.selection_set(childList[0])
            tvw_ntbColor_unicolor.see(childList[0])

        elif activeIndex == 2:

            childList = tvw_ntbColor_wooden.get_children()
            tvw_ntbColor_wooden.selection_set(childList[0])
            tvw_ntbColor_wooden.see(childList[0])

        elif activeIndex == 3:

            childList = tvw_ntbColor_material.get_children()
            tvw_ntbColor_material.selection_set(childList[0])
            tvw_ntbColor_material.see(childList[0])
        
        lastSelectedListbox = activeIndex

    def treeviewChange(self, treeview: ttk.Treeview):

        global lastSelectedListboxItem

        selection = treeview.selection()[0]

        itemValues = treeview.item(selection)["values"]

        color = itemValues[0] + " " + itemValues[1]
        
        ety_color_selectedVar.set(color)

        lastSelectedListboxItem = selection

    def fillTreeviewlists(self):

        global codesAluminum
        codesAluminum = []
        codes = fileHandler.readFile(dataHandler.fPth_codesAluminum)

        for line in codes:
            if line[0] != "#":
                content = line.split("#")
                tvw_ntbColor_aluminum.insert("", tk.END, values = (content[0], content[1]))
                codesAluminum.append((content[0], content[1]))

        global codesUnicolor
        codesUnicolor = []
        codes = fileHandler.readFile(dataHandler.fPth_codesUnicolor)

        for line in codes:
            if line[0] != "#":
                content = line.split("#")
                tvw_ntbColor_unicolor.insert("", tk.END, values = (content[0], content[1]))
                codesUnicolor.append((content[0], content[1]))

        global codesWooden
        codesWooden = []
        codes = fileHandler.readFile(dataHandler.fPth_codesWood)
        
        for line in codes:
            if line[0] != "#":
                content = line.split("#")
                tvw_ntbColor_wooden.insert("", tk.END, values = (content[0], content[1]))
                codesWooden.append((content[0], content[1]))

        global codesMaterial
        codesMaterial = []
        codes = fileHandler.readFile(dataHandler.fPth_codesMaterial)
        
        for line in codes:
            if line[0] != "#":
                content = line.split("#")
                tvw_ntbColor_material.insert("", tk.END, values = (content[0], content[1]))
                codesMaterial.append((content[0], content[1]))

    def fillCombobox(self):

        cbbListCorpusMeasure = [
            cbb_corpusMeasure_pos1type,
            cbb_corpusMeasure_pos2type,
            cbb_corpusMeasure_pos3type,
            cbb_corpusMeasure_pos4type,
            cbb_corpusMeasure_pos5type,
            cbb_corpusMeasure_pos6type,
            cbb_corpusMeasure_pos7type,
            cbb_corpusMeasure_pos8type
        ]

        cbbListGlassMeasure = [
            cbb_glassMeasure_pos1type,
            cbb_glassMeasure_pos2type,
            cbb_glassMeasure_pos3type,
            cbb_glassMeasure_pos4type,
            cbb_glassMeasure_pos5type,
            cbb_glassMeasure_pos6type,
            cbb_glassMeasure_pos7type,
            cbb_glassMeasure_pos8type
        ]

        content = [
            dataHandler.lang_data_genInfo_type_surface,
            dataHandler.lang_data_genInfo_type_concealed,
            dataHandler.lang_data_genInfo_type_concealedMF
        ]

        cbb_genInfo_type.delete(0, tk.END)
        cbb_genInfo_type.configure(values = content)
        cbb_genInfo_type.current(newindex = 0)

        content = [
            dataHandler.lang_general_none,
            dataHandler.lang_data_genInfo_specials_LEDfrontal,
            dataHandler.lang_data_genInfo_specials_LEDinternal
        ]

        cbb_genInfo_specials.delete(0, tk.END)
        cbb_genInfo_specials.configure(values = content)
        cbb_genInfo_specials.current(newindex = 0)

        content = [
            dataHandler.lang_general_none,
            dataHandler.lang_data_corInfo_light_warm,
            dataHandler.lang_data_corInfo_light_neutral,
            dataHandler.lang_data_corInfo_light_cct,
            dataHandler.lang_data_corInfo_light_rgb
        ]

        cbb_corInfo_light.delete(0, tk.END)
        cbb_corInfo_light.configure(values = content)
        cbb_corInfo_light.current(newindex = 0)

        content = [
            dataHandler.lang_general_none,
            dataHandler.lang_data_extra_type_1vert,
            dataHandler.lang_data_extra_type_2vert,
            dataHandler.lang_data_extra_type_1hori
        ]

        cbb_extra_type.delete(0, tk.END)
        cbb_extra_type.configure(values = content)
        cbb_extra_type.current(newindex = 0)

        for combobox in cbbListCorpusMeasure:

            content = [
                dataHandler.lang_general_none,
                dataHandler.lang_data_corpusMeasure_type_ground,
                dataHandler.lang_data_corpusMeasure_type_side,
                dataHandler.lang_data_corpusMeasure_type_middleground,
                dataHandler.lang_data_corpusMeasure_type_middleside,
                dataHandler.lang_data_corpusMeasure_type_MF_ground,
                dataHandler.lang_data_corpusMeasure_type_MF_side,
                dataHandler.lang_data_corpusMeasure_type_backwall
            ]

            combobox.delete(0, tk.END)
            combobox.configure(values = content)
            combobox.current(newindex = 0)

        for combobox in cbbListGlassMeasure:

            content = [
                dataHandler.lang_general_none,
                dataHandler.lang_data_glassMeasure_type_mirror3,
                dataHandler.lang_data_glassMeasure_type_mirror6,
                dataHandler.lang_data_glassMeasure_type_glass6
            ]
        
            combobox.delete(0, tk.END)
            combobox.configure(values = content)
            combobox.current(newindex = 0)

    def validateEntryInput(self, input, acttyp):

        if acttyp == "1":

            if not input.isdigit():

                return False

        return True

    def checkInputs(self):
        
        valid = True

        if ety_genInfo_orderIDVar.get() == "":

            lbl_genInfo_orderID.configure(foreground = "red")

            valid = False

        if ety_measure_widthVar.get() == "":

            lbl_measure_width.configure(foreground = "red")

            valid = False
        
        if ety_measure_heightVar.get() == "":

            lbl_measure_height.configure(foreground = "red")

            valid = False

        if ety_measure_depthVar.get() == "":

            lbl_measure_depth.configure(foreground = "red")

            valid = False

        if ety_corInfo_doorVar.get() == "":

            lbl_corInfo_door.configure(foreground = "red")

            valid = False

        if ety_corInfo_shelfVar.get() == "":

            lbl_corInfo_shelf.configure(foreground = "red")

            valid = False

        overhandList = [0, 1, 2]

        if cbb_extra_type.current() in overhandList and ety_corInfo_overhangUpperVar.get() == "":

            lbl_corInfo_overhangUpper.configure(foreground = "red")

            valid = False

        if cbb_extra_type.current() in overhandList and ety_corInfo_overhangLowerVar.get() == "":

            lbl_corInfo_overhangLower.configure(foreground = "red")

            valid = False

        if cbb_extra_type.current() != 0 and ety_extra_measureVar.get() == "":

            lbl_extra_measure.configure(foreground = "red")

            valid = False

        if valid == False:

            msgBox = tkmsg.showwarning(title = title, message = dataHandler.lang_error_inputs)
            return False

        else:
            
            return True

    def updateDependencies(self, enableAll = False):

        # overlapping
        if enableAll == True:

            ety_corInfo_overhangUpper.configure(state = "enabled")
            ety_corInfo_overhangLower.configure(state = "enabled")

        elif cbb_extra_type.current() == 3 or cbb_extra_type.current() == 4:

            ety_corInfo_overhangUpperVar.set("")
            ety_corInfo_overhangLowerVar.set("")

            self.resetLabel(lbl_corInfo_overhangUpper)
            self.resetLabel(lbl_corInfo_overhangLower)

            ety_corInfo_overhangUpper.configure(state = "disabled")
            ety_corInfo_overhangLower.configure(state = "disabled")

        else:

            ety_corInfo_overhangUpper.configure(state = "enabled")
            ety_corInfo_overhangLower.configure(state = "enabled")

        # extras
        if cbb_extra_type.current() != 0 or enableAll == True:

            ety_extra_measure.configure(state = "enabled")
            cbt_extra_covered.configure(state = "enabled")

        else:

            ety_extra_measureVar.set("")
            cbt_extra_coveredVar.set(0)

            self.resetLabel(lbl_extra_measure)

            ety_extra_measure.configure(state = "disabled")
            cbt_extra_covered.configure(state = "disabled")

        # corpus measurements
        if cbt_corpusMeasure_overrideVar.get() == 1 or enableAll == True:

            ety_corpusMeasure_pos1length.configure(state = "enabled")
            ety_corpusMeasure_pos2length.configure(state = "enabled")
            ety_corpusMeasure_pos3length.configure(state = "enabled")
            ety_corpusMeasure_pos4length.configure(state = "enabled")
            ety_corpusMeasure_pos5length.configure(state = "enabled")
            ety_corpusMeasure_pos6length.configure(state = "enabled")
            ety_corpusMeasure_pos7length.configure(state = "enabled")
            ety_corpusMeasure_pos8length.configure(state = "enabled")
            
            ety_corpusMeasure_pos1width.configure(state = "enabled")
            ety_corpusMeasure_pos2width.configure(state = "enabled")
            ety_corpusMeasure_pos3width.configure(state = "enabled")
            ety_corpusMeasure_pos4width.configure(state = "enabled")
            ety_corpusMeasure_pos5width.configure(state = "enabled")
            ety_corpusMeasure_pos6width.configure(state = "enabled")
            ety_corpusMeasure_pos7width.configure(state = "enabled")
            ety_corpusMeasure_pos8width.configure(state = "enabled")
            
            ety_corpusMeasure_pos1count.configure(state = "enabled")
            ety_corpusMeasure_pos2count.configure(state = "enabled")
            ety_corpusMeasure_pos3count.configure(state = "enabled")
            ety_corpusMeasure_pos4count.configure(state = "enabled")
            ety_corpusMeasure_pos5count.configure(state = "enabled")
            ety_corpusMeasure_pos6count.configure(state = "enabled")
            ety_corpusMeasure_pos7count.configure(state = "enabled")
            ety_corpusMeasure_pos8count.configure(state = "enabled")

            cbb_corpusMeasure_pos1type.configure(state = "readonly")
            cbb_corpusMeasure_pos2type.configure(state = "readonly")
            cbb_corpusMeasure_pos3type.configure(state = "readonly")
            cbb_corpusMeasure_pos4type.configure(state = "readonly")
            cbb_corpusMeasure_pos5type.configure(state = "readonly")
            cbb_corpusMeasure_pos6type.configure(state = "readonly")
            cbb_corpusMeasure_pos7type.configure(state = "readonly")
            cbb_corpusMeasure_pos8type.configure(state = "readonly")

        else:

            ety_corpusMeasure_pos1length.configure(state = "disabled")
            ety_corpusMeasure_pos2length.configure(state = "disabled")
            ety_corpusMeasure_pos3length.configure(state = "disabled")
            ety_corpusMeasure_pos4length.configure(state = "disabled")
            ety_corpusMeasure_pos5length.configure(state = "disabled")
            ety_corpusMeasure_pos6length.configure(state = "disabled")
            ety_corpusMeasure_pos7length.configure(state = "disabled")
            ety_corpusMeasure_pos8length.configure(state = "disabled")
            
            ety_corpusMeasure_pos1width.configure(state = "disabled")
            ety_corpusMeasure_pos2width.configure(state = "disabled")
            ety_corpusMeasure_pos3width.configure(state = "disabled")
            ety_corpusMeasure_pos4width.configure(state = "disabled")
            ety_corpusMeasure_pos5width.configure(state = "disabled")
            ety_corpusMeasure_pos6width.configure(state = "disabled")
            ety_corpusMeasure_pos7width.configure(state = "disabled")
            ety_corpusMeasure_pos8width.configure(state = "disabled")
            
            ety_corpusMeasure_pos1count.configure(state = "disabled")
            ety_corpusMeasure_pos2count.configure(state = "disabled")
            ety_corpusMeasure_pos3count.configure(state = "disabled")
            ety_corpusMeasure_pos4count.configure(state = "disabled")
            ety_corpusMeasure_pos5count.configure(state = "disabled")
            ety_corpusMeasure_pos6count.configure(state = "disabled")
            ety_corpusMeasure_pos7count.configure(state = "disabled")
            ety_corpusMeasure_pos8count.configure(state = "disabled")

            cbb_corpusMeasure_pos1type.configure(state = "disabled")
            cbb_corpusMeasure_pos2type.configure(state = "disabled")
            cbb_corpusMeasure_pos3type.configure(state = "disabled")
            cbb_corpusMeasure_pos4type.configure(state = "disabled")
            cbb_corpusMeasure_pos5type.configure(state = "disabled")
            cbb_corpusMeasure_pos6type.configure(state = "disabled")
            cbb_corpusMeasure_pos7type.configure(state = "disabled")
            cbb_corpusMeasure_pos8type.configure(state = "disabled")

        # glass measurements
        if cbt_glassMeasure_overrideVar.get() == 1 or enableAll == True:

            ety_glassMeasure_pos1length.configure(state = "enabled")
            ety_glassMeasure_pos2length.configure(state = "enabled")
            ety_glassMeasure_pos3length.configure(state = "enabled")
            ety_glassMeasure_pos4length.configure(state = "enabled")
            ety_glassMeasure_pos5length.configure(state = "enabled")
            ety_glassMeasure_pos6length.configure(state = "enabled")
            ety_glassMeasure_pos7length.configure(state = "enabled")
            ety_glassMeasure_pos8length.configure(state = "enabled")
            
            ety_glassMeasure_pos1width.configure(state = "enabled")
            ety_glassMeasure_pos2width.configure(state = "enabled")
            ety_glassMeasure_pos3width.configure(state = "enabled")
            ety_glassMeasure_pos4width.configure(state = "enabled")
            ety_glassMeasure_pos5width.configure(state = "enabled")
            ety_glassMeasure_pos6width.configure(state = "enabled")
            ety_glassMeasure_pos7width.configure(state = "enabled")
            ety_glassMeasure_pos8width.configure(state = "enabled")
            
            ety_glassMeasure_pos1count.configure(state = "enabled")
            ety_glassMeasure_pos2count.configure(state = "enabled")
            ety_glassMeasure_pos3count.configure(state = "enabled")
            ety_glassMeasure_pos4count.configure(state = "enabled")
            ety_glassMeasure_pos5count.configure(state = "enabled")
            ety_glassMeasure_pos6count.configure(state = "enabled")
            ety_glassMeasure_pos7count.configure(state = "enabled")
            ety_glassMeasure_pos8count.configure(state = "enabled")

            cbb_glassMeasure_pos1type.configure(state = "readonly")
            cbb_glassMeasure_pos2type.configure(state = "readonly")
            cbb_glassMeasure_pos3type.configure(state = "readonly")
            cbb_glassMeasure_pos4type.configure(state = "readonly")
            cbb_glassMeasure_pos5type.configure(state = "readonly")
            cbb_glassMeasure_pos6type.configure(state = "readonly")
            cbb_glassMeasure_pos7type.configure(state = "readonly")
            cbb_glassMeasure_pos8type.configure(state = "readonly")

        else:

            ety_glassMeasure_pos1length.configure(state = "disabled")
            ety_glassMeasure_pos2length.configure(state = "disabled")
            ety_glassMeasure_pos3length.configure(state = "disabled")
            ety_glassMeasure_pos4length.configure(state = "disabled")
            ety_glassMeasure_pos5length.configure(state = "disabled")
            ety_glassMeasure_pos6length.configure(state = "disabled")
            ety_glassMeasure_pos7length.configure(state = "disabled")
            ety_glassMeasure_pos8length.configure(state = "disabled")
            
            ety_glassMeasure_pos1width.configure(state = "disabled")
            ety_glassMeasure_pos2width.configure(state = "disabled")
            ety_glassMeasure_pos3width.configure(state = "disabled")
            ety_glassMeasure_pos4width.configure(state = "disabled")
            ety_glassMeasure_pos5width.configure(state = "disabled")
            ety_glassMeasure_pos6width.configure(state = "disabled")
            ety_glassMeasure_pos7width.configure(state = "disabled")
            ety_glassMeasure_pos8width.configure(state = "disabled")
            
            ety_glassMeasure_pos1count.configure(state = "disabled")
            ety_glassMeasure_pos2count.configure(state = "disabled")
            ety_glassMeasure_pos3count.configure(state = "disabled")
            ety_glassMeasure_pos4count.configure(state = "disabled")
            ety_glassMeasure_pos5count.configure(state = "disabled")
            ety_glassMeasure_pos6count.configure(state = "disabled")
            ety_glassMeasure_pos7count.configure(state = "disabled")
            ety_glassMeasure_pos8count.configure(state = "disabled")

            cbb_glassMeasure_pos1type.configure(state = "disabled")
            cbb_glassMeasure_pos2type.configure(state = "disabled")
            cbb_glassMeasure_pos3type.configure(state = "disabled")
            cbb_glassMeasure_pos4type.configure(state = "disabled")
            cbb_glassMeasure_pos5type.configure(state = "disabled")
            cbb_glassMeasure_pos6type.configure(state = "disabled")
            cbb_glassMeasure_pos7type.configure(state = "disabled")
            cbb_glassMeasure_pos8type.configure(state = "disabled")

        # packaging
        if cbt_packaging_overrideVar.get() == 1 or enableAll == True:

            ety_packaging_width.configure(state = "enabled")
            ety_packaging_height.configure(state = "enabled")
            ety_packaging_depth.configure(state = "enabled")

        else:

            ety_packaging_width.configure(state = "disabled")
            ety_packaging_height.configure(state = "disabled")
            ety_packaging_depth.configure(state = "disabled")

    def resetDefault(self, calcReset = False):

        # general Info
        if (calcReset == False):
            ety_genInfo_orderIDVar.set("")
            cbb_genInfo_type.current(newindex = 0)
            cbt_genInfo_ptoVar.set(0)
            cbb_genInfo_specials.current(newindex = 0)

        # color
        if (calcReset == False):
            ntb_colorcode.select(0)

            childList = tvw_ntbColor_aluminum.get_children()
            tvw_ntbColor_aluminum.selection_set(childList[0])

        # measure
        if (calcReset == False):
            ety_measure_widthVar.set("")
            ety_measure_heightVar.set("")
            ety_measure_depthVar.set("")

        # corpus Info
        if (calcReset == False):
            cbb_corInfo_light.current(newindex = 0)
            cbt_corInfo_indLightVar.set(0)
            ety_corInfo_doorVar.set("")
            ety_corInfo_shelfVar.set("")
            ety_corInfo_overhangUpperVar.set("")
            ety_corInfo_overhangLowerVar.set("")

        # extra Space
        if (calcReset == False):
            cbb_extra_type.current(newindex = 0)
            ety_extra_measureVar.set("")
            cbt_extra_coveredVar.set(0)

        # corpus Measurements
        if (calcReset == False or (calcReset == True and cbt_corpusMeasure_overrideVar.get() == 0)):
            ety_corpusMeasure_pos1lengthVar.set("")
            ety_corpusMeasure_pos2lengthVar.set("")
            ety_corpusMeasure_pos3lengthVar.set("")
            ety_corpusMeasure_pos4lengthVar.set("")
            ety_corpusMeasure_pos5lengthVar.set("")
            ety_corpusMeasure_pos6lengthVar.set("")
            ety_corpusMeasure_pos7lengthVar.set("")
            ety_corpusMeasure_pos8lengthVar.set("")
            ety_corpusMeasure_pos1widthVar.set("")
            ety_corpusMeasure_pos2widthVar.set("")
            ety_corpusMeasure_pos3widthVar.set("")
            ety_corpusMeasure_pos4widthVar.set("")
            ety_corpusMeasure_pos5widthVar.set("")
            ety_corpusMeasure_pos6widthVar.set("")
            ety_corpusMeasure_pos7widthVar.set("")
            ety_corpusMeasure_pos8widthVar.set("")
            ety_corpusMeasure_pos1countVar.set("")
            ety_corpusMeasure_pos2countVar.set("")
            ety_corpusMeasure_pos3countVar.set("")
            ety_corpusMeasure_pos4countVar.set("")
            ety_corpusMeasure_pos5countVar.set("")
            ety_corpusMeasure_pos6countVar.set("")
            ety_corpusMeasure_pos7countVar.set("")
            ety_corpusMeasure_pos8countVar.set("")
            cbb_corpusMeasure_pos1type.current(newindex = 0)
            cbb_corpusMeasure_pos2type.current(newindex = 0)
            cbb_corpusMeasure_pos3type.current(newindex = 0)
            cbb_corpusMeasure_pos4type.current(newindex = 0)
            cbb_corpusMeasure_pos5type.current(newindex = 0)
            cbb_corpusMeasure_pos6type.current(newindex = 0)
            cbb_corpusMeasure_pos7type.current(newindex = 0)
            cbb_corpusMeasure_pos8type.current(newindex = 0)

        if (calcReset == False):
            cbt_corpusMeasure_overrideVar.set(0)

        # glass Measurements
        if (calcReset == False or (calcReset == True and cbt_glassMeasure_overrideVar.get() == 0)):
            ety_glassMeasure_pos1lengthVar.set("")
            ety_glassMeasure_pos2lengthVar.set("")
            ety_glassMeasure_pos3lengthVar.set("")
            ety_glassMeasure_pos4lengthVar.set("")
            ety_glassMeasure_pos5lengthVar.set("")
            ety_glassMeasure_pos6lengthVar.set("")
            ety_glassMeasure_pos7lengthVar.set("")
            ety_glassMeasure_pos8lengthVar.set("")
            ety_glassMeasure_pos1widthVar.set("")
            ety_glassMeasure_pos2widthVar.set("")
            ety_glassMeasure_pos3widthVar.set("")
            ety_glassMeasure_pos4widthVar.set("")
            ety_glassMeasure_pos5widthVar.set("")
            ety_glassMeasure_pos6widthVar.set("")
            ety_glassMeasure_pos7widthVar.set("")
            ety_glassMeasure_pos8widthVar.set("")
            ety_glassMeasure_pos1countVar.set("")
            ety_glassMeasure_pos2countVar.set("")
            ety_glassMeasure_pos3countVar.set("")
            ety_glassMeasure_pos4countVar.set("")
            ety_glassMeasure_pos5countVar.set("")
            ety_glassMeasure_pos6countVar.set("")
            ety_glassMeasure_pos7countVar.set("")
            ety_glassMeasure_pos8countVar.set("")
            cbb_glassMeasure_pos1type.current(newindex = 0)
            cbb_glassMeasure_pos2type.current(newindex = 0)
            cbb_glassMeasure_pos3type.current(newindex = 0)
            cbb_glassMeasure_pos4type.current(newindex = 0)
            cbb_glassMeasure_pos5type.current(newindex = 0)
            cbb_glassMeasure_pos6type.current(newindex = 0)
            cbb_glassMeasure_pos7type.current(newindex = 0)
            cbb_glassMeasure_pos8type.current(newindex = 0)
        
        if (calcReset == False):
            cbt_glassMeasure_overrideVar.set(0)

        # packaging
        if (calcReset == False or (calcReset == True and cbt_packaging_overrideVar.get() == 0)):
            ety_packaging_widthVar.set("")
            ety_packaging_heightVar.set("")
            ety_packaging_depthVar.set("")
        
        if (calcReset == False):
            cbt_packaging_overrideVar.set(0)

        # textbox
        if (calcReset == False):
            txt_infoBox.delete(1.0, "end")

        # labels
        if (calcReset == False):
            self.resetLabel(lbl_genInfo_orderID)
            self.resetLabel(lbl_measure_width)
            self.resetLabel(lbl_measure_height)
            self.resetLabel(lbl_measure_depth)
            self.resetLabel(lbl_corInfo_door)
            self.resetLabel(lbl_corInfo_shelf)
            self.resetLabel(lbl_corInfo_overhangUpper)
            self.resetLabel(lbl_corInfo_overhangLower)
            self.resetLabel(lbl_extra_measure)

        self.updateDependencies()

    def resetLabel(self, label: ttk.Label):

        label.configure(foreground = "black")

    def addTracing(self):

        ety_genInfo_orderIDVar.trace("w", lambda name, index, mode, label = lbl_genInfo_orderID : self.resetLabel(label))
        ety_measure_widthVar.trace("w", lambda name, index, mode, label = lbl_measure_width : self.resetLabel(label))
        ety_measure_heightVar.trace("w", lambda name, index, mode, label = lbl_measure_height : self.resetLabel(label))
        ety_measure_depthVar.trace("w", lambda name, index, mode, label = lbl_measure_depth : self.resetLabel(label))
        ety_corInfo_doorVar.trace("w", lambda name, index, mode, label = lbl_corInfo_door : self.resetLabel(label))
        ety_corInfo_shelfVar.trace("w", lambda name, index, mode, label = lbl_corInfo_shelf : self.resetLabel(label))
        ety_corInfo_overhangUpperVar.trace("w", lambda name, index, mode, label = lbl_corInfo_overhangUpper : self.resetLabel(label))
        ety_corInfo_overhangLowerVar.trace("w", lambda name, index, mode, label = lbl_corInfo_overhangLower : self.resetLabel(label))
        ety_extra_measureVar.trace("w", lambda name, index, mode, label = lbl_extra_measure : self.resetLabel(label))

    def centerWindow(self):

        root.update()

        rootWidth = root.winfo_reqwidth()
        rootHeight = root.winfo_reqheight()

        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()

        posX = floor((screenWidth / 2) - (rootWidth / 2))
        posY = floor((screenHeight / 2) - (rootHeight / 2))

        root.geometry("+{}+{}".format(posX, posY))

    def closeWindow(self):

        dataHandler.deleteTmpFolder()
        self.quit()

    def cb_key_return(self, widget):

        widgetClass = widget.winfo_class()

        if widgetClass == "TCheckbutton":

            widget.invoke()

    def treeviewSort(self, treeview: ttk.Treeview, column: int):
        
        global tvw_ntbColor_aluminum_reversed
        global tvw_ntbColor_unicolor_reversed
        global tvw_ntbColor_wooden_reversed
        global tvw_ntbColor_material_reversed

        global tvw_ntbColor_aluminum_reversed_last
        global tvw_ntbColor_unicolor_reversed_last
        global tvw_ntbColor_wooden_reversed_last
        global tvw_ntbColor_material_reversed_last

        if lastSelectedListbox == 0:
            reverse = tvw_ntbColor_aluminum_reversed
            reverse_last = tvw_ntbColor_aluminum_reversed_last

        elif lastSelectedListbox == 1:
            reverse = tvw_ntbColor_unicolor_reversed
            reverse_last = tvw_ntbColor_unicolor_reversed_last

        elif lastSelectedListbox == 2:
            reverse = tvw_ntbColor_wooden_reversed
            reverse_last = tvw_ntbColor_wooden_reversed_last

        elif lastSelectedListbox == 3:
            reverse = tvw_ntbColor_material_reversed
            reverse_last = tvw_ntbColor_material_reversed_last

        if reverse_last != column or reverse_last == None:

            reverse = None

        if reverse == None:
            reverse = False
            if column == 0:
                treeview.heading("id", text = dataHandler.lang_general_ID + " ↑")
                treeview.heading("name", text = dataHandler.lang_general_name)
                reverse_last = 0
            else:
                treeview.heading("id", text = dataHandler.lang_general_ID)
                treeview.heading("name", text = dataHandler.lang_general_name + " ↑")
                reverse_last = 1

        elif reverse == False:
            reverse = True
            if column == 0:
                treeview.heading("id", text = dataHandler.lang_general_ID + " ↓")
                treeview.heading("name", text = dataHandler.lang_general_name)
                reverse_last = 0
            else:
                treeview.heading("id", text = dataHandler.lang_general_ID)
                treeview.heading("name", text = dataHandler.lang_general_name + " ↓")
                reverse_last = 1

        else:
            reverse = None
            if column == 0:
                treeview.heading("id", text = dataHandler.lang_general_ID)
                treeview.heading("name", text = dataHandler.lang_general_name)
                reverse_last = 0
            else:
                treeview.heading("id", text = dataHandler.lang_general_ID)
                treeview.heading("name", text = dataHandler.lang_general_name)
                reverse_last = 1
        
        reverse_last = column

        if lastSelectedListbox == 0:
            tvw_ntbColor_aluminum_reversed = reverse
            tvw_ntbColor_aluminum_reversed_last = reverse_last

        elif lastSelectedListbox == 1:
            tvw_ntbColor_unicolor_reversed = reverse
            tvw_ntbColor_unicolor_reversed_last = reverse_last

        elif lastSelectedListbox == 2:
            tvw_ntbColor_wooden_reversed = reverse
            tvw_ntbColor_wooden_reversed_last = reverse_last

        elif lastSelectedListbox == 3:
            tvw_ntbColor_material_reversed = reverse
            tvw_ntbColor_material_reversed_last = reverse_last

        i = 0
        if column == 0:
            i = 1

        if reverse != None:

            contentDict = {}

            for item in treeview.get_children():

                entry = treeview.item(item)["values"]

                contentDict[entry[column]] = entry[i]

                treeview.delete(item)

            entryList = sorted(contentDict.items(), reverse = reverse)

        else:

            for item in treeview.get_children():

                treeview.delete(item)

            if lastSelectedListbox == 0:

                entryList = codesAluminum

            elif lastSelectedListbox == 1:

                entryList = codesUnicolor

            elif lastSelectedListbox == 2:

                entryList = codesWooden

            elif lastSelectedListbox == 3:

                entryList = codesMaterial

        for entry in entryList:

            if reverse != None or (reverse == None and column == 0):

                treeview.insert("", tk.END, values = (entry[column], entry[i]))

            else:

                treeview.insert("", tk.END, values = (entry[i], entry[column]))

        childList = treeview.get_children()
        treeview.selection_set(childList[0])
        treeview.see(childList[0])

    def tooltip(self, tooltipID = None, hideTooltip = False):

        if infoShown == True:

            return

        if hideTooltip == True:

            ety_general_feedbackVar.set("")

        else:

            if tooltipID == None:

                tooltipID = 0

            ety_general_feedbackVar.set(dataHandler.dict_tooltips[tooltipID])

    def showInfo(self, infoContent: str, positive = True):

        global infoShown

        infoShown = True

        if positive == True:

            ety_general_feedback.configure(foreground = "green")

        else:

            ety_general_feedback.configure(foreground = "red")

        ety_general_feedbackVar.set(infoContent)
    
        self.after(5000, self.hideInfo)

    def hideInfo(self):

        global infoShown

        infoShown = False

        ety_general_feedbackVar.set("")
        ety_general_feedback.configure(foreground = "grey")

    def getLatestRelease(self):

        global releaseLatest
        global releaseExperimental

        releaseLatest, releaseExperimental = updateHandler.getReleases()

        if releaseLatest == None:

            return False

        releaseVersionTag = str(releaseLatest["tag_name"]).split(".")

        releaseVersion = int(releaseVersionTag[0] + releaseVersionTag[1] + releaseVersionTag[2])

        prgVersion = int(str(dataHandler.version) + str(dataHandler.subversion) + str(dataHandler.subsubversion))

        if releaseVersion > prgVersion:
                        
            runUpdaterInterface()

class settingsInterface(tk.Toplevel):

    def __init__(self):

        tk.Toplevel.__init__(self)
        self.withdraw()
        self.resizable(False, False)
        self.grab_set()
        self.iconbitmap(dataHandler.fPth_logo)
        self.createWidgets()
        self.centerWindow()
        self.loadSettings()
        self.update()
        self.deiconify()

    def createWidgets(self):

        global lbl_fileHandling_saveDir

        # -------------------------------------- #
        #      Info Header                       #
        # -------------------------------------- #

        # frame
        frm_prgInfo = ttk.LabelFrame(master = self, text = dataHandler.lang_frmPrgInfo, style = "Bold.TLabelframe")
        frm_prgInfo.grid(row = 0, column = 0, padx = 2, pady = 1)

        # spacer
        spc_prgInfo = tk.Label(master = frm_prgInfo, width = 27, height = 0)
        spc_prgInfo.grid(row = 0, column = 0)

        # label
        version = "Version " + str(dataHandler.version) + "." + str(dataHandler.subversion) + "." + str(dataHandler.subsubversion)
        lbl_prgInfo_name = ttk.Label(master = frm_prgInfo, text = dataHandler.title + " " + version, width = 32, anchor = "center", state = "disabled")
        lbl_prgInfo_author = ttk.Label(master = frm_prgInfo, text = "Made by Achim Abdinghoff", width = 32, anchor = "center", state = "disabled")
        lbl_prgInfo_git = ttk.Label(master = frm_prgInfo, text = dataHandler.lang_prgInfo_git, width = 32, anchor = "center", foreground = "blue", cursor = "hand2")
        lbl_prgInfo_contact = ttk.Label(master = frm_prgInfo, text = dataHandler.lang_prgInfo_contact, width = 32, anchor = "center", foreground = "blue", cursor = "hand2")

        # separator
        sep_prgInfo = ttk.Separator(master = frm_prgInfo, orient = "horizontal")

        # label grid
        lbl_prgInfo_name.grid(row = 0, column = 0, columnspan = 3, sticky = "we")
        lbl_prgInfo_author.grid(row = 1, column = 0, columnspan = 3, sticky = "we")
        lbl_prgInfo_git.grid(row = 3, column = 0, sticky = "we")
        lbl_prgInfo_contact.grid(row = 4, column = 0, sticky = "we")

        # separator grid
        sep_prgInfo.grid(row = 2, column = 0, sticky = "we", padx = 10)

        lbl_prgInfo_git.bind("<Button-1>", lambda event, url = dataHandler.gitPath: self.openUrl(url))
        lbl_prgInfo_contact.bind("<Button-1>", lambda event: self.mailSend())

        # -------------------------------------- #
        #      File Handling                     #
        # -------------------------------------- #

        # frame
        frm_fileHandling = ttk.LabelFrame(master = self, text = dataHandler.lang_frmFileHandling, style = "Bold.TLabelframe")
        frm_fileHandling.grid(row = 1, column = 0, padx = 2, pady = 1)

        # spacer
        spc_fileHandling = tk.Label(master = frm_fileHandling, width = 27, height = 0)
        spc_fileHandling.grid(row = 0, column = 0, columnspan = 2)
        
        # label
        lbl_fileHandling_saveDir = ttk.Label(master = frm_fileHandling, text = dataHandler.lang_fileHandling_saveDir)

        # input
        ety_fileHandling_saveDir = ttk.Entry(master = frm_fileHandling, width = 25, textvariable = ety_fileHandling_saveDirVar)
        cbt_fileHandling_calculate = ttk.Checkbutton(master = frm_fileHandling, text = dataHandler.lang_fileHandling_calculate, variable = cbt_fileHandling_calculateVar)
        cbt_fileHandling_RCFile = ttk.Checkbutton(master = frm_fileHandling, text = dataHandler.lang_fileHandling_RCFile, variable = cbt_fileHandling_RCFileVar)
        cbt_fileHandling_openPDF = ttk.Checkbutton(master = frm_fileHandling, text = dataHandler.lang_fileHandling_openPDF, variable = cbt_fileHandling_openPDFVar)
        cbt_fileHandling_printPDF = ttk.Checkbutton(master = frm_fileHandling, text = dataHandler.lang_fileHandling_printPDF, variable = cbt_fileHandling_printPDFVar)

        # buttons
        btn_fileHandling_saveDir = ttk.Button(master = frm_fileHandling, text = "...", width = 3, command = self.btn_saveDir_callback)
        btn_fileHandling_files = ttk.Button(master = frm_fileHandling, text = dataHandler.lang_fileHandling_files, command = self.btn_filesDir_callback)

        # label grid
        lbl_fileHandling_saveDir.grid(row = 0, column = 0, padx = 1, pady = 1, sticky = "w")

        # input grid
        ety_fileHandling_saveDir.grid(row = 1, column = 0, padx = 2, pady = 1)
        cbt_fileHandling_calculate.grid(row = 2, column = 0, columnspan = 2, padx = 1, pady = 1, sticky = "w")
        cbt_fileHandling_RCFile.grid(row = 3, column = 0, columnspan = 2, padx = 1, pady = 1, sticky = "w")
        cbt_fileHandling_openPDF.grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1, sticky = "w")
        cbt_fileHandling_printPDF.grid(row = 5, column = 0, columnspan = 2, padx = 1, pady = 1, sticky = "w")

        # buttons grid
        btn_fileHandling_saveDir.grid(row = 1, column = 1, padx = 1, pady = 1)
        btn_fileHandling_files.grid(row = 6, column = 0, columnspan = 2, padx = 1, pady = 1, sticky = "we")

        # -------------------------------------- #
        #      Material Presets                  #
        # -------------------------------------- #

        # frame
        frm_matPresets = ttk.LabelFrame(master = self, text = dataHandler.lang_frmMatPresets, style = "Bold.TLabelframe")
        frm_matPresets.grid(row = 2, column = 0, padx = 2, pady = 1)

        # spacer
        spc_matPresets = tk.Label(master = frm_matPresets, width = 27, height = 0)
        spc_matPresets.grid(row = 0, column = 0, columnspan = 2)

        # label
        lbl_matPresets_packaging = ttk.Label(master = frm_matPresets, text = dataHandler.lang_matPresets_packaging)
        lbl_matPresets_wood = ttk.Label(master = frm_matPresets, text = dataHandler.lang_matPresets_wood)
        lbl_matPresets_aluminum = ttk.Label(master = frm_matPresets, text = dataHandler.lang_matPresets_aluminum)
        lbl_matPresets_LEDFrontal = ttk.Label(master = frm_matPresets, text = dataHandler.lang_matPresets_LEDFrontal)
        lbl_matPresets_LEDInternal = ttk.Label(master = frm_matPresets, text = dataHandler.lang_matPresets_LEDInternal)

        # input
        ety_matPresets_packaging = ttk.Entry(master = frm_matPresets, textvariable = ety_matPresets_packagingVar, width = 13, justify = "right")
        ety_matPresets_wood = ttk.Entry(master = frm_matPresets, textvariable = ety_matPresets_woodVar, width = 13, justify = "right")
        ety_matPresets_aluminum = ttk.Entry(master = frm_matPresets, textvariable = ety_matPresets_aluminumVar, width = 13, justify = "right")
        ety_matPresets_LEDFrontal = ttk.Entry(master = frm_matPresets, textvariable = ety_matPresets_LEDFrontalVar, width = 13, justify = "right")
        ety_matPresets_LEDInternal = ttk.Entry(master = frm_matPresets, textvariable = ety_matPresets_LEDInternalVar, width = 13, justify = "right")

        # label grid
        lbl_matPresets_packaging.grid(row = 0, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_matPresets_wood.grid(row = 1, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_matPresets_aluminum.grid(row = 2, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_matPresets_LEDFrontal.grid(row = 3, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_matPresets_LEDInternal.grid(row = 4, column = 0, padx = 1, pady = 1, sticky = "w")

        # input grid
        ety_matPresets_packaging.grid(row = 0, column = 1, padx = 1, pady = 1, sticky = "e")
        ety_matPresets_wood.grid(row = 1, column = 1, padx = 1, pady = 1, sticky = "e")
        ety_matPresets_aluminum.grid(row = 2, column = 1, padx = 1, pady = 1, sticky = "e")
        ety_matPresets_LEDFrontal.grid(row = 3, column = 1, padx = 1, pady = 1, sticky = "e")
        ety_matPresets_LEDInternal.grid(row = 4, column = 1, padx = 1, pady = 1, sticky = "e")

        # -------------------------------------- #
        #      Other                             #
        # -------------------------------------- #

        # frame
        frm_other = ttk.LabelFrame(master = self, text = dataHandler.lang_frmOther, style = "Bold.TLabelframe")
        frm_other.grid(row = 3, column = 0, padx = 2, pady = 1)

        # spacer
        spc_other = tk.Label(master = frm_other, width = 27, height = 0)
        spc_other.grid(row = 0, column = 0, columnspan = 2)

        # label
        lbl_other_language = ttk.Label(master = frm_other, text = dataHandler.lang_other_language)
        lbl_other_info = ttk.Label(master = frm_other, text = dataHandler.lang_other_info, state = "disabled")

        # input
        cbt_other_autoUpdate = ttk.Checkbutton(master = frm_other, text = dataHandler.lang_other_autoUpdate, variable = cbt_other_autoUpdateVar)
        ety_other_language = ttk.Entry(master = frm_other, width = 25, textvariable = ety_other_languageVar)

        # buttons
        btn_other_languageDir = ttk.Button(master = frm_other, text = "...", width = 3, command = self.btn_langDir_callback)
        btn_other_update = ttk.Button(master = frm_other, text = dataHandler.lang_button_update, command = self.btn_update_callback)

        # label grid
        lbl_other_language.grid(row = 0, column = 0, padx = 1, pady = 1, sticky = "w")
        lbl_other_info.grid(row = 2, column = 0, columnspan = 2, padx = 1, pady = 1, sticky = "w")

        # input grid
        cbt_other_autoUpdate.grid(row = 3, column = 0, columnspan = 2, padx = 1, pady = 1, sticky = "w")
        ety_other_language.grid(row = 1, column = 0, padx = 1, pady = 1)

        # buttons grid
        btn_other_languageDir.grid(row = 1, column = 1, padx = 1, pady = 1)
        btn_other_update.grid(row = 4, column = 0, columnspan = 2, sticky = "we")

        # -------------------------------------- #
        #      Buttons                           #
        # -------------------------------------- #

        # buttons
        btn_settings_save = ttk.Button(master = self, text = dataHandler.lang_button_save, width = 31, command = self.btn_save_callback)
        btn_settings_close = ttk.Button(master = self, text = dataHandler.lang_button_close, width = 31, command = self.btn_close_callback)

        # buttons grid
        btn_settings_save.grid(row = 4, column = 0, padx = 1, pady = 1)
        btn_settings_close.grid(row = 5, column = 0, padx = 1, pady = 1)

    def btn_saveDir_callback(self):

        saveDir = tkfile.askdirectory(mustexist = True)

        if saveDir != "" and isdir(saveDir) == True:

            ety_fileHandling_saveDirVar.set(saveDir)

    def btn_langDir_callback(self):

        langDir = tkfile.askopenfilename(filetypes = [("RC-Language-File", "*.rcl")], initialdir = "./lang")

        if langDir != "" and isfile(langDir) == True:

            ety_other_languageVar.set(langDir)

    def btn_filesDir_callback(self):

        path = join(curdir, "files")

        Popen('explorer "{}"'.format(path))

    def btn_update_callback(self):

        self.grab_release()

        global releaseLatest
        global releaseExperimental

        releaseLatest, releaseExperimental = updateHandler.getReleases()

        runUpdaterInterface()

    def btn_save_callback(self):

        self.saveSettings()
        closingSettingsInterface()

    def btn_close_callback(self):

        closingSettingsInterface()

    def loadSettings(self):

        dataHandler.readConfigINI()

        ety_fileHandling_saveDirVar.set(dataHandler.saveDir)
        cbt_fileHandling_calculateVar.set(dataHandler.calculateBeforeCreate)
        cbt_fileHandling_RCFileVar.set(dataHandler.createRCFile)
        cbt_fileHandling_openPDFVar.set(dataHandler.openPDF)
        cbt_fileHandling_printPDFVar.set(dataHandler.printPDF)

        ety_matPresets_packagingVar.set(dataHandler.packingMatThickness)
        ety_matPresets_woodVar.set(dataHandler.woodenThickness)
        ety_matPresets_aluminumVar.set(dataHandler.aluminiumThickness)
        ety_matPresets_LEDFrontalVar.set(dataHandler.LEDThicknessFrontal)
        ety_matPresets_LEDInternalVar.set(dataHandler.LEDThicknessInternal)

        cbt_other_autoUpdateVar.set(dataHandler.autoaskUpdate)
        ety_other_languageVar.set(dataHandler.activeLang)

    def saveSettings(self):

        dataHandler.saveDir = ety_fileHandling_saveDirVar.get()
        dataHandler.calculateBeforeCreate = cbt_fileHandling_calculateVar.get()
        dataHandler.createRCFile = cbt_fileHandling_RCFileVar.get()
        dataHandler.openPDF = cbt_fileHandling_openPDFVar.get()
        dataHandler.printPDF = cbt_fileHandling_printPDFVar.get()

        dataHandler.packingMatThickness = int(ety_matPresets_packagingVar.get())
        dataHandler.woodenThickness = int(ety_matPresets_woodVar.get())
        dataHandler.aluminiumThickness = int(ety_matPresets_aluminumVar.get())
        dataHandler.LEDThicknessFrontal = int(ety_matPresets_LEDFrontalVar.get())
        dataHandler.LEDThicknessInternal = int(ety_matPresets_LEDInternalVar.get())

        dataHandler.autoaskUpdate = cbt_other_autoUpdateVar.get()
        dataHandler.activeLang = ety_other_languageVar.get()

        dataHandler.writeConfigINI()

    def centerWindow(self):

        self.update()

        settingsWidth = self.winfo_reqwidth()
        settingsHeight = self.winfo_reqheight()

        rootWidth = root.winfo_reqwidth()
        rootHeight = root.winfo_reqheight()

        rootPosX = root.winfo_x()
        rootPosY = root.winfo_y()

        posX = floor(rootPosX + ((rootWidth / 2) - (settingsWidth / 2)))
        posY = floor(rootPosY + ((rootHeight / 2) - (settingsHeight / 2)))

        self.geometry("+{}+{}".format(posX, posY))

    def openUrl(self, url):

        webbrowser.open_new_tab(url)

    def mailSend(self):

        webbrowser.open("mailto:?to=roarcalc-supp@mailbox.org&subject=Feedback", new = 2)

    def closeWindow(self):

        self.destroy()

class updaterInterface(tk.Toplevel):

    def __init__(self):

        tk.Toplevel.__init__(self)
        self.withdraw()
        self.resizable(False, False)
        self.grab_set()
        self.lift()
        self.iconbitmap(dataHandler.fPth_logo)
        self.createWidgets()
        self.loadSettings()
        self.setRelease()
        self.centerWindow()
        self.update()
        self.deiconify()

    def createWidgets(self):

        # -------------------------------------- #
        #      Info Header                       #
        # -------------------------------------- #

        global lbl_updateInfo_state
        global ety_updateInfo_versionLatest

        # frame
        frm_updateInfo = ttk.LabelFrame(master = self, text = dataHandler.lang_frmUpdateInfo, style = "Bold.TLabelframe")
        frm_updateInfo.grid(row = 0, column = 0, padx = 2, pady = 1, columnspan = 2)

        # spacer
        spc_updateInfo = tk.Label(master = frm_updateInfo, width = 46)
        spc_updateInfo.grid(row = 0, column = 0, columnspan = 2)

        # label
        lbl_updateInfo_state = ttk.Label(master = frm_updateInfo, text = dataHandler.lang_updateInfo_statusNone, style = "Header.TLabel.Label")
        lbl_updateInfo_versionUsed = ttk.Label(master = frm_updateInfo, text = dataHandler.lang_updateInfo_versionUsed)
        lbl_updateInfo_versionLatest = ttk.Label(master = frm_updateInfo, text = dataHandler.lang_updateInfo_versionLatest)

        # inputs
        ety_updateInfo_versionUsed = ttk.Entry(master = frm_updateInfo, state = "disabled", textvariable = ety_updateInfo_versionUsedVar, foreground = "black")
        ety_updateInfo_versionLatest = ttk.Entry(master = frm_updateInfo, state = "disabled", textvariable = ety_updateInfo_versionLatestVar, foreground = "black")

        # label grid
        lbl_updateInfo_state.grid(row = 0, column = 0, columnspan = 2, pady = 5)
        lbl_updateInfo_versionUsed.grid(row = 1, column = 0, sticky = "w", padx = 1, pady = 1)
        lbl_updateInfo_versionLatest.grid(row = 2, column = 0, sticky = "w", padx = 1, pady = 1)

        # inputs grid
        ety_updateInfo_versionUsed.grid(row = 1, column = 1, sticky = "e", padx = 1, pady = 1)
        ety_updateInfo_versionLatest.grid(row = 2, column = 1, sticky = "e", padx = 1, pady = 1)

        # -------------------------------------- #
        #      Changelog                         #
        # -------------------------------------- #

        global txt_changelog

        # frame
        frm_changelog = ttk.LabelFrame(master = self, text = dataHandler.lang_frmChangelog, style = "Bold.TLabelframe")
        frm_changelog.grid(row = 1, column = 0, padx = 2, pady = 1, columnspan = 2)

        # spacer
        spc_changelog = tk.Label(master = frm_changelog, width = 46)
        spc_changelog.grid(row = 0, column = 0, columnspan = 2)

        # inputs
        txt_changelog = tk.Text(master = frm_changelog, width = 38, height = 10)

        # scrollbar
        scr_changelog = ttk.Scrollbar(master = frm_changelog)

        # inputs grid
        txt_changelog.grid(row = 0, column = 0, padx = 1, pady = 1)

        # scrollbar grid
        scr_changelog.grid(row = 0, column = 1, pady = 1, sticky = "ns")

        # scroll binding
        txt_changelog.configure(yscrollcommand = scr_changelog.set)

        scr_changelog.configure(command = txt_changelog.yview)

        # -------------------------------------- #
        #      Settings                          #
        # -------------------------------------- #

        # frame
        frm_updateSettings = ttk.LabelFrame(master = self, text = dataHandler.lang_frmUpdateSettings, style = "Bold.TLabelframe")
        frm_updateSettings.grid(row = 2, column = 0, padx = 2, pady = 1, columnspan = 2)

        # spacer
        spc_updateSettings = tk.Label(master = frm_updateSettings, width = 46)
        spc_updateSettings.grid(row = 0, column = 0)

        # inputs
        cbt_updateSettings_experimental = ttk.Checkbutton(master = frm_updateSettings, text = dataHandler.lang_updateSettings_experimental, variable = cbt_updateSettings_experimentalVar, command = self.cbt_updateSettings_experimental_callback)
        cbt_updateSettings_exportConfig = ttk.Checkbutton(master = frm_updateSettings, text = dataHandler.lang_updateSettings_exportConfig, variable = cbt_updateSettings_exportConfigVar)
        cbt_updateSettings_exportDatabase = ttk.Checkbutton(master = frm_updateSettings, text = dataHandler.lang_updateSettings_exportDatabase, variable = cbt_updateSettings_exportDatabaseVar)
        cbt_updateSettings_createShortcut = ttk.Checkbutton(master = frm_updateSettings, text = dataHandler.lang_updateSettings_shortcut, variable = cbt_updateSettings_createShortcutVar)

        # inputs grid
        cbt_updateSettings_experimental.grid(row = 0, column = 0, sticky = "w", padx = 1, pady = 1)
        cbt_updateSettings_exportConfig.grid(row = 1, column = 0, sticky = "w", padx = 1, pady = 1)
        cbt_updateSettings_exportDatabase.grid(row = 2, column = 0, sticky = "w", padx = 1, pady = 1)
        cbt_updateSettings_createShortcut.grid(row = 3, column = 0, sticky = "w", padx = 1, pady = 1)

        # -------------------------------------- #
        #      Buttons                           #
        # -------------------------------------- #

        global btn_startUpdate

        # buttons
        btn_startUpdate = ttk.Button(master = self, text = dataHandler.lang_button_updateStart, command = self.btn_startUpdate_callback, state = "disabled")
        btn_viewGithub = ttk.Button(master = self, text = dataHandler.lang_button_github, command = self.btn_viewGithub_callback)
        btn_closeUpdater = ttk.Button(master = self, text = dataHandler.lang_button_close, command = self.btn_closeUpdater_callback)

        # buttons grid
        btn_startUpdate.grid(row = 3, column = 0, columnspan = 2, sticky = "we", padx = 1, pady = 1)
        btn_viewGithub.grid(row = 4, column = 0, sticky = "we", padx = 1, pady = 1)
        btn_closeUpdater.grid(row = 4, column = 1, sticky = "we", padx = 1, pady = 1)

    def cbt_updateSettings_experimental_callback(self):

        self.setRelease()

    def btn_startUpdate_callback(self):

        if tkmsg.askyesno(title = dataHandler.titleVersion, message = dataHandler.lang_update_info) == False:

            return False

        runUpdateProcessInterface()

        root.update()

        dlPath = None

        if cbt_updateSettings_experimentalVar.get() == 1:

            if releaseExperimental != None:

                dlPath = updateHandler.downloadRelease(releaseExperimental)

        else:

            if releaseLatest != None:

                dlPath = updateHandler.downloadRelease(releaseLatest)

        if dlPath == None:

            return False

        else:

            if cbt_updateSettings_experimentalVar.get() == 1:

                newExePath = updateHandler.installRelease(dlPath, releaseExperimental)

                if newExePath != None:

                    startfile(newExePath)
                    root.destroy()

            else:

                newExePath = updateHandler.installRelease(dlPath, releaseLatest)

                if newExePath != None:

                    startfile(newExePath)
                    root.destroy()

    def btn_viewGithub_callback(self):

        webbrowser.open_new_tab(dataHandler.gitPath)

    def btn_closeUpdater_callback(self):

        self.saveSettings()
        closingUpdaterInterface()

    def loadSettings(self):

        dataHandler.readConfigINI()

        cbt_updateSettings_experimentalVar.set(dataHandler.updaterExperimentalBuilds)
        cbt_updateSettings_exportConfigVar.set(dataHandler.updaterExportConfig)
        cbt_updateSettings_exportDatabaseVar.set(dataHandler.updaterExportDatabase)
        cbt_updateSettings_createShortcutVar.set(dataHandler.updaterShortcut)

    def saveSettings(self):

        dataHandler.updaterExperimentalBuilds = cbt_updateSettings_experimentalVar.get()
        dataHandler.updaterExportConfig = cbt_updateSettings_exportConfigVar.get()
        dataHandler.updaterExportDatabase = cbt_updateSettings_exportDatabaseVar.get()

        dataHandler.writeConfigINI()

    def setRelease(self):

        releaseVersion = None
        prgVersion = int(str(dataHandler.version) + str(dataHandler.subversion) + str(dataHandler.subsubversion))

        if cbt_updateSettings_experimentalVar.get() == 1 and releaseExperimental != None:

            releaseVersionTag = str(releaseExperimental["tag_name"]).split(".")

            releaseVersion = int(releaseVersionTag[0] + releaseVersionTag[1] + releaseVersionTag[2])

        else:

            if releaseLatest != None:

                releaseVersionTag = str(releaseLatest["tag_name"]).split(".")

                releaseVersion = int(releaseVersionTag[0] + releaseVersionTag[1] + releaseVersionTag[2])

        if releaseVersion == None:

            lbl_updateInfo_state.configure(foreground = "red", text = dataHandler.lang_updateInfo_statusNone)
            btn_startUpdate.configure(state = "disabled")

        else:

            if releaseVersion > prgVersion:

                lbl_updateInfo_state.configure(foreground = "green", text = dataHandler.lang_updateInfo_statusTrue)
                btn_startUpdate.configure(state = "enabled")
                
            else:

                lbl_updateInfo_state.configure(foreground = "black", text = dataHandler.lang_updateInfo_statusFalse)
                btn_startUpdate.configure(state = "disabled")

        ety_updateInfo_versionUsedVar.set(dataHandler.completeVersion)

        ety_updateInfo_versionLatest.configure(foreground = "black")

        if cbt_updateSettings_experimentalVar.get() == 1 and releaseExperimental != None:

            ety_updateInfo_versionLatest.configure(foreground = "red")
            ety_updateInfo_versionLatestVar.set(releaseExperimental["tag_name"] + " (Exp.)")

        elif releaseLatest != None:

            ety_updateInfo_versionLatestVar.set(releaseLatest["tag_name"])

        else:

            ety_updateInfo_versionLatestVar.set("")
            return False

        filePath = None

        if cbt_updateSettings_experimentalVar.get() == 1 and releaseExperimental != None:

            filePath = updateHandler.getChangelog(releaseExperimental)

        else:

            filePath = updateHandler.getChangelog(releaseLatest)

        self.insertChangelog(filePath)

    def insertChangelog(self, filePath):

        txt_changelog.delete(0.0, tk.END)

        if filePath != None:

            with open(filePath, "r") as changelog:

                content = changelog.readlines()

                for line in content:

                    txt_changelog.insert("end", line)
        
        else:

            txt_changelog.insert("end", dataHandler.lang_changlog_false)

    def centerWindow(self):

        self.update()

        updaterWidth = self.winfo_reqwidth()
        updaterHeight = self.winfo_reqheight()

        rootWidth = root.winfo_reqwidth()
        rootHeight = root.winfo_reqheight()

        rootPosX = root.winfo_x()
        rootPosY = root.winfo_y()

        posX = floor(rootPosX + ((rootWidth / 2) - (updaterWidth / 2)))
        posY = floor(rootPosY + ((rootHeight / 2) - (updaterHeight / 2)))

        self.geometry("+{}+{}".format(posX, posY))

    def closeWindow(self):

        if ui_settings != None:

            ui_settings.grab_set()

        self.destroy()

class updateProcessInterface(tk.Toplevel):

    def __init__(self):

        tk.Toplevel.__init__(self)
        self.withdraw()
        self.overrideredirect(1)
        self.resizable(False, False)
        self.createWidgets()
        self.centerWindow()
        self.deiconify()
        self.attributes("-topmost", True)
        self.withdrawWindows()

    def createWidgets(self):

        col_updateProcess = tk.Frame(master = self, width = 450, height = 250)
        col_updateProcess.grid(row = 0, column = 0)

        frm_updateProcessMain = ttk.Frame(master = self)
        frm_updateProcessMain.grid(row = 0, column = 0)

        img_logo = Image.open(dataHandler.fPth_logo)
        img_logo = img_logo.resize((75, 75), Image.ANTIALIAS)
        self.ptk_logo = ImageTk.PhotoImage(img_logo)

        lbl_updateProcess_image = ttk.Label(master = frm_updateProcessMain, image = self.ptk_logo)
        lbl_updateProcess_image.grid(row = 0, column = 0, rowspan = 4, padx = (0, 10))

        lbl_updateProcess_title = ttk.Label(master = frm_updateProcessMain, text = dataHandler.title, style = "BoldUpdate.TLabel.Label")
        lbl_updateProcess_title.grid(row = 1, column = 1, sticky = "w")

        lbl_updateProcess_update = ttk.Label(master = frm_updateProcessMain, text = "updating...", style = "NormalUpdate.TLabel.Label")
        lbl_updateProcess_update.grid(row = 2, column = 1, sticky = "w")

    def centerWindow(self):

        self.update()

        uProcessWidth = self.winfo_reqwidth()
        uProcessHeight = self.winfo_reqheight()

        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()

        posX = floor((screenWidth / 2) - (uProcessWidth / 2))
        posY = floor((screenHeight / 2) - (uProcessHeight / 2))

        self.geometry("+{}+{}".format(posX, posY))

    def withdrawWindows(self):

        try:
            if "normal" == root.state():
                root.withdraw()
        except:
            pass

        try:
            if "normal" == ui_settings.state():
                ui_settings.withdraw()
        except:
            pass

        try:
            if "normal" == ui_updater.state():
                ui_updater.withdraw()
        except:
            pass

    def deiconfyWindows(self):

        try:
            root.deiconify()
        except:
            pass

        try:
            ui_settings.deiconify()
        except:
            pass

        try:
            ui_updater.deiconify()
        except:
            pass

    def closeWindow(self):

        self.deiconfyWindows()
        self.destroy()

def runSettingsInterface():

    global ui_settings

    if ui_settings == None:

        ui_settings = settingsInterface()
        ui_settings.protocol("WM_DELETE_WINDOW", closingSettingsInterface)

    return True

def runUpdaterInterface():

    global ui_updater

    if ui_updater == None:

        ui_updater = updaterInterface()
        ui_updater.protocol("WM_DELETE_WINDOW", closingUpdaterInterface)

def runUpdateProcessInterface():

    try:
        ui_updater.grab_release()

    except:
        pass

    global ui_updateProcess

    if ui_updateProcess == None:

        ui_updateProcess = updateProcessInterface()
        ui_updateProcess.protocol("WM_DELETE_WINDOW", closingUpdateProcessInterface)

def closingSettingsInterface():

    global ui_settings

    if ui_settings != None:

        ui_settings.closeWindow()

        ui_settings = None

def closingUpdaterInterface():

    global ui_updater

    if ui_updater != None:

        ui_updater.closeWindow()

        ui_updater = None

def closingUpdateProcessInterface():

    global ui_updateProcess

    if ui_updateProcess != None:

        ui_updateProcess.closeWindow()

        ui_updateProcess = None