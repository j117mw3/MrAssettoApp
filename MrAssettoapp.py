import ac
import acsys
#YouTube:   https://www.youtube.com/@Mr.Assetto
#Git:   https://github.com/j117mw3/Mr.Assetto-Server-Manager/releases
#Patreon:    https://www.patreon.com/GodsAssettoCorsaServerManager
#Discord:   https://discord.gg/59hS5e5zua
appWindow = 0
textInput = 0
lastMessageLabel = 0
buttonMorning = 0
buttonNoon = 0
buttonAfternoon = 0
buttonNight = 0
WeatherId = 0 
buttonIgnoreMissingCarChecksums = 0
buttonIgnoreMissingTrackParams = 0
buttonIgnoreWrongServerDetails = 0
buttonIgnoreUnsafeAdminWhitelist = 0
playerInfoArea = 0
buttonStates = {}
#There is def a better way to code these but holy shit assetto is sensitive to slight changes. Might have something to do with whatever python version they are running. Anywho, if you have sugestions for the code and wish to show me please do.
def acMain(ac_version):
    global textInput, appWindow, playerInfoArea, lastMessageLabel, buttonMorning, buttonNoon, buttonAfternoon, buttonNight, buttonPrevWeather, buttonNextWeather, WeatherId, buttonExtra1, buttonExtra2, buttonExtra3, buttonExtra4, buttonEnabledAI, buttonNew1, buttonNew2, buttonNew3, playerRadiusLabel, playerRadiusInput, button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, textInput1, textInput2, textInput3,textInput4, textInput5, textInput6, textInput7, textInput8, textInput9, textInput10, textInput11, buttonIgnoreMissingCarChecksums, buttonIgnoreMissingTrackParams, buttonIgnoreWrongServerDetails, buttonIgnoreUnsafeAdminWhitelist
    appWindow = ac.newApp("MrAssetto Server Manager App")
    ac.setSize(appWindow, 400, 580)

    # Initialize button states
    global buttonStates
    buttonStates = {
        'extra1': False,
        'extra2': False,
        'extra3': False,
        'extra4': False,
        'enabledAI': False,
        'new1': False,
        'new2': False,
        'new3': False,
        'ignoreMissingCarChecksums': False,
        'ignoreMissingTrackParams': False,
        'ignoreWrongServerDetails': False,
        'ignoreUnsafeAdminWhitelist': False
    }

    # Create header and buttons
    timeHeader = ac.addLabel(appWindow, "Time")
    ac.setPosition(timeHeader, 10, 30)
    ac.setFontSize(timeHeader, 24)
    
    buttonMorning = ac.addButton(appWindow, "Morning")
    ac.setPosition(buttonMorning, 10, 70)
    ac.setSize(buttonMorning, 90, 30)
    ac.addOnClickedListener(buttonMorning, onButtonMorningClick)

    buttonNoon = ac.addButton(appWindow, "Noon")
    ac.setPosition(buttonNoon, 105, 70)
    ac.setSize(buttonNoon, 90, 30)
    ac.addOnClickedListener(buttonNoon, onButtonNoonClick)

    buttonAfternoon = ac.addButton(appWindow, "Afternoon")
    ac.setPosition(buttonAfternoon, 200, 70)
    ac.setSize(buttonAfternoon, 90, 30)
    ac.addOnClickedListener(buttonAfternoon, onButtonAfterNoonClick)

    buttonNight = ac.addButton(appWindow, "Night")
    ac.setPosition(buttonNight, 295, 70)
    ac.setSize(buttonNight, 90, 30)
    ac.addOnClickedListener(buttonNight, onButtonNightClick)  

    # Weather header and buttons
    weatherHeader = ac.addLabel(appWindow, "Weather")
    ac.setPosition(weatherHeader, 10, 100)
    ac.setFontSize(weatherHeader, 24)

    # Create weather control buttons
    buttonPrevWeather = ac.addButton(appWindow, "Previous Weather")
    ac.setPosition(buttonPrevWeather, 10, 140)
    ac.setSize(buttonPrevWeather, 150, 30)
    ac.addOnClickedListener(buttonPrevWeather, onButtonPrevWeatherClick)
    
    buttonNextWeather = ac.addButton(appWindow, "Next Weather")
    ac.setPosition(buttonNextWeather, 235, 140)
    ac.setSize(buttonNextWeather, 150, 30) 
    ac.addOnClickedListener(buttonNextWeather, onButtonNextWeatherClick)

    # Weather Id Text Field
    WeatherId = ac.addTextInput(appWindow, "0")
    ac.setPosition(WeatherId, 167, 140)
    ac.setSize(WeatherId, 60, 30)
    ac.setText(WeatherId, "0")

    # Extra Header
    ExtrasHeader = ac.addLabel(appWindow, "Extras")
    ac.setPosition(ExtrasHeader, 10, 170)
    ac.setFontSize(ExtrasHeader, 24)

    # Extra Buttons
    buttonExtra1 = ac.addButton(appWindow, "Anti AFK")
    ac.setFontSize(buttonExtra1, 12)  # Smaller font size for extra buttons
    ac.setPosition(buttonExtra1, 10, 210)
    ac.setSize(buttonExtra1, 90, 30)
    ac.addOnClickedListener(buttonExtra1, onButtonExtra1Click)

    buttonExtra2 = ac.addButton(appWindow, "Force Lights")
    ac.setFontSize(buttonExtra2, 12)
    ac.setPosition(buttonExtra2, 105, 210)
    ac.setSize(buttonExtra2, 90, 30)
    ac.addOnClickedListener(buttonExtra2, onButtonExtra2Click)

    buttonExtra3 = ac.addButton(appWindow, "Custom Update")
    ac.setFontSize(buttonExtra3, 12)
    ac.setPosition(buttonExtra3, 200, 210)
    ac.setSize(buttonExtra3, 90, 30)
    ac.addOnClickedListener(buttonExtra3, onButtonExtra3Click)

    buttonExtra4 = ac.addButton(appWindow, "Weather FX")
    ac.setFontSize(buttonExtra4, 12)
    ac.setPosition(buttonExtra4, 295, 210)
    ac.setSize(buttonExtra4, 90, 30)
    ac.addOnClickedListener(buttonExtra4, onButtonExtra4Click)

    buttonEnabledAI = ac.addButton(appWindow, "AI Debug")
    ac.setFontSize(buttonEnabledAI, 12)
    ac.setPosition(buttonEnabledAI, 10, 250)
    ac.setSize(buttonEnabledAI, 90, 30)
    ac.addOnClickedListener(buttonEnabledAI, onButtonEnabledAIClick)

    # New buttons setup
    buttonNew1 = ac.addButton(appWindow, "Hide AiCars")
    ac.setFontSize(buttonNew1, 12)
    ac.setPosition(buttonNew1, 105, 250)
    ac.setSize(buttonNew1, 90, 30)
    ac.addOnClickedListener(buttonNew1, onButtonNew1Click)

    buttonNew2 = ac.addButton(appWindow, "TwoWay Traffic")
    ac.setFontSize(buttonNew2, 12)
    ac.setPosition(buttonNew2, 200, 250)
    ac.setSize(buttonNew2, 90, 30)
    ac.addOnClickedListener(buttonNew2, onButtonNew2Click)

    buttonNew3 = ac.addButton(appWindow, "Smooth Camber")
    ac.setFontSize(buttonNew3, 12)
    ac.setPosition(buttonNew3, 295, 250)
    ac.setSize(buttonNew3, 90, 30)
    ac.addOnClickedListener(buttonNew3, onButtonNew3Click)

    playerRadiusLabel = ac.addButton(appWindow, "PlayerRadius")
    ac.setPosition(playerRadiusLabel, 10, 290)  # Below the last row of extra buttons
    ac.setSize(playerRadiusLabel, 130, 20)
    ac.setFontSize(playerRadiusLabel, 12)
    ac.addOnClickedListener(playerRadiusLabel, onPlayerRadiusLabelClick)

    playerRadiusInput = ac.addTextInput(appWindow, "")
    ac.setPosition(playerRadiusInput, 150, 290)  # Position right next to the label
    ac.setSize(playerRadiusInput, 40, 20)
    
    button1 = ac.addButton(appWindow, "TrafficDensity")
    ac.setPosition(button1, 10, 320)
    ac.setSize(button1, 130, 20)
    ac.setFontSize(button1, 12)
    ac.addOnClickedListener(button1, onButtonTrafficDensityClick)

    textInput1 = ac.addTextInput(appWindow, "")
    ac.setPosition(textInput1, 150, 320)
    ac.setSize(textInput1, 40, 20)

    # Button 2 and TextInput 2
    button2 = ac.addButton(appWindow, "MinSpawnDistancePoints")
    ac.setPosition(button2, 10, 350)
    ac.setSize(button2, 130, 20)
    ac.setFontSize(button2, 11)
    ac.addOnClickedListener(button2, onButtonMinSpawnDistancePointsClick)

    textInput2 = ac.addTextInput(appWindow, "")
    ac.setPosition(textInput2, 150, 350)
    ac.setSize(textInput2, 40, 20)

    # Button 3 and TextInput 3
    button3 = ac.addButton(appWindow, "MaxSpawnDistancePoints")
    ac.setPosition(button3, 10, 380)
    ac.setSize(button3, 130, 20)
    ac.setFontSize(button3, 11)
    ac.addOnClickedListener(button3, onButtonMaxSpawnDistancePointsClick)

    textInput3 = ac.addTextInput(appWindow, "")
    ac.setPosition(textInput3, 150, 380)
    ac.setSize(textInput3, 40, 20)

    # Button 4 and TextInput 4
    button4 = ac.addButton(appWindow, "MinAiSafetyDistance")
    ac.setPosition(button4, 10, 410)
    ac.setSize(button4, 130, 20)
    ac.setFontSize(button4, 11)
    ac.addOnClickedListener(button4, onButtonMinAiSafetyDistanceClick)

    textInput4 = ac.addTextInput(appWindow, "")
    ac.setPosition(textInput4, 150, 410)
    ac.setSize(textInput4, 40, 20)

    # Button 5 and TextInput 5
    button5 = ac.addButton(appWindow, "MaxAiSafetyDistance")
    ac.setPosition(button5, 10, 440)
    ac.setSize(button5, 130, 20)
    ac.setFontSize(button5, 11)
    ac.addOnClickedListener(button5, onButtonMaxAiSafetyDistanceClick)

    textInput5 = ac.addTextInput(appWindow, "")
    ac.setPosition(textInput5, 150, 440)
    ac.setSize(textInput5, 40, 20)

    # Button 6 and TextInput 6
    button6 = ac.addButton(appWindow, "StateSpawnDistance")
    ac.setPosition(button6, 200, 290)
    ac.setSize(button6, 130, 20)
    ac.setFontSize(button6, 11)
    ac.addOnClickedListener(button6, onButtonStateSpawnDistanceClick)

    textInput6 = ac.addTextInput(appWindow, "")
    ac.setPosition(textInput6, 340, 290)
    ac.setSize(textInput6, 40, 20)

    # Button 7 and TextInput 7
    button7 = ac.addButton(appWindow, "MinStateDistance")
    ac.setPosition(button7, 200, 320)
    ac.setSize(button7, 130, 20)
    ac.setFontSize(button7, 12)
    ac.addOnClickedListener(button7, onButtonMinStateDistanceClick)

    textInput7 = ac.addTextInput(appWindow, "")
    ac.setPosition(textInput7, 340, 320)
    ac.setSize(textInput7, 40, 20)

    # Button 8 and TextInput 8
    button8 = ac.addButton(appWindow, "MaxAiTargetCount")
    ac.setPosition(button8, 200, 350)
    ac.setSize(button8, 130, 20)
    ac.setFontSize(button8, 12)
    ac.addOnClickedListener(button8, onButtonMaxAiTargetCountClick)

    textInput8 = ac.addTextInput(appWindow, "")
    ac.setPosition(textInput8, 340, 350)
    ac.setSize(textInput8, 40, 20)

    # Button 9 and TextInput 9
    button9 = ac.addButton(appWindow, "AiPerPlayerTargetCount")
    ac.setPosition(button9, 200, 380)
    ac.setSize(button9, 130, 20)
    ac.setFontSize(button9, 11)
    ac.addOnClickedListener(button9, onButtonAiPerPlayerTargetCountClick)

    textInput9 = ac.addTextInput(appWindow, "")
    ac.setPosition(textInput9, 340, 380)
    ac.setSize(textInput9, 40, 20)

    # Button 10 and TextInput 10
    button10 = ac.addButton(appWindow, "MaxSpeedKph")
    ac.setPosition(button10, 200, 410)
    ac.setSize(button10, 130, 20)
    ac.setFontSize(button10, 12)
    ac.addOnClickedListener(button10, onButtonMaxSpeedKphClick)

    textInput10 = ac.addTextInput(appWindow, "")
    ac.setPosition(textInput10, 340, 410)
    ac.setSize(textInput10, 40, 20)

    # Button 11 and TextInput 11
    button11 = ac.addButton(appWindow, "RightLaneOffsetKph")
    ac.setPosition(button11, 200, 440)
    ac.setSize(button11, 130, 20)
    ac.setFontSize(button11, 11)
    ac.addOnClickedListener(button11, onButtonRightLaneOffsetKphClick)

    textInput11 = ac.addTextInput(appWindow, "")
    ac.setPosition(textInput11, 340, 440)
    ac.setSize(textInput11, 40, 20)

    buttonIgnoreMissingCarChecksums = ac.addButton(appWindow, "MissingCarChecksums")
    ac.setFontSize(buttonIgnoreMissingCarChecksums, 12)
    ac.setPosition(buttonIgnoreMissingCarChecksums, 10, 470)
    ac.setSize(buttonIgnoreMissingCarChecksums, 185, 20)
    ac.addOnClickedListener(buttonIgnoreMissingCarChecksums, onButtonIgnoreMissingCarChecksumsClick)

    buttonIgnoreMissingTrackParams = ac.addButton(appWindow, "MissingTrackParams")
    ac.setFontSize(buttonIgnoreMissingTrackParams, 12)
    ac.setPosition(buttonIgnoreMissingTrackParams, 200, 470)
    ac.setSize(buttonIgnoreMissingTrackParams, 185, 20)
    ac.addOnClickedListener(buttonIgnoreMissingTrackParams, onButtonIgnoreMissingTrackParamsClick)

    buttonIgnoreWrongServerDetails = ac.addButton(appWindow, "WrongServerDetails")
    ac.setFontSize(buttonIgnoreWrongServerDetails, 12)
    ac.setPosition(buttonIgnoreWrongServerDetails, 10, 500)
    ac.setSize(buttonIgnoreWrongServerDetails, 185, 20)
    ac.addOnClickedListener(buttonIgnoreWrongServerDetails, onButtonIgnoreWrongServerDetailsClick)

    buttonIgnoreUnsafeAdminWhitelist = ac.addButton(appWindow, "UnsafeAdminWhitelist")
    ac.setFontSize(buttonIgnoreUnsafeAdminWhitelist, 12)
    ac.setPosition(buttonIgnoreUnsafeAdminWhitelist, 200, 500)
    ac.setSize(buttonIgnoreUnsafeAdminWhitelist, 185, 20)
    ac.addOnClickedListener(buttonIgnoreUnsafeAdminWhitelist, onButtonIgnoreUnsafeAdminWhitelistClick)

    # Chat functionality
    lastMessageLabel = ac.addLabel(appWindow, "Chat:")
    ac.setPosition(lastMessageLabel, 10, 525)

    textInput = ac.addTextInput(appWindow, "")
    ac.setPosition(textInput, 10, 550)
    ac.setSize(textInput, 380, 20)
    ac.addOnValidateListener(textInput, onValidateListener)
    
    return "MrAssetto Server Manager App"

