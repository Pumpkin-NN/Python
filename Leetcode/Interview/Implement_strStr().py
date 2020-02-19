haystack = "mississippi"
needle = "issip"
def strStr(haystack, needle):
    if len(needle) == 0:
        return 0
    if len(haystack) == 0:
        return -1
    if needle in haystack:
        index = haystack.index(needle)
        return index
    else:
        return -1

strStr(haystack, needle)