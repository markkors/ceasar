def encrypt_caesar(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            # Bepaal of het karakter een hoofdletter of een kleine letter is
            is_upper = char.isupper()
            
            # Versleutel het karakter
            char_code = ord(char) + shift
            if is_upper:
                if char_code > ord('Z'):
                    char_code -= 26
            else:
                if char_code > ord('z'):
                    char_code -= 26
            
            encrypted_text += chr(char_code)
        else:
            # Als het geen letter is, voeg het onveranderd toe aan de versleutelde tekst
            encrypted_text += char

    return encrypted_text

def decrypt_caesar(ciphertext, shift):
    # Decriptie is hetzelfde als encryptie met een negatieve verschuiving
    return encrypt_caesar(ciphertext, -shift)

# Voorbeeldgebruik
message = "Dit is een geheim bericht."
shift_value = 3

# Versleutelen
encrypted_message = encrypt_caesar(message, shift_value)
print("Versleutelde tekst:", encrypted_message)

# Ontsleutelen
decrypted_message = decrypt_caesar(encrypted_message, shift_value)
print("Ontsleutelde tekst:", decrypted_message)
