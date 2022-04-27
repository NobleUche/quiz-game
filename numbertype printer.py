#This is just the building block for this code as it can be used with values till infinity
input()#request user input
def normal_numbers(A):
    if input() == "odd":
        print(normal_numbers.pop(-10))
        print(normal_numbers.pop(-8))
        print(normal_numbers.pop(-6))
        print(normal_numbers.pop(-4))
        print(normal_numbers.pop(-2))
    if input() == "even":
        print(normal_numbers.pop(-9))
        print(normal_numbers.pop(-7))
        print(normal_numbers.pop(-5))
        print(normal_numbers.pop(-3))
        print(normal_numbers.pop(-1))
A=[1,2,3,4,5,6,7,8,9,10]
normal_numbers(A)
