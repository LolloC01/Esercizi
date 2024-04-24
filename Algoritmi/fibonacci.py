#Lorenzo Colitto
#22/04/2024

def fibonacci(num: int) -> int:
    num_0: int = 0
    num_1: int = 1
    for i in range(1,num):
        num_2: int = num_0 + num_1
        num_0 = num_1
        num_1 = num_2
    return num_2

def fibonacci_ric(num: int, num_0: int = 0, num_1: int = 1) -> int:
    x: int = num_0 + num_1
    if num > 2:
        return fibonacci_ric(num-1, num_1, x)
    else:
        return x
    
print(fibonacci(10))
print(fibonacci_ric(10))