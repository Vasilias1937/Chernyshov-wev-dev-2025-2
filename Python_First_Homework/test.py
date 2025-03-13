import subprocess  
import pytest  

INTERPRETER = 'python'  

def run_script(filename, input_data=None):  
    proc = subprocess.run(  
        [INTERPRETER, filename],  
        input='\n'.join(input_data if input_data else []),  
        capture_output=True,  
        text=True,  
        check=False  
    )  
    return proc.stdout.strip()  

test_data = {  
    'python_if_else': [  
        ('1', 'Weird'),  
        ('4', 'Not Weird'),  
        ('3', 'Weird'),  
        ('6', 'Weird'),  
        ('22', 'Not Weird')  
    ],  
    'arithmetic_operators': [  
        (['1', '2'], ['3', '-1', '2']),  
        (['10', '5'], ['15', '5', '50'])  
    ],  
    'division_test': [  
        (['3', '5'], ['0', '0.6']),  
        (['10', '2'], ['5', '5.0']),  
        (['1', '0'], ['undefined', 'undefined'])  
    ],  
    'squares_test': [  
        ('3', ['0', '1', '4']),  
        ('5', ['0', '1', '4', '9', '16']),  
        ('1', ['0']),  
        ('4', ['0', '1', '4', '9'])  
    ],  
    'print_function': [  
        ('1', '1'),  
        ('2', '12'),  
        ('3', '123'),  
        ('4', '1234'),  
        ('5', '12345'),  
        ('10', '12345678910')  
    ],  
    'second_score': [  
        ('5\n2 3 6 6 5', '5'),          
        ('5\n1 1 2 2 3', '2'),          
        ('2\n1 2', '1'),                
        ('4\n7 8 8 6', '7')             
    ],  
    'second_highest_score': [  
        ('5\nГарри\n37.21\nБерри\n37.21\nТина\n37.2\nАкрити\n41\nХарш\n39', 'Харш'),  
        ('4\nАлекс\n50\nБоб\n50\nСаша\n40\nДаша\n30', 'Саша'),  
        ('3\nИван\n60\nПетр\n70\nСергей\n80', 'Петр'),  
        ('2\nНикита\n25\nДима\n30', 'Никита'),  
        ('3\nАлексей\n60\nПетр\n55\nСергей\n55', 'Петр\nСергей'),  
    ],  
    'list_commands': [  
        ('5\nappend 1\nappend 2\nappend 3\npop\nprint\n',   
         '[1, 2]'),  
        ('7\nappend 3\nappend 2\nappend 1\nreverse\nprint\nremove 2\nprint',   
         '[1, 2, 3]\n[1, 3]'),  
        ('8\ninsert 0 10\ninsert 1 20\ninsert 2 30\nsort\nprint\nremove 20\nprint',   
         '[10, 20, 30]\n[10, 30]'),  
        ('9\ninsert 0 1\ninsert 0 2\ninsert 0 3\nsort\nprint\nappend 4\nprint\nreverse\nprint',   
         '[1, 2, 3]\n[1, 2, 3, 4]\n[4, 3, 2, 1]'),  
    ],  
    'swap_case': [  # Добавляем тесты для swap_case  
        ('Www.MosPolytech.ru', 'wWW.mOSpOLYTECH.RU'),  
        ('Hello World!', 'hELLO wORLD!'),  
        ('Python', 'pYTHON'),  
        ('TeStInG 123', 'tEsTiNg 123'),  
        ('sWaP CaSe', 'SwAp cAsE'),  
    ],  
     'split_and_join': [  # Добавляем тесты для split_and_join  
        ('Hello World', 'Hello-World'),  
        ('This is a test', 'This-is-a-test'),  
        ('Join these words', 'Join-these-words'),  
        ('  Leading and trailing spaces  ', 'Leading-and-trailing-spaces'),  
        ('Multiple    spaces in  between', 'Multiple-spaces-in-between'),  
    ],  
     'longest_words': [
        ('example.txt', ["['сосредоточенности']"]),
     ],
     
    'anagram_check' : [
        (('listen', 'silent'), True),
        (('triangle', 'integral'), True),
        (('apple', 'pineapple'), False),
        (('hello', 'world'), False),
        (('python', 'typhon'), True),
     ],
    'metro_passengers': [  # Добавляем тестовые данные для пассажиров метро  
        (  
            '1\n0 1\n0\n',  # 1 пассажир, время входа 0 и выхода 1, Т = 0  
            '1'  # В момент 0 пассажир в метро (вошёл в 0 и ещё не вышел)  
        ),  
        (  
            '5\n0 5\n1 3\n2 6\n4 7\n5 10\n5\n',  # 5 пассажиров  
            '4'  # В момент времени T = 5 (в метро пассажиры 1, 2, 3, 4 и 5)  
        ),  
        (  
            '3\n1 2\n2 3\n3 4\n2\n',  # 3 пассажира  
            '2'  # В момент времени T = 2 (пассажиры 1 и 2 находятся в метро)  
        ),  
        (  
            '4\n3 5\n1 4\n2 6\n5 7\n4\n',  # 4 пассажира  
            '3'  # В момент времени T = 4 (пассажиры 1, 2 и 3)  
        ),  
        (  
            '2\n3 4\n2 3\n3\n',  # 2 пассажира  
            '2'  # В момент времени T = 3 (оба пассажира)  
        ),  
        (  
            '2\n4 5\n6 7\n5\n',  # 2 пассажира  
            '1'  # На момент времени T=5 только первый пассажир (вышел в 5)  
        ),  
    ],
    
    'minion_game': [  
        ("BANANA\n", "Стюарт 12"),  
        ("APPLE\n", "Стюарт 9"),  
        ("BCDFGH\n", "Стюарт 21"),  
        ("A\n", "Кевин 1"),  
        ("B\n", "Стюарт 1"),  
    ],  
    
    'years': [
        
        ("2000\n", "True"),
        ("1900\n", "False"), 
        ("2024\n", "True"),  
        ("2023\n", "False")
    
    ],
    
    'happiness': [
        ("3 2\n1 5 3\n3 1\n5 7\n", "1"),
        ("4 2\n1 2 3 4\n5 6\n7 8\n", "0"),
        ("6 3\n \n \n \n", "0"),
    ],
    
     'pirate_ship': [
        (
            "50 3\n"
            "Gold 10 60\n"
            "Silver 20 100\n"
            "Bronze 30 120\n", 
            [   
                "Silver 20.00 100.00",
                "Bronze 20.00 80.00",
                "Gold 10.00 60.00"
                
            ]
        ),
        (
            "100 2\n"
            "Jewels 40 200\n"
            "Gems 60 300\n", 
            [
                "Gems 60.00 300.00",
                "Jewels 40.00 200.00"
            ]
        ),
        (
            "70 3\n"
            "Diamonds 10 150\n"
            "Platinum 20 200\n"
            "Emeralds 50 100\n", 
            [
                "Platinum 20.00 200.00",
                "Diamonds 10.00 150.00",
                "Emeralds 40.00 80.00"
            ]
        ),
    ],
     
    'matrix_mult': [
        ("2\n1 2\n3 4\n5 6\n7 8\n","19 22\n43 50"),
        ("3\n1 2 3\n4 5 6\n7 8 9\n1 0 0\n0 1 0\n0 0 1\n","1 2 3\n4 5 6\n7 8 9")
    ]
}  

