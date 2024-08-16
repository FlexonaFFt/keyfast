from pynput import keyboard

def on_press(key):
    try:
        print(f"Нажата клавиша:", {key.char})
    except AttributeError:
        print(f'Нажата специальная клавиша: {key}')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Нажмите esc для выхода")
    listener.join()
