alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
text = input("Type your message:").lower()
shift = int(input("Enter the shift number:"))

def encrypt(plain_text, shift_number):
    encoded_text = ""
   
    for letter in plain_text:
        position = alphabet.index(letter) #used to know the position in the list
        new_position = position + shift_number
        new_letter = alphabet[new_position]
        encoded_text += new_letter
    print(f"Your encoded text is {encoded_text}")

def decrypt(encoded_message, shifted_number):
    decoded_text =""
    for letter in encoded_message:
        position = alphabet.index(letter)
        new_position = position - shifted_number
        new_letter = alphabet[new_position]
        decoded_text += new_letter
    print(f"Your decoded text is {decoded_text}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Envalid input!!")
    
