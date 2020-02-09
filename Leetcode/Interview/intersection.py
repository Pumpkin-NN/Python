'''
nums1 = [54,93,21,73,84,60,18,62,59,89,83,89,25,39,41,55,78,27,65,82,94,61,12,38,76,5,35,6,51,48,61,0,47,60,84,9,13,28,38,21,55,37,4,67,64,86,45,33,41]

nums2 = [17,17,87,98,18,53,2,69,74,73,20,85,59,89,84,91,84,34,44,48,20,42,68,84,8,54,66,62,69,52,67,27,87,49,92,14,92,53,22,90,60,14,8,71,0,61,94,1,22,84,10,55,55,60,98,76,27,35,84,28,4,2,9,44,86,12,17,89,35,68,17,41,21,65,59,86,42,53,0,33,80,20]
'''
'''
nums1 = [1,2,2,1]
nums2 = [2,2]
'''
'''
nums = []
for i in nums1:
    for j in nums2:
        if i == j:
            if i not in nums:
                nums.append(i)
                break
            elif nums1.count(i) == nums2.count(j):
                #print(j, nums2.count(j))
                m = nums1.count(i)
                while m > 0:
                    nums.append(i)
                    m -= 2
                break
            
print(nums)

'''





'''
nums1 = [1,2,2,1]
nums2 = [2,2]
'''

'''
nums1 = [54,93,21,73,84,60,18,62,59,89,83,89,25,39,41,55,78,27,65,82,94,61,12,38,76,5,35,6,51,48,61,0,47,60,84,9,13,28,38,21,55,37,4,67,64,86,45,33,41]

nums2 = [17,17,87,98,18,53,2,69,74,73,20,85,59,89,84,91,84,34,44,48,20,42,68,84,8,54,66,62,69,52,67,27,87,49,92,14,92,53,22,90,60,14,8,71,0,61,94,1,22,84,10,55,55,60,98,76,27,35,84,28,4,2,9,44,86,12,17,89,35,68,17,41,21,65,59,86,42,53,0,33,80,20]

nums_1 = nums1
nums_2 = nums2

if len(nums_1) < len(nums_2):
    nums_1, nums_2 = nums_2, nums_1

nums = []
for index, item in enumerate(nums_1):
    for ind, it in enumerate(nums_2):
        if item == it:
            if nums_1.count(item) == nums_2.count(it):
                if nums_1.count(item) == nums_2.count(it) == 1:
                    nums.append(item)
                    break
                else:
                    nums.append(item)
                    nums.append(item)
                    break
        elif item == it:
            if nums_1.count(item) > nums_2.count(it) or nums_1.count(item) < nums_2.count(it):
                diff = abs(nums_1.count(item) - nums_2.count(it))
                for m in range(diff):
                    nums.append(item)
        
print(nums)
'''

# Find the intersection of two lists

#nums1 = [1,2,2,1]
#nums2 = [2]

nums1 = [54,93,21,73,84,60,18,62,59,89,83,89,25,39,41,55,78,27,65,82,94,61,12,38,76,5,35,6,51,48,61,0,47,60,84,9,13,28,38,21,55,37,4,67,64,86,45,33,41]

nums2 = [17,17,87,98,18,53,2,69,74,73,20,85,59,89,84,91,84,34,44,48,20,42,68,84,8,54,66,62,69,52,67,27,87,49,92,14,92,53,22,90,60,14,8,71,0,61,94,1,22,84,10,55,55,60,98,76,27,35,84,28,4,2,9,44,86,12,17,89,35,68,17,41,21,65,59,86,42,53,0,33,80,20]

nums = []
for i in nums1:
    for j in nums2:
        if i == j and i not in nums:
            num_i = nums1.count(i)
            num_j = nums2.count(j)
            # print(num_i)
            # print(num_j)
            count = min(num_i, num_j)
            for m in range(count):
                nums.append(i)
                  
print(nums)