import os  
import sys  

def files_sort(directory):  
    try:  
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]  
        files.sort()  
        extensions = sorted(list(set([f.split('.')[-1] for f in files if '.' in f])))  

        for ext in extensions:  
            for file in files:  
                if '.' in file and file.split('.')[-1] == ext:  
                    print(file)  
    except FileNotFoundError:  
        print(f"Ошибка: Директория '{directory}' не найдена.")  
    except Exception as e:  
        print(f"Ошибка: {e}")  

if __name__ == '__main__':  
    if len(sys.argv) > 1:  
        directory = sys.argv[1]  
        files_sort(directory)  
    else:  
        print("Ошибка: Необходимо указать путь к директории в качестве аргумента командной строки.")  