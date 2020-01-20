def find_first_nonrecurring(s):
    counts = {}
    count = 0
    for item in s:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
        if count == len(s)-1:
            for k, v in counts.items():
                if v == 1:
                    print(f"The first non-recurring item is: {k}")
                    return k 
        count = count + 1
    
    print("There is no recurring items")
    return None
    
if __name__ == '__main__':
    find_first_nonrecurring('BSBASSB')
    find_first_nonrecurring('ABS')
    find_first_nonrecurring('BSAABSSB')