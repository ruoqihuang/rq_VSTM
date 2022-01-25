#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Mon Aug 16 12:45:20 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'CIS_5'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/athenahuang/SchoolWorksAndOthers/Downloads/CIS Experiment/CIS_5.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Consent"
ConsentClock = core.Clock()
textConsent = visual.TextStim(win=win, name='textConsent',
    text='Please make sure you have read the consent form and agree to particiate before you click any keys.\n\nParticipation is completely voluntary.\n\nPress space to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyconsent = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
textWelcome = visual.TextStim(win=win, name='textWelcome',
    text='Welcome to the visual short-term memory experiment! \n\nThank you so much to participate!\n\nPress space to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keywelcome = keyboard.Keyboard()

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
textintroduction = visual.TextStim(win=win, name='textintroduction',
    text='You will be shown one photos for a short while, afterwards, you will be shown four choices.\n\nChose the one you think you have seen.\n\nPress space to enter the training phase.',
    font='Open Sans',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyintroduction = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
imageT1 = visual.ImageStim(
    win=win,
    name='imageT1', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.375, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
imageT2 = visual.ImageStim(
    win=win,
    name='imageT2', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.125, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
imageT3 = visual.ImageStim(
    win=win,
    name='imageT3', 
    image='sin', mask=None,
    ori=0.0, pos=(0.125, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
imageT4 = visual.ImageStim(
    win=win,
    name='imageT4', 
    image='sin', mask=None,
    ori=0.0, pos=(0.375, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='1',
    font='Open Sans',
    pos=(-0.375, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='2',
    font='Open Sans',
    pos=(-0.125, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='3',
    font='Open Sans',
    pos=(0.125, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='4',
    font='Open Sans',
    pos=(0.375, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "Interruption1"
Interruption1Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Wait for instruction from the monitor.\n\nPress space only when told to do so.\n\nThank you!',
    font='Open Sans',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Nextsession = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
imageT1 = visual.ImageStim(
    win=win,
    name='imageT1', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.375, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
imageT2 = visual.ImageStim(
    win=win,
    name='imageT2', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.125, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
imageT3 = visual.ImageStim(
    win=win,
    name='imageT3', 
    image='sin', mask=None,
    ori=0.0, pos=(0.125, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
imageT4 = visual.ImageStim(
    win=win,
    name='imageT4', 
    image='sin', mask=None,
    ori=0.0, pos=(0.375, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='1',
    font='Open Sans',
    pos=(-0.375, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='2',
    font='Open Sans',
    pos=(-0.125, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='3',
    font='Open Sans',
    pos=(0.125, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='4',
    font='Open Sans',
    pos=(0.375, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "Interruption1"
Interruption1Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Wait for instruction from the monitor.\n\nPress space only when told to do so.\n\nThank you!',
    font='Open Sans',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Nextsession = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
imageT1 = visual.ImageStim(
    win=win,
    name='imageT1', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.375, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
imageT2 = visual.ImageStim(
    win=win,
    name='imageT2', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.125, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
imageT3 = visual.ImageStim(
    win=win,
    name='imageT3', 
    image='sin', mask=None,
    ori=0.0, pos=(0.125, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
imageT4 = visual.ImageStim(
    win=win,
    name='imageT4', 
    image='sin', mask=None,
    ori=0.0, pos=(0.375, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='1',
    font='Open Sans',
    pos=(-0.375, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='2',
    font='Open Sans',
    pos=(-0.125, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='3',
    font='Open Sans',
    pos=(0.125, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='4',
    font='Open Sans',
    pos=(0.375, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "Interruption1"
Interruption1Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Wait for instruction from the monitor.\n\nPress space only when told to do so.\n\nThank you!',
    font='Open Sans',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Nextsession = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
imageT1 = visual.ImageStim(
    win=win,
    name='imageT1', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.375, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
imageT2 = visual.ImageStim(
    win=win,
    name='imageT2', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.125, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
imageT3 = visual.ImageStim(
    win=win,
    name='imageT3', 
    image='sin', mask=None,
    ori=0.0, pos=(0.125, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
imageT4 = visual.ImageStim(
    win=win,
    name='imageT4', 
    image='sin', mask=None,
    ori=0.0, pos=(0.375, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='1',
    font='Open Sans',
    pos=(-0.375, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='2',
    font='Open Sans',
    pos=(-0.125, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='3',
    font='Open Sans',
    pos=(0.125, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='4',
    font='Open Sans',
    pos=(0.375, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "Interruption1"
Interruption1Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Wait for instruction from the monitor.\n\nPress space only when told to do so.\n\nThank you!',
    font='Open Sans',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Nextsession = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
imageT1 = visual.ImageStim(
    win=win,
    name='imageT1', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.375, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
imageT2 = visual.ImageStim(
    win=win,
    name='imageT2', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.125, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
imageT3 = visual.ImageStim(
    win=win,
    name='imageT3', 
    image='sin', mask=None,
    ori=0.0, pos=(0.125, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
imageT4 = visual.ImageStim(
    win=win,
    name='imageT4', 
    image='sin', mask=None,
    ori=0.0, pos=(0.375, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='1',
    font='Open Sans',
    pos=(-0.375, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='2',
    font='Open Sans',
    pos=(-0.125, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='3',
    font='Open Sans',
    pos=(0.125, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='4',
    font='Open Sans',
    pos=(0.375, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "Interruption1"
Interruption1Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Wait for instruction from the monitor.\n\nPress space only when told to do so.\n\nThank you!',
    font='Open Sans',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Nextsession = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
imageT1 = visual.ImageStim(
    win=win,
    name='imageT1', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.375, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
imageT2 = visual.ImageStim(
    win=win,
    name='imageT2', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.125, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
imageT3 = visual.ImageStim(
    win=win,
    name='imageT3', 
    image='sin', mask=None,
    ori=0.0, pos=(0.125, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
imageT4 = visual.ImageStim(
    win=win,
    name='imageT4', 
    image='sin', mask=None,
    ori=0.0, pos=(0.375, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='1',
    font='Open Sans',
    pos=(-0.375, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='2',
    font='Open Sans',
    pos=(-0.125, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='3',
    font='Open Sans',
    pos=(0.125, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='4',
    font='Open Sans',
    pos=(0.375, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "EndAndDebrief"
EndAndDebriefClock = core.Clock()
textThankYou = visual.TextStim(win=win, name='textThankYou',
    text='Thank you for your participation.\n\nPlease reach out to the monitor if you would like a debrief.\n\nPress esc to exit only when told to do so.',
    font='Open Sans',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Consent"-------
continueRoutine = True
# update component parameters for each repeat
keyconsent.keys = []
keyconsent.rt = []
_keyconsent_allKeys = []
# keep track of which components have finished
ConsentComponents = [textConsent, keyconsent]
for thisComponent in ConsentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ConsentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Consent"-------
while continueRoutine:
    # get current time
    t = ConsentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ConsentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textConsent* updates
    if textConsent.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textConsent.frameNStart = frameN  # exact frame index
        textConsent.tStart = t  # local t and not account for scr refresh
        textConsent.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textConsent, 'tStartRefresh')  # time at next scr refresh
        textConsent.setAutoDraw(True)
    
    # *keyconsent* updates
    waitOnFlip = False
    if keyconsent.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyconsent.frameNStart = frameN  # exact frame index
        keyconsent.tStart = t  # local t and not account for scr refresh
        keyconsent.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyconsent, 'tStartRefresh')  # time at next scr refresh
        keyconsent.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyconsent.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyconsent.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyconsent.status == STARTED and not waitOnFlip:
        theseKeys = keyconsent.getKeys(keyList=['space'], waitRelease=False)
        _keyconsent_allKeys.extend(theseKeys)
        if len(_keyconsent_allKeys):
            keyconsent.keys = _keyconsent_allKeys[-1].name  # just the last key pressed
            keyconsent.rt = _keyconsent_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ConsentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Consent"-------
for thisComponent in ConsentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textConsent.started', textConsent.tStartRefresh)
thisExp.addData('textConsent.stopped', textConsent.tStopRefresh)
# check responses
if keyconsent.keys in ['', [], None]:  # No response was made
    keyconsent.keys = None
thisExp.addData('keyconsent.keys',keyconsent.keys)
if keyconsent.keys != None:  # we had a response
    thisExp.addData('keyconsent.rt', keyconsent.rt)
thisExp.addData('keyconsent.started', keyconsent.tStartRefresh)
thisExp.addData('keyconsent.stopped', keyconsent.tStopRefresh)
thisExp.nextEntry()
# the Routine "Consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
# update component parameters for each repeat
keywelcome.keys = []
keywelcome.rt = []
_keywelcome_allKeys = []
# keep track of which components have finished
WelcomeComponents = [textWelcome, keywelcome]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcome* updates
    if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcome.frameNStart = frameN  # exact frame index
        textWelcome.tStart = t  # local t and not account for scr refresh
        textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
        textWelcome.setAutoDraw(True)
    
    # *keywelcome* updates
    waitOnFlip = False
    if keywelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keywelcome.frameNStart = frameN  # exact frame index
        keywelcome.tStart = t  # local t and not account for scr refresh
        keywelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keywelcome, 'tStartRefresh')  # time at next scr refresh
        keywelcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keywelcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keywelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keywelcome.status == STARTED and not waitOnFlip:
        theseKeys = keywelcome.getKeys(keyList=['space'], waitRelease=False)
        _keywelcome_allKeys.extend(theseKeys)
        if len(_keywelcome_allKeys):
            keywelcome.keys = _keywelcome_allKeys[-1].name  # just the last key pressed
            keywelcome.rt = _keywelcome_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textWelcome.started', textWelcome.tStartRefresh)
thisExp.addData('textWelcome.stopped', textWelcome.tStopRefresh)
# check responses
if keywelcome.keys in ['', [], None]:  # No response was made
    keywelcome.keys = None
thisExp.addData('keywelcome.keys',keywelcome.keys)
if keywelcome.keys != None:  # we had a response
    thisExp.addData('keywelcome.rt', keywelcome.rt)
thisExp.addData('keywelcome.started', keywelcome.tStartRefresh)
thisExp.addData('keywelcome.stopped', keywelcome.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instruction"-------
continueRoutine = True
# update component parameters for each repeat
keyintroduction.keys = []
keyintroduction.rt = []
_keyintroduction_allKeys = []
# keep track of which components have finished
InstructionComponents = [textintroduction, keyintroduction]
for thisComponent in InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction"-------
while continueRoutine:
    # get current time
    t = InstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textintroduction* updates
    if textintroduction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textintroduction.frameNStart = frameN  # exact frame index
        textintroduction.tStart = t  # local t and not account for scr refresh
        textintroduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textintroduction, 'tStartRefresh')  # time at next scr refresh
        textintroduction.setAutoDraw(True)
    
    # *keyintroduction* updates
    waitOnFlip = False
    if keyintroduction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyintroduction.frameNStart = frameN  # exact frame index
        keyintroduction.tStart = t  # local t and not account for scr refresh
        keyintroduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyintroduction, 'tStartRefresh')  # time at next scr refresh
        keyintroduction.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyintroduction.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyintroduction.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyintroduction.status == STARTED and not waitOnFlip:
        theseKeys = keyintroduction.getKeys(keyList=['space'], waitRelease=False)
        _keyintroduction_allKeys.extend(theseKeys)
        if len(_keyintroduction_allKeys):
            keyintroduction.keys = _keyintroduction_allKeys[-1].name  # just the last key pressed
            keyintroduction.rt = _keyintroduction_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textintroduction.started', textintroduction.tStartRefresh)
thisExp.addData('textintroduction.stopped', textintroduction.tStopRefresh)
# check responses
if keyintroduction.keys in ['', [], None]:  # No response was made
    keyintroduction.keys = None
thisExp.addData('keyintroduction.keys',keyintroduction.keys)
if keyintroduction.keys != None:  # we had a response
    thisExp.addData('keyintroduction.rt', keyintroduction.rt)
thisExp.addData('keyintroduction.started', keyintroduction.tStartRefresh)
thisExp.addData('keyintroduction.stopped', keyintroduction.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_7 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('image_stimuli.xlsx', selection='51:53'),
    seed=None, name='trials_7')
thisExp.addLoop(trials_7)  # add the loop to the experiment
thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
if thisTrial_7 != None:
    for paramName in thisTrial_7:
        exec('{} = thisTrial_7[paramName]'.format(paramName))

for thisTrial_7 in trials_7:
    currentLoop = trials_7
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
    if thisTrial_7 != None:
        for paramName in thisTrial_7:
            exec('{} = thisTrial_7[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    imageT1.setImage(ImageFile1)
    imageT2.setImage(ImageFile2)
    imageT3.setImage(ImageFile3)
    imageT4.setImage(ImageFile4)
    # keep track of which components have finished
    trialComponents = [Fixation, image, key_resp, imageT1, imageT2, imageT3, imageT4, text_2, text_3, text_4, text_5]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *imageT1* updates
        if imageT1.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT1.frameNStart = frameN  # exact frame index
            imageT1.tStart = t  # local t and not account for scr refresh
            imageT1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT1, 'tStartRefresh')  # time at next scr refresh
            imageT1.setAutoDraw(True)
        if imageT1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT1.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT1.tStop = t  # not accounting for scr refresh
                imageT1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT1, 'tStopRefresh')  # time at next scr refresh
                imageT1.setAutoDraw(False)
        
        # *imageT2* updates
        if imageT2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT2.frameNStart = frameN  # exact frame index
            imageT2.tStart = t  # local t and not account for scr refresh
            imageT2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT2, 'tStartRefresh')  # time at next scr refresh
            imageT2.setAutoDraw(True)
        if imageT2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT2.tStop = t  # not accounting for scr refresh
                imageT2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT2, 'tStopRefresh')  # time at next scr refresh
                imageT2.setAutoDraw(False)
        
        # *imageT3* updates
        if imageT3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT3.frameNStart = frameN  # exact frame index
            imageT3.tStart = t  # local t and not account for scr refresh
            imageT3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT3, 'tStartRefresh')  # time at next scr refresh
            imageT3.setAutoDraw(True)
        if imageT3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT3.tStop = t  # not accounting for scr refresh
                imageT3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT3, 'tStopRefresh')  # time at next scr refresh
                imageT3.setAutoDraw(False)
        
        # *imageT4* updates
        if imageT4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT4.frameNStart = frameN  # exact frame index
            imageT4.tStart = t  # local t and not account for scr refresh
            imageT4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT4, 'tStartRefresh')  # time at next scr refresh
            imageT4.setAutoDraw(True)
        if imageT4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT4.tStop = t  # not accounting for scr refresh
                imageT4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT4, 'tStopRefresh')  # time at next scr refresh
                imageT4.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_7.addData('Fixation.started', Fixation.tStartRefresh)
    trials_7.addData('Fixation.stopped', Fixation.tStopRefresh)
    trials_7.addData('image.started', image.tStartRefresh)
    trials_7.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials_7.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials_7.addData('key_resp.rt', key_resp.rt)
    trials_7.addData('key_resp.started', key_resp.tStartRefresh)
    trials_7.addData('key_resp.stopped', key_resp.tStopRefresh)
    trials_7.addData('imageT1.started', imageT1.tStartRefresh)
    trials_7.addData('imageT1.stopped', imageT1.tStopRefresh)
    trials_7.addData('imageT2.started', imageT2.tStartRefresh)
    trials_7.addData('imageT2.stopped', imageT2.tStopRefresh)
    trials_7.addData('imageT3.started', imageT3.tStartRefresh)
    trials_7.addData('imageT3.stopped', imageT3.tStopRefresh)
    trials_7.addData('imageT4.started', imageT4.tStartRefresh)
    trials_7.addData('imageT4.stopped', imageT4.tStopRefresh)
    trials_7.addData('text_2.started', text_2.tStartRefresh)
    trials_7.addData('text_2.stopped', text_2.tStopRefresh)
    trials_7.addData('text_3.started', text_3.tStartRefresh)
    trials_7.addData('text_3.stopped', text_3.tStopRefresh)
    trials_7.addData('text_4.started', text_4.tStartRefresh)
    trials_7.addData('text_4.stopped', text_4.tStopRefresh)
    trials_7.addData('text_5.started', text_5.tStartRefresh)
    trials_7.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials_7'


# ------Prepare to start Routine "Interruption1"-------
continueRoutine = True
# update component parameters for each repeat
Nextsession.keys = []
Nextsession.rt = []
_Nextsession_allKeys = []
# keep track of which components have finished
Interruption1Components = [text, Nextsession]
for thisComponent in Interruption1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Interruption1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Interruption1"-------
while continueRoutine:
    # get current time
    t = Interruption1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Interruption1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *Nextsession* updates
    waitOnFlip = False
    if Nextsession.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Nextsession.frameNStart = frameN  # exact frame index
        Nextsession.tStart = t  # local t and not account for scr refresh
        Nextsession.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Nextsession, 'tStartRefresh')  # time at next scr refresh
        Nextsession.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Nextsession.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Nextsession.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Nextsession.status == STARTED and not waitOnFlip:
        theseKeys = Nextsession.getKeys(keyList=['space'], waitRelease=False)
        _Nextsession_allKeys.extend(theseKeys)
        if len(_Nextsession_allKeys):
            Nextsession.keys = _Nextsession_allKeys[-1].name  # just the last key pressed
            Nextsession.rt = _Nextsession_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Interruption1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Interruption1"-------
for thisComponent in Interruption1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if Nextsession.keys in ['', [], None]:  # No response was made
    Nextsession.keys = None
thisExp.addData('Nextsession.keys',Nextsession.keys)
if Nextsession.keys != None:  # we had a response
    thisExp.addData('Nextsession.rt', Nextsession.rt)
thisExp.addData('Nextsession.started', Nextsession.tStartRefresh)
thisExp.addData('Nextsession.stopped', Nextsession.tStopRefresh)
thisExp.nextEntry()
# the Routine "Interruption1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/Users/athenahuang/Downloads/CIS Experiment/image_stimuli.xlsx', selection='0:10'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    imageT1.setImage(ImageFile1)
    imageT2.setImage(ImageFile2)
    imageT3.setImage(ImageFile3)
    imageT4.setImage(ImageFile4)
    # keep track of which components have finished
    trialComponents = [Fixation, image, key_resp, imageT1, imageT2, imageT3, imageT4, text_2, text_3, text_4, text_5]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *imageT1* updates
        if imageT1.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT1.frameNStart = frameN  # exact frame index
            imageT1.tStart = t  # local t and not account for scr refresh
            imageT1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT1, 'tStartRefresh')  # time at next scr refresh
            imageT1.setAutoDraw(True)
        if imageT1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT1.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT1.tStop = t  # not accounting for scr refresh
                imageT1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT1, 'tStopRefresh')  # time at next scr refresh
                imageT1.setAutoDraw(False)
        
        # *imageT2* updates
        if imageT2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT2.frameNStart = frameN  # exact frame index
            imageT2.tStart = t  # local t and not account for scr refresh
            imageT2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT2, 'tStartRefresh')  # time at next scr refresh
            imageT2.setAutoDraw(True)
        if imageT2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT2.tStop = t  # not accounting for scr refresh
                imageT2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT2, 'tStopRefresh')  # time at next scr refresh
                imageT2.setAutoDraw(False)
        
        # *imageT3* updates
        if imageT3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT3.frameNStart = frameN  # exact frame index
            imageT3.tStart = t  # local t and not account for scr refresh
            imageT3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT3, 'tStartRefresh')  # time at next scr refresh
            imageT3.setAutoDraw(True)
        if imageT3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT3.tStop = t  # not accounting for scr refresh
                imageT3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT3, 'tStopRefresh')  # time at next scr refresh
                imageT3.setAutoDraw(False)
        
        # *imageT4* updates
        if imageT4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT4.frameNStart = frameN  # exact frame index
            imageT4.tStart = t  # local t and not account for scr refresh
            imageT4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT4, 'tStartRefresh')  # time at next scr refresh
            imageT4.setAutoDraw(True)
        if imageT4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT4.tStop = t  # not accounting for scr refresh
                imageT4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT4, 'tStopRefresh')  # time at next scr refresh
                imageT4.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Fixation.started', Fixation.tStartRefresh)
    trials.addData('Fixation.stopped', Fixation.tStopRefresh)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    trials.addData('imageT1.started', imageT1.tStartRefresh)
    trials.addData('imageT1.stopped', imageT1.tStopRefresh)
    trials.addData('imageT2.started', imageT2.tStartRefresh)
    trials.addData('imageT2.stopped', imageT2.tStopRefresh)
    trials.addData('imageT3.started', imageT3.tStartRefresh)
    trials.addData('imageT3.stopped', imageT3.tStopRefresh)
    trials.addData('imageT4.started', imageT4.tStartRefresh)
    trials.addData('imageT4.stopped', imageT4.tStopRefresh)
    trials.addData('text_2.started', text_2.tStartRefresh)
    trials.addData('text_2.stopped', text_2.tStopRefresh)
    trials.addData('text_3.started', text_3.tStartRefresh)
    trials.addData('text_3.stopped', text_3.tStopRefresh)
    trials.addData('text_4.started', text_4.tStartRefresh)
    trials.addData('text_4.stopped', text_4.tStopRefresh)
    trials.addData('text_5.started', text_5.tStartRefresh)
    trials.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "Interruption1"-------
continueRoutine = True
# update component parameters for each repeat
Nextsession.keys = []
Nextsession.rt = []
_Nextsession_allKeys = []
# keep track of which components have finished
Interruption1Components = [text, Nextsession]
for thisComponent in Interruption1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Interruption1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Interruption1"-------
while continueRoutine:
    # get current time
    t = Interruption1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Interruption1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *Nextsession* updates
    waitOnFlip = False
    if Nextsession.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Nextsession.frameNStart = frameN  # exact frame index
        Nextsession.tStart = t  # local t and not account for scr refresh
        Nextsession.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Nextsession, 'tStartRefresh')  # time at next scr refresh
        Nextsession.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Nextsession.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Nextsession.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Nextsession.status == STARTED and not waitOnFlip:
        theseKeys = Nextsession.getKeys(keyList=['space'], waitRelease=False)
        _Nextsession_allKeys.extend(theseKeys)
        if len(_Nextsession_allKeys):
            Nextsession.keys = _Nextsession_allKeys[-1].name  # just the last key pressed
            Nextsession.rt = _Nextsession_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Interruption1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Interruption1"-------
for thisComponent in Interruption1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if Nextsession.keys in ['', [], None]:  # No response was made
    Nextsession.keys = None
thisExp.addData('Nextsession.keys',Nextsession.keys)
if Nextsession.keys != None:  # we had a response
    thisExp.addData('Nextsession.rt', Nextsession.rt)
thisExp.addData('Nextsession.started', Nextsession.tStartRefresh)
thisExp.addData('Nextsession.stopped', Nextsession.tStopRefresh)
thisExp.nextEntry()
# the Routine "Interruption1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('image_stimuli.xlsx', selection='10:20'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    imageT1.setImage(ImageFile1)
    imageT2.setImage(ImageFile2)
    imageT3.setImage(ImageFile3)
    imageT4.setImage(ImageFile4)
    # keep track of which components have finished
    trialComponents = [Fixation, image, key_resp, imageT1, imageT2, imageT3, imageT4, text_2, text_3, text_4, text_5]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *imageT1* updates
        if imageT1.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT1.frameNStart = frameN  # exact frame index
            imageT1.tStart = t  # local t and not account for scr refresh
            imageT1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT1, 'tStartRefresh')  # time at next scr refresh
            imageT1.setAutoDraw(True)
        if imageT1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT1.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT1.tStop = t  # not accounting for scr refresh
                imageT1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT1, 'tStopRefresh')  # time at next scr refresh
                imageT1.setAutoDraw(False)
        
        # *imageT2* updates
        if imageT2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT2.frameNStart = frameN  # exact frame index
            imageT2.tStart = t  # local t and not account for scr refresh
            imageT2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT2, 'tStartRefresh')  # time at next scr refresh
            imageT2.setAutoDraw(True)
        if imageT2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT2.tStop = t  # not accounting for scr refresh
                imageT2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT2, 'tStopRefresh')  # time at next scr refresh
                imageT2.setAutoDraw(False)
        
        # *imageT3* updates
        if imageT3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT3.frameNStart = frameN  # exact frame index
            imageT3.tStart = t  # local t and not account for scr refresh
            imageT3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT3, 'tStartRefresh')  # time at next scr refresh
            imageT3.setAutoDraw(True)
        if imageT3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT3.tStop = t  # not accounting for scr refresh
                imageT3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT3, 'tStopRefresh')  # time at next scr refresh
                imageT3.setAutoDraw(False)
        
        # *imageT4* updates
        if imageT4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT4.frameNStart = frameN  # exact frame index
            imageT4.tStart = t  # local t and not account for scr refresh
            imageT4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT4, 'tStartRefresh')  # time at next scr refresh
            imageT4.setAutoDraw(True)
        if imageT4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT4.tStop = t  # not accounting for scr refresh
                imageT4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT4, 'tStopRefresh')  # time at next scr refresh
                imageT4.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('Fixation.started', Fixation.tStartRefresh)
    trials_2.addData('Fixation.stopped', Fixation.tStopRefresh)
    trials_2.addData('image.started', image.tStartRefresh)
    trials_2.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials_2.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials_2.addData('key_resp.rt', key_resp.rt)
    trials_2.addData('key_resp.started', key_resp.tStartRefresh)
    trials_2.addData('key_resp.stopped', key_resp.tStopRefresh)
    trials_2.addData('imageT1.started', imageT1.tStartRefresh)
    trials_2.addData('imageT1.stopped', imageT1.tStopRefresh)
    trials_2.addData('imageT2.started', imageT2.tStartRefresh)
    trials_2.addData('imageT2.stopped', imageT2.tStopRefresh)
    trials_2.addData('imageT3.started', imageT3.tStartRefresh)
    trials_2.addData('imageT3.stopped', imageT3.tStopRefresh)
    trials_2.addData('imageT4.started', imageT4.tStartRefresh)
    trials_2.addData('imageT4.stopped', imageT4.tStopRefresh)
    trials_2.addData('text_2.started', text_2.tStartRefresh)
    trials_2.addData('text_2.stopped', text_2.tStopRefresh)
    trials_2.addData('text_3.started', text_3.tStartRefresh)
    trials_2.addData('text_3.stopped', text_3.tStopRefresh)
    trials_2.addData('text_4.started', text_4.tStartRefresh)
    trials_2.addData('text_4.stopped', text_4.tStopRefresh)
    trials_2.addData('text_5.started', text_5.tStartRefresh)
    trials_2.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# ------Prepare to start Routine "Interruption1"-------
continueRoutine = True
# update component parameters for each repeat
Nextsession.keys = []
Nextsession.rt = []
_Nextsession_allKeys = []
# keep track of which components have finished
Interruption1Components = [text, Nextsession]
for thisComponent in Interruption1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Interruption1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Interruption1"-------
while continueRoutine:
    # get current time
    t = Interruption1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Interruption1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *Nextsession* updates
    waitOnFlip = False
    if Nextsession.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Nextsession.frameNStart = frameN  # exact frame index
        Nextsession.tStart = t  # local t and not account for scr refresh
        Nextsession.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Nextsession, 'tStartRefresh')  # time at next scr refresh
        Nextsession.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Nextsession.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Nextsession.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Nextsession.status == STARTED and not waitOnFlip:
        theseKeys = Nextsession.getKeys(keyList=['space'], waitRelease=False)
        _Nextsession_allKeys.extend(theseKeys)
        if len(_Nextsession_allKeys):
            Nextsession.keys = _Nextsession_allKeys[-1].name  # just the last key pressed
            Nextsession.rt = _Nextsession_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Interruption1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Interruption1"-------
for thisComponent in Interruption1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if Nextsession.keys in ['', [], None]:  # No response was made
    Nextsession.keys = None
thisExp.addData('Nextsession.keys',Nextsession.keys)
if Nextsession.keys != None:  # we had a response
    thisExp.addData('Nextsession.rt', Nextsession.rt)
thisExp.addData('Nextsession.started', Nextsession.tStartRefresh)
thisExp.addData('Nextsession.stopped', Nextsession.tStopRefresh)
thisExp.nextEntry()
# the Routine "Interruption1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('image_stimuli.xlsx', selection='20:30'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    imageT1.setImage(ImageFile1)
    imageT2.setImage(ImageFile2)
    imageT3.setImage(ImageFile3)
    imageT4.setImage(ImageFile4)
    # keep track of which components have finished
    trialComponents = [Fixation, image, key_resp, imageT1, imageT2, imageT3, imageT4, text_2, text_3, text_4, text_5]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *imageT1* updates
        if imageT1.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT1.frameNStart = frameN  # exact frame index
            imageT1.tStart = t  # local t and not account for scr refresh
            imageT1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT1, 'tStartRefresh')  # time at next scr refresh
            imageT1.setAutoDraw(True)
        if imageT1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT1.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT1.tStop = t  # not accounting for scr refresh
                imageT1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT1, 'tStopRefresh')  # time at next scr refresh
                imageT1.setAutoDraw(False)
        
        # *imageT2* updates
        if imageT2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT2.frameNStart = frameN  # exact frame index
            imageT2.tStart = t  # local t and not account for scr refresh
            imageT2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT2, 'tStartRefresh')  # time at next scr refresh
            imageT2.setAutoDraw(True)
        if imageT2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT2.tStop = t  # not accounting for scr refresh
                imageT2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT2, 'tStopRefresh')  # time at next scr refresh
                imageT2.setAutoDraw(False)
        
        # *imageT3* updates
        if imageT3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT3.frameNStart = frameN  # exact frame index
            imageT3.tStart = t  # local t and not account for scr refresh
            imageT3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT3, 'tStartRefresh')  # time at next scr refresh
            imageT3.setAutoDraw(True)
        if imageT3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT3.tStop = t  # not accounting for scr refresh
                imageT3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT3, 'tStopRefresh')  # time at next scr refresh
                imageT3.setAutoDraw(False)
        
        # *imageT4* updates
        if imageT4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT4.frameNStart = frameN  # exact frame index
            imageT4.tStart = t  # local t and not account for scr refresh
            imageT4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT4, 'tStartRefresh')  # time at next scr refresh
            imageT4.setAutoDraw(True)
        if imageT4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT4.tStop = t  # not accounting for scr refresh
                imageT4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT4, 'tStopRefresh')  # time at next scr refresh
                imageT4.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('Fixation.started', Fixation.tStartRefresh)
    trials_3.addData('Fixation.stopped', Fixation.tStopRefresh)
    trials_3.addData('image.started', image.tStartRefresh)
    trials_3.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials_3.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials_3.addData('key_resp.rt', key_resp.rt)
    trials_3.addData('key_resp.started', key_resp.tStartRefresh)
    trials_3.addData('key_resp.stopped', key_resp.tStopRefresh)
    trials_3.addData('imageT1.started', imageT1.tStartRefresh)
    trials_3.addData('imageT1.stopped', imageT1.tStopRefresh)
    trials_3.addData('imageT2.started', imageT2.tStartRefresh)
    trials_3.addData('imageT2.stopped', imageT2.tStopRefresh)
    trials_3.addData('imageT3.started', imageT3.tStartRefresh)
    trials_3.addData('imageT3.stopped', imageT3.tStopRefresh)
    trials_3.addData('imageT4.started', imageT4.tStartRefresh)
    trials_3.addData('imageT4.stopped', imageT4.tStopRefresh)
    trials_3.addData('text_2.started', text_2.tStartRefresh)
    trials_3.addData('text_2.stopped', text_2.tStopRefresh)
    trials_3.addData('text_3.started', text_3.tStartRefresh)
    trials_3.addData('text_3.stopped', text_3.tStopRefresh)
    trials_3.addData('text_4.started', text_4.tStartRefresh)
    trials_3.addData('text_4.stopped', text_4.tStopRefresh)
    trials_3.addData('text_5.started', text_5.tStartRefresh)
    trials_3.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'


# ------Prepare to start Routine "Interruption1"-------
continueRoutine = True
# update component parameters for each repeat
Nextsession.keys = []
Nextsession.rt = []
_Nextsession_allKeys = []
# keep track of which components have finished
Interruption1Components = [text, Nextsession]
for thisComponent in Interruption1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Interruption1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Interruption1"-------
while continueRoutine:
    # get current time
    t = Interruption1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Interruption1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *Nextsession* updates
    waitOnFlip = False
    if Nextsession.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Nextsession.frameNStart = frameN  # exact frame index
        Nextsession.tStart = t  # local t and not account for scr refresh
        Nextsession.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Nextsession, 'tStartRefresh')  # time at next scr refresh
        Nextsession.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Nextsession.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Nextsession.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Nextsession.status == STARTED and not waitOnFlip:
        theseKeys = Nextsession.getKeys(keyList=['space'], waitRelease=False)
        _Nextsession_allKeys.extend(theseKeys)
        if len(_Nextsession_allKeys):
            Nextsession.keys = _Nextsession_allKeys[-1].name  # just the last key pressed
            Nextsession.rt = _Nextsession_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Interruption1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Interruption1"-------
for thisComponent in Interruption1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if Nextsession.keys in ['', [], None]:  # No response was made
    Nextsession.keys = None
thisExp.addData('Nextsession.keys',Nextsession.keys)
if Nextsession.keys != None:  # we had a response
    thisExp.addData('Nextsession.rt', Nextsession.rt)
thisExp.addData('Nextsession.started', Nextsession.tStartRefresh)
thisExp.addData('Nextsession.stopped', Nextsession.tStopRefresh)
thisExp.nextEntry()
# the Routine "Interruption1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('image_stimuli.xlsx', selection='30:40'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    imageT1.setImage(ImageFile1)
    imageT2.setImage(ImageFile2)
    imageT3.setImage(ImageFile3)
    imageT4.setImage(ImageFile4)
    # keep track of which components have finished
    trialComponents = [Fixation, image, key_resp, imageT1, imageT2, imageT3, imageT4, text_2, text_3, text_4, text_5]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *imageT1* updates
        if imageT1.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT1.frameNStart = frameN  # exact frame index
            imageT1.tStart = t  # local t and not account for scr refresh
            imageT1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT1, 'tStartRefresh')  # time at next scr refresh
            imageT1.setAutoDraw(True)
        if imageT1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT1.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT1.tStop = t  # not accounting for scr refresh
                imageT1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT1, 'tStopRefresh')  # time at next scr refresh
                imageT1.setAutoDraw(False)
        
        # *imageT2* updates
        if imageT2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT2.frameNStart = frameN  # exact frame index
            imageT2.tStart = t  # local t and not account for scr refresh
            imageT2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT2, 'tStartRefresh')  # time at next scr refresh
            imageT2.setAutoDraw(True)
        if imageT2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT2.tStop = t  # not accounting for scr refresh
                imageT2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT2, 'tStopRefresh')  # time at next scr refresh
                imageT2.setAutoDraw(False)
        
        # *imageT3* updates
        if imageT3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT3.frameNStart = frameN  # exact frame index
            imageT3.tStart = t  # local t and not account for scr refresh
            imageT3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT3, 'tStartRefresh')  # time at next scr refresh
            imageT3.setAutoDraw(True)
        if imageT3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT3.tStop = t  # not accounting for scr refresh
                imageT3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT3, 'tStopRefresh')  # time at next scr refresh
                imageT3.setAutoDraw(False)
        
        # *imageT4* updates
        if imageT4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT4.frameNStart = frameN  # exact frame index
            imageT4.tStart = t  # local t and not account for scr refresh
            imageT4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT4, 'tStartRefresh')  # time at next scr refresh
            imageT4.setAutoDraw(True)
        if imageT4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT4.tStop = t  # not accounting for scr refresh
                imageT4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT4, 'tStopRefresh')  # time at next scr refresh
                imageT4.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_4.addData('Fixation.started', Fixation.tStartRefresh)
    trials_4.addData('Fixation.stopped', Fixation.tStopRefresh)
    trials_4.addData('image.started', image.tStartRefresh)
    trials_4.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials_4.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials_4.addData('key_resp.rt', key_resp.rt)
    trials_4.addData('key_resp.started', key_resp.tStartRefresh)
    trials_4.addData('key_resp.stopped', key_resp.tStopRefresh)
    trials_4.addData('imageT1.started', imageT1.tStartRefresh)
    trials_4.addData('imageT1.stopped', imageT1.tStopRefresh)
    trials_4.addData('imageT2.started', imageT2.tStartRefresh)
    trials_4.addData('imageT2.stopped', imageT2.tStopRefresh)
    trials_4.addData('imageT3.started', imageT3.tStartRefresh)
    trials_4.addData('imageT3.stopped', imageT3.tStopRefresh)
    trials_4.addData('imageT4.started', imageT4.tStartRefresh)
    trials_4.addData('imageT4.stopped', imageT4.tStopRefresh)
    trials_4.addData('text_2.started', text_2.tStartRefresh)
    trials_4.addData('text_2.stopped', text_2.tStopRefresh)
    trials_4.addData('text_3.started', text_3.tStartRefresh)
    trials_4.addData('text_3.stopped', text_3.tStopRefresh)
    trials_4.addData('text_4.started', text_4.tStartRefresh)
    trials_4.addData('text_4.stopped', text_4.tStopRefresh)
    trials_4.addData('text_5.started', text_5.tStartRefresh)
    trials_4.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_4'


# ------Prepare to start Routine "Interruption1"-------
continueRoutine = True
# update component parameters for each repeat
Nextsession.keys = []
Nextsession.rt = []
_Nextsession_allKeys = []
# keep track of which components have finished
Interruption1Components = [text, Nextsession]
for thisComponent in Interruption1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Interruption1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Interruption1"-------
while continueRoutine:
    # get current time
    t = Interruption1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Interruption1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *Nextsession* updates
    waitOnFlip = False
    if Nextsession.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Nextsession.frameNStart = frameN  # exact frame index
        Nextsession.tStart = t  # local t and not account for scr refresh
        Nextsession.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Nextsession, 'tStartRefresh')  # time at next scr refresh
        Nextsession.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Nextsession.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Nextsession.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Nextsession.status == STARTED and not waitOnFlip:
        theseKeys = Nextsession.getKeys(keyList=['space'], waitRelease=False)
        _Nextsession_allKeys.extend(theseKeys)
        if len(_Nextsession_allKeys):
            Nextsession.keys = _Nextsession_allKeys[-1].name  # just the last key pressed
            Nextsession.rt = _Nextsession_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Interruption1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Interruption1"-------
for thisComponent in Interruption1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if Nextsession.keys in ['', [], None]:  # No response was made
    Nextsession.keys = None
thisExp.addData('Nextsession.keys',Nextsession.keys)
if Nextsession.keys != None:  # we had a response
    thisExp.addData('Nextsession.rt', Nextsession.rt)
thisExp.addData('Nextsession.started', Nextsession.tStartRefresh)
thisExp.addData('Nextsession.stopped', Nextsession.tStopRefresh)
thisExp.nextEntry()
# the Routine "Interruption1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('image_stimuli.xlsx', selection='40:50'),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    imageT1.setImage(ImageFile1)
    imageT2.setImage(ImageFile2)
    imageT3.setImage(ImageFile3)
    imageT4.setImage(ImageFile4)
    # keep track of which components have finished
    trialComponents = [Fixation, image, key_resp, imageT1, imageT2, imageT3, imageT4, text_2, text_3, text_4, text_5]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *imageT1* updates
        if imageT1.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT1.frameNStart = frameN  # exact frame index
            imageT1.tStart = t  # local t and not account for scr refresh
            imageT1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT1, 'tStartRefresh')  # time at next scr refresh
            imageT1.setAutoDraw(True)
        if imageT1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT1.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT1.tStop = t  # not accounting for scr refresh
                imageT1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT1, 'tStopRefresh')  # time at next scr refresh
                imageT1.setAutoDraw(False)
        
        # *imageT2* updates
        if imageT2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT2.frameNStart = frameN  # exact frame index
            imageT2.tStart = t  # local t and not account for scr refresh
            imageT2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT2, 'tStartRefresh')  # time at next scr refresh
            imageT2.setAutoDraw(True)
        if imageT2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT2.tStop = t  # not accounting for scr refresh
                imageT2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT2, 'tStopRefresh')  # time at next scr refresh
                imageT2.setAutoDraw(False)
        
        # *imageT3* updates
        if imageT3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT3.frameNStart = frameN  # exact frame index
            imageT3.tStart = t  # local t and not account for scr refresh
            imageT3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT3, 'tStartRefresh')  # time at next scr refresh
            imageT3.setAutoDraw(True)
        if imageT3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT3.tStop = t  # not accounting for scr refresh
                imageT3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT3, 'tStopRefresh')  # time at next scr refresh
                imageT3.setAutoDraw(False)
        
        # *imageT4* updates
        if imageT4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            imageT4.frameNStart = frameN  # exact frame index
            imageT4.tStart = t  # local t and not account for scr refresh
            imageT4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageT4, 'tStartRefresh')  # time at next scr refresh
            imageT4.setAutoDraw(True)
        if imageT4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageT4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imageT4.tStop = t  # not accounting for scr refresh
                imageT4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageT4, 'tStopRefresh')  # time at next scr refresh
                imageT4.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('Fixation.started', Fixation.tStartRefresh)
    trials_5.addData('Fixation.stopped', Fixation.tStopRefresh)
    trials_5.addData('image.started', image.tStartRefresh)
    trials_5.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials_5.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials_5.addData('key_resp.rt', key_resp.rt)
    trials_5.addData('key_resp.started', key_resp.tStartRefresh)
    trials_5.addData('key_resp.stopped', key_resp.tStopRefresh)
    trials_5.addData('imageT1.started', imageT1.tStartRefresh)
    trials_5.addData('imageT1.stopped', imageT1.tStopRefresh)
    trials_5.addData('imageT2.started', imageT2.tStartRefresh)
    trials_5.addData('imageT2.stopped', imageT2.tStopRefresh)
    trials_5.addData('imageT3.started', imageT3.tStartRefresh)
    trials_5.addData('imageT3.stopped', imageT3.tStopRefresh)
    trials_5.addData('imageT4.started', imageT4.tStartRefresh)
    trials_5.addData('imageT4.stopped', imageT4.tStopRefresh)
    trials_5.addData('text_2.started', text_2.tStartRefresh)
    trials_5.addData('text_2.stopped', text_2.tStopRefresh)
    trials_5.addData('text_3.started', text_3.tStartRefresh)
    trials_5.addData('text_3.stopped', text_3.tStopRefresh)
    trials_5.addData('text_4.started', text_4.tStartRefresh)
    trials_5.addData('text_4.stopped', text_4.tStopRefresh)
    trials_5.addData('text_5.started', text_5.tStartRefresh)
    trials_5.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_5'


# ------Prepare to start Routine "EndAndDebrief"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
EndAndDebriefComponents = [textThankYou]
for thisComponent in EndAndDebriefComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndAndDebriefClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndAndDebrief"-------
while continueRoutine:
    # get current time
    t = EndAndDebriefClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndAndDebriefClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textThankYou* updates
    if textThankYou.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textThankYou.frameNStart = frameN  # exact frame index
        textThankYou.tStart = t  # local t and not account for scr refresh
        textThankYou.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textThankYou, 'tStartRefresh')  # time at next scr refresh
        textThankYou.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndAndDebriefComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndAndDebrief"-------
for thisComponent in EndAndDebriefComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textThankYou.started', textThankYou.tStartRefresh)
thisExp.addData('textThankYou.stopped', textThankYou.tStopRefresh)
# the Routine "EndAndDebrief" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
