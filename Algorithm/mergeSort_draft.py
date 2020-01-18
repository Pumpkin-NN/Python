L3 = []
L4 = []
MS = []
def merge_sort(L):
    # End condition
    if len(L) == 2:
        if L[0] > L[1]:
            temp = L[0]
            L[0] = L[1]
            L[1] = temp
        return L
    
    # Divide the given list by half
    s = len(L) // 2
    L1 = L[:s]
    L2 = L[s:]
    
    # Recursion
    merge_sort(L1)
    merge_sort(L2)
    print(f'L1: {L1}', f'L2: {L2}')
    # for i, k in zip(L1, L2):
    #     # print(f'i:{i},k:{k}')
    #     if i > k:
    #         hold = i
    #         i = k
    #         k = hold
    #         L3.append(i)
    #         L3.append(k)
    #     else:
    #         L3.append(i)
    #         L3.append(k)
    
    # print(f'After: L3:{L3}')
    # L4 = L3[:8]
    # L5 = L4[:4]
    # L6 = L4[4:]
    # print(f'L5:{L5}, L6{L6}')
    # # for a, b in zip(L5, L6):
    # #     if a > b:
    # #         occupy = a
    # #         a = b
    # #         b = occupy
    # #         if a not in MS:
    # #             MS.append(a)
    # #         if b not in MS:   
    # #             MS.append(b)
    # #     else:
    # #         if a not in MS:
    # #             MS.append(a)
    # #         if b not in MS:   
    # #             MS.append(b)
    
    # for a in L5:
    #     print(f'a:{a}')
    #     for b in L6:
    #         print(f'b:{b}')
    #         if a > b:
    #             occupy = a
    #             a = b
    #             b = occupy
    #             if a not in MS:
    #                 MS.append(a)
    #             if b not in MS:   
    #                 MS.append(b)
    #         else:
    #             if a not in MS:
    #                 MS.append(a)
    #             if b not in MS:   
    #                 MS.append(b)
    
    # print(MS)
    
    return MS

    
if __name__ == "__main__":
    # TODO Set L as the user input string
    L = "23759416"
    L = [int(x) for x in L]
    MSL = merge_sort(L)
    # print(MSL)