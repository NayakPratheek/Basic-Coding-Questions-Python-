class Object:
    def LCM(self,num1, num2):
        if num1>num2:
            higher = num1
        else:
            higher = num2
        high_val = higher

        while True:
            if higher%num1 ==0 and higher%num2 == 0:
                return higher
            else:
                higher = higher + high_val

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
obj = Object()
lcm = obj.LCM(num1,num2)
print(f'LCM of {num1} and {num2} is : {lcm}')