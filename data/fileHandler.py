#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################
#                               #
#   ----      FILE      ----    #
#   ----    HANDLING    ----    #
#                               #
#################################

import os
from pdfrw import PdfReader, PdfWriter, PageMerge
from subprocess import Popen

from data import dataHandler, uiHandler

from reportlab.pdfgen.canvas import Canvas as PDFCanvas
from reportlab.pdfbase import pdfform as PDFForm
from reportlab.pdfbase import pdfmetrics as PDFMetrics
from reportlab.pdfbase.ttfonts import TTFont as PDFTTFont
from reportlab.lib import colors as PDFColors
from reportlab import rl_config, rl_settings

from datetime import date

from tkinter import END
from tkinter import messagebox as tkmsg
from textwrap import wrap

inputID = 0
inputType = "ERR"
inputPTO = "ERR"
inputColor = "ERR"
inputWidth = 0
inputHeight = 0
inputDepth = 0
inputLight = "ERR"
inputIndirectLight = 0
inputDoors = 0
inputShelfs = 0
inputOverlapUpper = 0
inputOverlapLower = 0

inputCor1Length = 0
inputCor1Width = 0
inputCor1Type = "ERR"
inputCor1Count = 0
inputCor2Length = 0
inputCor2Width = 0
inputCor2Type = "ERR"
inputCor2Count = 0
inputCor3Length = 0
inputCor3Width = 0
inputCor3Type = "ERR"
inputCor3Count = 0
inputCor4Length = 0
inputCor4Width = 0
inputCor4Type = "ERR"
inputCor4Count = 0
inputCor5Length = 0
inputCor5Width = 0
inputCor5Type = "ERR"
inputCor5Count = 0
inputCor6Length = 0
inputCor6Width = 0
inputCor6Type = "ERR"
inputCor6Count = 0
inputCor7Length = 0
inputCor7Width = 0
inputCor7Type = "ERR"
inputCor7Count = 0
inputCor8Length = 0
inputCor8Width = 0
inputCor8Type = "ERR"
inputCor8Count = 0

inputGlass1Length = 0
inputGlass1Width = 0
inputGlass1Type = "ERR"
inputGlass1Count = 0
inputGlass2Length = 0
inputGlass2Width = 0
inputGlass2Type = "ERR"
inputGlass2Count = 0
inputGlass3Length = 0
inputGlass3Width = 0
inputGlass3Type = "ERR"
inputGlass3Count = 0
inputGlass4Length = 0
inputGlass4Width = 0
inputGlass4Type = "ERR"
inputGlass4Count = 0
inputGlass5Length = 0
inputGlass5Width = 0
inputGlass5Type = "ERR"
inputGlass5Count = 0
inputGlass6Length = 0
inputGlass6Width = 0
inputGlass6Type = "ERR"
inputGlass6Count = 0
inputGlass7Length = 0
inputGlass7Width = 0
inputGlass7Type = "ERR"
inputGlass7Count = 0
inputGlass8Length = 0
inputGlass8Width = 0
inputGlass8Type = "ERR"
inputGlass8Count = 0

packingWidth = 0
packingHeight = 0
packingDepth = 0

def createPDF():

    getInputs()
    createOverlayForm()

    if merge_pdfs(dataHandler.fPth_formOrig, dataHandler.fPth_formOvrl, inputID) == True:

        if dataHandler.openPDF == True:

            try:

                os.startfile(dataHandler.fPth_output)
                
            except:

                pass

        if dataHandler.printPDF == True:

            try:

                os.startfile(dataHandler.fPth_output, "print")

            except:

                pass
    
    deleteFile(dataHandler.fPth_formOvrl)

    return True

