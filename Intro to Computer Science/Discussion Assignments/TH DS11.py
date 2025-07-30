def generateMarkerString(currentTweetIndex, tweetLatLonList, mapCenterLatLon):

    if tweetLatLonList[currentTweetIndex] == None:
        tweetMarkers = "&markers=color:red|{},{}".format(mapCenterLatLon[0], mapCenterLatLon[1])
    else:
        tweetMarkers = "&markers=color:red|{},{}".format(tweetLatLonList[currentTweetIndex][0], tweetLatLonList[currentTweetIndex][1]) 

    if len(tweetLatLonList) > 1:
        tweetMarkers = tweetMarkers + "&markers=color:green|size:small"
    
    tweetIndex = 0
    while tweetIndex < len(tweetLatLonList):
        #print(tweetLatLonList[tweetIndex])
        if tweetIndex != currentTweetIndex:
            if tweetLatLonList[tweetIndex] == None:
                tweetMarkers = tweetMarkers + "|{},{}".format(mapCenterLatLon[0], mapCenterLatLon[1])
            else:
                tweetMarkers = tweetMarkers + "|{},{}".format(tweetLatLonList[tweetIndex][0], tweetLatLonList[tweetIndex][1])
        
        tweetIndex += 1
    #print(tweetMarkers)
    return tweetMarkers
