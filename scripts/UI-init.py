import bge
import traceback
logic = bge.logic
render = bge.render
render.showMouse(1)
scene = logic.getCurrentScene()
cont = logic.getCurrentController()
owner = cont.owner
flowState = logic.flowState
UI = bge.UI
textColor = [1,1,1,1]
blockColor = [0,0,0.05,0.75]
flowState = logic.flowState

def beginnerAction():
    logic.flowState.setEasyDefaults()
    proceedAction()

def proAction():
    proceedAction()

def proceedAction():
    currentScene = logic.getCurrentScene()
    currentScene.replace("Menu Background")


def quitGameAction():
    logic.endGame()



if(owner['init']!=True):
    owner['init'] = True
    window = UI.Window()

    inset = 0.2


    if(flowState.isFirstRun()):
        welcomeText = UI.TextElement(window,[50+inset,70], textColor, 0, "Welcome to the Flow State drone racing simulator!")
        welcomeText = UI.TextElement(window,[50+inset,60], textColor, 0, "What type of controller do you have?")
        beginnerBlockElement = UI.BoxElement(window,[30,30],3,2.5, blockColor, 1)
        beginnerText = UI.TextElement(window,beginnerBlockElement.position, textColor, 0, "Game Controller")
        beginnerButton = UI.UIButton(beginnerText,beginnerBlockElement,beginnerAction)

        beginnerBlockElement = UI.BoxElement(window,[70,30],3,2.5, blockColor, 1)
        beginnerText = UI.TextElement(window,beginnerBlockElement.position, textColor, 0, "RC Radio")
        beginnerButton = UI.UIButton(beginnerText,beginnerBlockElement,proAction)
    else:
        multiplayerGameText = UI.TextElement(window,[10+inset,10], textColor, 0, "Loading...")
        proceedAction()
else:
    UI.run(cont)
    try:
        UI.run(cont)
    except Exception as e:
        logic.flowState.error(traceback.format_exc())
        owner['init'] = -1
