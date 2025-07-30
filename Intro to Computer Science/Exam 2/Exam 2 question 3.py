def binarySearch(L, x): 
     finished = False
     low = 0
     high = len(L) - 1
     while (finished == False):
         midIndex = (low + high) // 2
         if L[midIndex] == x:
             finished = True
         elif L[midIndex] > x:
             binarySearch(L, L[midIndex])
         else:
             binarySearch(L, L[midIndex])

     return midIndex
