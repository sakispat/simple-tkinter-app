import tkinter as tk


def on_button_click():
    label.config(text='Hello, Tkinter!')
    

# Initializ the main window
root = tk.Tk()
root.title('Simple Tkinter App')
root.geometry('300x200')

# Create a label widget
label = tk.Label(root, text='Welcome to Tkinter!', font=('Helvetica', 16))
label.pack(pady=20)

# Create a button widget
button = tk.Button(root, text='Click Me', command=on_button_click, font=('Helvetica', 12))
button.pack(pady=10)

# Start the main loop
root.mainloop()
