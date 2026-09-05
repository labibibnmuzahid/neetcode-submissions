class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort() # Fixed: Added parentheses to call the sort method

        for i, a in enumerate(nums):
            # Skip positive integers as the sum can never be zero if the first element is > 0
            if a > 0:
                break
            
            # Skip duplicates for the anchor element
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Fixed: Left pointer should start after 'i', not at 0
            l, r = i + 1, len(nums) - 1 
            
            while l < r:
                # Fixed: Added 'a' to the current sum
                threeSum = a + nums[l] + nums[r] 
                
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # Fixed: Corrected append syntax and list indexing
                    res.append([a, nums[l], nums[r]]) 
                    
                    # Move the left pointer and skip any duplicates to avoid duplicate triplets
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        # Fixed: Return the final result array at the very end
        return res