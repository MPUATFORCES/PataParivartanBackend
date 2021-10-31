#Base
def format(text, addJSON):
    Clean_list=[i.strip() for i in text.replace("\f", "").split(',')]

    finalList=[]
    for i in Clean_list:
        if '\n' in i:
            finalList+=i.split('\n')
        else:
            finalList+=[i]

    keysList = ['houseno', 'streetname', 'area', 'landmark']
    for index in range(len(finalList)):
        if finalList[index] not in addJSON.values():
            addJSON[keysList[0]] = finalList[index]
            keysList.pop(0)

    return addJSON
