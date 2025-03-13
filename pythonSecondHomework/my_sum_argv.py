import sys  

def my_sum_argv():  
    args = sys.argv[1:]
    total = 0  
    try:  
        for arg in args:  
            total += float(arg)
        print(total)  
    except ValueError:  
        print("Ошибка: Все аргументы должны быть числами.")  

if __name__ == '__main__':  
    my_sum_argv()  