##Author: Rishabh Dalal
##Description: Brute force convex hull implementation; O(n^3)
##             Can take care of hulls with boundaries of slope 0 or infinity
##             Three points should not lie on a single line
##             Enter all points, one on each line, with x and y coordinate separated by space in a text file
##             Enter your filename at the end

def convexHullBruteForce(pointInfo, count):
    hull = {}
    
    for i in range(count):
        for j in range(i+1, count):
            flag = True
            lyst = []

            for k in range(count):
                if k != i and k != j:

                    if (pointInfo[j][0] != pointInfo[i][0]):
                        slope = (pointInfo[j][1] - pointInfo[i][1]) / (pointInfo[j][0] - pointInfo[i][0])
                        if slope != 0:
                            left = slope * (pointInfo[k][0] - pointInfo[i][0]) - pointInfo[k][1] + pointInfo[i][1]
                            if left < 0:
                                lyst.append("-")
                            else:
                                lyst.append("+")
                            
                        else:
                            if pointInfo[k][1] > pointInfo[i][1]:
                                lyst.append("U")
                            else:
                                lyst.append("D")
                        
                    else:
                        if pointInfo[k][0] > pointInfo[i][0]:
                                lyst.append("R")
                        else:
                            lyst.append("L")

                    if len(lyst) > 1:
                        if lyst[-1] != lyst[-2]:
                            flag = False                    

            if flag:
                
                if i in hull:
                    hull[i].append(j)
                else:
                    hull[i] = [j]

    ourHull = createHull(hull)
    ourHull = ourHull.split("-")
    print("The hull is:\n")

    output = ""
    for i in ourHull:
        output += str(pointInfo[int(i)]) + " -> "
    print(output[:-4])
    
def createHull(aDict):
    hullL = []
    for i in aDict.keys():
        if len(aDict[i]) == 2:
            last = aDict[i][0]
            new = aDict[i][1]
            hull = str(aDict[i][0]) + "-" + str(i) + "-" + str(aDict[i][1]) + "-"
            hullL.append(last)
            hullL.append(new)
            hullL.append(i)
            break
    try:
        while (1):
            if new in aDict:
                hull += str(aDict[new][0]) + "-"
                new = aDict[new][0]
            else:
                hull = reverse(hull) + "-"
                hull += str(aDict[last][0]) + "-"
                new = aDict[new][0]
    except:
        print("Computaions Complete. Printing...")

    return (hull[:-1])

def reverse(string):
    string = string.split("-")
    string = string.reverse()
    newString = ""
    
    for i in string:
        newString += i + "-"
    return newString[:-1]
    
def readData(filename):
    print("Processing hull...")
    file = open(filename, 'r')
    myDict = {}
    count = 0
    for line in file:
        pointA, pointB = line.strip().split()
        if "." in pointA:
            pointA = float(pointA)
        else:
            pointA = int(pointA)
        if "." in pointB:
            pointB = float(pointB)
        else:
            pointB = int(pointB)

        myDict[count] = [pointA, pointB]
        count += 1
    convexHullBruteForce(myDict, count)

readData("file1.txt")
