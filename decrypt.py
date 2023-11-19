from cfb_cipher import CFB_decryptor
import base64

#Функція входу до програми
def main():
    encrypted_text = input("Enter the encrypted text: ") #введення шифротексту
    key = input("Enter the encryption key: ") #введення ключа
    iv = input("Enter the IV: ") #введення вектору ініціалізації

    decryptor = CFB_decryptor(base64.b64decode(key)) #параметр, що ініціалізує клас дешифрації
    decrypted_text = decryptor.decrypt(iv, encrypted_text) #параметр, що дешифрує текст

    print("Decrypted Text:", decrypted_text) #виведення шифротексту
    #Зберігання файлу
    with open("decrypted_data.txt", "w") as file:
        file.write(f"Decrypted Text: {decrypted_text}\n")


if __name__ == "__main__":
    main()