def onButtonIgnoreMissingCarChecksumsClick(*args):
    global buttonIgnoreMissingCarChecksums, textInput
    current_state = buttonStates['extra2']
    if current_state:
        ac.setText(textInput, "/set Extra.IgnoreConfigurationErrors.MissingCarChecksums false")
    else:
        ac.setText(textInput, "/set Extra.IgnoreConfigurationErrors.MissingCarChecksums true")
    onValidateListener(None)
    toggleButtonState('extra2', buttonIgnoreMissingCarChecksums)
    ac.console("Force Lights toggled to {}".format("enabled" if not current_state else "disabled"))

def onButtonIgnoreMissingTrackParamsClick(*args):
    global buttonIgnoreMissingTrackParams, textInput
    current_state = buttonStates['extra2']
    if current_state:
        ac.setText(textInput, "/set Extra.IgnoreConfigurationErrors.MissingTrackParams false")
    else:
        ac.setText(textInput, "/set Extra.IgnoreConfigurationErrors.MissingTrackParams true")
    onValidateListener(None)
    toggleButtonState('extra2', buttonIgnoreMissingTrackParams)
    ac.console("Force Lights toggled to {}".format("enabled" if not current_state else "disabled"))

def onButtonIgnoreWrongServerDetailsClick(*args):
    global buttonIgnoreWrongServerDetails, textInput
    current_state = buttonStates['extra2']
    if current_state:
        ac.setText(textInput, "/set Extra.IgnoreConfigurationErrors.WrongServerDetails false")
    else:
        ac.setText(textInput, "/set Extra.IgnoreConfigurationErrors.WrongServerDetails true")
    onValidateListener(None)
    toggleButtonState('extra2', buttonIgnoreWrongServerDetails)
    ac.console("Force Lights toggled to {}".format("enabled" if not current_state else "disabled"))

