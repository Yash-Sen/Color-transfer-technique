import numpy as np
import cv2
import os
from tkinter import filedialog, Tk, Button, Label, messagebox, DoubleVar
from tkinter.ttk import Progressbar, Style
from matplotlib import pyplot as plt
from threading import Thread
from tkinter import Tk, Text, END

#functions 
def read_file(sn, tn):
    s = cv2.imread(sn)
    s = cv2.cvtColor(s, cv2.COLOR_BGR2LAB)
    t = cv2.imread(tn)
    t = cv2.cvtColor(t, cv2.COLOR_BGR2LAB)
    return s, t

def get_mean_and_std(x):
    x_mean, x_std = cv2.meanStdDev(x)
    x_mean = np.hstack(np.around(x_mean, 2))
    x_std = np.hstack(np.around(x_std, 2))
    return x_mean, x_std

def color_transfer(sources, targets, output_folder):
    results = []  # List to store the source, target, and result images for display

    for n in range(len(sources)):
        print("Converting picture " + str(n+1) + "...")
        s, t = read_file(sources[n], targets[n])
        s_mean, s_std = get_mean_and_std(s)
        t_mean, t_std = get_mean_and_std(t)

        height, width, channel = s.shape
        for i in range(height):
            for j in range(width):
                for k in range(channel):
                    x = s[i, j, k]
                    x = ((x - s_mean[k]) * (t_std[k] / s_std[k])) + t_mean[k]
                    x = round(x)
                    x = 0 if x < 0 else x
                    x = 255 if x > 255 else x
                    s[i, j, k] = x
        result = cv2.cvtColor(s, cv2.COLOR_LAB2BGR)
        result_path = os.path.join(output_folder, 'r' + str(n+1) + '.bmp')
        cv2.imwrite(result_path, result)

        # Store images for later display
        results.append((cv2.cvtColor(cv2.imread(sources[n]), cv2.COLOR_BGR2RGB),
                        cv2.cvtColor(cv2.imread(targets[n]), cv2.COLOR_BGR2RGB),
                        cv2.cvtColor(result, cv2.COLOR_BGR2RGB)))
        
        # Update the progress bar
        progress_var.set((n + 1) / len(sources) * 100)
        root.update_idletasks()

    return results

def show_images(results):
    for idx, (source, target, result) in enumerate(results):
        plt.figure(figsize=(15, 5))

        plt.subplot(1, 3, 1)
        plt.imshow(source)
        plt.title(f'Source Image {idx+1}')
        plt.axis('off')

        plt.subplot(1, 3, 2)
        plt.imshow(target)
        plt.title(f'Target Image {idx+1}')
        plt.axis('off')

        plt.subplot(1, 3, 3)
        plt.imshow(result)
        plt.title(f'Result Image {idx+1}')
        plt.axis('off')

        plt.tight_layout()
        plt.show() 

def select_source_files():
    global source_files
    source_files = filedialog.askopenfilenames(title='Select Source Images', filetypes=[("Image files", "*.bmp;*.jpg;*.jpeg;*.png")])

    if not source_files:
        messagebox.showerror("Error", "No source files selected.")
    else:
        source_label.config(text=f"Selected {len(source_files)} source files")

def select_target_files():
    global target_files
    target_files = filedialog.askopenfilenames(title='Select Target Images', filetypes=[("Image files", "*.bmp;*.jpg;*.jpeg;*.png")])

    if not target_files:
        messagebox.showerror("Error", "No target files selected.")
    else:
        target_label.config(text=f"Selected {len(target_files)} target files")

def select_output_folder():
    global output_folder
    output_folder = filedialog.askdirectory(title='Select Output Folder')

    if not output_folder:
        messagebox.showerror("Error", "No output folder selected.")
    else:
        output_label.config(text=f"Output folder selected: {output_folder}")

