import tkinter as tk

# Function to encrypt the text
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt the text
def decrypt(text, shift):
    return encrypt(text, -shift)

# Function for the Encrypt button
def encrypt_text():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        encrypted_message = encrypt(text, shift)
        result_label.config(text=f"Encrypted message: {encrypted_message}")
    except ValueError:
        result_label.config(text="Please enter a valid shift value.")

# Function for the Decrypt button
def decrypt_text():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        decrypted_message = decrypt(text, shift)
        result_label.config(text=f"Decrypted message: {decrypted_message}")
    except ValueError:
        result_label.config(text="Please enter a valid shift value.")

# Creating the main window
root = tk.Tk()
root.title("Caesar Cipher")

# Labels and entries for text and shift input
label_text = tk.Label(root, text="Enter the message:")
label_text.pack()

entry_text = tk.Entry(root, width=50)
entry_text.pack()

label_shift = tk.Label(root, text="Enter the shift value:")
label_shift.pack()

entry_shift = tk.Entry(root, width=10)
entry_shift.pack()

# Buttons for Encrypt and Decrypt
button_encrypt = tk.Button(root, text="Encrypt", command=encrypt_text)
button_encrypt.pack(pady=5)

button_decrypt = tk.Button(root, text="Decrypt", command=decrypt_text)
button_decrypt.pack(pady=5)

# Label to display the result
result_label = tk.Label(root, text="", fg="blue", font=("Helvetica", 12))
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
