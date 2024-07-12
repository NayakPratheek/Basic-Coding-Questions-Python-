class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            num_str = str(num)
            sum_digits = 0
            for digit in num_str:
                sum_digits += int(digit)
            num = sum_digits
        return num

sol = Solution()

num = 6767
y = sol.addDigits(num)
print(y) 
