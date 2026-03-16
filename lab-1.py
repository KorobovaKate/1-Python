# Извлечение букв из строки, содержащей числа и буквы.

def main():

    while True:
        try:
            # Ввод данных с клавиатуры
            user_input = input("Введите строку (числа и буквы): ")

            # Проверка на пустой ввод
            if not user_input:
                print("Ошибка: введена пустая строка. Попробуйте снова.")
                continue

            # Проверка, является ли символ буквой
            is_letter = lambda char: char.isalpha()

            # Фильтрация строки 
            filtered_chars = filter(is_letter, user_input)

            # Преобразование фильтра в список и соединение в строку
            result_string = "".join(list(filtered_chars))

            if not result_string:
                print("Ошибка: В строке нет букв. Попробуйте снова.")
                continue

            break

        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем.")
            return
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}. Попробуйте снова.")
            continue

    print("-" * 30)
    print(f"Исходная строка: {user_input}")
    print(f"Извлеченные буквы: {result_string}")
    print("-" * 30)


if __name__ == "__main__":
    main()