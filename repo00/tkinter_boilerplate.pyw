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
frame1 = ttk.LabelFrame(tab1, text="Frame")
frame1.grid(column=0, row=0, padx=8, pady=4)
a_label = ttk.Label(frame1, text="Enter a name:")
a_label.grid(column=0, row=0, sticky='W')
tabControl.add(tab1, text='Tab 1')

tab2 = ttk.Frame(tabControl)
frame2 = ttk.LabelFrame(tab2, text="Frame")
frame2.grid(column=0, row=0, padx=8, pady=4)
b_label = ttk.Label(frame2, text="Enter a name:")
b_label.grid(column=0, row=0, sticky='W')
tabControl.add(tab2, text='Tab 2')

tab3 = ttk.Frame(tabControl)
frame3 = ttk.LabelFrame(tab3, text="Frame")
frame3.grid(column=0, row=0, padx=8, pady=4)
c_label = ttk.Label(frame3, text="Enter a name:")
c_label.grid(column=0, row=0, sticky='W')
tabControl.add(tab3, text='Tab 3')

tabControl.pack(expand=1, fill="both")

app.mainloop()
