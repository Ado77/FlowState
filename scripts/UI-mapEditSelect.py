import bge
import traceback
import os
from os.path import isfile, join
logic = bge.logic
flowState = logic.flowState
render = bge.render
scene = logic.getCurrentScene()
cont = logic.getCurrentController()
owner = cont.owner
flowState = logic.flowState
UI = bge.UI
textColor = [1,1,1,1]
blockColor = [0,0,0.05,0.75]
mapButtons = []


if "window" not in owner:
    owner['window'] = UI.Window()

window = owner['window']

def mapSelectAction(key,mapName):
    scenes = logic.getSceneList()
    currentScene = logic.getCurrentScene()
    for scene in scenes:
        if(scene!=currentScene):
            scene.end()
    flowState.selectMap(mapName)
    flowState.setGameMode(flowState.GAME_MODE_SINGLE_PLAYER)
    flowState.setViewMode(flowState.VIEW_MODE_PLAY)
    currentScene.replace("Map Editor")

def multiplayerAction():
    pass

def settingsAction():
    bge.logic.sendMessage("cam2")
    currentScene = logic.getCurrentScene()
    currentScene.replace("UI-settings")

def backAction():
    currentScene = logic.getCurrentScene()
    sceneHistory = flowState.sceneHistory
    print(sceneHistory)
    backScene = sceneHistory[-2]
    removedScene = sceneHistory.pop(-1)
    removedScene = sceneHistory.pop(-1)
    print("removing scene "+str(removedScene))
    currentScene.replace(backScene)

def passAction():
    pass

def addMapButton(name,spacing):
    buttonIndex = len(mapButtons)
    height = 70-(buttonIndex*spacing)
    print(height)
    mapButtonBlock = UI.BoxElement(window,[50,height],5,0.5, blockColor, 1)
    mapButtonText = UI.TextElement(window,mapButtonBlock.position, textColor, 0,name)
    mapButton = UI.UIButton(mapButtonText,mapButtonBlock,mapSelectAction,"map",name)
    mapButtons.append(mapButton)

    owner['window'].add("mapButtonBlock"+name,mapButtonBlock)
    owner['window'].add("mapButtonText"+name,mapButtonText)
    owner['window'].add("mapButton"+name,mapButton)

def createMapAction():
    currentScene = logic.getCurrentScene()
    currentScene.replace("UI-map-name")

def importMapAction():
    currentScene = logic.getCurrentScene()
    currentScene.replace("UI-map-import-edit-select")

def createMapButton(name,spacing):
    buttonIndex = len(mapButtons)
    height = 70-(buttonIndex*spacing)
    print(height)
    mapButtonBlock = UI.BoxElement(window,[50,height],5,0.5, blockColor, 1)
    mapButtonText = UI.TextElement(window,mapButtonBlock.position, textColor, 0,name)
    mapButton = UI.UIButton(mapButtonText,mapButtonBlock,createMapAction,"map",name)
    mapButtons.append(mapButton)

    owner['window'].add("mapButtonBlock"+name,mapButtonBlock)
    owner['window'].add("mapButtonText"+name,mapButtonText)
    owner['window'].add("mapButton"+name,mapButton)

def importMapButton(name,spacing):
    buttonIndex = len(mapButtons)
    height = 70-(buttonIndex*spacing)
    print(height)
    mapButtonBlock = UI.BoxElement(window,[50,height],5,0.5, blockColor, 1)
    mapButtonText = UI.TextElement(window,mapButtonBlock.position, textColor, 0,name)
    mapButton = UI.UIButton(mapButtonText,mapButtonBlock,importMapAction,"map",name)
    mapButtons.append(mapButton)

    owner['window'].add("mapButtonBlock"+name,mapButtonBlock)
    owner['window'].add("mapButtonText"+name,mapButtonText)
    owner['window'].add("mapButton"+name,mapButton)


if(owner['init']!=True):
    flowState.setViewMode(flowState.VIEW_MODE_MENU)
    flowState.sceneHistory.append(logic.getCurrentScene().name)
    owner['init'] = True
    window = UI.Window()

    inset = 0.2

    headerBox = UI.BoxElement(window,[50,95],11,1, blockColor, 1)
    headerText = UI.TextElement(window,headerBox.position, textColor, 0, "SELECT MAP")
    blendPath = logic.expandPath("//")
    mapsPath = blendPath+"maps"+os.sep
    f = []
    maps = [f for f in os.listdir(mapsPath) if os.path.isfile(os.path.join(mapsPath, f))]
    maps.append("CREATE NEW")
    #maps = ["2018 Regional Final.fmp", "2018 Regional Qualifier.fmp", "custom.fmp"]
    spacing = 8

    for m in range(0,len(maps)-1):
        map = maps[m]
        addMapButton(map,spacing)

    importMapButton("IMPORT VD",spacing)
    createMapButton("CREATE NEW",spacing)

    itemNumber = len(mapButtons)
    mapListBox = UI.BoxElement(window,[50,50],5,((itemNumber)*spacing)/10, blockColor, 15)
    mapList = UI.UIList(mapListBox,mapButtons,1)

    #back button
    backBlockElement = UI.BoxElement(window,[10,10],1,.5, blockColor, 1)
    backText = UI.TextElement(window,backBlockElement.position, textColor, 0, "BACK")
    backButton = UI.UIButton(backText,backBlockElement,backAction)

    owner['window'].add("backBlockElement",backBlockElement)
    owner['window'].add("backText",backText)
    owner['window'].add("backButton",backButton)
    owner['window'].add("headerBox",headerBox)
    owner['window'].add("headerText",headerText)
    owner['window'].add("mapList",mapList)

else:
    try:
        #UI.run(cont)
        UI.runWindow(window,cont)
    except Exception as e:
        flowState.log(traceback.format_exc())
        owner['init'] = -1
