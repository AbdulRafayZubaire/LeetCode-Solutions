class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = [str(num) for num in nums]
        print(nums)
        # Sort the numbers using the custom comparison function
        nums.sort(key=lambda x: (x * 10, x), reverse=True)
        
        # Join the sorted numbers to form the largest number
        largest_num = ''.join(nums)
        
        # Remove leading zeros
        largest_num = largest_num.lstrip('0')
        
        # If the number is empty (all numbers were zeros), return '0'
        return largest_num if largest_num else '0'