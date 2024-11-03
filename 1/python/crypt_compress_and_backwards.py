import gzip
import base64
from cryptography.fernet import Fernet

# Генерация ключа для шифрования
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Данные для шифрования
data = "Lorem ipsum." * 5

# Шифрование данных
encrypted_data = cipher_suite.encrypt(data.encode('utf-8'))
print(f"Зашифрованные данные: {base64.urlsafe_b64encode(encrypted_data).decode()}")
print(f"Размер зашифрованных данных: {len(encrypted_data)} байт")

# Сжатие зашифрованных данных
compressed_data = gzip.compress(encrypted_data)
print(f"Сжатые данные: {base64.urlsafe_b64encode(compressed_data).decode()}")
print(f"Размер сжатых данных: {len(compressed_data)} байт")

# Распаковка сжатых данных
decompressed_data = gzip.decompress(compressed_data)

# Расшифровка данных
decrypted_data = cipher_suite.decrypt(decompressed_data).decode('utf-8')
print(f"Расшифрованные данные: {decrypted_data}")

