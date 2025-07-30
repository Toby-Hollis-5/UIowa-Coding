# CS 1210, Fall 2020
# Discussion section 5, Sept. 29

# DISCUSSION SECTION WORK:
#

# 1. Download this file, ds5.py from the ICON link
#
# 2. Complete function q1 as specified below.
# 
# 3. Review printLetterCounts, which was discussed at the beginning
#    of the September 28 lecture and provided for study.
#    Then complete printLetterCounts2, which is the same as printLetterCounts
#    except must use dictionaries instead of lists.
#
# 4. SUBMIT THIS FILE to ICON
#

#####

#
# Conmplete function q1(listOfStrings) that takes a list of strings as input
# and returns a dictionary where integer key k is in the dictionary and has 
# value v exactly when there are v length-k strings in the input list.
# For example,
# >>> q1(["a", "b", "cc", "zqsrtsssss", " ", "Z12", "!$"])
# {1: 3, 2: 2, 10: 1, 3: 1}
#
def q1(listOfStrings):
    result = {}
    # finish this function
    for string in listOfStrings:
        currLen = len(string)
        if currLen in result:
            result[currLen] = result[currLen] + 1
        
        if currLen not in result:
            result[currLen] = 1
    return result

#
# printLettersCounts prints the number of occurrences in inputString
# of each letter in letters.
# For example, printLetterCounts("This is a sentence containing a variety of letters", "aeiouy")
# yields:
#
#  'This is a sentence containing a variety of letters' has:
#       4 'a's
#       6 'e's
#       5 'i's
#       2 'o's
#       0 'u's
#       1 'y's
#       and 32 other characters
#
def printLetterCounts(inputString, letters):

    # 1. create a list, letterCounts, containing a 0 for each letter in letters
    letterCounts = len(letters) * [0]
    
    # 2. go through characters of string incrementing appropriate letterCounts item if char in letters - l
    for char in inputString:
        if char in letters:
            charPositionInLetters = letters.index(char)
            letterCounts[charPositionInLetters] = letterCounts[charPositionInLetters] + 1
    
    # at this point, values in letterCounts should contain correct counts of
    #     of number of times chars in letters appear in inpuString
    #     E.g. for printLetterCounts('this is a sentence', 'aze')
    #             letterCounts should be [1, 0, 3]
    # 3. compute (and store as otherChars Count) number of characters in inputString *not* in letters 
    otherCharsCount = len(inputString) - sum(letterCounts)
    print(letterCounts)
    
    # 4. print results
    print("'{}' has:".format(inputString))
    for l in letters:
        print("\t{} '{}'s".format(letterCounts[letters.index(l)], l))
    print("\tand {} other characters".format(otherCharsCount))

# NOTE: this code will crash if you run it before completing Step 1.
#       After completing step 1, you can test it and it will at least not crash.
#
def printLetterCounts2(inputString, letters):

    # 1. create an empty dictionary. Use variable name letterCounts
    # 
    # ADD A LINE HERE
    letterCounts = {}
    inputStringLower = inputString.lower()
    # 2. go through characters of string. If an entry for that characters
    #     already appears in dictionary, increment it. Otherwise, add an entry
    #     with value 1.  (Note: this is *just* like the code in makeBirdDict!)
    # 
    #     The code should start with
    #         for char in inputString:
    # ADD A FEW LINES HERE       
    for char in inputStringLower:
        if char in letters:
            if char in letterCounts:
                letterCounts[char] = letterCounts[char] + 1
            else:
                letterCounts[char] = 1
            
    # uncomment the next line if you want to see the dictionary:
    #print(letterCounts)
    
    # 3. compute (and store as otherChars Count) number of characters in inputString *not* in letters 
    # NOTE: sum(letterCounts.values()) adds together all the values associated with all the keys in
    # the dictionary.  Since we haven't mentioned the sum function in class, WE'VE DONE THIS LINE
    # FOR YOU - DON'T CHANGE IT.
    otherCharsCount = len(inputString) - sum(letterCounts.values())
    
    # 4. print results
    #
    # YOU JUST NEED TO CHANGE ONE LINE HERE - the one with "... something ...".
    #
    # There is a small difficulty to deal with here.  If any letter of letters is not
    # in inputString, that letter will have no dictionary entry. So you need to handle
    # this special 0-occurrence case.  You can either explicitly check
    # via, e.g., 'if l in letterCounts:' or just use letterCounts.get(l,0).
    # The second argument to the 'get' method is the value to return if the first argument
    # is *not* in the dictonary!
    #
    print("'{}' has:".format(inputString))
    for l in letters:
        if l in letters:
            if l in letterCounts:
                print("\t{} '{}'s".format(letterCounts[l], l))
            else:
                print("\t{} '{}'s".format(0, l))
    print("\tand {} other characters".format(otherCharsCount))
