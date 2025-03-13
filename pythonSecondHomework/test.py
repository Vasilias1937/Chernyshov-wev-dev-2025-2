import pytest  
import subprocess  
import os  
import tempfile  
import shutil  
import math  
import operator  
from fact import fact_rec, fact_it  
from show_employee import show_employee  
from sum_and_sub import sum_and_sub
from process_list import process_list, process_list_comp, process_list_gen  
from my_sum import my_sum  
from my_sum_argv import my_sum_argv
from email_validation import fun, filter_mail  
from fibonacci import fibonacci, cube  
from average_scores import compute_average_scores  
from phone_number import wrapper, sort_phone
from plane_angle import Point, plane_angle  
from people_sort import person_lister, name_format 
from complex_numbers import Complex 
from circle_square_mk import circle_square_mk
from log_decorator import greeting_format

#///////////////////////////// 1
def test_fact_rec_positive():  
    assert fact_rec(5) == 120  

def test_fact_it_positive():  
    assert fact_it(5) == 120  

def test_fact_rec_zero():  
    assert fact_rec(0) == 1  

def test_fact_it_zero():  
    assert fact_it(0) == 1  
#//////////////////////////// 2
def test_show_employee_with_salary():  
    assert show_employee("Иванов Иван Иванович", 30000) == "Иванов Иван Иванович: 30000 ₽"  

def test_show_employee_default_salary():  
    assert show_employee("Петров Петр Петрович") == "Петров Петр Петрович: 100000 ₽"  

def test_show_employee_zero_salary():  
    assert show_employee("Сидоров Сидор Сидорович", 0) == "Сидоров Сидор Сидорович: 0 ₽"  

def test_show_employee_float_salary():  
    assert show_employee("Смирнов", 75000.50) == "Смирнов: 75000.5 ₽"  
#///////////////////////////////// 3
def test_sum_and_sub_positive():  
    assert sum_and_sub(5, 2) == (7, 3)  

def test_sum_and_sub_negative():  
    assert sum_and_sub(-5, -2) == (-7, -3)  

def test_sum_and_sub_mixed():  
    assert sum_and_sub(5, -2) == (3, 7)  

def test_sum_and_sub_float():  
    assert sum_and_sub(10.5, 3.2) == (13.7, 7.3)  

def test_sum_and_sub_zero():  
    assert sum_and_sub(0, 0) == (0, 0)  
#///////////////////////////////// 4
test_data = [  
    ([1, 2, 3, 4, 5], [1, 4, 27, 16, 125]),  
    ([2, 4, 6, 8], [4, 16, 36, 64]),  
    ([1, 3, 5, 7], [1, 27, 125, 343]),  
    ([1, 2, 3, 4, 5, 6], [1, 4, 27, 16, 125, 36]),  
    ([], []),  # Пустой список  
    ([0, 1, 2], [0, 1, 4]), # Проверка с нулем  
    ([-2, -1, 0, 1, 2], [4, -1, 0, 1, 4]), # Проверка с отрицательными числами  
    ([2.0, 3.0, 4.0], [4.0, 27.0, 16.0]), # Проверка с float числами  
    ([1, 1, 1, 1], [1, 1, 1, 1]), # Проверка с одинаковыми числами  
    ([2, 2, 2, 2], [4, 4, 4, 4]), # Проверка с одинаковыми числами  
]  

@pytest.mark.parametrize("input_list, expected_output", test_data)  
def test_process_list(input_list, expected_output):  
    assert process_list(input_list) == expected_output  

@pytest.mark.parametrize("input_list, expected_output", test_data)  
def test_process_list_comp(input_list, expected_output):  
    assert process_list_comp(input_list) == expected_output  

@pytest.mark.parametrize("input_list, expected_output", test_data)  
def test_process_list_gen(input_list, expected_output):  
    assert list(process_list_gen(input_list)) == expected_output  
#///////////////////////////////// 5
def test_my_sum_empty():  
    assert my_sum() == 0  

def test_my_sum_positive():  
    assert my_sum(1, 2, 3) == 6  

def test_my_sum_negative():  
    assert my_sum(-1, -2, -3) == -6  

def test_my_sum_mixed():  
    assert my_sum(1, -2, 3) == 2  

def test_my_sum_float():  
    assert my_sum(1.5, 2.5, 3.5) == 7.5  

def test_my_sum_large():  
    assert my_sum(100, 200, 300) == 600  

def test_my_sum_single():  
    assert my_sum(5) == 5  

def test_my_sum_zero():  
    assert my_sum(0, 0, 0) == 0  

def test_my_sum_mixed_float():  
    assert my_sum(1, 2.5, -3) == 0.5  

def test_my_sum_many_args():  
    assert my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 55
