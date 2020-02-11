# Use Recursion
nums = [3,3] 
target = 6

lst = nums
def twoSums(lst, target):
    ans = []
    for i in range(len(lst)):
        if i == len(lst):
            break
        if i == 0:
            ans.append(lst[i])
        else:
            if lst[0] + lst[i] == target:
                ans.append(lst[i])
    if len(ans) == 2 or len(lst) == 0:
        return ans
    return twoSums(lst[1:], target)

ans = twoSums(nums, target)
print(ans)