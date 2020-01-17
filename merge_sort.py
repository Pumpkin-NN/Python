def merge_sort(L):
    
#--------------------------------Divide List-------------------------------------------------------
    # Divide List
    Dlist = []
    def divide_list(L):
        # End condition
        if len(L) == 2:
            if L[0] > L[1]:
                temp = L[0]
                L[0] = L[1]
                L[1] = temp
            Dlist.append(L)
            return None
        
        # Divide the given list by half
        s = len(L) // 2
        L1 = L[:s]
        L2 = L[s:]
        
        # Recursion
        divide_list(L1)
        divide_list(L2)
        return Dlist
    
    MS = divide_list(L)
    
#--------------------------------Merge List-------------------------------------------------------
    # Merge List
    Slist = []
    Tlist = []
    Rlist = []
    def merge_list(MS):
        print(len(MS))
        for i in MS:
            print(i)
            for j in i:
                print(j)
                
                
                
                
                
                
                
                
                
            #     Tlist.append(j)
            # if len(Tlist) == len(MS):
            #     Slist.append(Tlist[:len(MS)])
                
            # if len(Tlist) == len(L):
            #     Slist.append(Tlist[len(MS):])
            #     for k in Slist:
            #         for t in range(len(k)):
            #             print(f't:{k[t]}')
            #             if t+1 == len(k):
            #                 break
            #             if k[t] > k[t+1]:
                            
                    
                    
                    
                    
                    
        # print(Slist)
        
    
    merge_list(MS)
    
    
    
    return None
    
if __name__ == "__main__":
    # TODO Set as the user input
    L = "28539417"
    L = [int(x) for x in L]
    merge_sort(L)