import csv

# Инициализация суммарных затрат для каждой категории
total_expenses = {
    'Взрослый': 0.0,
    'Пенсионер': 0.0,
    'Ребенок': 0.0
}

# Чтение данных из CSV-файла
with open('products.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    # Подсчет суммарных затрат для каждой категории
    for row in csv_reader:
        total_expenses['Взрослый'] += float(row['Взрослый'].replace(',', '.'))
        total_expenses['Пенсионер'] += float(row['Пенсионер'].replace(',', '.'))
        total_expenses['Ребенок'] += float(row['Ребенок'].replace(',', '.'))

# Вывод суммарных затрат для каждой категории
for category, total in total_expenses.items():
    print(f"Суммарные затраты для {category}: {total:.2f}")