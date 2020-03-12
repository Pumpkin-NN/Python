'''
nums = [3,2,4] 
target = 6

def twoSums(nums, target):
    cur = 0
    while True:
        ans = []
        for k, i in enumerate(nums[cur:]):
            print(nums[cur:])
            print(k,i)
            ans.append(nums[cur])
            if k != cur:
                if nums[k] + nums[cur] == target:
                    ans.append(i)
                    if len(ans) == 2:
                        return ans
                    if k == len(nums)-1:
                        cur = cur + 1
            # if k == len(nums)-1:
            #     if len(ans) != 2:
            #         cur = cur + 1
            #     elif len(ans) == 2:
            #         return ans
    print(ans)
    
ans = twoSums(nums, target)
'''

nums = [3,4,5] 
target = 9

def twoSums(nums, target):
    lst = nums
    cur = 0
    ans = []
    while True:
        if cur == len(nums):
            break
        for k, i in enumerate(lst[cur:]):
            print(k,i)
            if k == len(lst) - 1:
                break
            if k == cur:
                ans.append(i)
                print(f'ans:{ans}')
            if ans[0] + i == target:
                ans.append(i)
                # print(f'ans:{ans}')
                # print(len(ans))
            if len(ans) == 2:
                print(ans)
                return ans
            ans.clear()
            print(ans)
        cur = cur + 1

ans = twoSums(nums, target)
print(ans)