def onButtonIgnoreUnsafeAdminWhitelistClick(*args):
    global buttonIgnoreUnsafeAdminWhitelist, textInput
    current_state = buttonStates['extra2']
    if current_state:
        ac.setText(textInput, "/set Extra.IgnoreConfigurationErrors.UnsafeAdminWhitelist false")
    else:
        ac.setText(textInput, "/set Extra.IgnoreConfigurationErrors.UnsafeAdminWhitelist true")
    onValidateListener(None)
    toggleButtonState('extra2', buttonIgnoreUnsafeAdminWhitelist)
    ac.console("Force Lights toggled to {}".format("enabled" if not current_state else "disabled"))    


def onButtonTrafficDensityClick(*args):
    global textInput1, textInput
    try:
        value = ac.getText(textInput1)
        if value:
            command = "/set Extra.AiParams.TrafficDensity " + value
            ac.setText(textInput, command)
            onValidateListener(None)  # Trigger message sending as if Enter was pressed
            ac.console("Traffic Density set to: " + value)
        else:
            ac.console("Traffic Density input is empty")
    except Exception as e:
        ac.log("Error handling Traffic Density button click: " + str(e))
        ac.console("Error handling Traffic Density button click: " + str(e))

def onButtonMinSpawnDistancePointsClick(*args):
    global textInput2, textInput
    try:
        value = ac.getText(textInput2)
        if value:
            command = "/set Extra.AiParams.MinSpawnDistancePoints " + value
            ac.setText(textInput, command)
            onValidateListener(None)  # Trigger message sending as if Enter was pressed
            ac.console("Min Spawn Distance Points set to: " + value)
        else:
            ac.console("Min Spawn Distance Points input is empty")
    except Exception as e:
        ac.log("Error handling Min Spawn Distance Points button click: " + str(e))
        ac.console("Error handling Min Spawn Distance Points button click: " + str(e))

