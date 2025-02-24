import cv2
from tkinter import filedialog, messagebox, simpledialog

def encode_message():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not filepath:
        return
    
    img = cv2.imread(filepath)
    if img is None:
        messagebox.showerror("Error", "Invalid image file!")
        return
    
    msg = simpledialog.askstring("Input", "Enter secret message:")
    password = simpledialog.askstring("Input", "Enter a passcode:", show='*')
    
    if not msg or not password:
        messagebox.showerror("Error", "Message and password cannot be empty!")
        return
    
    d = {chr(i): i for i in range(255)}
    n, m, z = 0, 0, 0
    
    for char in msg:
        if n >= img.shape[0] or m >= img.shape[1]:
            messagebox.showerror("Error", "Message too long for the image!")
            return
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        cv2.imwrite(save_path, img)
        messagebox.showinfo("Success", "Message encoded and image saved!")
