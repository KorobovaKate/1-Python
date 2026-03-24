#Проверка, является ли символ буквой
def is_letter(char):
    return char.isalpha()

def main():

    while True:
        
        user_input = input("Введите строку (числа и буквы): ")

        if not user_input:
            print("Ошибка: введена пустая строка. Попробуйте снова.")
            continue
        
        filtered_chars = list(filter(is_letter, user_input))
        
        # Преобразование списка символов в единую строку
        result_string = "".join( filtered_chars)

        if not result_string:
            print("Ошибка: В строке нет букв. Попробуйте снова.")
            continue

        break

    print("-" * 30)
    print(f"Исходная строка: {user_input}")
    print(f"Извлеченные буквы: {result_string}")
    print("-" * 30)

if __name__ == "__main__":
    main()

    