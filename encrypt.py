from cfb_cipher import CFB_encryptor
import base64

#Функція входу до програми
def main():
    text_to_encrypt = input("Enter the text to encrypt: ")  #параметр введення тексту
    encryptor = CFB_encryptor() #параметр ініціалізації класу шифратора
    iv, encrypted_text = encryptor.encrypt(text_to_encrypt) #викликання методу для шифрування тексту

    print("Encrypted Text:", encrypted_text) #виведення шифротексту
    print("Encryption Key:", base64.b64encode(encryptor.key).decode('utf-8')) #виведення ключа
    print("IV:", iv) #виведення вектору ініціалізації
    #Збереження файлу
    with open("encrypted_data.txt", "w") as file:
        file.write(f"Key: {base64.b64encode(encryptor.key).decode('utf-8')}\n")
        file.write(f"IV: {iv}\n")
        file.write(f"Encrypted Text: {encrypted_text}\n")


if __name__ == "__main__":
    main()
