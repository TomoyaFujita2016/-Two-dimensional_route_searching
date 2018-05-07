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

def pickMinrouteValue(routeValue, y, x):
    numbers = []
    idx = 0
    if 0 < y:
        numbers.append(routeValue[y-1][x][2])
    if 0 < x:
        numbers.append(routeValue[y][x-1][0])
    if 0 < x and 0 < y:
        numbers.append(routeValue[y-1][x-1][1])
    numbers = [x for x in numbers if x != None]
    return min(numbers)


def calcrouteValue(bigMap):
    routeValue = []
    for y in range(len(bigMap)):
        routeValue.append([])
        for x in range(len(bigMap[0])):
            tmpValue = []
            
            if [x, y] == [0, 0]:
                tmpValue.append(bigMap[y][x] + bigMap[y][x + 1])
                tmpValue.append(bigMap[y][x] + 2 * bigMap[y + 1][x + 1])
                tmpValue.append(bigMap[y][x] + bigMap[y + 1][x])
            else:
                minrouteValue = pickMinrouteValue(routeValue, y, x)
                #right
                if x != len(bigMap[0])-1:
                    tmpValue.append(minrouteValue + bigMap[y][x+1])
                else:
                    tmpValue.append(None)
                
                # right down
                if not(y == len(bigMap)-1 or x == len(bigMap[0])-1):
                    tmpValue.append(minrouteValue + 2 * bigMap[y+1][x+1])
                else:
                    tmpValue.append(None)
                
                # down
                if y != len(bigMap)-1:
                    tmpValue.append(minrouteValue + bigMap[y+1][x])
                else:
                    tmpValue.append(None)
            
            routeValue[y].append(tmpValue)
    return routeValue

def createValueFlag(routeValue):
    return [[False for _ in range(len(routeValue[0]))] for _ in range(len(routeValue))]

def checkParentRoute(routeValue, y, x):
    numbers = []
    routeYX = []
    if 0 < y:
        numbers.append([2, routeValue[y-1][x][2]])
    if 0 < x:
        numbers.append([0, routeValue[y][x-1][0]])
    if 0 < x and 0 < y:
        numbers.append([1, routeValue[y-1][x-1][1]])
    
    numbers = [x for x in numbers if x[1] != None] 
    sortedNumbers = sorted(numbers, key=lambda x: x[1])
    if len(sortedNumbers) != 0:
        minNumber = sortedNumbers[0][1]

    for i in range(len(sortedNumbers[:-1])):
        if sortedNumbers[i][0] == 2:
            routeYX.append([y-1, x])
        if sortedNumbers[i][0] == 0:
            routeYX.append([y, x-1])
        if sortedNumbers[i][0] == 1:
            routeYX.append([y-1, x-1])
        if sortedNumbers[i][1] != sortedNumbers[i+1][1]:
            break
    return routeYX, minNumber
        
def putTrue(routeFlag, routeYX):
    routeFlag[routeYX[0]][routeYX[1]] = True
    return routeFlag

def exploreMap(routeValue):
    output = [] #flag map
    maxLoopNum = -1 + len(routeValue) + len(routeValue[0])
    y = len(routeValue) -1
    x = len(routeValue[0]) -1
    _, minNumber = checkParentRoute(routeValue, y, x )
    print("Minimum value: %d" % minNumber)
    routeFlag = createValueFlag(routeValue)
    routeFlag = putTrue(routeFlag, [y,x])
    routeFlagYXs = [[routeFlag, [y,x]]]
    for cnt in range(maxLoopNum):
        tmprouteFlagYXs = []
        for routeFlagYX in routeFlagYXs:
            YXs, _ = checkParentRoute(routeValue, routeFlagYX[1][0], routeFlagYX[1][1])
            if len(YXs) == 0:
                route = putTrue(routeFlagYX[0], [routeFlagYX[1][0], routeFlagYX[1][1]])
                output.append(putTrue(route, [0, 0]))
                continue
            for YX in YXs:
                route = putTrue(copy.deepcopy(routeFlagYX[0]), copy.deepcopy(routeFlagYX[1]))
                tmprouteFlagYXs.append([route, YX])
        routeFlagYXs = copy.deepcopy(tmprouteFlagYXs)
    return output

def drawMap(flagMaps, bigMap):
    for i, flagMap in enumerate(flagMaps):
        if 0 < i:
            print("or")
        for lineNum, lineBool in zip(bigMap, flagMap):
            for Num, Bool in zip(lineNum, lineBool):
                if Bool:
                    print("\033[92m%3s\033[0m " % "#", end="")
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
    routeValue = calcrouteValue(bigMap)
    exMaps = exploreMap(routeValue)
    drawMap(exMaps, bigMap)

if __name__=="__main__":
    main()

