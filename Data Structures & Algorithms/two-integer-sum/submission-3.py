class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
    
        # 2. Sort the pairs based on the numbers
        # Becomes: [(2, 1), (3, 0), (3, 2)]
        indexed_nums.sort(key=lambda x: x[0])
        
        left = 0
        right = len(indexed_nums) - 1
        
        while left < right:
            # Use .x[0] to get the actual value for the sum
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            
            if current_sum == target:
                # Return the original indices stored at x[1]
                return sorted([indexed_nums[left][1], indexed_nums[right][1]])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
        return []
