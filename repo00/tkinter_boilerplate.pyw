import tkinter as tk
from tkinter import ttk

app = tk.Tk()

# Menu Bar
menu_bar = tk.Menu(app)

# Menus
file_menu = tk.Menu(menu_bar)
edit_menu = tk.Menu(menu_bar)
option_menu = tk.Menu(menu_bar)
help_menu = tk.Menu(menu_bar)

file_menu.add_command(label="New")
edit_menu.add_command(label="Undo")
option_menu.add_command(label="Pull")
help_menu.add_command(label="About")

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="Options", menu=option_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

app.config(menu=menu_bar)
app.title("App")

# Tabs
tabControl = ttk.Notebook(app)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill="both")

app.mainloop()
