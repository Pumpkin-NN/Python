def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if j+1 >= len(lst):
                break
            if lst[j+1] < lst[j]:
                hold = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = hold
    return lst

                
if __name__ == '__main__': 
#     lst = [3,2,4,5,6,4,8,3,5,6,7,4,3]
    lst = input("Please type numbers: ")
    lst = list(lst)
    lst = [int(i) for i in lst]
    print("The Original List is:\n{}".format(lst))
    sorted_lst = bubble_sort(lst)
    print("The Sorted List is:\n{}".format(sorted_lst))