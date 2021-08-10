dictOfList = {
    'Boys':[72,68,70,69,74],
    'Girls':[63,65,69,62,61]
}

listOfDict = []
len = len(dictOfList['Boys'])

for i in range(0, len):
    listOfDict.append({'Boys': dictOfList['Boys'][i],'Girls': dictOfList['Girls'][i]})

print(listOfDict)