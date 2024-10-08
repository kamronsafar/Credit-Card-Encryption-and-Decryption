from cryptography.fernet import Fernet

#generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

#sample credit card number
credit_card_number = "1234-5678-9876-5432"

#encrypt the credit card number
encrypted_cc = cipher_suite.encrypt(credit_card_number.encode())
print("Encrypted Credit Card Number:", encrypted_cc)

#decrypt the credit card number
decrypted_cc = cipher_suite.decrypt(encrypted_cc).decode()
print("Decrypted Credit Card Number:", decrypted_cc)
