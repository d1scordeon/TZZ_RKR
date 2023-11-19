#Використання бібліотек для шифрування
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

#Клас шифрування тексту
class CFB_encryptor:
    #Ініціалізація ключа
    def __init__(self, key=None):
        self.key = key if key else get_random_bytes(16) #атрибут, де зберігається ключ

    #Функція шифрування
    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_CFB) #параметр, що приймає вибраний режим шифрування
        ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))#параметр, що шифрує та доповнує введений текст
        iv = base64.b64encode(cipher.iv).decode('utf-8')#параметр, що кодує ініціалізований вектор
        ct = base64.b64encode(ct_bytes).decode('utf-8')#параметр, що кодує шифротекст
        return iv, ct

#Клас дешифрування тексту
class CFB_decryptor:
    # Ініціалізація ключа
    def __init__(self, key):
        self.key = key

    #Функція дешифрування
    def decrypt(self, iv, ciphertext):
        iv = base64.b64decode(iv) #параметр, що приймає векторний ключ
        ct = base64.b64decode(ciphertext) #параметр, що приймає шифротекст
        cipher = AES.new(self.key, AES.MODE_CFB, iv=iv) #параметр, що приймає вибраний режим шифрування
        pt = unpad(cipher.decrypt(ct), AES.block_size) #параметр, у котрому використовується
        return pt.decode('utf-8')

