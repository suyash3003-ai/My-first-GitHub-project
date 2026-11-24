def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using a Caesar Cipher.
    """
    result = ""
    
    # Reverse the shift for decryption
    if mode == 'decrypt':
        shift = -shift
        
    for char in text:
        if char.isalpha():
            # Determine ASCII base (65 for 'A', 97 for 'a')
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around using modulo 26
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            # Keep spaces, numbers, and punctuation unchanged
            result += char
            
    return result

def brute_force_decrypt(ciphertext):
    """
    Tries all 25 possible shifts to crack a Caesar Cipher without a known key.
    """
    print("\n--- Brute-Force Results ---")
    for shift in range(1, 26):
        decrypted_text = caesar_cipher(ciphertext, shift, mode='decrypt')
        print(f"Shift {shift:2d}: {decrypted_text}")
    print("---------------------------\n")

def main():
    while True:
        print("=== Caesar Cipher Tool ===")
        print("1. Encrypt text")
        print("2. Decrypt text (with known shift)")
        print("3. Brute-force decrypt (unknown shift)")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift value (e.g., 3): "))
            print(f"\nEncrypted Text: {caesar_cipher(text, shift, 'encrypt')}\n")
            
        elif choice == '2':
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift value (e.g., 3): "))
            print(f"\nDecrypted Text: {caesar_cipher(text, shift, 'decrypt')}\n")
            
        elif choice == '3':
            text = input("Enter text to brute-force: ")
            brute_force_decrypt(text)
            
        elif choice == '4':
            print("Exiting program.")
            break
            
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()
