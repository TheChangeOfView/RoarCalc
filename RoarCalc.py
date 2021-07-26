#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data import dataHandler, uiHandler
import tkinter as tk

def showCheckError(missing, isdir):

    root = tk.Tk()
    root.withdraw()

    if isdir == True:

        tk.messagebox.showerror(title = dataHandler.titleVersion, message = "Fatal Error: Files are corrupted\nMissing Directory: " + missing)

    else:

        tk.messagebox.showerror(title = dataHandler.titleVersion, message = "Fatal Error: Files are corrupted\nMissing File: " + missing)

    root.destroy()

if __name__ == '__main__':

    check, missing, isdir = dataHandler.checkFiles()

    if check == True:

        dataHandler.readConfigINI()
        dataHandler.getLanguage()
        uiHandler.createUI()

    else:

        showCheckError(missing, isdir)