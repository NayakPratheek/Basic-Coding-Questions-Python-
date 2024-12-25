class Solution:
    def uniqueSum(self, nums):
        return sum(set(nums))

nums = list(map(int, input("Enter the values: ").split()))

solu = Solution()
sumunique = solu.uniqueSum(nums)
print(f"Sum of unique elements of the array is: {sumunique}")
