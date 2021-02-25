from vigenere import Vigenere
import argparse


def main():
    parser = argparse.ArgumentParser(description='Vigenere cipher.')

    parser.add_argument('ciphertext', type=str, help='Cipher text for encryption')
    parser.add_argument('--encrypt', type=str, help='Text to encrypt')
    parser.add_argument('--decrypt', type=str, help='Text to decrypt')

    args = parser.parse_args()
    
    v = Vigenere(args.ciphertext)

    if args.encrypt:
        encrypted_text = v.encrypt(args.encrypt)
        print("Text to encrypt is: ", args.encrypt)
        print("Encrypted text is : ", encrypted_text)

    if args.decrypt:
        decrypted_text = v.decrypt(args.decrypt)
        print("Text to decrypt is: ", args.decrypt)
        print("Decrypted text is : ", decrypted_text)


if __name__ == '__main__':
    main()
