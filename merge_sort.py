

merge_sort_list = []
final_list = []
def merge_sort(l):
    def final(msl):
        print(f'msl:{msl}')
        for k in range(len(msl)):
            # print(msl[k])
            if k+1 == len(msl):
                break
            if msl[k] > msl[k+1]:
                hold = msl[k]
                msl[k] = msl[k+1]
                msl[k+1] = hold
                print(f'\nphase1: {msl[k],msl[k+1]}')
                final_list.extend([msl[k],msl[k+1]])
            else:
                print(f'\nphase2: {msl[k],msl[k+1]}')
                final_list.extend([msl[k],msl[k+1]]) 
            # if msl[k] not in final_list and len(final_list) != 0:
            #     for j in range(len(final_list)):
            #         if msl[k] > final_list[j]:
            #             hold = msl[k]
            #             msl[k] = final_list[j]
            #             final_list[j] = hold
            #             print(f'\nphase3: {msl[k]}')
            #             final_list.append(msl[k])
            #         else:
            #             print(f'\nphase4: {msl[k]}')
            #             final_list.append(msl[k])
                
            # final_list.extend([msl[k],msl[k+1]])
        # for k in range(len(msl)):
        #     # print(f'k:{msl[k]}')
        #     if k+1 == len(msl):
        #         break
        #     if msl[k] > msl[k+1]:
        #         temp = msl[k]
        #         msl[k] = msl[k+1]
        #         msl[k+1] = temp
        #         final_list.append(msl[k])
        #         final_list.append(msl[k+1])
        #     else:
        #         final_list.append(msl[k])
        #         final_list.append(msl[k+1])
        print(f'final_list:{final_list}')
        return final_list
    
    if len(l) == 2:
        for i in range(len(l)):
            if i+1 == len(l):
                break
            if l[i] > l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
                merge_sort_list.extend([l[i],l[i+1]])
            else:
                merge_sort_list.extend([l[i],l[i+1]])
        print(f'merge_sort_list:{merge_sort_list}')
        final(merge_sort_list)
        return merge_sort_list
        
    m = int(len(l)/2)
    l1 = l[:m]
    l2 = l[m:]
    # print(f'l1, l2:{l1, l2}')
    return merge_sort(l1), merge_sort(l2)
    


if __name__ == "__main__":
    L = [2, 8, 5, 3, 9, 4, 1, 7]
    merge_sort(L)