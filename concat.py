def writeData(path, data):
    with open(path, 'w') as file:
        file.write('\n'.join(data))


def getData(path):
    with open(path, 'r') as file:
        return file.readlines()

def concat(data, keyword):
    res = []
    for line in data:
        for key in keyword:
            res.append('"'+key.rstrip('\n') + ' ' + line.rstrip('\n')+'"')
    
    return res

if __name__ == "__main__":
    dataPath = 'ville_commune.txt'
    keywordPath = 'keyword.txt'

    newLst = concat(getData(dataPath),getData(keywordPath))
    writeData('result_v2.txt', newLst)