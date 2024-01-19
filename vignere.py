# This function is responsible for generating a key that matches the length of the given message.
# It takes two parameters, st (the message) and key (the initial key).
# It first converts the key into a list of characters.
# If the length of the key is equal to the length of the message, it directly returns the key.
# If the length of the key is less than the length of the message,
# it shortens the key by removing characters from the end.
# If the length of the key is greater than the length of the message,
# it repeats characters from the key to match the length of the message.
def keyGeneration(st, key):
    key = list(key)  # Convert the key string into a list of characters
    try:
        if (len(st) == len(key)):  # Check if the length of the key is equal to the length of the message
            return key

        elif (len(st) < len(key)):  # Execute when the length of key is greater than the message
            size = len(st) - 1
            for i in range(len(key) - len(st)):
                del key[size - i]  # Remove excess characters from the end of the key
            return key
        else:  # Execute when the length of key is less than the message
            for i in range(len(st) - len(key)):
                key.append(key[i % len(key)])  # Repeat characters from the key to match the length of the message
            return key

    except:
        print("\nThe key is not aligning with the Message")


"""THE ENCRYPTION PART"""

# This function takes a message (st) and a key, and it performs encryption using the Vigenère cipher.
# It initializes an empty list lst to store the encrypted characters.
# It iterates through each character in the message and performs the encryption using the Vigenère cipher formula:
# (Pi + Ki) mod 26, where Pi is the plaintext character, Ki is the key character,
# and mod 26 ensures that the result remains within the range of the alphabet.
# The encrypted character is then converted back to a character and appended to the lst.
# Finally, the encrypted message is printed and returned.


def ciphertext(st, key):
    lst = []  # Initialize an empty list to store encrypted characters

    for i in range(len(st)):
        cipher = (ord(st[i]) + ord(key[i])) % 26  # Vigenère cipher encryption: (Pi + Ki) mod 26
        # Convert the result to ASCII value of 'A' to get the encrypted character
        cipher += ord('A')  # cipher = cipher + ord('A')
        lst.append(chr(cipher))  # Append the encrypted character to the list

    encrypted_message = "".join(lst)  # Join the list of encrypted characters to form the encrypted message
    print("\nThe Cipher TXT is", encrypted_message)
    print("THE cipher text in list :", lst)
    return encrypted_message


"""ASCII VALUES OF A TO Z
A = 65,B = 66,C = 67,D = 68,E = 69,F = 70,G = 71,H = 72,I = 73,J = 74,K = 75,L = 76,M = 77,N = 78,O = 79
P = 80,Q = 81,R = 82,S = 83,T = 84,U = 85,V = 86,W = 87,X = 88,Y = 89,Z = 90

ASCII VALUES OF a TO z
a = 97,b = 98,c = 99,d = 100,e = 101,f = 102,g = 103,h = 104,i = 105,j = 106,k = 107,l = 108.m = 109,n = 110,o = 111
p = 112,q = 113,r = 114,s = 115,t = 116,u = 117,v = 118,w = 119,x = 120,y = 121,z = 122



THE DECRYPTION PART"""


# This function takes an encrypted message (st) and a key, and it performs decryption using the Vigenère cipher.
# It follows a similar process as the ciphertext function, but uses the decryption formula: (Pi - Ki) mod 26.
# The decrypted character is then appended to the text list.
# The decrypted message is printed.
def plaintext(st, key):
    text = []  # Initialize an empty list to store decrypted characters

    for i in range(len(st)):
        plaintxt = (ord(st[i]) - ord(key[i])) % 26  # Vigenère cipher decryption: (Pi - Ki) mod 26
        plaintxt += ord('A')  # Convert the result to ASCII value of 'A' to get the decrypted character
        text.append(chr(plaintxt))  # Append the decrypted character to the list

    decrypted_message = "".join(text)  # Join the list of decrypted characters to form the decrypted message
    print("\nThe PLAIN TXT is", decrypted_message, "\n")

# The user is prompted to enter a message and a key.
# The keyGeneration function is used to generate a key that matches the length of the message.
# The ciphertext function is used to encrypt the message using the Vigenère cipher
# The plaintext function is used to decrypt the message back to its original form.


if __name__ == "__main__":
    # User input for the message and key, converted to uppercase for consistency
    st = input("Enter the message: ").upper()
    key = input("Enter the key: ").upper()

    # Print the original message and key
    print("THE MESSAGE WAS (", st, ") and The key is :(", key, ")")

    # Generate the key with the keyGeneration function
    key = keyGeneration(st, key)

    # Encrypt the message using the Vigenère cipher and print the result
    st = ciphertext(st, key)

    # Decrypt the message back to its original form and print the result
    plaintext(st, key)