def start_conversion():
    if not source_files or not target_files:
        messagebox.showerror("Error", "Please select source and target files first.")
        return

    if len(source_files) != len(target_files):
        messagebox.showerror("Error", "The number of source and target files must be the same.")
        return

    if not output_folder:
        messagebox.showerror("Error", "Please select an output folder.")
        return

    # Start the conversion in a separate thread to keep the UI responsive
    conversion_thread = Thread(target=run_conversion)
    conversion_thread.start()

def run_conversion():
    results = color_transfer(source_files, target_files, output_folder)
    show_images(results)

if __name__ == "__main__":
    source_files = []
    target_files = []
    output_folder = ""

    root = Tk()
    root.title("Color Transfer Application")

    style = Style()
    style.configure("TButton", font=("Arial", 12), width=20)
    style.configure("TLabel", font=("Arial", 12), foreground="blue")
    style.configure("TProgressbar", thickness=30)  # Increase the height of the progress bar

    # Create a Text widget
    text_widget = Text(root, height=2, width=40, font=("Arial", 16, "bold"), bd=0, bg=root.cget("bg"), wrap="word")
    text_widget.pack(pady=10)

    # Insert text with colored word "color"
    text_widget.insert(END, "Welcome to ", "color_black")
    text_widget.insert(END, "C", "color_red")
    text_widget.insert(END, "O", "color_green")
    text_widget.insert(END, "L", "color_blue")
    text_widget.insert(END, "O", "color_orange")
    text_widget.insert(END, "R", "color_purple")
    text_widget.insert(END, " transfer app", "color_black")

    # Add tags for colors
    #different colors to make it nice
    text_widget.tag_configure("color_black", foreground="black", font=("Arial", 16, "bold"))
    text_widget.tag_configure("color_red", foreground="red", font=("Arial", 20, "bold"))
    text_widget.tag_configure("color_green", foreground="green", font=("Arial", 20, "bold"))
    text_widget.tag_configure("color_blue", foreground="blue", font=("Arial", 20, "bold"))
    text_widget.tag_configure("color_orange", foreground="orange", font=("Arial", 20, "bold"))
    text_widget.tag_configure("color_purple", foreground="purple", font=("Arial", 20, "bold"))

    # Make the Text widget read-only
    text_widget.configure(state="disabled")

    # Center the text using padding
    text_widget.tag_add("center", "1.0", END)  # Add a tag to center the text
    text_widget.tag_configure("center", justify="center")
    
    #Source file selection
    Label(root, text="Select source and target images", font=("Arial", 12, "bold"), fg="green").pack(pady=10)
    Button(root, text="Select Source Files", command=select_source_files).pack(pady=10)
    source_label = Label(root, text="", font=("Arial", 12), fg="red")
    source_label.pack(pady=5)
    
    #Target file selection
    Button(root, text="Select Target Files", command=select_target_files).pack(pady=10)
    target_label = Label(root, text="", font=("Arial", 12), fg="red")
    target_label.pack(pady=5)
    Label(root, text="", height=2).pack()

    #Output folder selection
    Label(root, text="Select where to save result images", font=("Arial", 12, "bold"), fg="green").pack(pady=10) 
    Button(root, text="Select Output Folder", command=select_output_folder).pack(pady=10)
    output_label = Label(root, text="", font=("Arial", 12), fg="red")
    output_label.pack(pady=5)
    Label(root, text="", height=2).pack()

    #Button to Start the operation
    Button(root, text="Start", command=start_conversion, width=20, height=2, 
       bg="red", fg="white", font=("Arial", 14, "bold")).pack(pady=10)

    #progress bar
    progress_var = DoubleVar()
    progress_bar = Progressbar(root, variable=progress_var, maximum=100, style="TProgressbar")
    progress_bar.pack(pady=10, padx=20, fill="x")

    # Add credentials at the bottom
    Label(root, text="Yashmika Senadheera\n21/ENG/128", font=("Arial", 10), fg="purple").pack(pady=20)

    root.mainloop()
