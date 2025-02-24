import cv2
from tkinter import filedialog, messagebox, simpledialog

def decode_message():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not filepath:
        return
    
    img = cv2.imread(filepath)
    if img is None:
        messagebox.showerror("Error", "Invalid image file!")
        return
    
    password = simpledialog.askstring("Input", "Enter passcode for decryption:", show='*')
    
    if not password:
        messagebox.showerror("Error", "Password cannot be empty!")
        return
    
    message = ""
    n, m, z = 0, 0, 0
    c = {i: chr(i) for i in range(255)}
    
    try:
        while True:
            message += c.get(img[n, m, z], "")
            n += 1
            m += 1
            z = (z + 1) % 3
    except (IndexError, KeyError):
        messagebox.showinfo("Decrypted Message", f"Message: {message}")
