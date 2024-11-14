"""Module for testing exceptions"""

def string_to_int(number):
    """Converts string number value to int"""
    return int(number)

def divide(dividend, divider):
    """Divides two numbers"""
    return dividend / divider

def string_to_int_with_exception_handling(number):
    """Converts string number value to int. If not, displays the error"""
    try:
        result = int(number)
    except Exception:
        print(f"Произошла ошибка при переводе строки в число. {number} - не число")
    return result

def string_to_int_with_better_exception_handling(number):
    """Converts string number value to int. If not, displays and handles the error"""
    try:
        number = int(number)
    except Exception:
        print(f"Произошла ошибка при переводе строки в число. {number} - не число")
    finally:
        if isinstance(number, int):
            result = number
        else:
            result = 0
    return result

def string_to_int_with_better_exception_type_handling(number):
    """Converts string number value to int. If not, displays and handles specific errors"""
    try:
        number = int(number)
    except ValueError:
        print("Произошла ошибка при переводе строки в число. Строка не содержит число")
    except TypeError:
        print("Произошла ошибка при переводе строки в число. На вход получена не строковая \
переменная")
    except ModuleNotFoundError:
        print("Произошла ошибка при переводе строки в число. Модуль перевода не найден")
    finally:
        if isinstance(number, int):
            result = number
        else:
            result = 0
    return result

def divide_with_better_exception_type_handling(dividend, divider):
    """Divides two numbers. If not, displays and handles specifics errors"""
    quotient = ""
    try:
        quotient = dividend / divider
    except ZeroDivisionError:
        print("Произошла ошибка при делении чисел. Деление на ноль невозможно")
    except TypeError:
        print("Произошла ошибка при делении чисел. На вход получена(ы) не числовая(ые) \
переменная(ые)")
    except ValueError:
        print("Произошла ошибка при делении чисел. На вход получена(ы) некорректные значения чисел")
    finally:
        if isinstance(quotient, (float, int)):
            result = quotient
        else:
            result = 0
    return result

def check_age(age):
    """Returns result of checking age for restrictions"""
    try:
        if age < 18:
            age = False
            raise ValueError
        if age > 70:
            age = False
            raise KeyError
        if age == 30:
            age = False
            raise BufferError
    except ValueError:
        print("Ошибка при проверке возраста. Возраст меньше 18")
    except KeyError:
        print("Ошибка при проверке возраста. Возраст больше 70")
    except BufferError:
        print("Ошибка при проверке возраста. Возраст равен 30")
    finally:
        result = not isinstance(age, bool)
    return result

def check_age_with_custom_exceptions(age):
    """Returns result of checking age for restrictions"""
    try:
        if age < 18:
            age = False
            raise UnderageError
        if age > 70:
            age = False
            raise OverageError
        if age == 30:
            age = False
            raise ThirtyYearsError
    except UnderageError:
        print("Ошибка при проверке возраста. Возраст меньше 18")
    except OverageError:
        print("Ошибка при проверке возраста. Возраст больше 70")
    except ThirtyYearsError:
        print("Ошибка при проверке возраста. Возраст равен 30")
    finally:
        result = not isinstance(age, bool)
    return result


class UnderageError(Exception):
    """Exception for age under 18"""

class OverageError(Exception):
    """Exception for age above 70"""

class ThirtyYearsError(Exception):
    """Exception for age 30"""

def get_element_from_list(index):
    """Returns element from list by index"""
    llist = [1, 2, 3]
    element = 0
    try:
        element = llist[index]
    except IndexError as e:
        print(e)
    return element

def get_value_from_dict(key):
    """Returns value from dictionary by key"""
    ddict = {"name": "Alice", "age": 30}
    try:
        return ddict[key]
        #value = get_value_from_dict(my_dict, "address")
    except KeyError as e:
        print(e)
    return ""

def read_file(file_path):
    """Returns content of file from path"""
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError as e:
        print(e)
        return ""
