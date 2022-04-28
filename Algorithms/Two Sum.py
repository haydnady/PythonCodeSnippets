def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for idx, val in enumerate(nums):
            if val > target and val > 0:
                continue
                
            for i, v in enumerate(nums):
                # print(val, v, "---------------->", idx, i, "Target ->", target)
                if (val + v) == target and idx != i:
                    return [idx, i]

# Test Cases
print("Passed!" if twoSum(nums=[2,7,11,15], target=9) == [0,1] else "Failed!")
print("Passed!" if twoSum(nums=[-1,-2,-3,-4,-5], target=-8) == [2,4] else "Failed!")
print("Passed!" if twoSum(nums=[-3,4,3,90], target=0) == [0,2] else "Failed!")