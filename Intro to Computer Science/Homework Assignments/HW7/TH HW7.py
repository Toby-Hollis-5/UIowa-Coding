def selectionSort(L):
    i = 0
    # invariant: L[0:i] sorted and in final position
    while i < len(L):
        minIndex = findMinIndex(L, i)
        L[i], L[minIndex] = L[minIndex], L[i]
        # now L[0:i+1] sorted an in final position.
        i = i + 1
        # L[0:i] sorted/in final position,and "loop invariant" (loop entry point assumption) holds again

        ## uncomment this if you want to see progress (don't do for large L though!)
        #print("sorted and in final pos:", L[0:i], "unsorted:", L[i:])

# return index of min item in L[startIndex:]
# assumes startIndex < len(L)
#
def findMinIndex(L, startIndex):
    minIndex = startIndex
    currIndex = minIndex + 1
    while currIndex < len(L):
        if L[currIndex] < L[minIndex]:
            minIndex = currIndex
        currIndex = currIndex + 1
    return minIndex

def insertionSort(L):
    i = 1
    
    # invariant: L[0:i] is sorted
    while i < len(L):
        itemToMove = L[i]
        # find where itemToMove should go, shifting larger items right one slot along the way
        j = i-1
        while ((j>=0) and (itemToMove<L[j])):
            L[j+1] = L[j]
            j = j-1

        # found the spot - put itemToMove there
        L[j+1] = itemToMove

        # now L[0:i+1] is sorted (though items not necessarily in final position)
        i = i + 1
        # L[0:i] sorted and "loop invariant" (loop entry point assumption) holds again

        ## uncomment this if you want to see progress (don't do for large L though!)
        #print("sorted:", L[0:i], "unsorted:", L[i:])
        
    return

# Recursive version of merge sort.  
# (It's much easier for most people to correctly implement mergesort recursively.)
# Note: this version modifies L itself, like the other sorts.
#
def mergeSort(L):
    if (len(L) < 2):
        return 
    else:
        # 1. divide list into (almost) equal halves
        middleIndex = len(L)//2
        left = L[:middleIndex]
        right = L[middleIndex:]
        
        #2. recursively sort left and right parts
        mergeSort(left)
        mergeSort(right)
        
        #3. merge sorted left/right parts
        mergedL = merge(left, right)
        
        # mergedL is now sorted but we need to do one more thing (related to Note above)
        # this copies the contents of margedL into L
        L[:] = mergedL[:]
        return
    
# Merge function used by both the recursive and non-recursive merge sorts.
def merge(L1, L2):
    mergedL = []
    iL1 = 0
    iL2 = 0

    while iL1 != len(L1) and iL2 != len(L2):
        if L1[iL1] <= L2[iL2]:
            mergedL.append(L1[iL1])
            iL1 = iL1 + 1
        else:
            mergedL.append(L2[iL2])
            iL2 = iL2 + 1

    # At this point, we've used up all the items from one of the lists.
    # Use list "extend" method to add all the remaining items to mergedL
    mergedL.extend(L1[iL1:])
    mergedL.extend(L2[iL2:])

    return mergedL

def builtinSort(L):
    L.sort()

##########

import random
# return a new list with the same elements as input L but randomly rearranged
def mixup(L):
    newL = L[:]
    length = len(L)
    for i in range(length):
        newIndex = random.randint(i,length-1)
        newL[newIndex], newL[i] = newL[i], newL[newIndex]
    return(newL)

##########

import time

def timeSort(sortfn, L):
    t1 = time.time()
    sortfn(L)
    t2 = time.time()
    return (t2 - t1)

# try, e.g.,
# l = mixup(list(range(4000)))
# timeAllSorts(l)
def timeAllSorts(L):

    Lcopy = L[:]
    sTime = timeSort(selectionSort, Lcopy)
    Lcopy = L[:]
    iTime = timeSort(insertionSort, Lcopy)
    Lcopy = L[:]
    mTime = timeSort(mergeSort, Lcopy)
    Lcopy = L[:]
    biTime = timeSort(builtinSort, Lcopy)
    
    print("{}\t sel: {:.2f}\t ins: {:.2f}\t merge: {:.2f}\t builtin: {:.2f}".format(len(L), sTime, iTime, mTime, biTime))


