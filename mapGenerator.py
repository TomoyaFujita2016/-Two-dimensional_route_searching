import random
import sys

def generateList(row, col, minValue, maxValue):
    return  [[str(random.randint(minValue, maxValue)) for _ in range(col)] for _ in range(row)]

def saveListAsMap(path, mList):
    with open(path, "w") as f:
        for line in mList:
            f.write(",".join(line) + "\n")

def main():
    argv = sys.argv
    if len(argv) < 6:
        print("$ python3 mapGenerator.py [save path] [row] [col] [minValue] [maxValue]")
        return

    mList = generateList(int(argv[2]), int(argv[3]), int(argv[4]), int(argv[5]))
    saveListAsMap(argv[1], mList)

if __name__=="__main__":
    main()

