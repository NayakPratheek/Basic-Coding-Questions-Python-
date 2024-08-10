class Object:
    def greatest_common_divisor(self,num1, num2):
        if num2 == 0:
            return num1
        else:
            return self.greatest_common_divisor(num2,num1%num2)

num1 = int(input("Enter 1st number: "))        
num2 = int(input("Enter 2nd number: "))        
obj = Object()
great = obj.greatest_common_divisor(num1,num2)
print(f'{great}')