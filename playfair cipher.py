# This function takes a key as input and generates the key matrix
# used for encryption and decryption in the Playfair cipher.
def generate_playfair_key(key):
    # Convert key to uppercase and replace 'J' with 'I'
    key = key.upper().replace('J', 'I')
    # Remove any spaces from the key
    key = key.replace(' ', '')
    # Remove duplicates and maintain order of the characters
    # EXAMPLE: if the word is 'jatin' then it should take 'iatn' but
    # if we are removing find function the key is taking in the alphabetical order 'aint'
    key = ''.join(sorted(set(key), key=key.find))

    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    # Add remaining letters of the alphabet that are not present in the key
    # ensuring that all letters are accounted for in the key.
    for char in alphabet:
        if char not in key:
            key += char
    #  Divides the key into 5-character segments to create the 5x5 key matrix.
    key_matrix = [key[i:i + 5] for i in range(0, 25, 5)]
    return key_matrix


# This function takes a matrix and a character as input
# and returns the row and column indices of that character in the matrix.
# It is used to find the positions of characters in the key matrix during encryption and decryption.

def find_position(matrix, char):
    # Find the row and column of a character in the key matrix
    # The function uses a loop to iterate through each row of the matrix using enumerate(matrix).
    # For each row, it checks if the character char is present in that row (if char in row).
    # If the character is found,
    # the function returns a tuple containing the row index (i) and the column index (row.index(char)).
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None


# This function encrypts plaintext using the Playfaircipher.
# It  first preprocesses the plaintext by converting it to uppercase and replacing 'J' with 'I'.
# If the length of the plaintext is odd, it adds a padding character('X') to make it even.
# The plaintext is then divided into pairs(digraphs).
# For each digraph, the positions in the key matrix are determined, and the corresponding ciphertext digraph is formed.
# The resulting ciphertext is returned.

def encrypt_playfair(plaintext, key):
    # Generate the key matrix
    key_matrix = generate_playfair_key(key)

    # Preprocess plaintext
    plaintext = plaintext.upper().replace('J', 'I')
    # Add padding character if the plain text length is odd
    if len(plaintext) % 2 != 0:
        plaintext += "X"
    # Divide plaintext into pairs (digraphs)
    plaintext_pairs = [plaintext[i:i + 2] for i in range(0, len(plaintext), 2)]

    # Encryption
    ciphertext = ''
    for pair in plaintext_pairs:
        # Find positions of characters in the key matrix
        row1, col1 = find_position(key_matrix, pair[0])
        row2, col2 = find_position(key_matrix, pair[1])
        # Apply Playfair rules for encryption
        if row1 == row2:
            ciphertext += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_matrix[row1][col2] + key_matrix[row2][col1]

    return ciphertext


def decrypt_playfair(ciphertext, key):
    # Generates the key matrix using the provided key.
    key_matrix = generate_playfair_key(key)

    # Preprocess ciphertext:Divides the ciphertext into pairs (digraphs) of two characters each.
    ciphertext_pairs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]

    # Decryption
    plaintext = ''
    for pair in ciphertext_pairs:
        # # Find positions of characters in the key matrix
        row1, col1 = find_position(key_matrix, pair[0])
        row2, col2 = find_position(key_matrix, pair[1])

        # Apply Playfair rules for decryption
        if row1 == row2:
            plaintext += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += key_matrix[row1][col2] + key_matrix[row2][col1]

    return plaintext


# The user is prompted to input the key and plaintext.
# The key matrix is generated using the generate_playfair_key function.
# The key matrix is then displayed to the user.
# The plaintext is encrypted using the Playfair cipher, and the resulting ciphertext is print.
# The ciphertext is decrypted using the Playfair cipher, and the resulting plaintext is print.
def main():
    # Take user input for the key and plaintext
    key = input("Enter the key for Playfair cipher: ")
    plaintext = input("Enter the plaintext to encrypt: ")

    length=len(plaintext)

    # Generate the key matrix using the provided key
    key_matrix = generate_playfair_key(key)

    # Display the key matrix
    print("Key Matrix:")
    for row in key_matrix:
        print("[", end=" ")
        print(", ".join(row), end=" ")
        print("]")

    # Encrypt the plaintext using the Playfair cipher
    ciphertext = encrypt_playfair(plaintext, key)

    # Decrypt the ciphertext to verify
    decrypt_text = decrypt_playfair(ciphertext, key)
    pt=decrypt_text[:-1] if len(decrypt_text) != length else decrypt_text
    # Print the results
    print("\nCiphertext:", ciphertext)
    print("\nPlaintext:", pt)


if __name__== "__main__":
    main()
