import tkinter as tk
import time
import RPi.GPIO as GPIO
import threading

# GPIO setup
GPIO.setmode(GPIO.BCM)
StepPins = [24, 25, 8, 7]
for pin in StepPins:
    GPIO.setup(pin, import tkinter as tk
import time
import RPi.GPIO as GPIO
import threading

# GPIO setup
GPIO.setmode(GPIO.BCM)
StepPins = [24, 25, 8, 7]
for pin in StepPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

# Stepper motor sequences
StepCount = 8
Seq = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]

# Variables
step_counter = 0
running = False
direction = 1  # 1 = clockwise, -1 = counterclockwise
wait_time = 0.005  # Speed control

# Stepper motor control function
def move_motor():
    global step_counter, running, direction
    while running:
        for pin in range(4):
            GPIO.output(StepPins[pin], Seq[step_counter][pin])
        step_counter += direction
        if step_counter >= StepCount:
            step_counter = 0
        if step_counter < 0:
            step_counter = StepCount - 1
        time.sleep(wait_time)

# Start motor
def start_motor():
    global running
    if not running:
        running = True
        threading.Thread(target=move_motor).start()

# Stop motor
def stop_motor():
    global running
    running = False
    for pin in StepPins:
        GPIO.output(pin, False)

# Increase speed
def increase_speed():
    global wait_time
    if wait_time > 0.001:
        wait_time -= 0.001

# Decrease speed
def decrease_speed():
    global wait_time
    wait_time += 0.001

# Set clockwise direction
def clockwise():
    global direction
    direction = 1

# Set counterclockwise direction
def counterclockwise():
    global direction
    direction = -1

# GUI setup
root = tk.Tk()
root.title("Stepper Motor Control")

# Buttons
tk.Button(root, text="Start", command=start_motor, width=15).grid(row=0, column=0)
tk.Button(root, text="Stop", command=stop_motor, width=15).grid(row=0, column=1)
tk.Button(root, text="Faster", command=increase_speed, width=15).grid(row=1, column=0)
tk.Button(root, text="Slower", command=decrease_speed, width=15).grid(row=1, column=1)
tk.Button(root, text="Left", command=counterclockwise, width=15).grid(row=2, column=0)
tk.Button(root, text="Right", command=clockwise, width=15).grid(row=2, column=1)

# Run the GUI
root.mainloop()

# Cleanup GPIO on exit
GPIO.cleanup()


GPIO.OUT)
    GPIO.output(pin, False)

# Stepper motor sequences
StepCount = 8
Seq = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]

# Variables
step_counter = 0
running = False
direction = 1  # 1 = clockwise, -1 = counterclockwise
wait_time = 0.005  # Speed control

# Stepper motor control function
def move_motor():
    global step_counter, running, direction
    while running:
        for pin in range(4):
            GPIO.output(StepPins[pin], Seq[step_counter][pin])
        step_counter += direction
        if step_counter >= StepCount:
            step_counter = 0
        if step_counter < 0:
            step_counter = StepCount - 1
        time.sleep(wait_time)

# Start motor
def start_motor():
    global running
    if not running:
        running = True
        threading.Thread(target=move_motor).start()

# Stop motor
def stop_motor():
    global running
    running = False
    for pin in StepPins:
        GPIO.output(pin, False)

# Increase speed
def increase_speed():
    global wait_time
    if wait_time > 0.001:
        wait_time -= 0.001

# Decrease speed
def decrease_speed():
    global wait_time
    wait_time += 0.001

# Set clockwise direction
def clockwise():
    global direction
    direction = 1

# Set counterclockwise direction
def counterclockwise():
    global direction
    direction = -1

# GUI setup
root = tk.Tk()
root.title("Stepper Motor Control")

# Buttons
tk.Button(root, text="Start", command=start_motor, width=15).grid(row=0, column=0)
tk.Button(root, text="Stop", command=stop_motor, width=15).grid(row=0, column=1)
tk.Button(root, text="Faster", command=increase_speed, width=15).grid(row=1, column=0)
tk.Button(root, text="Slower", command=decrease_speed, width=15).grid(row=1, column=1)
tk.Button(root, text="Left", command=counterclockwise, width=15).grid(row=2, column=0)
tk.Button(root, text="Right", command=clockwise, width=15).grid(row=2, column=1)

# Run the GUI
root.mainloop()

# Cleanup GPIO on exit
GPIO.cleanup()



