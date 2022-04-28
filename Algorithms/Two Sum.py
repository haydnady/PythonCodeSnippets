def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = 0
        output = []
        
        for idx, val in enumerate(nums):
            if val > target:
                continue
                
            for i, v in enumerate(nums):
                print()
                if val + v == target and idx != i:
                    output.append(idx)
                    output.append(i)
                    
                    return output

# Test Cases
print("Passed!" if twoSum(nums=[2,7,11,15], target=9) == [0,1] else "Failed!")
print("Passed!" if twoSum(nums=[-1,-2,-3,-4,-5], target=-8) == [2,4] else "Failed!")