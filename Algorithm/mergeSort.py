
def mergeSort(arr):
    # End condition
    if len(arr) > 1:   
        # Recursion Acending
        div = len(arr) // 2
        L = arr[:div]
        R = arr[div:]
        
        # Recursion
        mergeSort(L)
        mergeSort(R)
        
        #Recurion Decending
        print(L, R)
        
        i = j = k = 0
        
        
        
    
if __name__ == "__main__":
    # TODO Set L as the user input string
    arr = "28539417"
    arr = [int(count) for count in arr]
    mergeSort(arr)