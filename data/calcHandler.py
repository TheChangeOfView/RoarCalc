#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################
#                               #
#   ----      CALC      ----    #
#   ----    HANDLING    ----    #
#                               #
#################################

from data import uiHandler, dataHandler

from tkinter import messagebox as tkmsg

def calculateCuttings(corMainWidth: int, corMainHeight: int, corMainDepth: int):

    aluminiumFrame = False
    LED = "none"
    mountingFrame = False
    extraWalls = 0
    extraShelfs = 0

    if uiHandler.lastSelectedListbox == 3:

        aluminiumFrame = True

    if uiHandler.cbb_genInfo_specials.current() == 1:

        LED = "frontal"

    elif uiHandler.cbb_genInfo_specials.current() == 2:

        LED = "internal"

    if uiHandler.cbb_genInfo_type.current() == 2:

        mountingFrame = True    

    if uiHandler.cbb_extra_type.current() == 1: # One extra middle wall

        extraWalls += 1

    elif uiHandler.cbb_extra_type.current() == 2: # Two extra middle walls

        extraWalls += 2

    elif uiHandler.cbb_extra_type.current() == 3: # One extra shelf

        extraShelfs += 1

    if uiHandler.cbt_corpusMeasure_overrideVar.get() != 1:

        if calculateCuttingsCorpus(corMainWidth, corMainHeight, corMainDepth, aluminiumFrame, LED, mountingFrame, extraWalls, extraShelfs) == False:

            return False

    if uiHandler.cbt_glassMeasure_overrideVar.get() != 1:

        if calculateCuttingsGlass(corMainWidth, corMainHeight, corMainDepth, aluminiumFrame, extraWalls, extraShelfs, LED) == False:

            return False

    if uiHandler.cbt_packaging_overrideVar.get() != 1:

        if calculateCuttingsPackaging(corMainWidth, corMainHeight, corMainDepth) == False:

            return False

    return True

def calculateCuttingsCorpus(corMainWidth: int, corMainHeight: int, corMainDepth: int, aluminiumFrame: bool, LED: str, mountingFrame: bool, extraWalls: int, extraShelfs: int):

    #-- MOUNTING FRAME ---------------------------------------------------------------------

    if mountingFrame == True:

        mountingFrameGroud = corMainWidth + 40
        mountingFrameSide = corMainHeight + 40
        mountingFrameDepth = corMainDepth - 50

        setMeasureUI(5, mountingFrameGroud, mountingFrameDepth, 5, 2)
        setMeasureUI(6, mountingFrameSide, mountingFrameDepth, 6, 2)

    #-- BACK WALL ---------------------------------------------------------------------

    backLength = corMainWidth - 24
    backWidth = corMainHeight - 24

    setMeasureUI(8, backLength, backWidth, 7, 1, sortMeasures = False)

    #-- MAIN CORPUS ---------------------------------------------------------------------

    corGroundWidth = corMainDepth
    corSideWidth = corMainDepth

    if aluminiumFrame == False and LED == "frontal":

        corGroundWidth -= dataHandler.dict_config["ledthicknessfrontal"]
        corSideWidth -= dataHandler.dict_config["ledthicknessfrontal"]

    setMeasureUI(1, corMainWidth, corGroundWidth, 1, 2)
    setMeasureUI(2, corMainHeight, corSideWidth, 2, 2)

    #-- MIDDLE WALL AND SHELF ---------------------------------------------------------------------

    try:
        if extraShelfs != 0:
            extraMeasure = int(uiHandler.ety_extra_measureVar.get())
        else:
            extraMeasure = 0

        doorAmount = int(uiHandler.ety_corInfo_doorVar.get())

    except:

        showCalcError(1)
        return False

    matThickness = dataHandler.dict_config["woodenthickness"]

    if aluminiumFrame == True:

        matThickness = dataHandler.dict_config["aluminumthickness"]

    if doorAmount == 4:

        middleSideCount = 1

    elif doorAmount == 3 and corMainWidth < 1200:

        middleSideCount = 1

    elif doorAmount == 2 and corMainWidth < 800:

        middleSideCount = 0

    else:

        middleSideCount = doorAmount - 1 + extraWalls

    middleSideLength = corMainHeight

    shelfLength = 0

    middleWidth = corMainDepth - 28

    middleSideLength -= matThickness * 2

    if extraShelfs != 0:

        middleSideLength -= matThickness * extraShelfs

        if uiHandler.ety_extra_measureVar.get() != "":

            middleSideLength -= extraMeasure * extraShelfs

        shelfLength = corMainWidth - (matThickness * 2)

    if middleSideCount > 0:

        setMeasureUI(3, middleSideLength, middleWidth, 4, middleSideCount)

    if extraShelfs != 0:

        setMeasureUI(4, shelfLength, middleWidth, 3, extraShelfs)

        if doorAmount >= 2:

            setMeasureUI(7, extraMeasure, middleWidth, 4, 1)

    return True

