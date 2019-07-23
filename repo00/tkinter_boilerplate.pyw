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

# Menu commands
file_menu.add_command(label="New")
file_menu.add_command(label="Close")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
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
tab3 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')
tabControl.add(tab3, text='Tab 3')
tabControl.pack(expand=1, fill="both")

app.mainloop()
