# Числа Чёрча
def zero(f):
    return lambda x: x

def succ(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    return lambda x: f(x)

def two(f):
    return lambda x: f(f(x))

def three(f):
    return lambda x: f(f(f(x)))

# Арифметические операции
def add(m, n):
    return lambda f: lambda x: m(f)(n(f)(x))

def mul(m, n):
    return lambda f: m(n(f))

def exp(m, n):
    return n(m)

# Преобразование чисел Чёрча в Python-числа
def church_to_int(n):
    return n(lambda x: x + 1)(0)

# Преобразование Python-чисел в числа Чёрча
def int_to_church(num):
    if num == 0:
        return zero
    result = zero
    for _ in range(num):
        result = succ(result)
    return result

# Словарь для чисел Чёрча по имени
predefined_numbers = {
    "zero": zero,
    "one": one,
    "two": two,
    "three": three,
}

def get_number(input_str):
    """
    Получает число Чёрча из строки. Если это известное имя (zero, one и т.д.),
    возвращает соответствующее значение. Если это целое число, преобразует в число Чёрча.
    """
    input_str = input_str.strip().lower()
    if input_str in predefined_numbers:
        return predefined_numbers[input_str]
    try:
        num = int(input_str)
        if num < 0:  # Проверка на отрицательное число
            raise ValueError(f"Отрицательные числа '{num}' не поддерживаются.")
        return int_to_church(num)
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

# Основной интерфейс
def main():
    print("Калькулятор с использованием кодирования Чёрча")
    print("Введите числа (zero, one, two, three или целые числа).")
    print("Доступные операции: add (сложение), mul (умножение), exp (возведение в степень).")
    print("Пример: add two three")
    print("Введите 'exit' для выхода.")

    while True:
        user_input = input("\nВведите команду: ").strip().lower()
        if user_input == "exit":
            print("Выход из программы. До свидания!")
            break

        try:
            # Разбор команды
            parts = user_input.split()
            if len(parts) != 3:
                print("Ошибка: команда должна быть в формате 'операция число число'.")
                continue

            operation, num1_str, num2_str = parts

            # Получение чисел Чёрча
            num1 = get_number(num1_str)
            num2 = get_number(num2_str)
            if num1 is None or num2 is None:
                continue

            # Выполнение операции
            if operation == "add":
                result = add(num1, num2)
            elif operation == "mul":
                result = mul(num1, num2)
            elif operation == "exp":
                result = exp(num1, num2)
            else:
                print(f"Ошибка: неизвестная операция '{operation}'.")
                continue

            # Вывод результата
            res_int = church_to_int(result)
            res_church = "λf.λx."
            res_church_temp_part = ""
            for i in range(res_int):
                res_church_temp_part += "f("
            if res_church_temp_part != "":
                res_church_temp_part = res_church_temp_part[:-1]
            res_church_temp_part += "x"
            for i in range(res_int - 1):
                res_church_temp_part += ")"
            res_church += res_church_temp_part

            print(f"Результат: {res_int}")
            print(f'Результат в виде нумерала чёрча: {res_church}')

        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