def onButtonMaxSpawnDistancePointsClick(*args):
    global textInput3, textInput
    try:
        value = ac.getText(textInput3)
        if value:
            command = "/set Extra.AiParams.MaxSpawnDistancePoints " + value
            ac.setText(textInput, command)
            onValidateListener(None)  # Trigger message sending as if Enter was pressed
            ac.console("Max Spawn Distance Points set to: " + value)
        else:
            ac.console("Max Spawn Distance Points input is empty")
    except Exception as e:
        ac.log("Error handling Max Spawn Distance Points button click: " + str(e))
        ac.console("Error handling Max Spawn Distance Points button click: " + str(e))

def onButtonMinAiSafetyDistanceClick(*args):
    global textInput4, textInput
    try:
        value = ac.getText(textInput4)
        if value:
            command = "/set Extra.AiParams.MinAiSafetyDistanceMeters " + value
            ac.setText(textInput, command)
            onValidateListener(None)  # Trigger message sending as if Enter was pressed
            ac.console("Min AI Safety Distance set to: " + value)
        else:
            ac.console("Min AI Safety Distance input is empty")
    except Exception as e:
        ac.log("Error handling Min AI Safety Distance button click: " + str(e))
        ac.console("Error handling Min AI Safety Distance button click: " + str(e))

