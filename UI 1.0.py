import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import cv2
import numpy as np
from kidney_damage_analyzer import KidneyDamageAnalyzer


class KidneyDamageAnalyzerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kidney Damage Analyzer")
        self.root.geometry("800x600")

        self.file_label = tk.Label(root, text="Select Image:")
        self.file_label.grid(row=0, column=0, padx=10, pady=10)

        self.file_path = tk.StringVar()
        self.file_entry = tk.Entry(root, textvariable=self.file_path, width=50)
        self.file_entry.grid(row=0, column=1, padx=10, pady=10)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        self.analysis_button = tk.Button(root, text="Analyze", command=self.analyze_image)
        self.analysis_button.grid(row=0, column=3, padx=10, pady=10)

        self.image_canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.image_canvas.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.results_text = tk.Text(root, height=10, width=80)
        self.results_text.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.bmp")])
        if file_path:
            self.file_path.set(file_path)

    def analyze_image(self):
        image_path = self.file_path.get()
        if not image_path:
            messagebox.showerror("Error", "Please select an image.")
            return

        try:
            analyzer = KidneyDamageAnalyzer(image_path)
            analyzer.analyze()
            results = analyzer.generate_report()

            # Display image
            image = cv2.imread(image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            plt.imshow(image)
            plt.axis('off')
            self.display_image()

            # Display results
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, results)

            # Display quantification graph
            self.display_graph(analyzer.damage_quantification)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def display_image(self):
        plt.tight_layout()
        self.image_canvas.delete("all")
        self.image_canvas.figure = plt.gcf()
        self.image_canvas.draw()

    def display_graph(self, quantification_results):
        labels = list(quantification_results.keys())
        values = list(quantification_results.values())

        fig, ax = plt.subplots()
        ax.bar(labels, values, color='skyblue')
        ax.set_xlabel('Damage Type')
        ax.set_ylabel('Quantification')
        ax.set_title('Quantification of Kidney Damage')
        plt.xticks(rotation=45)

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=3, column=0, columnspan=4, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = KidneyDamageAnalyzerUI(root)
    root.mainloop()
