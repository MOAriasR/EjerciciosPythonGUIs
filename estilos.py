import tkinter as tk
import ttkbootstrap as ttk

# Crear ventana con tema por defecto
window = ttk.Window(themename="darkly")
window.title("Ejemplos de Bootstyles")
window.geometry("600x500")

# Botones con diferentes estilos
ttk.Button(window, text="Primary", bootstyle="primary").pack(pady=5)
ttk.Button(window, text="Secondary", bootstyle="secondary").pack(pady=5)
ttk.Button(window, text="Success", bootstyle="success").pack(pady=5)
ttk.Button(window, text="Info", bootstyle="info").pack(pady=5)
ttk.Button(window, text="Warning", bootstyle="warning").pack(pady=5)
ttk.Button(window, text="Danger", bootstyle="danger").pack(pady=5)

# Botones con variantes
ttk.Button(window, text="Primary Outline", bootstyle="primary-outline").pack(pady=5)
ttk.Checkbutton(window, text="Success Round", bootstyle="success, round-toggle").pack(pady=5)
ttk.Button(window, text="Danger Link", bootstyle="danger,link").pack(pady=5)

# Otros widgets que aceptan bootstyle
ttk.Checkbutton(window, text="Check Success", bootstyle="success").pack(pady=5)
ttk.Radiobutton(window, text="Radio Primary", bootstyle="primary").pack(pady=5)
ttk.Entry(window, bootstyle="info").pack(pady=5)
window.mainloop()