def onButtonMaxAiSafetyDistanceClick(*args):
    global textInput5, textInput
    try:
        value = ac.getText(textInput5)
        if value:
            command = "/set Extra.AiParams.MaxAiSafetyDistanceMeters " + value
            ac.setText(textInput, command)
            onValidateListener(None)  # Trigger message sending as if Enter was pressed
            ac.console("Max AI Safety Distance set to: " + value)
        else:
            ac.console("Max AI Safety Distance input is empty")
    except Exception as e:
        ac.log("Error handling Max AI Safety Distance button click: " + str(e))
        ac.console("Error handling Max AI Safety Distance button click: " + str(e))

def onButtonStateSpawnDistanceClick(*args):
    global textInput6, textInput
    try:
        value = ac.getText(textInput6)
        if value:
            command = "/set Extra.AiParams.StateSpawnDistanceMeters " + value
            ac.setText(textInput, command)
            onValidateListener(None)  # Trigger message sending as if Enter was pressed
            ac.console("State Spawn Distance set to: " + value)
        else:
            ac.console("State Spawn Distance input is empty")
    except Exception as e:
        ac.log("Error handling State Spawn Distance button click: " + str(e))
        ac.console("Error handling State Spawn Distance button click: " + str(e))

def onButtonMinStateDistanceClick(*args):
    global textInput7, textInput
    try:
        value = ac.getText(textInput7)
        if value:
            command = "/set Extra.AiParams.MinStateDistanceMeters " + value
            ac.setText(textInput, command)
            onValidateListener(None)  # Trigger message sending as if Enter was pressed
            ac.console("Min State Distance set to: " + value)
        else:
            ac.console("Min State Distance input is empty")
    except Exception as e:
        ac.log("Error handling Min State Distance button click: " + str(e))
        ac.console("Error handling Min State Distance button click: " + str(e))

