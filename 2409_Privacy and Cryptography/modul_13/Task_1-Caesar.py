import string
from collections import Counter

# Функція для шифрування тексту за допомогою шифру Цезаря
def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():  # Якщо символ є літерою
            # Перевірка на малі та великі літери
            start = ord('a') if char.islower() else ord('A')
            # Зсув літери в межах алфавіту
            result.append(chr((ord(char) - start + shift) % 26 + start))
        else:
            result.append(char)
    return ''.join(result)

# Функція для частотного аналізу
def frequency_analysis(text):
    # Очищаємо текст від неалфавітних символів
    text = ''.join([c.lower() for c in text if c.isalpha()])
    # Підрахунок частоти кожної літери
    frequency = Counter(text)
    total_letters = sum(frequency.values())
    # Вираховуємо відсоток для кожної літери
    return {char: count / total_letters * 100 for char, count in frequency.items()}

# Функція для розшифровки тексту
def decrypt_caesar_cipher(ciphertext, shift):
    return caesar_cipher(ciphertext, -shift)

# Приклад шифрування та частотного аналізу
if __name__ == "__main__":
    # Крок 1: Шифруємо текст
    original_text = """The Dursleys had everything they wanted, plus one secret, and they were most afraid that someone would find out about it. They thought they would die if anyone heard about the Potters. Mrs. Potter was Mrs. Dursley's sister, but they had not seen each other for several years. Mrs. Dursley pretended she didn't have a sister at all, because her sister and her no-nonsense husband were the complete opposite of the Dursleys. The Dursleys shuddered to think what the neighbors would say if they saw the Potters outside. The Dursleys knew that the Potters also had a son, but they had never seen him. That boy was another reason to stay away from the Potters: the Dursleys didn't want their Dudley hanging out with kids like that."""
    shift = 3
    encrypted_text = caesar_cipher(original_text, shift)
    print(f"Encrypted Text: {encrypted_text}")
    
    # Крок 2: Частотний аналіз шифрованого тексту
    freq_analysis = frequency_analysis(encrypted_text)
    print("Frequency Analysis of Encrypted Text:")
    for letter, freq in sorted(freq_analysis.items()):
        print(f"{letter}: {freq:.2f}%")
    
    # Крок 3: Розшифровуємо текст
    shift_decrypted=3
    decrypted_text = decrypt_caesar_cipher(encrypted_text, shift_decrypted)
    print(f"Decrypted Text: {decrypted_text}")
