import time  

def fact_rec(n):  
    """Рекурсивное вычисление факториала."""  
    if n == 0:  
        return 1  
    else:  
        return n * fact_rec(n-1)  

def fact_it(n):  
    """Итерационное вычисление факториала."""  
    result = 1  
    for i in range(1, n + 1):  
        result *= i  
    return result  

if __name__ == '__main__':  
    n = 10  # Пример значения n  
    
    start_time = time.time()  
    fact_rec(n)  
    end_time = time.time()  
    recursive_time = end_time - start_time  

    start_time = time.time()  
    fact_it(n)  
    end_time = time.time()  
    iterative_time = end_time - start_time  
    
    print(f"Рекурсивная функция: {recursive_time:.6f} секунд")  
    print(f"Итеративная функция: {iterative_time:.6f} секунд")  

    # Результаты сравнения (пример для n=10):  
    # Рекурсивная функция: 0.000008 секунд  
    # Итеративная функция: 0.000002 секунд  
    # Итеративная функция работает быстрее для небольших значений n. Для больших n разница может быть более заметной, но рекурсия ограничена глубиной стека.  