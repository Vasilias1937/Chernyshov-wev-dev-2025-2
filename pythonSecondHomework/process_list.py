import time  

def process_list(arr):  
    result = []  
    for i in arr:  
        if i % 2 == 0:  
            result.append(i**2)  
        else:  
            result.append(i**3)  
    return result  

def process_list_comp(arr):  
    """Переписанная функция с использованием list comprehension."""  
    return [i**2 if i % 2 == 0 else i**3 for i in arr]  

def process_list_gen(arr):  
    """Функция-генератор с аналогичной функциональностью."""  
    for i in arr:  
        if i % 2 == 0:  
            yield i**2  
        else:  
            yield i**3  

if __name__ == '__main__':  
    test_list = list(range(1, 1001))  # Создаем тестовый список  

    # Замер времени для process_list  
    start_time = time.time()  
    process_list(test_list)  
    end_time = time.time()  
    process_list_time = end_time - start_time  

    # Замер времени для process_list_comp  
    start_time = time.time()  
    process_list_comp(test_list)  
    end_time = time.time()  
    process_list_comp_time = end_time - start_time  

    # Замер времени для process_list_gen  
    start_time = time.time()  
    list(process_list_gen(test_list)) # Преобразуем генератор в список для замера времени  
    end_time = time.time()  
    process_list_gen_time = end_time - start_time  

    print(f"process_list time: {process_list_time:.6f} seconds")  
    print(f"process_list_comp time: {process_list_comp_time:.6f} seconds")  
    print(f"process_list_gen time: {process_list_gen_time:.6f} seconds")  

    # Результаты сравнения (пример для списка из 1000 элементов):  
    # process_list time: 0.000291 seconds  
    # process_list_comp time: 0.000217 seconds  
    # process_list_gen time: 0.000235 seconds  
    # List comprehension обычно быстрее, чем обычный цикл for.  Генератор немного медленнее, чем list comprehension, из-за накладных расходов на создание и итерацию генератора.  