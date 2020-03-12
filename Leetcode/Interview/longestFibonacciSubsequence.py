# A = [3,4,8,11,12,15,16,20,21,22,24,26,27,28,30,39,42,43,44,45,47,50,51,53,56,58,64,72,75,78,80,81,86,103,105,107,108,116,120,123,129,130,142,156,163,171,172,188,195,204,210,228,259,278,280,304,315,327,340,370,415,449,452,550,598,674,727,732,890,1089,1176,1184,1440,1763,1903,1916,2330,2852,3079,3100,3770,4615,4982,5016,6100,7467,8061,8116,9870,12082,13043,13132,15970,19549,21104,21248,31631,34147,34380,51180,55251,55628,90008,145636]

A = [2,4,7,8,9,10,14,15,18,23,32,50]
def lenLongestFibSubseq(A):
    total = []
    sub = []
    
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            
            if len(sub) != 0:
                if sub[-1] + sub[-2] in A:
                    sub.append(sub[-1] + sub[-2])
                    print(sub)
                    print("\n")
                else:
                    total.append(sub)
                    sub = []
            else:
                if A[i] + A[j] in A:
                    sub.extend([A[i], A[j], A[i] + A[j]])
                    print(f"new sub:{sub}")
       
    print(total)         
    # print(max(total, key = len))
    try:
        return len(max(total, key = len))
    except:
        return 0
    

lenLongestFibSubseq(A)