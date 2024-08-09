#Remove specific element and return length of the final array

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

nums = list(map(int, input("Enter the list elements: ").split()))
val = int(input("Enter the value to be removed: "))

s = Solution()
new_length = s.removeElement(nums, val)
print(f'Length of the final array is : {new_length}')
