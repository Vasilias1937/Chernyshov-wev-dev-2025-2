import operator

def person_lister(f):
    def inner(people):
        # Сортируем список людей по возрасту
        people.sort(key=operator.itemgetter(2))
        # Применяем функцию форматирования имени к каждому человеку
        return [f(person) for person in people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    # Пример ввода
    people = [
        ["Mike", "Thomson", 20, "M"],
        ["Robert", "Bustle", 32, "M"],
        ["Andria", "Bustle", 30, "F"]
    ]
    # Выводим отформатированные имена
    print(*name_format(people), sep='\n')
