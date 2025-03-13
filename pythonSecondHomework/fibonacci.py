cube = lambda x: x**3 # complete the lambda function   

def fibonacci(n):  
    """  
    Возвращает список из n чисел Фибоначчи, начиная с 0.  
    """  
    fib_list = []  
    a, b = 0, 1  
    for _ in range(n):  
        fib_list.append(a)  
        a, b = b, a + b  
    return fib_list  

if __name__ == '__main__':  
    n = int(input())  
    print(list(map(cube, fibonacci(n))))