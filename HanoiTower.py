import HanoiTower_Action as action

# Global variables
originalStack = []
destinationStack = []
auxStack = []

# Calling functions of HanoiTower_Action
originalStack = action.appendNumbersOfOriginalStack()
action.transferDisc(len(originalStack), originalStack, destinationStack, auxStack)



