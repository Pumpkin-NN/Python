def find_first_recurring(s):
    counts = {}
    for item in s:
        if item in counts:
            print(item)
            return item
        counts[item] = 1
    return None
    
if __name__ == '__main__':
    find_first_recurring('ABSBSSB')
    find_first_recurring('BSAABSSB')
    n = find_first_recurring('ABS')
    print(n)