def onButtonMaxAiTargetCountClick(*args):
    global textInput8, textInput
    try:
        value = ac.getText(textInput8)
        if value:
            command = "/set Extra.AiParams.MaxAiTargetCount " + value
            ac.setText(textInput, command)
            onValidateListener(None)  # Trigger message sending as if Enter was pressed
            ac.console("Max AI Target Count set to: " + value)
        else:
            ac.console("Max AI Target Count input is empty")
    except Exception as e:
        ac.log("Error handling Max AI Target Count button click: " + str(e))
        ac.console("Error handling Max AI Target Count button click: " + str(e))

def onButtonAiPerPlayerTargetCountClick(*args):
    global textInput9, textInput
    try:
        value = ac.getText(textInput9)
        if value:
            command = "/set Extra.AiParams.AiPerPlayerTargetCount " + value
            ac.setText(textInput, command)
            onValidateListener(None)  # Trigger message sending as if Enter was pressed
            ac.console("AI Per Player Target Count set to: " + value)
        else:
            ac.console("AI Per Player Target Count input is empty")
    except Exception as e:
        ac.log("Error handling AI Per Player Target Count button click: " + str(e))
        ac.console("Error handling AI Per Player Target Count button click: " + str(e))

def onButtonMaxSpeedKphClick(*args):
    global textInput10, textInput
    try:
        value = ac.getText(textInput10)
        if value:
            command = "/set Extra.AiParams.MaxSpeedKph " + value
            ac.setText(textInput, command)
            onValidateListener(None)  # Trigger message sending as if Enter was pressed
            ac.console("Max Speed (Kph) set to: " + value)
        else:
            ac.console("Max Speed (Kph) input is empty")
    except Exception as e:
        ac.log("Error handling Max Speed (Kph) button click: " + str(e))
        ac.console("Error handling Max Speed (Kph) button click: " + str(e))

def onButtonRightLaneOffsetKphClick(*args):
    global textInput11, textInput
    try:
        value = ac.getText(textInput11)
        if value:
            command = "/set Extra.AiParams.RightLaneOffsetKph " + value
            ac.setText(textInput, command)
            onValidateListener(None)  # Trigger message sending as if Enter was pressed
            ac.console("Right Lane Offset (Kph) set to: " + value)
        else:
            ac.console("Right Lane Offset (Kph) input is empty")
    except Exception as e:
        ac.log("Error handling Right Lane Offset (Kph) button click: " + str(e))
        ac.console("Error handling Right Lane Offset (Kph) button click: " + str(e))

