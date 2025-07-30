# CS 1210, Fall 2020, Discussion Section 3, Sept. 15, 2020

#
# TODAY'S WORK: The TA will demonstrate some of the parts in this file.
# Students will be graded on correct completion of Parts 5 and 6 (but
# the entire file must load into Python without error)
#
# PART 1. STUDENTS: Download three files from the Discussion Sections section
# of the course website:
# - this file, ds3.py
# - wordsMany.txt, a set of 113,809 words permitted in crossword puzzles
#   from Moby Project (now at Project Gutenberg).
#        http://www.gutenberg.org/files/3201/files/CROSSWD.TXT
# - wordsFew.txt, a file containing three words
#
# PUT ALL THREE FILES IN THE SAME FOLDER
#
# PART 2. TA: demonstrate, explain the testWords function below.
# It is not necessary for students to understand how opening/reading files
# works right now.  Students only need to be able to use the function and
# modify the non-file-related part slightly.
#
# Run testWords on a couple examples:
#  1) with returnTrue(word) as the if condition,
#          testWords("wordsFew.txt") prints three words
#          NOTE: don't run with returnTrue(word) on wordsMany.txt.
#                You don't want to print 113,809 words!
#  2) with 'qi' in word
#     as the if condition, testWords('wordsMany.txt') prints eight words
#
def testWords(filename):
    fileStream = open(filename, 'r')
    for line in fileStream:
        word = line.strip()
        #if returnTrue(word):
        #if 'qi' in word:
        #if hasMoreThanTwentyChars(word):
        #if hasThreeConsecPairs(word):
        if hasFourConsecVowels(word):
            print(word)

# not a useful function except to understand basic structure of
# testWords above.
#
# Always returns True.
#
def returnTrue(string):
    return True

# PART 3. TA: finish this hasMoreThanTwentyChars(word) stub below
#
#     1) test it by calling it directly on a few words
#     2) test if more fully by calling it in testWords and
#                        calling testWords with wordsMany.txt
#        This should yield all words in wordsMany.txt longer than 20 chars.
#
#         Expected output:
#
#         >>> testWords("wordsMany.txt")
#         counterdemonstrations
#         hyperaggressivenesses
#         microminiaturizations
#
def hasMoreThanTwentyChars(word):
    # change this
    return False

#
# PART 4. TA: describe and demonstrate solution to the following problem
#             posed on the well-known Car Talk radio show:
#
#        Problem: Find all words that contain three consecutive pairs of double letters.
#
#        Example: committee is *not* such as word.  There are three sets of double letters, but
#        there is an 'i' between the first ('mm') and second ('tt')
#
#        TA: After describing this code, execute testWords("wordsMany.txt") with
#            using if hasThreeConsecPairs(word):
#            instead of if returnTrue(word):
#            Four words should be printed out of the 113,809
#
#     Solution
#
def hasThreeConsecPairs(word):
    result = False
    index = 0
    while (index + 5) < len(word):
        if ((word[index] == word[index + 1]) and
            (word[index + 2] == word[index + 3]) and
            (word[index + 4] == word[index + 5])):
            result = True
            break
        index = index + 1
    return result

# PART5. Write function hasFourConsecVowels(word)
# that returns True if the given word contains four (or more) vowels in a row
# (consider only lowercase 'a', 'e', 'i', 'o', 'u' vowels, not 'y')
#
#
#
# FOR YOUR TESTING:
# Test your code on the big wordsMany.txt file by using 
#         if hasFourConsecVowels(word):
# instead of other 'if's in testWords, and calling testWords("wordsMany.txt")

# You might be suprised to see how many English words have four consecutive vowels!

# change this to be correct
def hasFourConsecVowels(word):
    result = False
    index = 0
    while (index+3) < len(word):
        if word[index] in ('aeiou'):
            #print(word[index])
            if word[index+1] in ('aeiou'):
                #print(word[index+1])
                if word[index+2] in ('aeiou'):
                    #print(word[index+2])
                    if word[index+3] in ('aeiou'):
                        #print(word[index+3])
                        result = True
                        #print(word)
                        break
        index = index + 1    
    return result


# PART6. Complete function part6 so that it returns two things:
# 1) the largest character in inputString that is not a character in charsToIngore
# 2) the least index at which that character occurs.
# If there is no such character return None for both values. i.e. (None None)
#
# The input will be a string of zero or more lower case characters.
# Use a simple while or for loop. You may not use any string methods,
# but you may use the 'in' or 'not in' operators.
#
# E.g.
# >>> part6("bca", "")
# ('c', 1)
# >>> part6("agcdexfb", "ed")
# ('x', 5)
# >>> part6("agcdexfb", "edx")
# ('g', 1)
# >>> part6("baaaca", "abc")
# (None, None)
# >>> part6("baaaca", "bc")
# ('a', 1)
#
# Remember, as in HW1, to return two values, simply list both in the return
# statement with a comma separating them.
# E.g. return largestChar, indexOfLargestChar
#
def part6(inputString, charsToIgnore):
    largestChar = None
    indexOfLargestChar = None
    # add code here.
    index = 0
    while index < len(inputString):
        if inputString[index] not in charsToIgnore:
            if largestChar == None:
                largestChar = inputString[index]
                indexOfLargestChar = index
            if inputString[index] > largestChar:
                largestChar = inputString[index]
                indexOfLargestChar = index
        index = index + 1
    return largestChar, indexOfLargestChar





