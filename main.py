import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()

label_1 = tk.Label(text="Hello, Tkinter")
label_2 = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label_1.pack()
label_2.pack()

text_box = tk.Text()
text_box.pack()
window.mainloop()
