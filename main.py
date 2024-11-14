"""Main module"""
from exceptions import string_to_int, divide, string_to_int_with_exception_handling, \
    string_to_int_with_better_exception_handling, \
    string_to_int_with_better_exception_type_handling, divide_with_better_exception_type_handling, \
    check_age, check_age_with_custom_exceptions, \
    read_file, get_element_from_list, get_value_from_dict

# Задание 9

def test_functions():
    """Exercise 9. Function to test all the previous ones"""
    # Задание 1
    print("Задание 1")

    try:
        print(string_to_int("12"))
        print(string_to_int("twelve")) # will cause exception
    except Exception as e:
        print(e)

    try:
        print(divide(10, 0)) # will cause exception
        print(divide(10, 3))
    except Exception as e:
        print(e)

    # Задание 2
    print("Задание 2")

    try:
        print(string_to_int_with_exception_handling("15"))
        print(string_to_int_with_exception_handling("fifteen")) # will cause exception
    except Exception as e:
        print(e)

    # Задание 3
    print("Задание 3")

    try:
        print(string_to_int_with_better_exception_handling("17"))
        print(string_to_int_with_better_exception_handling("seventeen")) # will cause exception
    except Exception as e:
            print(e)
    # Задание 4
    print("Задание 4")

    print(string_to_int_with_better_exception_type_handling("xd"))
    print(string_to_int_with_better_exception_type_handling(None))
    print(string_to_int_with_better_exception_type_handling("20"))

    print(divide_with_better_exception_type_handling(10, 0))
    print(divide_with_better_exception_type_handling(10, "0"))
    print(divide_with_better_exception_type_handling(10, None))

    # Задание 5
    print("Задание 5")

    print(check_age(17))
    print(check_age(30))
    print(check_age(72))
    print(check_age(20))

    # Задание 6-7
    print("Задание 6-7")

    print(check_age_with_custom_exceptions(10))
    print(check_age_with_custom_exceptions(100))
    print(check_age_with_custom_exceptions(30))

    # Задание 8
    print("Задание 8")

    print(read_file("a"))
    print(get_element_from_list(3))
    print(get_value_from_dict("a"))

if __name__ == "__main__":
    test_functions()
