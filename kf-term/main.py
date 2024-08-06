import time
from TextProvider import TextProvider
from database import Database

def typing_test():
    text_provider = TextProvider()
    text_to_type = text_provider.get_random_text()
    
    print("Введите следующий текст:")
    print(text_to_type)
    
    input("Нажмите Enter, чтобы начать...")
    
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    time_in_seconds = round(elapsed_time, 2)
    
    # Подсчет ошибок
    errors = sum(1 for i in range(min(len(text_to_type), len(user_input))) if text_to_type[i] != user_input[i])
    
    # Вычисление скорости печати
    words_per_minute = (len(user_input.split()) / time_in_seconds) * 60
    
    print(f"\nВремя: {time_in_seconds} секунд")
    print(f"Ошибки: {errors}")
    print(f"Скорость печати: {words_per_minute:.2f} слов в минуту")
    
    # Сохранение результата в базе данных
    db.add_result(time_in_seconds, errors, words_per_minute)

def main_menu():
    while True:
        print("\nМеню:")
        print("1. Тест скорости печати")
        print("2. Показать результаты")
        print("3. Выход")
        
        choice = input("Выберите команду: ")
        
        if choice == '1':
            typing_test()
        elif choice == '2':
            results = db.get_results()
            if results:
                print("\nРезультаты тестов:")
                for result in results:
                    print(f"ID: {result[0]}, Время: {result[1]} секунд, Ошибки: {result[2]}, Скорость: {result[3]:.2f} слов в минуту")
            else:
                print("Нет результатов.")
        elif choice == '3':
            db.close()
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    db = Database()
    main_menu()