#///////////////////////////////// 6
def test_my_sum_argv_positive():  
    result = subprocess.run(['python', 'my_sum_argv.py', '1', '2', '3'], capture_output=True, text=True)  
    assert result.stdout.strip() == '6.0'  

def test_my_sum_argv_negative():  
    result = subprocess.run(['python', 'my_sum_argv.py', '-1', '-2', '-3'], capture_output=True, text=True)  
    assert result.stdout.strip() == '-6.0'  

def test_my_sum_argv_mixed():  
    result = subprocess.run(['python', 'my_sum_argv.py', '1', '-2', '3'], capture_output=True, text=True)  
    assert result.stdout.strip() == '2.0'  

def test_my_sum_argv_float():  
    result = subprocess.run(['python', 'my_sum_argv.py', '1.5', '2.5', '3.5'], capture_output=True, text=True)  
    assert result.stdout.strip() == '7.5'  

def test_my_sum_argv_large():  
    result = subprocess.run(['python', 'my_sum_argv.py', '100', '200', '300'], capture_output=True, text=True)  
    assert result.stdout.strip() == '600.0'  
#///////////////////////////////// 7
def create_test_directory(files):  
    """Создает временную директорию с заданными файлами."""  
    temp_dir = tempfile.mkdtemp()  
    for filename in files:  
        with open(os.path.join(temp_dir, filename), 'w') as f:  
            f.write("test content")  
    return temp_dir  

def remove_test_directory(temp_dir):  
    """Удаляет временную директорию."""  
    shutil.rmtree(temp_dir)  

def run_files_sort(directory):  
    """Запускает скрипт files_sort.py и возвращает вывод."""  
    result = subprocess.run(['python', 'files_sort.py', directory], capture_output=True, text=True)  
    return result.stdout.strip()  

def test_files_sort_empty_directory():  
    """Тест для пустой директории."""  
    temp_dir = create_test_directory([])  
    output = run_files_sort(temp_dir)  
    remove_test_directory(temp_dir)  
    assert output == ""      
#///////////////////////////////// 8
def create_test_files(directory, files):  
    """Создает тестовые файлы в указанной директории."""  
    for filename, content in files.items():  
        filepath = os.path.join(directory, filename)  
        with open(filepath, 'w') as f:  
            f.write(content)  

def run_file_search(filename, directory):  
    """Запускает скрипт file_search.py с указанным именем файла и директорией."""  
    process = subprocess.run(['python', 'file_search.py', filename], cwd=directory, capture_output=True, text=True)  
    return process.stdout.strip(), process.stderr.strip() 
#///////////////////////////////// 9
def test_fun_valid_email():  
    """Тест для валидного email."""  
    assert fun("lara@mospolytech.ru") == True  

def test_fun_invalid_email():  
    """Тест для невалидного email."""  
    assert fun("lara@mospolytech. дуже довгий домен") == False  
    assert fun("user@example.verylongextension") == False  
    assert fun("user#123@example.com") == False  

def test_filter_mail_mixed_emails():  
    """Тест для смешанного списка email (валидные и невалидные)."""  
    emails = ["lara@mospolytech.ru", "invalid", "brian-23@mospolytech.ru"]  
    expected = ['lara@mospolytech.ru', 'brian-23@mospolytech.ru']  
    assert filter_mail(emails) == expected  
#///////////////////////////////// 10
def test_fibonacci_zero():  
    """Тест для n = 0."""  
    assert fibonacci(0) == []  

def test_fibonacci_positive():  
    """Тест для n > 0."""  
    assert fibonacci(5) == [0, 1, 1, 2, 3]  
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]  

def test_cube():  
    """Тест для лямбда-функции cube."""  
    assert cube(0) == 0  
    assert cube(1) == 1  
    assert cube(2) == 8  
    assert cube(3) == 27  
    assert cube(4) == 64  

def test_fibonacci_and_cube():  
    """Тест для комбинации fibonacci и cube."""  
    n = 5  
    fib_numbers = fibonacci(n)  
    cubed_numbers = list(map(cube, fib_numbers))  
    assert cubed_numbers == [0, 1, 1, 8, 27]  

    n = 3  
    fib_numbers = fibonacci(n)  
    cubed_numbers = list(map(cube, fib_numbers))  
    assert cubed_numbers == [0, 1, 1]  
#//////////////////////////// 11

def test_compute_average_scores_example():  
    """Тест для примера из условия."""  
    scores = [  
        (89, 90, 78, 93, 80),  
        (90, 91, 85, 88, 86),  
        (91, 92, 83, 89, 90.5)  
    ]  
    expected_averages = [90.0, 91.0, 82.0, 90.0, 85.5]  
    assert compute_average_scores(scores) == expected_averages  

