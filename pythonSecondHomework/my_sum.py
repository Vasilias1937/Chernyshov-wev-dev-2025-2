def my_sum(*args):  
    total = 0  
    for num in args:  
        total += num  
    return total  

if __name__ == '__main__':  
    print(my_sum(1, 2, 3))  
    print(my_sum(1.5, 2.5, 3.5))  
    print(my_sum())  