def onPlayerRadiusLabelClick(*args):
    global playerRadiusInput, textInput
    try:
        radius = ac.getText(playerRadiusInput)
        if radius:
            command = "/set Extra.AiParams.PlayerRadiusMeters " + radius
            ac.setText(textInput, command)
            onValidateListener(None)  # Trigger message sending as if Enter was pressed
            ac.console("Player radius set to: " + radius)
        else:
            ac.console("Player radius input is empty")
    except Exception as e:
        ac.log("Error handling player radius button click: " + str(e))
        ac.console("Error handling player radius button click: " + str(e))

def onButtonMorningClick(*args):
    try:
        global textInput
        ac.setText(textInput, "/settime 6:00")
        onValidateListener(None)  # Trigger message sending as if Enter was pressed
        ac.console("Button clicked, set time to 6:00")
    except Exception as e:
        ac.log("Error handling button click: " + str(e))
        ac.console("Error handling button click: " + str(e))

def onButtonNoonClick(*args):
    try:
        global textInput
        ac.setText(textInput, "/settime 12:00")
        onValidateListener(None)  # Trigger message sending as if Enter was pressed
        ac.console("Button clicked, set time to 12:00")
    except Exception as e:
        ac.log("Error handling button click: " + str(e))
        ac.console("Error handling button click: " + str(e))

def onButtonAfterNoonClick(*args):
    try:
        global textInput
        ac.setText(textInput, "/settime 18:00")
        onValidateListener(None)  # Trigger message sending as if Enter was pressed
        ac.console("Button clicked, set time to 18:00")
    except Exception as e:
        ac.log("Error handling button click: " + str(e))
        ac.console("Error handling button click: " + str(e))

def onButtonNightClick(*args):
    try:
        global textInput
        ac.setText(textInput, "/settime 23:59")
        onValidateListener(None)  # Trigger message sending as if Enter was pressed
        ac.console("Button clicked, set time to 23:59")
    except Exception as e:
        ac.log("Error handling button click: " + str(e))
        ac.console("Error handling button click: " + str(e))

def onButtonNextWeatherClick(*args):
    global WeatherId, textInput
    try:
        currentWeatherId = int(ac.getText(WeatherId))
        currentWeatherId += 1
        ac.setText(WeatherId, str(currentWeatherId))
        ac.setText(textInput, "/setcspweather " + str(currentWeatherId) + " 0")
        onValidateListener(None)  # Trigger message sending as if Enter was pressed
        ac.console("Button clicked, set weather to ID " + str(currentWeatherId))
    except Exception as e:
        ac.log("Error handling button click: " + str(e))
        ac.console("Error handling button click: " + str(e))

def onButtonPrevWeatherClick(*args):
    global WeatherId, textInput
    try:
        currentWeatherId = int(ac.getText(WeatherId))
        currentWeatherId -= 1
        if currentWeatherId < 0:
            currentWeatherId = 0
        ac.setText(WeatherId, str(currentWeatherId))
        ac.setText(textInput, "/setcspweather " + str(currentWeatherId)+ " 0")
        onValidateListener(None)  # Trigger message sending as if Enter was pressed
        ac.console("Button clicked, set weather to ID " + str(currentWeatherId))
    except Exception as e:
        ac.log("Error handling button click: " + str(e))
        ac.console("Error handling button click: " + str(e))

# Button click event handlers
def onButtonExtra1Click(*args):
    global buttonExtra1, textInput
    current_state = buttonStates['extra1']
    if current_state:
        # If currently active, deactivate it
        ac.setText(textInput, "/set Extra.EnableAntiAfk false")
        onValidateListener(None)  # Send command as if Enter was pressed
        ac.console("Anti AFK disabled")
    else:
        # If currently inactive, activate it
        ac.setText(textInput, "/set Extra.EnableAntiAfk true")
        onValidateListener(None)  # Send command as if Enter was pressed
        ac.console("Anti AFK enabled")
    
    # Toggle the state after sending the command
    toggleButtonState('extra1', buttonExtra1)

