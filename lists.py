import csv
import re
import statistics
from collections import Iterable
from collections import defaultdict


def flattenForString(lis):
    for item in lis:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for x in flattenForString(item):
                yield x
        else:
            yield item


def flattenForInteger(lis):
    for item in lis:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for x in flattenForInteger(item):
                yield int(x)
        else:
            yield int(item)


def convertInDicofTuples(mergedList):
    global d
    d1 = defaultdict(list)
    for k, v in mergedList:
        d1[k].append(v)
    d = dict((k, tuple(v)) for k, v in d1.items())
    return d


def makeListOfAllDataValues(finalList):
    data = []
    allKeys = finalList.keys()
    for item in allKeys:
        className = item
        frequency = finalList[item].__len__()
        Wmin = min(finalList[item])
        Wmax = max(finalList[item])
        Wavg = round(statistics.mean(finalList[item]), 2)
        Wmed = round(statistics.median(finalList[item]), 2)
        data.append([className, frequency, Wmin, Wmax, Wavg, Wmed])
    return data


def writeDataToCsvFile(data):
    myFile = open('dataSetAnalysis.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        for row in data:
            writer.writerow(row)


def convertDicToList(l):
    d = {}
    for key, val in l:
        d.setdefault(key, []).append(val)
    return d


classes = [re.findall(r'[A-E0-9]{3,4}(?=@)', line)
           for line in open('index.txt')]

widths = [re.findall(r'(?<=w=)\d{1,3}', line)
          for line in open('index.txt')]

classesList = list(flattenForString(classes))
widthsList = list(flattenForInteger(widths))

# print(classesList)
# print('\n\n ****************')
# print(widthsList)

print('classes \n\n')
print(classes)
print('\n\n classesList\n\n')
print(classesList)

print('\n\nwidths \n')
print(widths)
print('\n\n')
print('widthslist \n\n')
print(widthsList)

mergedList = []
i = 0
for className in classesList:
    mergedList.append([className, widthsList[i]])
    i += 1

print('\n\n\n\n ***************')
print(mergedList)

# dicOfTuples = convertInDicofTuples(mergedList)
dicOfTuples = convertDicToList(mergedList)

data = makeListOfAllDataValues(dicOfTuples)

writeDataToCsvFile(data)
print('\n *************Done************************************')
# class_number, class_frequency, class_min_width, class_max_width, class_average, class_width_median