# The code below is commented out (with ''' before and after) so that the code above will run even
# when you are using a Python that does not have pylab.  If you are using a Python
# with pylab, as you will need to for HW P2, remove the '''s.
# As demonstrated in Lectures 28 and 29, you can call "compareSorts" to produce a chart graphing
# running times of selection and insertion sort on randomly ordered lists of various sizes.
# For HW 7, consider using several functions like this to compare all the sorting methods on various kinds of data
#

import pylab
def compareSortsRandom(minN = 1000, maxN=10000, step=2000):
    listSizes = list(range(minN, maxN, step))
    selectionSortTimes = []
    insertionSortTimes = []
    mergeSortTimes = []
    quickSortTimes = []
    heapSortTimes = []
    builtinSortTimes = []
    for listSize in listSizes:
        listToSortOrig = mixup(list(range(listSize)))
        #Selection Sort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        selectionSort(listToSort)
        endTime = time.time()
        selectionSortTimes.append(endTime-startTime)
        #Insertion Sort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        insertionSort(listToSort)
        endTime = time.time()
        insertionSortTimes.append(endTime-startTime)
        #Merge Sort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        mergeSort(listToSort)
        endTime = time.time()
        mergeSortTimes.append(endTime - startTime)
        #Quick Sort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        quickSort(listToSort)
        endTime = time.time()
        quickSortTimes.append(endTime-startTime)
        #heapSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        heap_sort(listToSort)
        endTime = time.time()
        heapSortTimes.append(endTime - startTime)
        #builtinSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        builtinSort(listToSort)
        endTime = time.time()
        builtinSortTimes.append(endTime - startTime)
    pylab.figure(1)
    pylab.clf()
    pylab.xlabel('List size')
    pylab.ylabel('Time (s)')
    pylab.title("Selection (blue) vs Insertion (red) sort and fast sorts on random data")
    pylab.plot(listSizes, selectionSortTimes, 'bo-')
    pylab.plot(listSizes, insertionSortTimes, 'ro-')
    pylab.plot(listSizes, quickSortTimes, 'ko-')
    pylab.plot(listSizes, mergeSortTimes, 'yo-')
    pylab.plot(listSizes, heapSortTimes, 'go-')
    pylab.plot(listSizes, builtinSortTimes, 'mo-')
    pylab.savefig('AllSortsRandom')
    
def compareSortsSorted(minN = 1000, maxN=10000, step=2000):
    listSizes = list(range(minN, maxN, step))
    selectionSortTimes = []
    insertionSortTimes = []
    mergeSortTimes = []
    quickSortTimes = []
    heapSortTimes = []
    builtinSortTimes = []
    for listSize in listSizes:
        listToSortOrig = list(range(listSize))
        #Selection Sort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        selectionSort(listToSort)
        endTime = time.time()
        selectionSortTimes.append(endTime-startTime)
        #Insertion Sort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        insertionSort(listToSort)
        endTime = time.time()
        insertionSortTimes.append(endTime-startTime)
        #Merge Sort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        mergeSort(listToSort)
        endTime = time.time()
        mergeSortTimes.append(endTime - startTime)
        #Quick Sort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        #quickSort(listToSort)
        endTime = time.time()
        quickSortTimes.append(endTime-startTime)
        #heapSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        heap_sort(listToSort)
        endTime = time.time()
        heapSortTimes.append(endTime - startTime)
        #builtinSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        builtinSort(listToSort)
        endTime = time.time()
        builtinSortTimes.append(endTime - startTime)
    pylab.figure(1)
    pylab.clf()
    pylab.xlabel('List size')
    pylab.ylabel('Time (s)')
    pylab.title("Selection (blue) vs Insertion (red) sort and fast sorts on sorted data")
    pylab.plot(listSizes, selectionSortTimes, 'bo-')
    pylab.plot(listSizes, insertionSortTimes, 'ro-')
    pylab.plot(listSizes, quickSortTimes, 'ko-')
    pylab.plot(listSizes, mergeSortTimes, 'yo-')
    pylab.plot(listSizes, heapSortTimes, 'go-')
    pylab.plot(listSizes, builtinSortTimes, 'mo-')
    pylab.savefig('AllSortsSorted')
    
    