def test_compute_average_scores_single_student():  
    """Тест для одного студента."""  
    scores = [  
        (80,),  
        (90,),  
        (100,)  
    ]  
    expected_averages = [90.0]  
    assert compute_average_scores(scores) == expected_averages  

def test_compute_average_scores_basic():  
    """Базовый тест со средним количеством студентов и предметов."""  
    scores = [  
        (70, 80),  
        (80, 90)  
    ]  
    expected_averages = [75.0, 85.0]  
    assert compute_average_scores(scores) == expected_averages  
#///////////////////////////////// 12
def almost_equal(a, b, tolerance=1e-6):  
    return abs(a - b) < tolerance  

def test_plane_angle_1():  
    a = Point(1, 0, 0)  
    b = Point(0, 1, 0)  
    c = Point(0, 0, 0)  
    d = Point(0, 0, 1)  
    angle = plane_angle(a, b, c, d)  
    assert almost_equal(angle, 90.0)  
    
#///////////////////////////////// 13
def test_sort_phone_basic():  
    """Базовый тест с 10-значными номерами."""  
    numbers = ["9195969878", "9195969877", "9195969879"]  
    expected = ["+7 (919) 596-98-77", "+7 (919) 596-98-78", "+7 (919) 596-98-79"]  
    assert sort_phone(numbers) == expected  

def test_sort_phone_with_different_prefixes():  
    """Тест с номерами, имеющими разные префиксы (8, +7, 0)."""  
    numbers = ["89875641230", "+79875641231", "07895462130", "9195969878"]  
    expected = ["+7 (789) 546-21-30", "+7 (919) 596-98-78", "+7 (987) 564-12-30", "+7 (987) 564-12-31"]  
    assert sort_phone(numbers) == sorted( ["+7 (789) 546-21-30", "+7 (919) 596-98-78", "+7 (987) 564-12-30", "+7 (987) 564-12-31"])  

def test_sort_phone_with_non_numeric():  
    """Тест с номерами, содержащими нецифровые символы."""  
    numbers = ["919-596-98-78", "919 596 98 77", "+7 (919) 596-98-79"]  
    expected = ["+7 (919) 596-98-77", "+7 (919) 596-98-78", "+7 (919) 596-98-79"]  
    assert sort_phone(numbers) == expected  

#///////////////////////////////// 14
people_data = [
    ["Mike", "Thomson", 20, "M"],
    ["Robert", "Bustle", 32, "M"],
    ["Andria", "Bustle", 30, "F"]
]

def test_person_lister_sorting():
    # Проверка сортировки по возрасту
    sorted_people = name_format(people_data)
    assert sorted_people == [
        "Mr. Mike Thomson",
        "Ms. Andria Bustle",
        "Mr. Robert Bustle"
    ]
#///////////////////////////////// 15
def test_addition():
    c1 = Complex(2, 1)
    c2 = Complex(5, 6)
    result = c1 + c2
    assert str(result) == "7.00+7.00i"

def test_subtraction():
    c1 = Complex(2, 1)
    c2 = Complex(5, 6)
    result = c1 - c2
    assert str(result) == "-3.00-5.00i"

def test_multiplication():
    c1 = Complex(2, 1)
    c2 = Complex(5, 6)
    result = c1 * c2
    assert str(result) == "4.00+17.00i"
#///////////////////////////////// 16
def test_circle_square_mk_small_n():
    r = 1
    n = 1000
    estimated_area = circle_square_mk(r, n)
    actual_area = math.pi * r ** 2
    assert math.isclose(estimated_area, actual_area, rel_tol=0.1)

def test_circle_square_mk_medium_n():
    r = 1
    n = 10000
    estimated_area = circle_square_mk(r, n)
    actual_area = math.pi * r ** 2
    assert math.isclose(estimated_area, actual_area, rel_tol=0.05)

def test_circle_square_mk_large_n():
    r = 1
    n = 100000
    estimated_area = circle_square_mk(r, n)
    actual_area = math.pi * r ** 2
    assert math.isclose(estimated_area, actual_area, rel_tol=0.01)
#///////////////////////////////// 17
# Путь к лог-файлу
LOG_FILE_PATH = 'test.log'

# Удаляем файл, если он уже существует

def test_greeting_format_empty_name():
    result = greeting_format('')
    assert result == 'Hello, !'

    with open(LOG_FILE_PATH, 'r') as file:
        log_content = file.read()

    assert 'greeting_format' in log_content
    assert "''" in log_content
    assert 'Hello, !' in log_content

# Удаляем файл, если он уже существует
if os.path.exists(LOG_FILE_PATH):
    os.remove(LOG_FILE_PATH)

@pytest.fixture(scope='function', autouse=True)
def cleanup():
    yield
    # Удаляем лог-файл после каждого теста
    if os.path.exists(LOG_FILE_PATH):
        os.remove(LOG_FILE_PATH)
