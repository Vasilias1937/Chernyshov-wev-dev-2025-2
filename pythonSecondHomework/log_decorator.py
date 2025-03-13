import datetime
import time
import functools

def function_logger(file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Получаем текущее время
            start_time = datetime.datetime.now()
            start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S.%f')

            # Логируем начало вызова функции
            log_entry = f"{func.__name__}\n{start_time_str}\n{args}\n{kwargs}\n"

            # Вызываем функцию и измеряем время выполнения
            result = func(*args, **kwargs)
            end_time = datetime.datetime.now()
            end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S.%f')
            duration = end_time - start_time

            # Логируем результат и время завершения
            log_entry += f"{result if result is not None else '-'}\n{end_time_str}\n{duration}\n\n"

            # Записываем лог в файл
            with open(file_path, 'a') as log_file:
                log_file.write(log_entry)

            return result
        return wrapper
    return decorator

# Пример использования
@function_logger('test.log')
def greeting_format(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    greeting_format('John')