def getInputs():

    global inputID
    global inputType
    global inputPTO
    global inputColor
    global inputWidth
    global inputHeight
    global inputDepth
    global inputLight
    global inputIndirectLight
    global inputDoors
    global inputShelfs
    global inputOverlapUpper
    global inputOverlapLower

    global inputCor1Length
    global inputCor1Width
    global inputCor1Type
    global inputCor1Count
    global inputCor2Length
    global inputCor2Width
    global inputCor2Type
    global inputCor2Count
    global inputCor3Length
    global inputCor3Width
    global inputCor3Type
    global inputCor3Count
    global inputCor4Length
    global inputCor4Width
    global inputCor4Type
    global inputCor4Count
    global inputCor5Length
    global inputCor5Width
    global inputCor5Type
    global inputCor5Count
    global inputCor6Length
    global inputCor6Width
    global inputCor6Type
    global inputCor6Count
    global inputCor7Length
    global inputCor7Width
    global inputCor7Type
    global inputCor7Count
    global inputCor8Length
    global inputCor8Width
    global inputCor8Type
    global inputCor8Count

    global inputGlass1Length
    global inputGlass1Width
    global inputGlass1Type
    global inputGlass1Count
    global inputGlass2Length
    global inputGlass2Width
    global inputGlass2Type
    global inputGlass2Count
    global inputGlass3Length
    global inputGlass3Width
    global inputGlass3Type
    global inputGlass3Count
    global inputGlass4Length
    global inputGlass4Width
    global inputGlass4Type
    global inputGlass4Count
    global inputGlass5Length
    global inputGlass5Width
    global inputGlass5Type
    global inputGlass5Count
    global inputGlass6Length
    global inputGlass6Width
    global inputGlass6Type
    global inputGlass6Count
    global inputGlass7Length
    global inputGlass7Width
    global inputGlass7Type
    global inputGlass7Count
    global inputGlass8Length
    global inputGlass8Width
    global inputGlass8Type
    global inputGlass8Count

    global packingWidth
    global packingHeight
    global packingDepth

    # ID
    inputID = uiHandler.ety_genInfo_orderIDVar.get()

    # Type
    inputType = uiHandler.cbb_genInfo_type.get()
    
    # Push-To-Open
    if uiHandler.cbt_genInfo_ptoVar.get() == 1:

        inputPTO = dataHandler.lang_general_yes

    else:

        inputPTO = dataHandler.lang_general_no

    # Color
    inputColor = uiHandler.ety_color_selectedVar.get()

    # Width
    inputWidth = uiHandler.ety_measure_widthVar.get()
    
    # Height
    inputHeight = uiHandler.ety_measure_heightVar.get()

    # Depth
    inputDepth = uiHandler.ety_measure_depthVar.get()

    # Light
    if uiHandler.cbb_corInfo_light.current() == 0:

        inputLight = dataHandler.lang_general_without

    else:

        inputLight = uiHandler.cbb_corInfo_light.get()

    # Indirect Light
    if uiHandler.cbt_corInfo_indLightVar.get() == 1:
        
        inputIndirectLight = dataHandler.lang_general_with

    else:

        inputIndirectLight = dataHandler.lang_general_without

    # Doors
    inputDoors = uiHandler.ety_corInfo_doorVar.get()

    # Shelfs
    inputShelfs = uiHandler.ety_corInfo_shelfVar.get()

    # Overlap Upper
    inputOverlapUpper = uiHandler.ety_corInfo_overhangUpperVar.get()

    # Overlap Lower
    inputOverlapLower = uiHandler.ety_corInfo_overhangLowerVar.get()

    inputCor1Length = uiHandler.ety_corpusMeasure_pos1lengthVar.get()
    inputCor2Length = uiHandler.ety_corpusMeasure_pos2lengthVar.get()
    inputCor3Length = uiHandler.ety_corpusMeasure_pos3lengthVar.get()
    inputCor4Length = uiHandler.ety_corpusMeasure_pos4lengthVar.get()
    inputCor5Length = uiHandler.ety_corpusMeasure_pos5lengthVar.get()
    inputCor6Length = uiHandler.ety_corpusMeasure_pos6lengthVar.get()
    inputCor7Length = uiHandler.ety_corpusMeasure_pos7lengthVar.get()
    inputCor8Length = uiHandler.ety_corpusMeasure_pos8lengthVar.get()

    inputCor1Width = uiHandler.ety_corpusMeasure_pos1widthVar.get()
    inputCor2Width = uiHandler.ety_corpusMeasure_pos2widthVar.get()
    inputCor3Width = uiHandler.ety_corpusMeasure_pos3widthVar.get()
    inputCor4Width = uiHandler.ety_corpusMeasure_pos4widthVar.get()
    inputCor5Width = uiHandler.ety_corpusMeasure_pos5widthVar.get()
    inputCor6Width = uiHandler.ety_corpusMeasure_pos6widthVar.get()
    inputCor7Width = uiHandler.ety_corpusMeasure_pos7widthVar.get()
    inputCor8Width = uiHandler.ety_corpusMeasure_pos8widthVar.get()

    inputCor1Type = getCuttingsTypeCorpus(uiHandler.cbb_corpusMeasure_pos1type)
    inputCor2Type = getCuttingsTypeCorpus(uiHandler.cbb_corpusMeasure_pos2type)
    inputCor3Type = getCuttingsTypeCorpus(uiHandler.cbb_corpusMeasure_pos3type)
    inputCor4Type = getCuttingsTypeCorpus(uiHandler.cbb_corpusMeasure_pos4type)
    inputCor5Type = getCuttingsTypeCorpus(uiHandler.cbb_corpusMeasure_pos5type)
    inputCor6Type = getCuttingsTypeCorpus(uiHandler.cbb_corpusMeasure_pos6type)
    inputCor7Type = getCuttingsTypeCorpus(uiHandler.cbb_corpusMeasure_pos7type)
    inputCor8Type = getCuttingsTypeCorpus(uiHandler.cbb_corpusMeasure_pos8type)

    inputCor1Count = uiHandler.ety_corpusMeasure_pos1countVar.get()
    inputCor2Count = uiHandler.ety_corpusMeasure_pos2countVar.get()
    inputCor3Count = uiHandler.ety_corpusMeasure_pos3countVar.get()
    inputCor4Count = uiHandler.ety_corpusMeasure_pos4countVar.get()
    inputCor5Count = uiHandler.ety_corpusMeasure_pos5countVar.get()
    inputCor6Count = uiHandler.ety_corpusMeasure_pos6countVar.get()
    inputCor7Count = uiHandler.ety_corpusMeasure_pos7countVar.get()
    inputCor8Count = uiHandler.ety_corpusMeasure_pos8countVar.get()

    inputGlass1Length = uiHandler.ety_glassMeasure_pos1lengthVar.get()
    inputGlass2Length = uiHandler.ety_glassMeasure_pos2lengthVar.get()
    inputGlass3Length = uiHandler.ety_glassMeasure_pos3lengthVar.get()
    inputGlass4Length = uiHandler.ety_glassMeasure_pos4lengthVar.get()
    inputGlass5Length = uiHandler.ety_glassMeasure_pos5lengthVar.get()
    inputGlass6Length = uiHandler.ety_glassMeasure_pos6lengthVar.get()
    inputGlass7Length = uiHandler.ety_glassMeasure_pos7lengthVar.get()
    inputGlass8Length = uiHandler.ety_glassMeasure_pos8lengthVar.get()

    inputGlass1Width = uiHandler.ety_glassMeasure_pos1widthVar.get()
    inputGlass2Width = uiHandler.ety_glassMeasure_pos2widthVar.get()
    inputGlass3Width = uiHandler.ety_glassMeasure_pos3widthVar.get()
    inputGlass4Width = uiHandler.ety_glassMeasure_pos4widthVar.get()
    inputGlass5Width = uiHandler.ety_glassMeasure_pos5widthVar.get()
    inputGlass6Width = uiHandler.ety_glassMeasure_pos6widthVar.get()
    inputGlass7Width = uiHandler.ety_glassMeasure_pos7widthVar.get()
    inputGlass8Width = uiHandler.ety_glassMeasure_pos8widthVar.get()

    inputGlass1Type = getCuttingsTypeGlass(uiHandler.cbb_glassMeasure_pos1type)
    inputGlass2Type = getCuttingsTypeGlass(uiHandler.cbb_glassMeasure_pos2type)
    inputGlass3Type = getCuttingsTypeGlass(uiHandler.cbb_glassMeasure_pos3type)
    inputGlass4Type = getCuttingsTypeGlass(uiHandler.cbb_glassMeasure_pos4type)
    inputGlass5Type = getCuttingsTypeGlass(uiHandler.cbb_glassMeasure_pos5type)
    inputGlass6Type = getCuttingsTypeGlass(uiHandler.cbb_glassMeasure_pos6type)
    inputGlass7Type = getCuttingsTypeGlass(uiHandler.cbb_glassMeasure_pos7type)
    inputGlass8Type = getCuttingsTypeGlass(uiHandler.cbb_glassMeasure_pos8type)

    inputGlass1Count = uiHandler.ety_glassMeasure_pos1countVar.get()
    inputGlass2Count = uiHandler.ety_glassMeasure_pos2countVar.get()
    inputGlass3Count = uiHandler.ety_glassMeasure_pos3countVar.get()
    inputGlass4Count = uiHandler.ety_glassMeasure_pos4countVar.get()
    inputGlass5Count = uiHandler.ety_glassMeasure_pos5countVar.get()
    inputGlass6Count = uiHandler.ety_glassMeasure_pos6countVar.get()
    inputGlass7Count = uiHandler.ety_glassMeasure_pos7countVar.get()
    inputGlass8Count = uiHandler.ety_glassMeasure_pos8countVar.get()

    # Packaging
    packingWidth = uiHandler.ety_packaging_widthVar.get()
    packingHeight = uiHandler.ety_packaging_heightVar.get()
    packingDepth = uiHandler.ety_packaging_depthVar.get()
    