def compareSortsReversed(minN = 1000, maxN=10000, step=2000):
    listSizes = list(range(minN, maxN, step))
    selectionSortTimes = []
    insertionSortTimes = []
    mergeSortTimes = []
    quickSortTimes = []
    heapSortTimes = []
    builtinSortTimes = []
    for listSize in listSizes:
        listToSortOrig = list(range(listSize))
        listToSortOrig.reverse()
        #Selection Sort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        selectionSort(listToSort)
        endTime = time.time()
        selectionSortTimes.append(endTime-startTime)
        #Insertion Sort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        insertionSort(listToSort)
        endTime = time.time()
        insertionSortTimes.append(endTime-startTime)
        #Merge Sort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        mergeSort(listToSort)
        endTime = time.time()
        mergeSortTimes.append(endTime - startTime)
        #Quick Sort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        #quickSort(listToSort)
        endTime = time.time()
        quickSortTimes.append(endTime-startTime)
        #heapSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        heap_sort(listToSort)
        endTime = time.time()
        heapSortTimes.append(endTime - startTime)
        #builtinSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        builtinSort(listToSort)
        endTime = time.time()
        builtinSortTimes.append(endTime - startTime)
    pylab.figure(1)
    pylab.clf()
    pylab.xlabel('List size')
    pylab.ylabel('Time (s)')
    pylab.title("Selection (blue) vs Insertion (red) sort and fast sorts on reversed data")
    pylab.plot(listSizes, selectionSortTimes, 'bo-')
    pylab.plot(listSizes, insertionSortTimes, 'ro-')
    pylab.plot(listSizes, quickSortTimes, 'ko-')
    pylab.plot(listSizes, mergeSortTimes, 'yo-')
    pylab.plot(listSizes, heapSortTimes, 'go-')
    pylab.plot(listSizes, builtinSortTimes, 'mo-')
    pylab.savefig('AllSortsReversed')



def quickSort(L):   #from https://www.educative.io/edpresso/how-to-implement-quicksort-in-python
                    #I tried really hard to figure out how to fix the recursion
    elements = len(L) #limit breaking but I just could not figure it out.
                    #I tried my best on the report without using quickSort, but
    if elements < 2:#I know the assignment specifically said I need to use quickSort. :(
        return L
    
    current_position = 0

    for i in range(1, elements):
         if L[i] <= L[0]:
              current_position += 1
              temp = L[i]
              L[i] = L[current_position]
              L[current_position] = temp

    temp = L[0]
    L[0] = L[current_position] 
    L[current_position] = temp
    
    left = quickSort(L[0:current_position])
    right = quickSort(L[current_position+1:elements])

    L = left + [L[current_position]] + right
    
    return L

def heapify(L, heap_size, root_index):      # from https://stackabuse.com/sorting-algorithms-in-python/#heapsort
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and L[left_child] > L[largest]:
        largest = left_child

    if right_child < heap_size and L[right_child] > L[largest]:
        largest = right_child

    if largest != root_index:
        L[root_index], L[largest] = L[largest], L[root_index]
        heapify(L, heap_size, largest)


def heap_sort(L):   #from https://stackabuse.com/sorting-algorithms-in-python/#heapsort
    n = len(L)

    for i in range(n, -1, -1):
        heapify(L, n, i)

    for i in range(n - 1, 0, -1):
        L[i], L[0] = L[0], L[i]
        heapify(L, i, 0)


