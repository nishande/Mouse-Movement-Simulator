import pyautogui
import time
import tkinter as tk

counter = 0
running = False

def start_mouse_movement():
    global running
    if not running:
        running = True
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
        status_label.config(text="Running", fg="green")
        move_mouse()

def stop_mouse_movement():
    global running
    running = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    status_label.config(text="Stopped", fg="red")

def move_mouse():
    global counter
    if running:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 5, y + 5)
        time.sleep(1)
        pyautogui.moveTo(x, y)
        
        counter += 1
        count_label.config(text=f"Activity occurred {counter} time(s)")
        
        window.after(60000, move_mouse) # 1 minute

window = tk.Tk()
window.title("Keep Teams Active")

status_label = tk.Label(window, text="Stopped", fg="red")
status_label.pack()

start_button = tk.Button(window, text="START", command=start_mouse_movement)
start_button.pack(pady=10)

stop_button = tk.Button(window, text="STOP", command=stop_mouse_movement, state=tk.DISABLED)
stop_button.pack()

count_label = tk.Label(window, text=f"Activity occurred {counter} time(s)")
count_label.pack(pady=10)

love_label = tk.Label(window, text="Made with ❤️ by Nishan")
love_label.pack()

window.mainloop()