def test_hello_world():  
    assert run_script('hello.py') == 'Hello, world!'  

@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])  
def test_python_if_else(input_data, expected):  
    assert run_script('python_if_else.py', [input_data]) == expected  

@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])  
def test_arithmetic_operators(input_data, expected):  
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected  

@pytest.mark.parametrize("input_data, expected", test_data['division_test'])  
def test_division(input_data, expected):  
    output = run_script('division.py', input_data).split('\n')  
    if (input_data[1] == '0' or input_data[0] == '0'):  
        assert output == ['undefined', 'undefined']   
    else:  
        assert output == expected  

@pytest.mark.parametrize("input_data, expected", test_data['squares_test'])  
def test_squares(input_data, expected):  
    output = run_script('loops.py', [input_data]).split('\n')  
    assert output == expected  

@pytest.mark.parametrize("input_data, expected", test_data['print_function'])  
def test_print_function(input_data, expected):  
    assert run_script('print_function.py', [input_data]) == expected  

@pytest.mark.parametrize("input_data, expected", test_data['second_score'])  
def test_second_score(input_data, expected):  
    assert run_script('second_score.py', input_data.splitlines()) == expected  
    
@pytest.mark.parametrize("input_data, expected", test_data['second_highest_score'])  
def test_second_highest_score(input_data, expected):  
    assert run_script('nested_list.py', input_data.splitlines()) == expected  
    
@pytest.mark.parametrize("input_data, expected", test_data['list_commands'])  
def test_list_commands(input_data, expected):  
    assert run_script('lists.py', input_data.splitlines()) == expected  

@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])  
def test_swap_case(input_data, expected):  
    assert run_script('swap_case.py', [input_data]) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])  # Тест для split_and_join  
def test_split_and_join(input_data, expected):  
    assert run_script('split_and_join.py', [input_data]) == expected  
    
@pytest.mark.parametrize("input_data, expected", test_data['longest_words'])
def test_longest_words(input_data, expected):
    # Запускаем скрипт и проверяем результат
    output = run_script('max_word.py').split('\n')
    assert sorted(output) == sorted(expected)
    
@pytest.mark.parametrize("input_data, expected", test_data['anagram_check'])
def test_anagram_check(input_data, expected):
    # Запускаем скрипт и проверяем результат
    output = run_script('anagram.py', input_data)
    assert output.strip() == str(expected)
    
@pytest.mark.parametrize("input_data, expected", test_data['metro_passengers'])  
def test_metro_passengers(input_data, expected):  
    output = run_script('metro.py', input_data.splitlines())  
    assert output.strip() == expected  
    
@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    assert run_script("minion_game.py", input_data.split("\n")) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['years'])
def test_is_leap(input_data, expected):
    assert run_script("is_leap.py", input_data.split("\n")) == expected

@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_happiness(input_data, expected):
    assert run_script("happiness.py", input_data.split("\n")) == expected

@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_load_cargo(input_data, expected):
    assert run_script("pirate_ship.py", input_data.split("\n")).split("\n") == expected


@pytest.mark.parametrize("input_data, expected", test_data['matrix_mult'])
def test_matrix_mult(input_data, expected):
    assert run_script("matrix_mult.py", input_data.split("\n")) == expected