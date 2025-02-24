import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
import cv2
import os

# Function to encode message into an image
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

# Function to decode message from an image
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

# GUI setup
root = tk.Tk()
root.title("Image Steganography")
root.geometry("300x200")
root.config(bg="lightgray")

tk.Label(root, text="Image Steganography", font=("Arial", 14, "bold"), bg="lightgray").pack(pady=10)
tk.Button(root, text="Encode Image", font=("Arial", 12), command=encode_message).pack(pady=5)
tk.Button(root, text="Decode Image", font=("Arial", 12), command=decode_message).pack(pady=5)

root.mainloop()
