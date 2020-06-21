# -*- coding: utf-8 -*-
import os
import sys
#change working directory to pandaVis folder
abspath = os.path.abspath(__file__)
workDir = os.path.dirname(abspath)
workDir = os.path.join(workDir,'PandaVis')
os.chdir(workDir)

sys.path.append(os.getcwd())

from entryWindow import cEntryWindow
from app import cApp
from dashVis.dashVis import cDashVis


if __name__ == "__main__":
    entryWin = cEntryWindow()
    entryWin.Show()

    if entryWin.command == 'terminate':
        print("App terminated")
    elif entryWin.command == '-run3Dexplorer-':
        print("RUN 3D explorer")
        app = cApp(entryWin.databaseFilePath)
        app.run()
        
    elif entryWin.command == '-runDash-':
        print("RUN DASH")
        dashVis = cDashVis()
        dashVis.run(entryWin.databaseFilePath, entryWin.dashLayout)
        
        
    
