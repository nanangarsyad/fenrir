#!/bin/python

class command():
    def __init__(self):
        pass
    def initialize(self, environment):
        pass
    def shutdown(self, environment):
        pass
    def getDescription(self, environment):
        return ''           
    
    def run(self, environment):
        if environment['screenData']['newTTY'] != environment['screenData']['oldTTY']:
            return environment
        if environment['screenData']['newDelta'] != environment['screenData']['oldDelta']:
            return environment    
        if environment['screenData']['newCursor']['y'] == environment['screenData']['oldCursor']['y']:
            return environment
        if environment['screenData']['newContentText'].split('\n')[environment['screenData']['newCursor']['y']].strip(" \t\n") == '':
            environment['runtime']['outputManager'].presentText(environment, "blank", soundIcon='EmptyLine', interrupt=True)
        else:
            environment['runtime']['outputManager'].presentText(environment, environment['screenData']['newContentText'].split('\n')[environment['screenData']['newCursor']['y']], True)
 
    def setCallback(self, callback):
        pass

