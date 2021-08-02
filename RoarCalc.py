#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data import dataHandler, uiHandler

if __name__ == '__main__':

    if dataHandler.initRoutine() == False:
        exit()

    else:

        uiHandler.createUI()