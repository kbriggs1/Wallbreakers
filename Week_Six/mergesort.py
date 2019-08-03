def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) / 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        h = 0
        k = 0
        
        # Iterator for the main list
        l = 0
        
        while h < len(left) and k < len(right):
            if left[h] < right[k]:
              # The value from the left half has been used
              myList[l] = left[h]
              # Move the iterator forward
              h += 1
            else:
                myList[l] = right[k]
                k += 1
            # Move to the next slot
            l += 1

        # For all the remaining values
        while h < len(left):
            myList[k] = left[h]
            h += 1
            l += 1

        while k < len(right):
            myList[l]=right[h]
            k += 1
            l += 1

myList = [54,26,93,17,77,31,44,55,20]
#mergeSort(myList)
print(myList)

