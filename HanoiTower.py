import HanoiTower_Action as action
import time

# Global variables
originalStack = []
destinationStack = []
auxStack = []

# Calling functions of HanoiTower_Action
originalStack = action.appendNumbersOfOriginalStack()
action.printStateOfHanoiTower(True, originalStack, destinationStack, auxStack)
action.transferDisc(len(originalStack), originalStack, destinationStack, auxStack)