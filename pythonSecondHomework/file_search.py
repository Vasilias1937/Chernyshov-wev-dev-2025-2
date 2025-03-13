import os  
import sys  

def file_search(filename, start_dir=None):  
    """  
    Рекурсивно ищет файл относительно заданной директории и выводит первые 5 строк, если файл найден.  
    """  
    if start_dir is None:  
        start_dir = os.getcwd()  # Текущая рабочая директория по умолчанию  

    for root, _, files in os.walk(start_dir):  
        if filename in files:  
            filepath = os.path.join(root, filename)  
            try:  
                with open(filepath, 'r') as f:  
                    lines = [next(f) for _ in range(5)] # Читаем первые 5 строк  
                    print("".join(lines), end="")  # Выводим без лишних пробелов/переводов строк  
                return  # Файл найден и обработан, выходим из функции  
            except FileNotFoundError:  
                print(f"Файл {filename} не найден") # Обработка, если вдруг файл удалили, пока искали  
                return  
            except Exception as e:  
                print(f"Ошибка при чтении файла: {e}")  # Другие ошибки чтения  
                return  

    print(f"Файл {filename} не найден")  # Если файл не найден после обхода всех каталогов  

if __name__ == '__main__':  
    if len(sys.argv) > 1:  
        filename = sys.argv[1]  
        file_search(filename)  
    else:  
        print("Ошибка: Необходимо указать имя файла в качестве аргумента командной строки.")  