# Инициализация списка  
arr = []  

# Считываем количество команд  
n = int(input())  

# Выполняем команды  
for _ in range(n):  
    command = input().strip().split()  # Считываем команду и разбиваем на части  
    cmd = command[0]  # Первая часть — это команда  

    if cmd == "insert":  
        i = int(command[1])  
        e = int(command[2])  
        arr.insert(i, e)  # Вставка элемента e на позицию i  
    elif cmd == "print":  
        print(arr)  # Печать списка  
    elif cmd == "remove":  
        e = int(command[1])  
        arr.remove(e)  # Удаление первого вхождения элемента e  
    elif cmd == "append":  
        e = int(command[1])  
        arr.append(e)  # Добавление элемента e в конец списка  
    elif cmd == "sort":  
        arr.sort()  # Сортировка списка  
    elif cmd == "pop":  
        if arr:  # Проверяем, что список не пустой  
            arr.pop()  # Удаление последнего элемента  
    elif cmd == "reverse":  
        arr.reverse()  # Переворот списка