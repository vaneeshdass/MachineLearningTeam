# code for making dictionary of tuple
import statistics

from collections import defaultdict

li = [['A', 1], ['A', 2], ['B', 3], ['A', 4], ['A', 7]]


def convertInDicofTuples(mergedList):
    global finalList
    d1 = defaultdict(list)
    for k, v in mergedList:
        d1[k].append(v)
    d = dict((k, tuple(v)) for k, v in d1.items())
    return d


def makeListOfAllDataValues(dicOfTuples):
    data = []
    allKeys = dicOfTuples.keys()
    for item in allKeys:
        print('\nclassName ' + item)
        print('\nfre ' + format(dicOfTuples[item].__len__()))
        print('\nWmin ' + format(min(dicOfTuples[item])))
        print('\nWmax ' + format(max(dicOfTuples[item])))
        print('\nWmed ' + format(statistics.median(dicOfTuples[item])))
        print('\nWavg ' + format(statistics.mean(dicOfTuples[item])))


finalList = convertInDicofTuples(li)

makeListOfAllDataValues(finalList)