def getCuttingsTypeCorpus(combobox):

    output = "ERR"

    if combobox.current() == 0:

        output = ""

    elif combobox.current() == 1:

        output = dataHandler.lang_data_corpusMeasure_type_ground_short

    elif combobox.current() == 2:

        output = dataHandler.lang_data_corpusMeasure_type_side_short

    elif combobox.current() == 3:

        output = dataHandler.lang_data_corpusMeasure_type_middleground_short

    elif combobox.current() == 4:

        output = dataHandler.lang_data_corpusMeasure_type_middleside_short

    elif combobox.current() == 5:

        output = dataHandler.lang_data_corpusMeasure_type_MF_ground_short

    elif combobox.current() == 6:

        output = dataHandler.lang_data_corpusMeasure_type_MF_side_short

    elif combobox.current() == 7:

        output = dataHandler.lang_data_corpusMeasure_type_backwall_short

    return output

def getCuttingsTypeGlass(combobox):

    output = "ERR"

    if combobox.current() == 0:

        output = ""

    else:

        output = combobox.get()

    return output

def createOverlayForm():

    registerFont()

    pdfFileCanvas = PDFCanvas("form_overlay.pdf")
    
    pdfFileForm = pdfFileCanvas.acroForm
    
    # ID
    addStringToCanvas(38, 123, 776, inputID, dataHandler.fnt_Bold, 18, pdfFileCanvas)

    # Date
    addStringToCanvas(126, 215, 777, date.today().strftime("%d.%m.%Y"), dataHandler.fnt_Normal, 14, pdfFileCanvas)
    
    # Type
    addStringToCanvas(218, 250, 777, inputType, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # PushToOpen
    addStringToCanvas(253, 343, 777, inputPTO, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # Color
    addStringToCanvas(345, 557, 777, inputColor, dataHandler.fnt_Normal, 11, pdfFileCanvas)

    # Width
    addStringToCanvas(377, 473, 730, inputWidth, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # Height
    addStringToCanvas(377, 473, 690, inputHeight, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # Depth
    addStringToCanvas(377, 473, 649, inputDepth, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # Light
    addStringToCanvas(377, 473, 610, inputLight, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # Indirect Light
    addStringToCanvas(377, 473, 569, inputIndirectLight, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # Doors
    addStringToCanvas(377, 424, 530, inputDoors, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # Shelfs
    addStringToCanvas(426, 473, 530, inputShelfs, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # OverlapUpper
    addStringToCanvas(493, 540, 671, inputOverlapUpper, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # OverlapLower
    addStringToCanvas(493, 540, 586, inputOverlapLower, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # --------------------------------------------------------------------------------

    # cor1
    addStringToCanvas(58, 155, 471, inputCor1Length, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(166, 262, 471, inputCor1Width, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(266, 291, 472, inputCor1Type, dataHandler.fnt_Normal, 10, pdfFileCanvas)
    addStringToCanvas(294, 320, 471, inputCor1Count, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # cor2
    addStringToCanvas(58, 155, 450, inputCor2Length, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(166, 262, 450, inputCor2Width, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(266, 291, 451, inputCor2Type, dataHandler.fnt_Normal, 10, pdfFileCanvas)
    addStringToCanvas(294, 320, 450, inputCor2Count, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # cor3
    addStringToCanvas(58, 155, 428, inputCor3Length, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(166, 262, 428, inputCor3Width, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(266, 291, 429, inputCor3Type, dataHandler.fnt_Normal, 10, pdfFileCanvas)
    addStringToCanvas(294, 320, 428, inputCor3Count, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # cor4
    addStringToCanvas(58, 155, 407, inputCor4Length, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(166, 262, 407, inputCor4Width, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(266, 291, 408, inputCor4Type, dataHandler.fnt_Normal, 10, pdfFileCanvas)
    addStringToCanvas(294, 320, 407, inputCor4Count, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # cor5
    addStringToCanvas(58, 155, 385, inputCor5Length, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(166, 262, 385, inputCor5Width, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(266, 291, 386, inputCor5Type, dataHandler.fnt_Normal, 10, pdfFileCanvas)
    addStringToCanvas(294, 320, 385, inputCor5Count, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # cor6
    addStringToCanvas(58, 155, 364, inputCor6Length, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(166, 262, 364, inputCor6Width, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(266, 291, 365, inputCor6Type, dataHandler.fnt_Normal, 10, pdfFileCanvas)
    addStringToCanvas(294, 320, 364, inputCor6Count, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # cor7
    addStringToCanvas(58, 155, 343, inputCor7Length, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(166, 262, 343, inputCor7Width, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(266, 291, 344, inputCor7Type, dataHandler.fnt_Normal, 10, pdfFileCanvas)
    addStringToCanvas(294, 320, 343, inputCor7Count, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # cor8
    addStringToCanvas(58, 155, 322, inputCor8Length, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(166, 262, 322, inputCor8Width, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(266, 291, 323, inputCor8Type, dataHandler.fnt_Normal, 10, pdfFileCanvas)
    addStringToCanvas(294, 320, 322, inputCor8Count, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # -------------------------------------------------------------------------

    # glass1
    addStringToCanvas(58, 155, 260, inputGlass1Length, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(166, 262, 260, inputGlass1Width, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(266, 291, 260, inputGlass1Count, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(294, 375, 260, inputGlass1Type, dataHandler.fnt_Normal, 12, pdfFileCanvas)

    # glass2
    addStringToCanvas(58, 155, 238, inputGlass2Length, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(166, 262, 238, inputGlass2Width, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(266, 291, 238, inputGlass2Count, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(294, 375, 238, inputGlass2Type, dataHandler.fnt_Normal, 12, pdfFileCanvas)

    # glass3
    addStringToCanvas(58, 155, 217, inputGlass3Length, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(166, 262, 217, inputGlass3Width, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(266, 291, 217, inputGlass3Count, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(294, 375, 217, inputGlass3Type, dataHandler.fnt_Normal, 12, pdfFileCanvas)

    # glass4
    addStringToCanvas(58, 155, 196, inputGlass4Length, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(166, 262, 196, inputGlass4Width, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(266, 291, 196, inputGlass4Count, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(294, 375, 196, inputGlass4Type, dataHandler.fnt_Normal, 12, pdfFileCanvas)

    # glass5
    addStringToCanvas(58, 155, 174, inputGlass5Length, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(166, 262, 174, inputGlass5Width, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(266, 291, 174, inputGlass5Count, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(294, 375, 174, inputGlass5Type, dataHandler.fnt_Normal, 12, pdfFileCanvas)

    # glass6
    addStringToCanvas(58, 155, 152, inputGlass6Length, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(166, 262, 152, inputGlass6Width, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(266, 291, 152, inputGlass6Count, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(294, 375, 152, inputGlass6Type, dataHandler.fnt_Normal, 12, pdfFileCanvas)

    # glass7
    addStringToCanvas(58, 155, 131, inputGlass7Length, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(166, 262, 131, inputGlass7Width, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(266, 291, 131, inputGlass7Count, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(294, 375, 131, inputGlass7Type, dataHandler.fnt_Normal, 12, pdfFileCanvas)

    # glass8
    addStringToCanvas(58, 155, 110, inputGlass8Length, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(166, 262, 110, inputGlass8Width, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(266, 291, 110, inputGlass8Count, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(294, 375, 110, inputGlass8Type, dataHandler.fnt_Normal, 12, pdfFileCanvas)

    # --------------------------------------------------------------------------------

    # packaging
    addStringToCanvas(386, 440, 112, packingWidth, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(444, 499, 112, packingHeight, dataHandler.fnt_Normal, 14, pdfFileCanvas)
    addStringToCanvas(502, 557, 112, packingDepth, dataHandler.fnt_Normal, 14, pdfFileCanvas)

    # --------------------------------------------------------------------------------

    textboxContent = uiHandler.txt_infoBox.get("1.0", END)[:(len(uiHandler.txt_infoBox.get("1.0", END)) - 1)]

    addTextFieldToCanvas(388, 490, textboxContent, dataHandler.fnt_Normal, 12, pdfFileCanvas, 22)

    pdfFileCanvas.save()

def addTextFieldToCanvas(lim_left, startHeight, content, font, font_size, canvas, maxChar):

    canvas.setFont(font, font_size)

    height = startHeight

    splitLines = content.split("\n")
    newLine = []
    wrapLines = []

    for line in splitLines:

        newLine.clear()

        if len(line) > maxChar:

            newLine = wrap(line, maxChar)

        else:

            newLine.append(line)

        for i in newLine:

            wrapLines.append(i)

    for line in wrapLines:

        canvas.drawString(lim_left, height, line)

        height -= (font_size + 2)

def addStringToCanvas(lim_left, lim_right, height, content, font, font_size, canvas):

    canvas.setFont(font, font_size)                                             # set font
    textWidth = PDFMetrics.stringWidth(content, font, font_size)                # get string width
    x = lim_right - ((lim_right - lim_left) / 2) - (textWidth / 2)              # get string positioned in the middle of the input field
    canvas.drawString(x, height, content)                                       # draw string

def deleteFile(fileDir):

    try:
        os.remove(fileDir)
    
    except:
        pass

def runFile(fileDir):

    if dataHandler.openPDF == True:

        if dataHandler.printPDF == True:

            os.startfile(fileDir, "print")

        else:

            os.startfile(fileDir)

def readFile(fileDir):

    # read File
    txtFile = open(fileDir, "r")
    content = txtFile.readlines()
    txtFile.close()

    # remove new line marks
    i = 0
    newcontent = []

    while i < len(content):

        newcontent.append(content[i].replace("\n", ""))

        i += 1

    return newcontent

def merge_pdfs(form_pdf, overlay_pdf, outputName):

    if outputName == "":

        outputName = "unidentified"

    outputFolder = os.path.join(os.curdir, "output")

    if os.path.isdir(outputFolder) == False:

        os.mkdir(outputFolder)

    if dataHandler.saveDir == "":

        dataHandler.fPth_output = os.path.join(outputFolder, (outputName + ".pdf"))

    else:

        dataHandler.fPth_output = os.path.join(dataHandler.saveDir, (outputName + ".pdf"))

    file_orig = PdfReader(form_pdf)
    file_ovrl = PdfReader(overlay_pdf)

    PageMerge(file_orig.pages[0]).add(file_ovrl.pages[0]).render()

    try:

        if os.path.isfile(dataHandler.fPth_output) == True:

            if tkmsg.askyesno(title = dataHandler.titleVersion, message = dataHandler.lang_msg_pdfoverride) == True:

                deleteFile(dataHandler.fPth_output)

            else:

                return False

        PdfWriter().write(dataHandler.fPth_output, file_orig)

        return True

    except:

        tkmsg.showerror(title = dataHandler.titleVersion, message = "Could not create PDF File! Please check if a PDF File with the assigned ID is already open and try again!")

        return False

def registerFont():

    PDFMetrics.registerFont(PDFTTFont(dataHandler.fnt_Normal, dataHandler.fnt_NormalTTF))
    PDFMetrics.registerFont(PDFTTFont(dataHandler.fnt_Bold, dataHandler.fnt_BoldTTF))