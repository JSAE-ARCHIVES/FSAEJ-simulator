MaxNumberOfTyresOut = 1
gOpacity            = 0.7        # 0.0 ... 1.0

'''
InvalidateLap App 0.2 for Assetto Corsa
based on "MaxNumberOfTyresOut" for CSP v0.1.37 and later
'''

import ac, acsys
import os, platform, sys, time, math
if platform.architecture()[0] == '64bit':
  sysdir='apps/python/InvalidateLap/stdlib64'
else:
  sysdir='apps/python/InvalidateLap/stdlib'
sys.path.insert(0, sysdir)
os.environ['PATH'] = os.environ['PATH'] + ';.'
from sim_info import info

appWindow = 0
timer = 0
bInvalidated = False
noOuts = 0
noOutsCurrLap = 0
lastTime = -1.0
isOut = False
sAppError=""
lastLap = -2
lastSessonTime = 10000

def getAddenum(noOuts, currentLap):
    if noOuts>0 and currentLap>0:
        if noOuts<2:
            return "\n   " + str(noOuts) + " cut total"
        else:
            return "\n   " + str(noOuts) + " cuts total"
    return ""

def getAddenum2(noOutsCurrLap, currentLap):
    if noOutsCurrLap>0:
        if noOutsCurrLap<2:
            return "\n   " + str(noOutsCurrLap) + " cut this lap"
        else:
            return "\n   " + str(noOutsCurrLap) + " cuts this lap"
    return ""

def CheckOffTrack():
    global MaxNumberOfTyresOut, lastLap, bInvalidated, appWindow
    global sAppError, info
    global noOuts, isOut, noOutsCurrLap, lastTime, lastSessonTime

    if sAppError!="":
        ac.setTitle(appWindow, sAppError)
    else:
        #currentCar = 0
        currentCar = ac.getFocusedCar()
        currentLap = ac.getCarState(currentCar, acsys.CS.LapCount)
        # currentLap = info.graphics.numberOfLaps
        currentTime = ac.getCarState(currentCar, acsys.CS.LapTime)

        # if currentTime < lastTime and lastLap > currentLap:
        currentSessonTime = info.graphics.sessionTimeLeft
        if currentSessonTime>lastSessonTime:
            # new session
            bInvalidated = False
            isOut = False
            noOuts = 0
            noOutsCurrLap = 0
            lastLap = -1
            lastTime = -1.0
            ac.setSize(appWindow, 200, 25)
        lastTime = currentTime
        lastSessonTime = currentSessonTime

        if lastLap < currentLap and currentTime > 0.05:
            # new lap
            bInvalidated = False
            noOutsCurrLap = 0
            lastLap = currentLap
            if noOuts>0:
                ac.setSize(appWindow, 200, 50)
            else:
                ac.setSize(appWindow, 200, 25)

        CurrNumberOfTyresOut = info.physics.numberOfTyresOut
        if CurrNumberOfTyresOut >= MaxNumberOfTyresOut:
            if not isOut:
                isOut = True
                noOuts += 1
                noOutsCurrLap += 1
                if currentLap>0:
                    ac.setSize(appWindow, 200, 75)
                else:
                    ac.setSize(appWindow, 200, 50)
            if not bInvalidated and currentCar==0: # only for ourself, not another car
                bInvalidated = True
                ac.ext_markLapAsSpoiled() # CSP function
            if CurrNumberOfTyresOut>1:
                ac.setTitle(appWindow," OFF track: " + str(CurrNumberOfTyresOut) + " wheels" + getAddenum(noOuts, currentLap) + getAddenum2(noOutsCurrLap, currentLap) ) # + "\n" + str(currentLap) + "\n" + str(currentTime))
            else:
                ac.setTitle(appWindow," OFF track: " + str(CurrNumberOfTyresOut) + " wheel"  + getAddenum(noOuts, currentLap) + getAddenum2(noOutsCurrLap, currentLap) ) # + "\n" + str(currentLap) + "\n" + str(currentTime))
        else:
            isOut = False
            addenum = ""
            if noOuts>0:
                addenum = "\n   " + str(noOuts) + " cut(s) already"
            ac.setTitle(appWindow," ON track" + getAddenum(noOuts, currentLap) + getAddenum2(noOutsCurrLap, currentLap) ) # + "\n" + str(currentLap) + "\n" + str(currentTime))

def acUpdate(deltaT):
    global timer, gOpacity
    timer += deltaT
    if timer > 0.05:
        timer = 0.0
        CheckOffTrack()
        ac.setBackgroundOpacity(appWindow, gOpacity)
        if gOpacity==0:
            ac.drawBorder(appWindow, 0)
        else:
            ac.drawBorder(appWindow, 1)

def acMain(ac_version):
    global appWindow, sAppError
    appWindow = ac.newApp("InvalidateLap")
    ac.setTitle(appWindow,"InvalidateLap")
    ac.setSize(appWindow, 200, 25)
    sAppError = ''
    try:
        sVerCode = ac.ext_patchVersionCode()
        if int(sVerCode)<=893: # version code for v0.1.36
            sAppError = str(ac.ext_patchVersion()) + ' CustomShadersPatch too old '
    except:
        sAppError = 'CustomShadersPatch not enabled or installed.'
    return "InvalidateLap"

def acShutdown(*args):
    pass