def calculateCuttingsGlass(corMainWidth: int, corMainHeight: int, corMainDepth: int, aluminiumFrame: bool, extraWalls: int, extraShelfs: int, LED: str):

    #-- MIRRORS ---------------------------------------------------------------------

    try:

        if  extraShelfs == 0 and extraWalls == 0:
            extraMeasure = 0
            overhangUpper = int(uiHandler.ety_corInfo_overhangUpperVar.get())
            overhangLower = int(uiHandler.ety_corInfo_overhangLowerVar.get())
        else:
            extraMeasure = int(uiHandler.ety_extra_measureVar.get())
            overhangUpper = 0
            overhangLower = 0

        doorAmount = int(uiHandler.ety_corInfo_doorVar.get())
        shelfAmount = int(uiHandler.ety_corInfo_shelfVar.get())

    except:

        showCalcError(2)
        return False

    if aluminiumFrame == False:
   
        matThickness = dataHandler.dict_config["woodenthickness"]
        matSubtraction = dataHandler.dict_config["woodensubtraction"]

    else:

        matThickness = dataHandler.dict_config["aluminumthickness"]
        matSubtraction = dataHandler.dict_config["aluminumsubtraction"]

    mainMirrorCount = doorAmount * 2
    mainMirrorLength = corMainHeight
    mainMirrorWidth = 0
    if doorAmount > 0:
        mainMirrorWidth = round(corMainWidth / doorAmount) - 1

    coveringMirrorCount = 0
    coveringMirrorLength = 0
    coveringMirrorWidth = 0

    if extraShelfs != 0:

        mainMirrorLength -= extraMeasure * extraShelfs

        if uiHandler.cbt_extra_coveredVar.get() == True:

            coveringMirrorCount = extraShelfs * 2

            mainMirrorLength -= (round(matThickness / 2) + 1) * extraShelfs

            coveringMirrorWidth = corMainWidth

            coveringMirrorLength = extraMeasure + (round(matThickness / 2) - 1)

    else:

        mainMirrorLength += (overhangUpper + overhangLower)

    if extraWalls != 0:

        widthSubstraction = extraMeasure * extraWalls

        if uiHandler.cbt_extra_coveredVar.get() == True:
            
            coveringMirrorCount = extraWalls * 2

            widthSubstraction += (round(matThickness / 2) + 1) * extraWalls

            coveringMirrorWidth = extraMeasure + (round(matThickness / 2) - 1)
            coveringMirrorLength = corMainHeight

        mainMirrorWidth = round((corMainWidth - int(widthSubstraction)) / doorAmount) - 1

    if mainMirrorCount > 0:

        setMeasureUI(1, mainMirrorLength, mainMirrorWidth, 1, mainMirrorCount, True)

    if coveringMirrorCount != 0:

        setMeasureUI(2, coveringMirrorLength, coveringMirrorWidth, 1, coveringMirrorCount, True)

    #-- GLASSES ---------------------------------------------------------------------

    if shelfAmount != 0:

        glassesWidth = corMainDepth - 31

        if LED == "internal":

            glassesWidth -= 9

        if doorAmount == 4:

            glassesLength = corMainWidth
            glassesLength -= (extraMeasure + matThickness) * extraWalls
            glassesLength -= matThickness * 3
            glassesLength /= 2
            glassesLength -= matSubtraction
            glassesLength = round(glassesLength)

            glassesCount = shelfAmount * 2

            setMeasureUI(3, glassesLength, glassesWidth, 3, glassesCount, True)

        elif doorAmount == 3 and corMainWidth < 1200:

            generalLength = corMainWidth
            generalLength -= (extraMeasure + matThickness) * extraWalls

            glassLength1 = (generalLength / 3) * 2
            glassLength1 -= matThickness * 1.5
            glassLength1 -= matSubtraction
            glassLength1 = round(glassLength1)

            glassLength2 = (generalLength / 3)
            glassLength2 -= matThickness * 1.5
            glassLength2 -= matSubtraction
            glassLength2 = round(glassLength2)

            glassesCount = shelfAmount
            
            setMeasureUI(3, glassLength1, glassesWidth, 3, glassesCount, True)
            setMeasureUI(4, glassLength2, glassesWidth, 3, glassesCount, True)

        elif doorAmount == 3 and corMainWidth >= 1200:

            generalLength = corMainWidth
            generalLength -= (extraMeasure + matThickness) * extraWalls

            glassLengthOuter = generalLength / 3
            glassLengthOuter -= matThickness * 1.5
            glassLengthOuter -= matSubtraction
            glassLengthOuter = round(glassLengthOuter)

            glassLengthInner = generalLength / 3
            glassLengthInner -= matThickness
            glassLengthInner -= matSubtraction
            glassLengthInner = round(glassLengthInner)

            glassCountOuter = shelfAmount * 2
            glassCountInner = shelfAmount
            
            setMeasureUI(3, glassLengthOuter, glassesWidth, 3, glassCountOuter, True)
            setMeasureUI(4, glassLengthInner, glassesWidth, 3, glassCountInner, True)

        elif (doorAmount == 2 and corMainWidth < 800) or doorAmount == 1:

            glassesLength = corMainWidth
            glassesLength -= (extraMeasure + matThickness) * extraWalls
            glassesLength -= matThickness * 2
            glassesLength -= matSubtraction
            glassesLength = round(glassesLength)

            glassesCount = shelfAmount

            setMeasureUI(3, glassesLength, glassesWidth, 3, glassesCount, True)

        else:

            glassesLength = corMainWidth
            glassesLength -= (extraMeasure + matThickness) * extraWalls
            glassesLength -= matThickness * 2                               # Subtract the outer Walls
            glassesLength -= matThickness * (doorAmount - 1)                # Subtract middle Walls
            glassesLength /= 2
            glassesLength -= matSubtraction
            glassesLength = round(glassesLength)
            
            glassesCount = shelfAmount * doorAmount
            
            setMeasureUI(3, glassesLength, glassesWidth, 3, glassesCount, True)

    return True

