# Function that make the logic to solve the hanoi tower
def transferDisc(itemSize, originalStack, destinationStack, auxStack):
    if(itemSize > 0):
        transferDisc(itemSize - 1, originalStack, auxStack, destinationStack)
        destinationStack.append(originalStack.pop())
        printStateOfHanoiTower(False, originalStack, destinationStack, auxStack)
        transferDisc(itemSize - 1, auxStack, destinationStack, originalStack)


# Functions that print the states of the hanoi tower
def printStateOfHanoiTower(isInitialStatus, originalStack, destinationStack, auxStack):
    if (isInitialStatus):
        print("Estado inicial")
    else:
        print("Estado Atual")

    print("------")
    print("Original: " + str(originalStack))
    print("Destination: " + str(destinationStack))
    print("Aux: " + str(auxStack))
    print("\n")

# Function that return the discs in the hanoi tower
def appendNumbersOfOriginalStack():
    newOriginalStack = []
    numOfItems = input("Type the count of discs of the Hanoi tower:\n")
    numOfItems = int(numOfItems)
    while numOfItems > 0: 
        newOriginalStack.append(numOfItems)
        numOfItems -= 1
    return newOriginalStack