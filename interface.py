import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class FibonacciJewelryDesign:
    def __init__(self, max_value=16):
        self.max_value = max_value
        self.fibonacci_sequence = self.generate_fibonacci_sequence()

    def generate_fibonacci_sequence(self):
        sequence = [0, 1]
        a, b = 0, 1
        while b < self.max_value:
            a, b = b, a + b
            sequence.append(b)
        return sequence

    def generate_pattern(self, pattern_type):
        if pattern_type == "spiral":
            return self.generate_spiral_pattern()
        elif pattern_type == "repeating":
            return self.generate_repeating_pattern()
        else:
            raise ValueError("Invalid pattern type. Choose 'spiral' or 'repeating'.")

    def generate_spiral_pattern(self):
        pattern = []
        for value in self.fibonacci_sequence:
            pattern.append(("jump-ring", value))
        return pattern

    def generate_repeating_pattern(self):
        pattern = []
        group_size = 16
        for value in self.fibonacci_sequence:
            pattern.extend([("chain-link", value)] * group_size)
            group_size += 1
        return pattern

    def visualize_pattern(self, pattern, figure):
        ax = figure.add_subplot(111)
        for element in pattern:
            shape, size = element
            if shape == "jump-ring":
                jump_ring = plt.Circle((0, 0), size, fill=False, edgecolor='black')
                ax.add_artist(jump_ring)
            elif shape == "chain-link":
                link_length = size / 2
                link_width = size / 4
                theta = np.linspace(0, 2 * np.pi, 100)
                x = link_length * np.cos(theta)
                y = link_width * np.sin(theta)
                ax.plot(x, y, 'k-')

        ax.set_aspect('equal')
        ax.axis('off')
        figure.canvas.draw()

class JewelryDesignGUI:
    def __init__(self, master):
        self.master = master
        master.title("Fibonacci Jewelry Design")

        # Create a label for the pattern type
        pattern_type_label = ttk.Label(master, text="Pattern Type:")
        pattern_type_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        # Create a dropdown menu for selecting the pattern type
        self.pattern_type_var = tk.StringVar()
        pattern_type_dropdown = ttk.Combobox(master, textvariable=self.pattern_type_var, values=["spiral", "repeating"], state='readonly')
        pattern_type_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Create a button to generate the design
        generate_button = ttk.Button(master, text="Generate Design", command=self.generate_design)
        generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Create a canvas to display the design
        self.figure = plt.Figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=master)
        self.canvas.get_tk_widget().grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def generate_design(self):
        pattern_type = self.pattern_type_var.get()
        jewelry_design = FibonacciJewelryDesign()
        pattern = jewelry_design.generate_pattern(pattern_type)
        jewelry_design.visualize_pattern(pattern, self.figure)

root = tk.Tk()
gui = JewelryDesignGUI(root)
root.mainloop()