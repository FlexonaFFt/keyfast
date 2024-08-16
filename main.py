#type: ignore
import time
from pynput import keyboard
import random

class TypingSpeedTest:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.total_keys = 0
        self.correct_keys = 0
        self.errors = 0
        self.sentence = self.load_sentence()
        self.current_input = ""

    def load_sentence(self):
        """Загружает случайное предложение из файла."""
        try:
            with open('sentences.txt', 'r', encoding='utf-8') as file:
                sentences = file.readlines()
                return random.choice(sentences).strip()
        except FileNotFoundError:
            print("Файл 'sentences.txt' не найден. Пожалуйста, создайте его с предложениями.")
            exit(1)

    def start_test(self):
        print(f"Ваше предложение для печати:\n'{self.sentence}'")
        input("Нажмите Enter, чтобы начать тест...")
        self.start_time = time.time()
        print("Тест начался! Начните печатать...")
        print()
        with keyboard.Listener(on_press=self.on_key_press) as listener:
            listener.join()

    def on_key_press(self, key):
        try:
            # Проверяем, если пользователь нажал клавишу "Esc", чтобы завершить тест
            if key == keyboard.Key.esc:
                self.end_test()
                return False

            # Получаем символ, соответствующий нажатой клавише
            if hasattr(key, 'char') and key.char is not None:
                self.current_input += key.char
                self.total_keys += 1

                # Проверяем, правильно ли напечатан символ
                if len(self.current_input) <= len(self.sentence):
                    if self.current_input[-1] == self.sentence[len(self.current_input) - 1]:
                        self.correct_keys += 1
                    else:
                        self.errors += 1

                # Если пользователь напечатал всё предложение, завершаем тест
                if self.current_input == self.sentence:
                    self.end_test()
                    return False

        except Exception as e:
            print(f"Ошибка: {e}")

    def end_test(self):
        self.end_time = time.time()
        self.calculate_speed()

    def calculate_speed(self):
        elapsed_time = self.end_time - self.start_time
        speed_wpm = (self.correct_keys / 5) / (elapsed_time / 60)  # переводим в слова в минуту
        print()
        print(f"Вы напечатали {self.total_keys} символов за {elapsed_time:.2f} секунд.")
        print(f"Скорость печати: {speed_wpm:.2f} слов в минуту.")
        print(f"Количество ошибок: {self.errors} из {self.total_keys} символов.")

if __name__ == "__main__":
    test = TypingSpeedTest()
    try:
        test.start_test()
    except KeyboardInterrupt:
        test.end_test()
