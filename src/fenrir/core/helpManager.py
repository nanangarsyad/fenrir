#!/bin/python
# -*- coding: utf-8 -*-

# Fenrir TTY screen reader
# By Chrys, Storm Dragon, and contributers.

from core import debug


class helpManager():
    def __init__(self):
        self.helpDict = None
        self.tutorialListIndex = None          
    def initialize(self, environment):
        self.env = environment
        self.createHelpDict()

    def shutdown(self):
        pass      
    def toggleTutorialMode(self):
        self.setTutorialMode(not self.env['general']['tutorialMode'])
    def setTutorialMode(self, newTutorialMode):
        self.env['general']['tutorialMode'] = newTutorialMode
    def isTutorialMode(self):
        return self.env['general']['tutorialMode']        
    def getCommandHelpText(self, command, section = 'commands'):
        commandName = command.lower()
        commandName = commandName.split('__-__')[0]       
        commandName = commandName.replace('_',' ')        
        commandName = commandName.replace('_',' ')
        helptext = commandName + ', Shortcut , Description' + self.env['runtime']['commandManager'].getCommandDescription( command, section = 'commands')
        return helptext
    def createHelpDict(self, section = 'commands'):
        self.helpDict = {}        
        for command in sorted(self.env['commands'][section].keys()):
            self.helpDict[len(self.helpDict)] = self.getCommandHelpText(command, section)            
        if len(self.helpDict) > 0:
            self.tutorialListIndex = 0
    def getHelpForCurrentIndex(self):            
        if self.tutorialListIndex == None:
            return '' 
        return self.helpDict[self.tutorialListIndex]
    def nextIndex(self):
        if self.tutorialListIndex == None:
            return    
        self.tutorialListIndex += 1
        if self.tutorialListIndex >= len(self.helpDict):
           self.tutorialListIndex = 0 
    def prevIndex(self):
        if self.tutorialListIndex == None:
            return    
        self.tutorialListIndex -= 1
        if self.tutorialListIndex < 0:
           self.tutorialListIndex = len(self.helpDict) - 1
    def handleTutorialMode(self):
        if self.env['runtime']['inputManager'].noKeyPressed():
            return    
        if self.env['input']['currInput'] in [['KEY_F1', 'KEY_FENRIR']]:
            self.env['runtime']['commandManager'].runCommand('TOGGLE_TUTORIAL_MODE', 'help')     
            return True                                       
        if not self.isTutorialMode():
            return
        if self.env['input']['currInput'] in [['KEY_ESC']]:
            self.env['runtime']['commandManager'].runCommand('TOGGLE_TUTORIAL_MODE', 'help')             
            return True                                       
        if self.env['input']['currInput'] in [['KEY_UP']]:
            self.env['runtime']['commandManager'].runCommand('PREV_HELP', 'help')                  
            return True                                       
        if self.env['input']['currInput'] in [['KEY_DOWN']]:              
            self.env['runtime']['commandManager'].runCommand('NEXT_HELP', 'help')  
            return True                                       
        if self.env['input']['currInput'] in [['KEY_SPACE']]:              
            self.env['runtime']['commandManager'].runCommand('CURR_HELP', 'help')   
            return True     
        return False                                                             
