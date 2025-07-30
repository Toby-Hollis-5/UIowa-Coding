#   2b. The thing I find most funny about the results of this program is
#   that the words 'call' and 'free' are in the top ten of the spam
#   messages. Spam messages are really trying to get you to call them for
#   free stuff. 


def analyzeTexts(filename, minWordLengthToConsider = 1):
    inStream = open(filename, encoding = 'utf-8')
    hamLineCount = 0
    spamLineCount = 0
    hamLengthCountTotal = 0
    spamLengthCountTotal = 0
    hamWordCount = 0
    spamWordCount = 0
    hamWordDifferent = 0
    spamWordDifferent = 0
    hamDict = {}
    spamDict = {}
    
    for line in inStream:
        line = line.lower()
        lineAsList = line.split()
        #print(line)
        #print(lineAsList)
        hamLengthCount = 0
        spamLengthCount = 0
        
        if lineAsList[0] == 'ham':
            hamLineCount = hamLineCount + 1
            #hamLengthCount = hamLengthCount + len(lineAsList)-1
            for word in lineAsList[1:]:
                #print(item)
                word = word.strip('''"().,..!?&...@#;:$%^*''')
                #print(item)
                if word in hamDict and word != '':
                    hamDict[word] = hamDict[word] + 1
                    hamWordCount = hamWordCount + 1
                    hamLengthCount = hamLengthCount + 1
                elif word not in hamDict and word != '':
                    hamDict[word] = 1
                    hamWordDifferent = hamWordDifferent + 1
                    hamWordCount = hamWordCount + 1
                    hamLengthCount = hamLengthCount + 1
            hamLengthCountTotal = hamLengthCountTotal + hamLengthCount
            #print(hamDict)
            
        elif lineAsList[0] == 'spam':
            spamLineCount = spamLineCount + 1
            #spamLengthCount = spamLengthCount + len(lineAsList)-1
            for word in lineAsList[1:]:
                #print(item)
                word = word.strip('''"().,..!?&...@#;:$%^*''')
                #print(item)
                if word != '':
                    spamWordCount = spamWordCount + 1
                    spamLengthCount = spamLengthCount + 1
                    if word in spamDict:
                        spamDict[word] = spamDict[word] + 1
                    elif word not in spamDict:
                        spamDict[word] = 1
                        spamWordDifferent = spamWordDifferent + 1
            spamLengthCountTotal = spamLengthCountTotal + spamLengthCount

            #print(spamDict)
    #print("'' =", hamDict[''])
    hamList = list(hamDict.items())
    hamList = sorted(hamList, key = lambda item: item[1], reverse=True)
    spamList = list(spamDict.items())
    spamList = sorted(spamList, key = lambda item: item[1], reverse=True)

    hamAverage = hamLengthCountTotal / hamLineCount
    spamAverage = spamLengthCountTotal / spamLineCount

    print("The number of ham messages was", hamLineCount)
    print("The number of spam messages was", spamLineCount)

    print("The total number of words in ham was", hamWordCount)
    print("The total number of words in spam was", spamWordCount)

    print("The number of different words in ham was", hamWordDifferent)
    print("The number of different words in spam was", spamWordDifferent)

    print("The top ten words for ham of at least length", minWordLengthToConsider, "were:")
    index = 0
    topTenHam = 0
    while topTenHam < 10:
        curr = hamList[index][0]
        if len(curr) >= minWordLengthToConsider:
            frequency = hamList[index][1] / hamWordCount * 100
            print("\t '{}' appeared {} times with a relative frequency of {:.2f}%.".format(curr, hamList[index][1], frequency))
            topTenHam = topTenHam + 1
            
        index = index + 1

    print("The top ten words for spam of at least length", minWordLengthToConsider, "were:")
    index = 0
    topTenSpam = 0
    while topTenSpam < 10:
        curr = spamList[index][0]
        if len(curr) >= minWordLengthToConsider:
            frequency = spamList[index][1] / spamWordCount * 100
            print("\t '{}' appeared {} times with a relative frequency of {:.2f}%.".format(curr, spamList[index][1], frequency))
            topTenSpam = topTenSpam + 1

        index = index + 1

    print("The average length in words of ham is {:.1f}.".format(hamAverage))
    print("The average length in words of spam is {:.1f}.".format(spamAverage))
    
