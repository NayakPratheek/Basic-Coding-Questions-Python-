# Program to check whether a number is strong number or not
# Ex: A number is strong number if the sum of factorial of each number is equal to the number itself (ie., 145 = 1!+4!+5!)

class Solution():
    def factorial(self,num):
        res = 1
        for i in range(2,num+1):
            res *= i
        return res

    def strong(self,n):
        num_sum = 0
        original_num = n
        while n>0:
            d = n%10
            num_sum += sol.factorial(d)
            n//=10
            
        return num_sum == original_num

num = int(input("enter the nuber: "))
sol = Solution()
if sol.strong(num):
    print(f'{num} is a strong number')
else:
    print(f'{num} is not a strong number')