def compareFastSortsRandom(minN=10000, maxN=1000000, step=100000):
    listSizes = list(range(minN, maxN, step))
    quickSortTimes = []
    mergeSortTimes = []
    heapSortTimes = []
    builtinSortTimes = []
    for listSize in listSizes:
        listToSortOrig = mixup(list(range(listSize)))
        #quickSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        quickSort(listToSort)
        endTime = time.time()
        quickSortTimes.append(endTime - startTime)
        #mergeSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        mergeSort(listToSort)
        endTime = time.time()
        mergeSortTimes.append(endTime - startTime)
        #heapSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        heap_sort(listToSort)
        endTime = time.time()
        heapSortTimes.append(endTime - startTime)
        #builtinSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        builtinSort(listToSort)
        endTime = time.time()
        builtinSortTimes.append(endTime - startTime)
    pylab.figure(1)
    pylab.clf()
    pylab.xlabel('List size (randomly sorted data)')
    pylab.ylabel('Time (s)')
    pylab.title("Quick (black) vs Merge (yellow) vs Heap (green) vs Built-in (magenta)")
    pylab.plot(listSizes, quickSortTimes, 'ko-')
    pylab.plot(listSizes, mergeSortTimes, 'yo-')
    pylab.plot(listSizes, heapSortTimes, 'go-')
    pylab.plot(listSizes, builtinSortTimes, 'mo-')
    pylab.savefig('FastSortRandom')
    
    
def compareFastSortsSorted(minN=10000, maxN=1000000, step=100000):
    listSizes = list(range(minN, maxN, step))
    quickSortTimes = []
    mergeSortTimes = []
    heapSortTimes = []
    builtinSortTimes = []
    for listSize in listSizes:
        listToSortOrig = list(range(listSize))
        #quickSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        #quickSort(listToSort)
        endTime = time.time()
        quickSortTimes.append(endTime - startTime)
        #mergeSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        mergeSort(listToSort)
        endTime = time.time()
        mergeSortTimes.append(endTime - startTime)
        #heapSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        heap_sort(listToSort)
        endTime = time.time()
        heapSortTimes.append(endTime - startTime)
        #builtInSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        builtinSort(listToSort)
        endTime = time.time()
        builtinSortTimes.append(endTime - startTime)
    pylab.figure(1)
    pylab.clf()
    pylab.xlabel('List size (already sorted data)')
    pylab.ylabel('Time (s)')
    pylab.title("Merge (yellow) vs Heap (green) vs Built-in (magenta)")
    #pylab.plot(listSizes, quickSortTimes, 'ko-')
    pylab.plot(listSizes, mergeSortTimes, 'yo-')
    pylab.plot(listSizes, heapSortTimes, 'go-')
    pylab.plot(listSizes, builtinSortTimes, 'mo-')
    pylab.savefig('FastSortSorted')
    
def compareFastSortsReversed(minN=10000, maxN=1000000, step=100000):
    listSizes = list(range(minN, maxN, step))
    quickSortTimes = []
    mergeSortTimes = []
    heapSortTimes = []
    builtinSortTimes = []
    for listSize in listSizes:
        listToSortOrig = list(range(listSize))
        listToSortOrig.reverse()
        #quickSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        #quickSort(listToSort)
        endTime = time.time()
        quickSortTimes.append(endTime - startTime)
        #mergeSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        mergeSort(listToSort)
        endTime = time.time()
        mergeSortTimes.append(endTime - startTime)
        #heapSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        heap_sort(listToSort)
        endTime = time.time()
        heapSortTimes.append(endTime - startTime)
        #builtInSort
        listToSort = listToSortOrig[:]
        startTime = time.time()
        builtinSort(listToSort)
        endTime = time.time()
        builtinSortTimes.append(endTime - startTime)
    pylab.figure(1)
    pylab.clf()
    pylab.xlabel('List size (reverse sorted data)')
    pylab.ylabel('Time (s)')
    pylab.title("Merge (yellow) vs Heap (green) vs Built-in (magenta)")
    #pylab.plot(listSizes, quickSortTimes, 'ko-')
    pylab.plot(listSizes, mergeSortTimes, 'yo-')
    pylab.plot(listSizes, heapSortTimes, 'go-')
    pylab.plot(listSizes, builtinSortTimes, 'mo-')
    pylab.savefig('FastSortReversed')