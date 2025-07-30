# CS 1210, Fall 2020.
# Discussion section 4, Sept. 22, 2020

# DISCUSSION SECTION WORK:
#
# 1. STUDENTS: Download two files from the Discussion Sections section
# of the course website:
#    - this file, ds4.py
#    - wordsMany.txt (this is the same as the one used for DS3)
#    Save both in the same folder.
#
# 2. TA (aloud) and STUDENTS:  Read the comments from START HERE! (just after these instructions)
#     to definition of wordInfo function. Discuss any questions about what the functions should do.
#    
# 3. TA demonstrate running wordInfo("wordsMany.txt", "anagrams") on this unchanged file, to
#         see that it behaves reasonably despite having incomplete anagram/neighbor-testing functions.
#         STUDENTS should do the same on their computers.
#         Try regular words ("cat", etc.) and non-words (e.g. "abcd"). Quit via Enter/Return.
#
# 4. STUDENTS: Implement areAnagrams, and test it directly.
#         E.g. test via areAnagrams("cat", "act"), areAnagrams("bull", "bulb"), etc.
#
#     BIG HINT (TA DISCUSS THIS HINT IF HELPFUL):
#            How can we test if two words are anagrams?
#            Type to a Python shell:  sorted("cat") and then sorted("act")
#            From what you see, you should get an idea of how to
#            implement areAnagrams very easily.
#   
# 5. STUDENTS: Implement getAnagramsOf and test it. There is a hint in getAnagramsOf stub below.
#
# 6. Now try wordInfo("wordsMany.txt", "anagrams") again.
#         Try on whatever words you want. Some suggestions: art, stop, spear, least
#
# 7. Like steps 4, 5, and 6, implement areNeighbors and getNeighborsOf, and then
#    try wordInfo("wordsMany.txt", "neighbors")
#    Hint: getNeighborsOf will be exactly the same as getAnagramsOf except for one function call.
#
# SUBMIT THIS WHOLE FILE ON ICON.
#

####### START HERE! (AFTER READING INSTRUCTIONS ABOVE) ##########  

#
# DEFINITIONS: 
# anagrams: two words are anagrams of each other if it is possible to rearrange
# the letters to produce the other. For example, "rat" and "art" and "tar"
# are anagrams of each other, as are "ropes" and "prose"
# Note: it is not enough for the two words just to have the same letters.
# E.g., "bull" and "bulb" are *not* anagrams.  They both contain b, u, and l but
# the bull cannot be rearranged to spell bulb.
#
# neighbors: two words are neighbors of each other if they are the same
# length and their letters are the same at all but one position. I.e. for
# equal length strings, string1 and string2, string1[i] != string2[i] for exactly
# one value 0<=i<len(string1). E.g. "cat" and "rat" are neighbors,
# while  "act" and "cab" are not.
#
# 
# Your job is to complete four simple functions:
#
# areAnagrams(word1, word2): returns True if word1 and word2 are anagrams, False otherwise
#
# getAnagramsOf(word1, wordList): returns a list of all words in wordList that are
#                               anagrams of word1 (a word is an anagram of itself, so if
#                               word1 is in wordList, it should be included in the result)
# areNeighbors(word1, word2): returns True if and only if word1 and word2 are neighbors
#
# getNeighborsOf(word1, wordList): returns a list of all words in wordList that are
#                               neighbors of word1 
# 
# Working "stubs" for these are at the bottom of this file.
#
# Two other functions, already complete, are provided for you.
#
#
# wordInfo(filename, infoType): provides an interactive loop for querying about anagrams and
#                               neighbors.
#
# getWordList(filename): given the name of a file of words, return a list containing all the words.
#

#
#. Given the filename of a file of words, this function
#
#  1. first reads all of the words of the file and stores them in a list.
#  2. prints the number of words read
#  3. enters an interactive loop that repeatedly
#      requests the user to type in a word.
#      - If the user types in a word that is in the word list,
#           the function will print a list of the anagrams or neighbors of that word,
#           depending on infoType argument
#      - if the user types a word that is not in the word list, a suitable
#        message is printed before requesting input from the user again.
#      - if the user presses only Enter/Return, the loop terminates and the
#        function returns.
#
# (DO NOT MODIFY THIS!)
#
def wordInfo(filename,infoType):
    if infoType not in ("anagrams", "neighbors"):
        print("second parameter to wordInfo must be 'anagrams' or 'neighbors'")
        return
    wordList = getWordList(filename)
    print("Read {} words from file '{}'.".format(len(wordList), filename))
    print("Now you can ask for the anagrams of any word you like.")
    print("(hit Return/Enter when you want to quit)")
    print()
    query = input("What word do you want to know about? ")
    while query != '':
        if query in wordList:
            if infoType == 'anagrams':
                resultList = getAnagramsOf(query, wordList)
            elif infoType == 'neighbors':
                resultList = getNeighborsOf(query, wordList)
            print(resultList)
        else:
            print("'{}' is not in the word list. Please try again.".format(query))
        #
        query = input("What word do you want to know about? ")

    print("Goodbye!")

#
#  given the name of a file of words, return a list containing all the words
#  (DO NOT MODIFY!)
#
def getWordList(filename):
    result = []
    fileStream = open(filename, 'r')
    for line in fileStream:
        word = line.strip()
        result.append(word)
    return result

# return True if word1 and word2 are anagrams, False otherwise
#
def areAnagrams(word1, word2):
    # MODIFY THIS!
    sortedWord1 = sorted(word1)
    sortedWord2 = sorted(word2)
    #print(sortedWord1, sortedWord2)

    if len(word1) != len(word2):
        return False
    
    index = 0
    while index < len(word1):
        curr1 = sortedWord1[index]
        curr2 = sortedWord2[index]
        if curr1 != curr2:
            return False

        index = index + 1
    # HINT: use Python's sorted function
    return True

#
#  returns a list of all words in wordList that are anagrams of word1
#  Note: a word is an anagram of itself so if word1 is in wordList,
#    it should be included in the result
#

def getAnagramsOf(word1, wordList):
    result = []
    # MODIFY THIS
    # HINT: you just need a simple loop that goes through word list, adding items
    #   to result if they are anagrams of word1

    sortedWord1 = sorted(word1)
    
    for word in wordList:
        sortedCurrentWord = sorted(word)
        #if sortedWord1 == sortedCurrentWord:
            #result.append(word)

        if areAnagrams(word1, sortedCurrentWord) == True:
            result.append(word)
        
    
    return result



# return True if word1 and word2 are the same length and
# the two words differ at exactly one character position.
# I.e. given strings word1 and word2, with lenth l, there
# is exactly one index i (0 <= l-1) such that word1[i] != word2[i].

def areNeighbors(word1, word2):
    # MODIFY THIS!
    if len(word1) != len(word2):
        return False

    difference = 0
    index = 0
    while index < len(word1):
        curr1 = word1[index]
        curr2 = word2[index]

        if curr1 != curr2:
            difference = difference + 1
        
        if difference > 1:
            return False

        index = index + 1

    if difference == 0:
        return False
    
    return True

#
#  returns a list of all words in wordList that are anagrams of word1
#  Note: a word is an anagram of itself so if word1 is in wordList,
#    it should be included in the result
#
def getNeighborsOf(word1, wordList):
    result = []
    # MODIFY THIS
    # HINT: this should be exactly like getAnagramsOf except for function
    # call within the loop

    for word in wordList:
        if areNeighbors(word1, word) == True:
            result.append(word)
    return result






        

            
