#for each file in subfolders in this directory the script will list them and have buttons to run each in a tkinter window

import tkinter as tk
import os
import subprocess
import sys
import threading

print("\n\n*Warning* Use this at your own risk, I am not responsible for any damage caused by this program. *Warning*\n\n")

def move_window(event):
    root.geometry(f'+{event.x_root}+{event.y_root}')

def minimize_window():
    root.state('iconic')

def start_resize(event):
    global x, y, w, h
    x = event.x
    y = event.y
    w = root.winfo_width()
    h = root.winfo_height()

def on_resize(event):
    deltax = event.x - x
    deltay = event.y - y
    new_size = (w + deltax, h + deltay)
    root.geometry(f"{new_size[0]}x{new_size[1]}")

#this is the directory where the script is located
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

#gets config.txt from current directory
config_file = open(dir_path + "/config.txt", "r")
config_file_lines = config_file.readlines()
config_file.close()

#the line that says if the window should be custom or not will be like "custom_window_look = True"
#so we need to get the part after the equals sign
custom_window_look = config_file_lines[0].split("=")[1].strip()

#the line that says the geometry size will be like "geometry_size = 500x500"
#so we need to get the part after the equals sign
geometry_size = config_file_lines[1].split("=")[1].strip()


#this is the directory where the scripts which are exe's are located
scripts_dir = dir_path + "/scripts"

def run_exe(exe_file):
    print("running exe")
    subprocess.call([scripts_dir + "\\" + exe_file])
    print("ran exe: " + exe_file)

root = tk.Tk()


if custom_window_look == True:
    root.overrideredirect(True)  # Turns off the title bar, geometry
    # Custom title bar
    title_bar = tk.Frame(root, bg='blue', relief='raised', bd=2)
    title_bar.pack(fill=tk.X)
    title_bar.bind('<Button-1>', move_window)
    title_bar.bind('<B1-Motion>', move_window)

    close_button = tk.Button(title_bar, text='X', command=root.destroy)
    close_button.pack(side=tk.RIGHT)

    minimize_button = tk.Button(title_bar, text='-', command=minimize_window)
    minimize_button.pack(side=tk.RIGHT)

    title_label = tk.Label(title_bar, text='Hackez Sidekick', bg='blue', fg='white')
    title_label.pack(side=tk.LEFT)

    # Resize grip
    resize_grip = tk.Label(root, bg='gray')
    resize_grip.pack(side=tk.BOTTOM, fill=tk.X)
    resize_grip.bind('<Button-1>', start_resize)
    resize_grip.bind('<B1-Motion>', on_resize)
else:
    root.title("Hakerz Sidekick")
    root.geometry(geometry_size)
    root.resizable(0, 0)

def run_exe_in_thread(exe_file):
    t = threading.Thread(target=run_exe, args=(exe_file,))
    t.start()

root.configure(bg="black")  # Change 'black' to your desired background color


#Label widget
label1 = tk.Label(root, font=("Times New Roman", 25), fg="white", bg="black", text="Hakerz Sidekick")
label1.pack()

#Label widget
label2 = tk.Label(root, text="Scripts", font=("Verdana", 18), fg="white", bg="black")
label2.pack()


# For each file in the scripts directory create a button for it
for file in os.listdir(scripts_dir):
    print(file)
    # Create a button widget with a default argument in lambda
    button = tk.Button(root, text=file, command=lambda file=file: run_exe_in_thread(file))
    # Add the button to the root window
    button.pack()

root.mainloop()
