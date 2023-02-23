import time

# Function that make the logic to solve the hanoi tower
def transferDisc(itemSize, originalStack, destinationStack, auxStack):
    if(itemSize > 0):
        transferDisc(itemSize - 1, originalStack, auxStack, destinationStack)
        destinationStack.append(originalStack.pop())
        time.sleep(0.001)
        print("------")
        print("Original: " + str(originalStack))
        print("Destination: " + str(destinationStack))
        print("Aux: " + str(auxStack))
        transferDisc(itemSize - 1, auxStack, destinationStack, originalStack)

# Function that return the discs in the hanoi tower
def appendNumbersOfOriginalStack():
    newOriginalStack = []
    numOfItems = input("Type the count of discs of the Hanoi tower:\n")
    numOfItems = int(numOfItems)
    while numOfItems > 0: 
        newOriginalStack.append(numOfItems)
        numOfItems -= 1
    return newOriginalStack