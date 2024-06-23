import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def customize_cipher(text, shift, operation):
    return hashfunc(text, shift, operation)

def hashfunc(plaintext, key, encrypt):
    output = []
    for c in plaintext:
        if c.isalpha():
            shift = key if encrypt else -key
            shifted = chr(ord(c) + shift)
            if c.isupper():
                if shifted > 'Z':
                    shifted = chr(ord(shifted) - 26)
                elif shifted < 'A':
                    shifted = chr(ord(shifted) + 26)
            elif c.islower():
                if shifted > 'z':
                    shifted = chr(ord(shifted) - 26)
                elif shifted < 'a':
                    shifted = chr(ord(shifted) + 26)
            output.append(shifted)
        else:
            output.append(c)
    return ''.join(output)

def execute_action():
    operation = operation_combo.get()
    is_encrypt = operation == "Encrypt"
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid shift value.")
        return
    
    text = text_entry.get()
    result = customize_cipher(text, shift, is_encrypt)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)

# Create the main window
root = tk.Tk()
root.title("Text Encrypter/Decrypter")
root.geometry("400x300")
root.configure(bg="lightgray")

# Create the panel and components
panel = tk.Frame(root, bg="lightgray")
panel.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

operation_label = tk.Label(panel, text="Operation:", bg="lightgray")
operation_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

operations = ["Encrypt", "Decrypt"]
operation_combo = ttk.Combobox(panel, values=operations)
operation_combo.grid(row=0, column=1, padx=10, pady=5)
operation_combo.current(0)

shift_label = tk.Label(panel, text="Shift:", bg="lightgray")
shift_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

shift_entry = tk.Entry(panel)
shift_entry.grid(row=1, column=1, padx=10, pady=5)

text_label = tk.Label(panel, text="Text:", bg="lightgray")
text_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

text_entry = tk.Entry(panel)
text_entry.grid(row=2, column=1, padx=10, pady=5)

execute_button = tk.Button(panel, text="Execute", command=execute_action)
execute_button.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

result_label = tk.Label(panel, text="Output:", bg="lightgray")
result_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

result_text = tk.Text(panel, height=5, width=30)
result_text.grid(row=4, column=1, padx=10, pady=5)

# Start the main loop
root.mainloop()
