import copy
import os
import sys

def readMap(path):
    bigMap = []
    with open(path, "r") as f:
        for line in f:
            bigMap.append([int(x) for x in line.strip().split(",")])
    print("==========Analyzing this map===========")
    for line in bigMap:
        for num in line:
            print("%3d " % num, end="")
        print()
    print("=======================================")
    return bigMap

def pickMinRoteValue(roteValue, y, x):
    numbers = []
    idx = 0
    if 0 < y:
        numbers.append(roteValue[y-1][x][2])
    if 0 < x:
        numbers.append(roteValue[y][x-1][0])
    if 0 < x and 0 < y:
        numbers.append(roteValue[y-1][x-1][1])
    numbers = [x for x in numbers if x != None]
    return min(numbers)


def calcRoteValue(bigMap):
    roteValue = []
    for y in range(len(bigMap)):
        roteValue.append([])
        for x in range(len(bigMap[0])):
            tmpValue = []
            
            if [x, y] == [0, 0]:
                tmpValue.append(bigMap[y][x] + bigMap[y][x + 1])
                tmpValue.append(bigMap[y][x] + 2 * bigMap[y + 1][x + 1])
                tmpValue.append(bigMap[y][x] + bigMap[y + 1][x])
            else:
                minRoteValue = pickMinRoteValue(roteValue, y, x)
                #right
                if x != len(bigMap[0])-1:
                    tmpValue.append(minRoteValue + bigMap[y][x+1])
                else:
                    tmpValue.append(None)
                
                # right down
                if not(y == len(bigMap)-1 or x == len(bigMap[0])-1):
                    tmpValue.append(minRoteValue + 2 * bigMap[y+1][x+1])
                else:
                    tmpValue.append(None)
                
                # down
                if y != len(bigMap)-1:
                    tmpValue.append(minRoteValue + bigMap[y+1][x])
                else:
                    tmpValue.append(None)
            
            roteValue[y].append(tmpValue)
    return roteValue

def createValueFlag(roteValue):
    return [[False for _ in range(len(roteValue[0]))] for _ in range(len(roteValue))]

def checkParentRote(roteValue, y, x):
    numbers = []
    roteYX = []
    if 0 < y:
        numbers.append([2, roteValue[y-1][x][2]])
    if 0 < x:
        numbers.append([0, roteValue[y][x-1][0]])
    if 0 < x and 0 < y:
        numbers.append([1, roteValue[y-1][x-1][1]])
    
    numbers = [x for x in numbers if x[1] != None] 
    sortedNumbers = sorted(numbers, key=lambda x: x[1])
    if len(sortedNumbers) != 0:
        minNumber = sortedNumbers[0][1]

    for i in range(len(sortedNumbers[:-1])):
        if sortedNumbers[i][0] == 2:
            roteYX.append([y-1, x])
        if sortedNumbers[i][0] == 0:
            roteYX.append([y, x-1])
        if sortedNumbers[i][0] == 1:
            roteYX.append([y-1, x-1])
        if sortedNumbers[i][1] != sortedNumbers[i+1][1]:
            break
    return roteYX, minNumber
        
def putTrue(roteFlag, roteYX):
    roteFlag[roteYX[0]][roteYX[1]] = True
    return roteFlag

def exploreMap(roteValue):
    output = [] #flag map
    maxLoopNum = -1 + len(roteValue) + len(roteValue[0])
    y = len(roteValue) -1
    x = len(roteValue[0]) -1
    _, minNumber = checkParentRote(roteValue, y, x )
    print("Minimum value: %d" % minNumber)
    roteFlag = createValueFlag(roteValue)
    roteFlag = putTrue(roteFlag, [y,x])
    roteFlagYXs = [[roteFlag, [y,x]]]
    for cnt in range(maxLoopNum):
        tmpRoteFlagYXs = []
        for roteFlagYX in roteFlagYXs:
            YXs, _ = checkParentRote(roteValue, roteFlagYX[1][0], roteFlagYX[1][1])
            if len(YXs) == 0:
                rote = putTrue(roteFlagYX[0], [roteFlagYX[1][0], roteFlagYX[1][1]])
                output.append(putTrue(rote, [0, 0]))
                continue
            for YX in YXs:
                rote = putTrue(copy.deepcopy(roteFlagYX[0]), copy.deepcopy(roteFlagYX[1]))
                tmpRoteFlagYXs.append([rote, YX])
        roteFlagYXs = copy.deepcopy(tmpRoteFlagYXs)
    return output

def drawMap(flagMaps, bigMap):
    for i, flagMap in enumerate(flagMaps):
        if 0 < i:
            print("or")
        for lineNum, lineBool in zip(bigMap, flagMap):
            for Num, Bool in zip(lineNum, lineBool):
                if Bool:
                    print("%3s " % "#", end="")
                else:
                    print("%3d " % Num, end="")
            print()

def main():
    argv = sys.argv
    if len(argv) < 2:
        print("Please pass the map file path as a argument.")
        return
    if not os.path.exists(argv[1]):
        print("%s was NOT FOUND.")
        return
    bigMap = readMap(argv[1])
    roteValue = calcRoteValue(bigMap)
    exMaps = exploreMap(roteValue)
    drawMap(exMaps, bigMap)

if __name__=="__main__":
    main()