def onButtonExtra2Click(*args):
    global buttonExtra2, textInput
    current_state = buttonStates['extra2']
    if current_state:
        ac.setText(textInput, "/set Extra.ForceLights false")
    else:
        ac.setText(textInput, "/set Extra.ForceLights true")
    onValidateListener(None)
    toggleButtonState('extra2', buttonExtra2)
    ac.console("Force Lights toggled to {}".format("enabled" if not current_state else "disabled"))

def onButtonExtra3Click(*args):
    global buttonExtra3, textInput
    current_state = buttonStates['extra3']
    if current_state:
        ac.setText(textInput, "/set Extra.EnableCustomUpdate false")
    else:
        ac.setText(textInput, "/set Extra.EnableCustomUpdate true")
    onValidateListener(None)
    toggleButtonState('extra3', buttonExtra3)
    ac.console("Real Time toggled to {}".format("enabled" if not current_state else "disabled"))

def onButtonExtra4Click(*args):
    global buttonExtra4, textInput
    current_state = buttonStates['extra4']
    if current_state:
        ac.setText(textInput, "/set Extra.EnableWeatherFx false")
    else:
        ac.setText(textInput, "/set Extra.EnableWeatherFx true")
    onValidateListener(None)
    toggleButtonState('extra4', buttonExtra4)
    ac.console("Weather FX toggled to {}".format("enabled" if not current_state else "disabled"))

def onButtonEnabledAIClick(*args):
    global buttonEnabledAI, textInput
    current_state = buttonStates['enabledAI']
    if current_state:
        ac.setText(textInput, "/set Extra.AiParams.Debug false")
    else:
        ac.setText(textInput, "/set Extra.AiParams.Debug true")
    onValidateListener(None)
    toggleButtonState('enabledAI', buttonEnabledAI)
    ac.console("AI Enabled toggled to {}".format("enabled" if not current_state else "disabled"))

def onButtonNew1Click(*args):
    global buttonNew1, textInput
    current_state = buttonStates['new1']
    command = "/set Extra.AiParams.HideAiCars true" if not current_state else "/set Extra.AiParams.HideAiCars false"
    ac.setText(textInput, command)
    onValidateListener(None)
    toggleButtonState('new1', buttonNew1)
    ac.console("Hide AI Cars toggled to {}".format("enabled" if not current_state else "disabled"))

def onButtonNew2Click(*args):
    global buttonNew2, textInput
    current_state = buttonStates['new2']
    command = "/set Extra.AiParams.TwoWayTraffic true" if not current_state else "/set Extra.AiParams.TwoWayTraffic false"
    ac.setText(textInput, command)
    onValidateListener(None)
    toggleButtonState('new2', buttonNew2)
    ac.console("Two-Way Traffic toggled to {}".format("enabled" if not current_state else "disabled"))

def onButtonNew3Click(*args):
    global buttonNew3, textInput
    current_state = buttonStates['new3']
    command = "/set Extra.AiParams.SmoothCamber true" if not current_state else "/set Extra.AiParams.SmoothCamber false"
    ac.setText(textInput, command)
    onValidateListener(None)
    toggleButtonState('new3', buttonNew3)
    ac.console("Smooth Camber toggled to {}".format("enabled" if not current_state else "disabled"))

# Utility function to toggle button appearance
def toggleButtonState(buttonKey, button):
    global buttonStates
    buttonStates[buttonKey] = not buttonStates[buttonKey]
    if buttonStates[buttonKey]:
        ac.setBackgroundColor(button, 0.5, 1, 0.5)  # Normal background
        ac.setBackgroundOpacity(button, 0.3)   # Normal opacity
    else:
        ac.setBackgroundColor(button, 1, 0.5, 0.5)  # Highlight color
        ac.setBackgroundOpacity(button, 1)           # Highlight opacity
       
def onChatMessage(message, author):
    global lastMessageLabel, WeatherId
    completeMessage = "{} : {}".format(author, message)
    ac.setText(lastMessageLabel, completeMessage)

def onValidateListener(_):
    global textInput, lastMessageLabel
    text = ac.getText(textInput)
    ac.setText(textInput, "")  # Clear the input to mimic message sending
    ac.setFocus(textInput, 1)
    ac.sendChatMessage(text)
    ac.setText(lastMessageLabel, "You: " + text)  # Display sent message in the app

def acUpdate(deltaT):
    pass

def acShutdown():
    pass