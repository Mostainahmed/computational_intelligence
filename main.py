import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.signal import find_peaks
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import Machine_Learning_Solution

fig = None


def find_all_peaks(y_axis):
    return find_peaks(y_axis, height=y_axis, distance=1000)


def remove_noisy_peaks(pulses, found_peaks):
    peak_heights = found_peaks[1]['peak_heights']
    peak_positions = pulses[found_peaks[0]]

    new_positions = []
    new_heights = []

    peak_mean = np.average(peak_heights)

    for i in range(0, len(peak_heights) - 1):
        if peak_heights[i] > peak_mean:
            new_heights.append(peak_heights[i])
            new_positions.append(peak_positions[i])

    return new_positions, new_heights


def draw_peaks(pulses, y_axis, peak_pos, peak_h):
    global fig
    print(f"First peak position: {peak_pos[0]}, height: {peak_h[0]}")
    peak_data = tk.Label(root, text=f"First peak position: {peak_pos[0]}, height: {peak_h[0]}", font=("Arial", 12))
    peak_data.pack(pady=10)
    fig = plt.figure(figsize=(8, 6))
    ax = fig.subplots()
    ax.plot(pulses, y_axis)
    ax.scatter(peak_pos[0], peak_h[0], color='r', s=15, marker='D', label='Maxima')
    ax.set_xlabel('Pulses')
    ax.set_ylabel('Amplitude')
    ax.set_title('Signal Data Analysis')
    return fig


def read_csv_file(path, starting_column, row_number):
    with open(path) as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        row_count = 1
        for row in rows:
            formatted_row = []
            if row_count == row_number:
                for pulse in row[starting_column:]:
                    formatted_row.append(float(pulse))
                return formatted_row
            row_count += 1\



def read_xlsx_file(path, starting_column, row_number):
    df = pd.read_excel(path)
    selected_row = df.iloc[row_number - 1, starting_column:].values
    return selected_row.astype(float)


def get_pulse_data():
    file_path = filedialog.askopenfilename(title="Select a file")
    column_value = column_entry.get()
    row_value = row_entry.get()

    if not column_value or not row_value:
        messagebox.showerror("Error", "Please enter valid row and column values.")
        return None, None

    try:
        starting_col = int(column_value)
        selected_row = int(row_value)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric row and column values.")
        return None, None

    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == '.csv':
        yaxis = np.array(read_csv_file(file_path, starting_col, selected_row))
    elif file_extension.lower() == '.xlsx':
        yaxis = np.array(read_xlsx_file(file_path, starting_col, selected_row))
    else:
        messagebox.showerror("Error", "Unsupported file type.")
        return None, None

    pulses = np.array(list(range(0, len(yaxis))))
    return pulses, yaxis


def reset_application():
    global fig  # Declare fig as global
    row_entry.delete(0, tk.END)
    column_entry.delete(0, tk.END)
    plt.close('all')
    if fig is not None:
        plt.close(fig)  # Close the existing figure
        fig = None  # Reset fig to None


def plot_graph():
    global fig
    loading_label = tk.Label(root, text="Loading data...", font=("Arial", 12))
    loading_label.pack(pady=10)

    x, y = get_pulse_data()
    loading_label.pack_forget()  # Remove the loading label once data is loaded

    if x is not None and y is not None:
        peaks = find_all_peaks(y)
        peak_positions, peak_heights = remove_noisy_peaks(x, peaks)
        fig = draw_peaks(x, y, peak_positions, peak_heights)

        # Display the graph in the GUI
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)


# Create a simple Tkinter GUI
root = tk.Tk()
root.title("First Peak Detector")
root.geometry("800x600")  # Set initial window size

# Input fields for row and column values
row_label = tk.Label(root, text="Row (e.g., 30):")
row_label.pack(pady=(20, 0))
row_entry = tk.Entry(root)
row_entry.pack(pady=(0, 10))

column_label = tk.Label(root, text="Starting Column (e.g., 6):")
column_label.pack()
column_entry = tk.Entry(root)
column_entry.pack(pady=(0, 10))


def machine_learning():
    Machine_Learning_Solution.ml_sol();


def open_file():
    row_value = row_entry.get()
    column_value = column_entry.get()

    if not column_value or not row_value:
        messagebox.showerror("Error", "Please enter valid row and column values.")
        return

    try:
        starting_col = int(column_value)
        selected_row = int(row_value)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric row and column values.")
        return
    plot_graph()


open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=(0, 20))

root.mainloop()
