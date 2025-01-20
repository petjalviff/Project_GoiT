import string
from collections import Counter
import re

# Шифрування тексту за допомогою шифру Віженера
def vigenere_encrypt(plaintext, key):
    alphabet = string.ascii_uppercase
    key = key.upper()
    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = []
    
    key_index = 0
    for char in plaintext:
        if char in alphabet:
            char_index = alphabet.index(char)
            key_char = key[key_index % len(key)]
            key_char_index = alphabet.index(key_char)
            encrypted_char = alphabet[(char_index + key_char_index) % len(alphabet)]
            ciphertext.append(encrypted_char)
            key_index += 1
        else:
            ciphertext.append(char)
    
    return ''.join(ciphertext)

# Частотний аналіз для шифру Віженера
def frequency_analysis(ciphertext, key_length):
    segments = [''] * key_length
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            segments[i % key_length] += char
    
    frequency_tables = []
    for segment in segments:
        counter = Counter(segment)
        frequency_tables.append(counter)
    
    return frequency_tables

# Визначення довжини ключа за методом Касіскі
def kasiski_examination(ciphertext):
    distances = []
    for i in range(len(ciphertext) - 3):
        substring = ciphertext[i:i+3]
        for j in range(i + 3, len(ciphertext) - 3):
            if ciphertext[j:j+3] == substring:
                distances.append(j - i)
    
    # Визначаємо найбільш поширену відстань
    if not distances:
        return 0
    
    # Обчислюємо найбільш поширену відстань
    most_common_distance = Counter(distances).most_common(1)[0][0]
    return most_common_distance

# Дешифрування тексту за допомогою шифру Віженера
def vigenere_decrypt(ciphertext, key):
    alphabet = string.ascii_uppercase
    key = key.upper()
    decrypted_text = []
    
    key_index = 0
    for char in ciphertext:
        if char in alphabet:
            char_index = alphabet.index(char)
            key_char = key[key_index % len(key)]
            key_char_index = alphabet.index(key_char)
            decrypted_char = alphabet[(char_index - key_char_index) % len(alphabet)]
            decrypted_text.append(decrypted_char)
            key_index += 1
        else:
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)

# Приклад виконання шифрування та дешифрування
if __name__ == "__main__":
    # Крок 1: Шифрування тексту
    plaintext = "The Dursleys had everything they wanted, plus one secret, and they were most afraid that someone would find out about it. They thought they would die if anyone heard about the Potters. Mrs. Potter was Mrs. Dursley's sister, but they had not seen each other for several years. Mrs. Dursley pretended she didn't have a sister at all, because her sister and her no-nonsense husband were the complete opposite of the Dursleys. The Dursleys shuddered to think what the neighbors would say if they saw the Potters outside. The Dursleys knew that the Potters also had a son, but they had never seen him. That boy was another reason to stay away from the Potters: the Dursleys didn't want their Dudley hanging out with kids like that."
    key = "KEY"
    ciphertext = vigenere_encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)
    
    # Крок 2: Частотний аналіз
    key_length = len(key)
    frequency_tables = frequency_analysis(ciphertext, key_length)
    for i, table in enumerate(frequency_tables):
        print(f"Frequency table for segment {i+1}:")
        print(table)
    
    # Крок 3: Визначення довжини ключа (метод Касіскі)
    key_length_guess = kasiski_examination(ciphertext)
    print("Guessed key length using Kasiski method:", key_length_guess)
    
    # Крок 4: Дешифрування тексту
    decrypted_text = vigenere_decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)
