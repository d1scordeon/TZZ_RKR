import tkinter as tk
from tkinter import messagebox, simpledialog
from cfb_cipher import CFB_encryptor, CFB_decryptor
import base64

#Клас, що відповідає за створення та керування графічним інтерфейсом
class crypto_app:
    #Ініціалізація елементів графічного інтерфейсу
    def __init__(self, root):
        self.root = root
        root.title("CFB encrypt and decrypt")

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt)
        self.decrypt_button.pack()
    #Метод для ініціалізації графічного інтерфейсу для функції шифрування
    def encrypt(self):
        plaintext = simpledialog.askstring("Input", "Enter text to encrypt", parent=self.root)
        if plaintext:
            encryptor = CFB_encryptor()
            iv, encrypted_text = encryptor.encrypt(plaintext)
            key = base64.b64encode(encryptor.key).decode('utf-8')

            messagebox.showinfo("Result", f"Encrypted: {encrypted_text}\nKey: {key}\nIV: {iv}")

            with open("encrypted_data.txt", "w") as file:
                file.write(f"Key: {key}\n")
                file.write(f"IV: {iv}\n")
                file.write(f"Encrypted Text: {encrypted_text}\n")

    # Метод для ініціалізації графічного інтерфейсу для функції дешифрування
    def decrypt(self):
        encrypted_text = simpledialog.askstring("Input", "Enter encrypted text", parent=self.root)
        key = simpledialog.askstring("Input", "Enter encryption key", parent=self.root)
        iv = simpledialog.askstring("Input", "Enter IV", parent=self.root)

        if encrypted_text and key and iv:
            try:
                decryptor = CFB_decryptor(base64.b64decode(key))
                decrypted_text = decryptor.decrypt(iv, encrypted_text)
                messagebox.showinfo("Result", f"Decrypted: {decrypted_text}")

                with open("decrypted_data.txt", "w") as file:
                    file.write(f"Decrypted Text: {decrypted_text}\n")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = crypto_app(root)
    root.mainloop()