def calculateCuttingsPackaging(corMainWidth: int, corMainHeight: int, corMainDepth: int):

    packWidth = corMainWidth + (dataHandler.dict_config["packingmatthickness"] * 2)
    packHeight = corMainHeight + (dataHandler.dict_config["packingmatthickness"] * 2)
    packDepth = corMainDepth + (dataHandler.dict_config["packingmatthickness"] * 2)

    uiHandler.ety_packaging_widthVar.set(packWidth)
    uiHandler.ety_packaging_heightVar.set(packHeight)
    uiHandler.ety_packaging_depthVar.set(packDepth)

    return True

def setMeasureUI(pos: int, length: int, width: int, index: int, count: int, isGlass = False, sortMeasures = True):

    if pos < 1 or pos > 8:

        showCalcError(100)
        return False

    if isGlass == False and (index > (len(uiHandler.cbb_corpusMeasure_pos1type["values"]) - 1) or index < 0):
        
        showCalcError(101)
        return False

    if length < width and sortMeasures == True:

        lengthOld = length
        widthOld = width

        length = widthOld
        width = lengthOld

    if isGlass == False:

        if pos == 1:
            uiHandler.ety_corpusMeasure_pos1lengthVar.set(length)
            uiHandler.ety_corpusMeasure_pos1widthVar.set(width)
            uiHandler.cbb_corpusMeasure_pos1type.current(newindex = index)
            uiHandler.ety_corpusMeasure_pos1countVar.set(count)

        elif pos == 2:
            uiHandler.ety_corpusMeasure_pos2lengthVar.set(length)
            uiHandler.ety_corpusMeasure_pos2widthVar.set(width)
            uiHandler.cbb_corpusMeasure_pos2type.current(newindex = index)
            uiHandler.ety_corpusMeasure_pos2countVar.set(count)

        elif pos == 3:
            uiHandler.ety_corpusMeasure_pos3lengthVar.set(length)
            uiHandler.ety_corpusMeasure_pos3widthVar.set(width)
            uiHandler.cbb_corpusMeasure_pos3type.current(newindex = index)
            uiHandler.ety_corpusMeasure_pos3countVar.set(count)

        elif pos == 4:
            uiHandler.ety_corpusMeasure_pos4lengthVar.set(length)
            uiHandler.ety_corpusMeasure_pos4widthVar.set(width)
            uiHandler.cbb_corpusMeasure_pos4type.current(newindex = index)
            uiHandler.ety_corpusMeasure_pos4countVar.set(count)

        elif pos == 5:
            uiHandler.ety_corpusMeasure_pos5lengthVar.set(length)
            uiHandler.ety_corpusMeasure_pos5widthVar.set(width)
            uiHandler.cbb_corpusMeasure_pos5type.current(newindex = index)
            uiHandler.ety_corpusMeasure_pos5countVar.set(count)

        elif pos == 6:
            uiHandler.ety_corpusMeasure_pos6lengthVar.set(length)
            uiHandler.ety_corpusMeasure_pos6widthVar.set(width)
            uiHandler.cbb_corpusMeasure_pos6type.current(newindex = index)
            uiHandler.ety_corpusMeasure_pos6countVar.set(count)

        elif pos == 7:
            uiHandler.ety_corpusMeasure_pos7lengthVar.set(length)
            uiHandler.ety_corpusMeasure_pos7widthVar.set(width)
            uiHandler.cbb_corpusMeasure_pos7type.current(newindex = index)
            uiHandler.ety_corpusMeasure_pos7countVar.set(count)

        elif pos == 8:
            uiHandler.ety_corpusMeasure_pos8lengthVar.set(length)
            uiHandler.ety_corpusMeasure_pos8widthVar.set(width)
            uiHandler.cbb_corpusMeasure_pos8type.current(newindex = index)
            uiHandler.ety_corpusMeasure_pos8countVar.set(count)

    else:

        if pos == 1:
            uiHandler.ety_glassMeasure_pos1lengthVar.set(length)
            uiHandler.ety_glassMeasure_pos1widthVar.set(width)
            uiHandler.cbb_glassMeasure_pos1type.current(newindex = index)
            uiHandler.ety_glassMeasure_pos1countVar.set(count)

        elif pos == 2:
            uiHandler.ety_glassMeasure_pos2lengthVar.set(length)
            uiHandler.ety_glassMeasure_pos2widthVar.set(width)
            uiHandler.cbb_glassMeasure_pos2type.current(newindex = index)
            uiHandler.ety_glassMeasure_pos2countVar.set(count)

        elif pos == 3:
            uiHandler.ety_glassMeasure_pos3lengthVar.set(length)
            uiHandler.ety_glassMeasure_pos3widthVar.set(width)
            uiHandler.cbb_glassMeasure_pos3type.current(newindex = index)
            uiHandler.ety_glassMeasure_pos3countVar.set(count)

        elif pos == 4:
            uiHandler.ety_glassMeasure_pos4lengthVar.set(length)
            uiHandler.ety_glassMeasure_pos4widthVar.set(width)
            uiHandler.cbb_glassMeasure_pos4type.current(newindex = index)
            uiHandler.ety_glassMeasure_pos4countVar.set(count)

        elif pos == 5:
            uiHandler.ety_glassMeasure_pos5lengthVar.set(length)
            uiHandler.ety_glassMeasure_pos5widthVar.set(width)
            uiHandler.cbb_glassMeasure_pos5type.current(newindex = index)
            uiHandler.ety_glassMeasure_pos5countVar.set(count)

        elif pos == 6:
            uiHandler.ety_glassMeasure_pos6lengthVar.set(length)
            uiHandler.ety_glassMeasure_pos6widthVar.set(width)
            uiHandler.cbb_glassMeasure_pos6type.current(newindex = index)
            uiHandler.ety_glassMeasure_pos6countVar.set(count)

        elif pos == 7:
            uiHandler.ety_glassMeasure_pos7lengthVar.set(length)
            uiHandler.ety_glassMeasure_pos7widthVar.set(width)
            uiHandler.cbb_glassMeasure_pos7type.current(newindex = index)
            uiHandler.ety_glassMeasure_pos7countVar.set(count)

        elif pos == 8:
            uiHandler.ety_glassMeasure_pos8lengthVar.set(length)
            uiHandler.ety_glassMeasure_pos8widthVar.set(width)
            uiHandler.cbb_glassMeasure_pos8type.current(newindex = index)
            uiHandler.ety_glassMeasure_pos8countVar.set(count)

    return True

def showCalcError(code: int):

    msg = dataHandler.dict_lang["lang_error_calculation"] + " {:05d}".format(code)
    tkmsg.showerror(title = dataHandler.titleVersion, message = msg)