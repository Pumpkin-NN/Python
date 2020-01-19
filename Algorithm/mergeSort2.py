import math

def mergeSort(items):
    # UNCOMMENT FOR DEBUG OUTPUT:
    print(' mergeSort() called on:', items)

    if len(items) == 1:
        # BASE CASE
        # With only zero or one items, `items` is already sorted.
        print(f'no_need_to_sort_single_item: {items}')
        return items

    # RECURSIVE CASE
    middle = math.floor(len(items) / 2)

    # UNCOMMENT FOR DEBUG OUTPUT:
    print('            Split into:', items[:middle], 'and', items[middle:])

    left = mergeSort(items[:middle])
    print(f'mergeSort recursion left: {left}')
    right = mergeSort(items[middle:])
    print(f'mergeSort recursion right: {right}')

    # At this point, `left` should be sorted and `right` should be
    # sorted. We can merge them into a single sorted list.
    sortedResult = []
    leftPointer = 0
    rightPointer = 0
    while (len(sortedResult) < len(items)):
        print(f'items_before_sort: {items}')
        if left[leftPointer] < right[rightPointer]:
            print(f'i am the left1: {left}')
            sortedResult.append(left[leftPointer])
            print(f'left_sortedResult: {sortedResult}')
            leftPointer += 1
        else:
            sortedResult.append(right[rightPointer])
            print(f'i am the right1: {right}')
            print(f'right_sortedResult: {sortedResult}')
            rightPointer += 1

        # If one of the pointers has reached the end of its list,
        # put the rest of the other list into `sortedResult`.
        if leftPointer == len(left):
            print(f'i am the left2: {left}')
            print(f'rightPointer: {rightPointer}')
            print(f'right[rightPointer:]: {right[rightPointer:]}')
            sortedResult.extend(right[rightPointer:])
            print(f'sortedResult_left: {sortedResult}')
            break
        elif rightPointer == len(right):
            print(f'i am the right2: {right}')
            print(f'leftPointer: {leftPointer}')
            print(f'left[leftPointer:]: {left[leftPointer:]}')
            sortedResult.extend(left[leftPointer:])
            print(f'sortedResult_right: {sortedResult}')
            break

    # UNCOMMENT FOR DEBUG OUTPUT:
    print('Two halves sorted into:', sortedResult)

    return sortedResult # Returns a sorted version of `items`.

myList = [9, 7, 0, 6, 3, 1, 8, 2, 5, 4]
myList = mergeSort(myList)
print(myList)