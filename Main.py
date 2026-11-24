def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha() and char.isascii():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def brute_force_decrypt(text):
    print("\n========== BRUTE FORCE RESULTS ==========")

    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(text, shift)
        print(f"Shift {shift:2}: {decrypted_text}")

    print("=========================================")


def get_shift():
    while True:
        try:
            shift = int(input("Enter shift key (integer): "))
            return shift % 26
        except ValueError:
            print("Invalid input! Please enter an integer.")


def main():
    while True:
        print("\n================================")
        print("       CAESAR CIPHER TOOL")
        print("================================")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Brute Force Decryption")
        print("4. Exit")
        print("================================")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            text = input("\nEnter text to encrypt: ")
            shift = get_shift()

            encrypted = caesar_encrypt(text, shift)

            print("\nEncrypted Text:", encrypted)

        elif choice == '2':
            text = input("\nEnter text to decrypt: ")
            shift = get_shift()

            decrypted = caesar_decrypt(text, shift)

            print("\nDecrypted Text:", decrypted)

        elif choice == '3':
            text = input("\nEnter encrypted text: ")

            brute_force_decrypt(text)

        elif choice == '4':
            print("\nThank you for using Caesar Cipher!")
            break

        else:
            print("\nInvalid choice! Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
