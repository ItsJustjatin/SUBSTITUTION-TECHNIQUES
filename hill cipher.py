# uppercase() function takes a string letter as input and converts any lowercase letters to uppercase.
# It ignores non-alphabetic characters.
# It uses ASCII values to check if a character is a lowercase letter and then converts it to uppercase if needed.
def up(letter):
    text1 = ""  # Initialize an empty string to store the result
    for i in letter:
        # Condition ord('a') <= ord(i) <= ord('z') checks
        # if the ASCII value of i is within the range of lowercase letters
        # If this condition is true,it means 'i' is a lowercase letter

        if ord('a') <= ord(i) <= ord('z'):              # ord() returns the ASCII value.
            # If 'i' is a lowercase letter, this line converts it to uppercase.
            text2 = chr(ord(i) - 32)                     # EX: ASCII value of a-97
            text1 = text1 + text2                        # 97-32=65(ASCII value of A)
        elif ord('A') <= ord(i) <= ord('Z'):
            # If the character is already uppercase,keep it same
            text2 = i
            text1 = text1 + text2
        else:
            # If a character is not an alphabet,print a message
            print("Not Alphabet")
    return text1

# This function removes spaces from a given string s.
# It iterates through each character in the string and appends non-space characters to a new string.
def space(s):
    text = ""  # Initialize an empty string to store characters without spaces
    for i in s:
        if ord(i) != 32:  # Check if the ASCII value of the character is not equal to 32 (the ASCII value for space)
            text += i  # Add the non-space character to the 'text' string
    return text  # Return the modified string without spaces


# This function performs matrix multiplication between two matrices a and b.
# It initializes a result matrix result with zeros and then performs the matrix multiplication using nested loops.
# The resulting matrix is then copied to a new matrix res.
def mat(a,b):
    # EX:
    # matrix_a = [[1, 2, 3, 4], [4, 5, 6, 4], [7, 8, 9, 4]]
    # row=len(matrix_a)
    # column=len(matrix_a[0])
    # print(row)
    # print(column)
    # OUTPUT:3 and 4
    row1 = len(a)       # Number of rows in matrix a
    row2 = len(b)       # Number of rows in matrix b
    col1 = len(a[0])    # Number of columns in matrix a
    col2 = len(b[0])    # Number of columns in matrix b

    # Initialize a result matrix with zeros
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Perform matrix multiplication
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result[i][j] += a[i][k] * b[k][j]           # result[i][j] = result[i][j] + a[i][k] * b[k][j]

    # Copy the result to a new matrix
    res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    m = 0
    for row in result:
        res[m] = row
        m += 1

    return res


# This function converts an uppercase letter to its corresponding numerical value (A=0, B=1, ..., Z=25).
def letter_to_number(letter):
    return ord(letter) - ord('A')


# This function converts a numerical value to its corresponding uppercase letter.
def number_to_letter(number):
    return chr(number + ord('A'))


# Prints a 3x3 matrix.
def print_matrix(matrix):
    for row in matrix:
        print(row)


# Calculates the modular inverse of a modulo m. This function is used in the determinant inverse calculation.
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1

    while a > 1:
        q = a // m  # Floor operator
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    return x1 + m0 if x1 < 0 else x1
# EX:Suppose we want to find the modular inverse of a = 3 modulo m = 11.
# Initialize m0 = 11, x0 = 0, and x1 = 1.
# Enter the loop since a > 1:
# Calculate q = 3 // 11, which is 0.
# Update m = 3 % 11, which is 3, and a = 11.
# Update x0 and x1 using the extended Euclidean algorithm: x0, x1 = 1, -3.
# The loop continues:
# Calculate q = 11 // 3, which is 3.
# Update m = 11 % 3, which is 2, and a = 3.
# Update x0 and x1 using the extended Euclidean algorithm: x0, x1 = -3, 10.
# The loop continues:
# Calculate q = 3 // 2, which is 1.
# Update m = 3 % 2, which is 1, and a = 2.
# Update x0 and x1 using the extended Euclidean algorithm: x0, x1 = 10, -13.
# The loop continues:
# Calculate q = 2 // 1, which is 2.
# Update m = 2 % 1, which is 0, and a = 1.
# Update x0 and x1 using the extended Euclidean algorithm: x0, x1 = -13, 23.
# The loop exits since a is now 1. Finally, the function returns x1 + m0 because x1 is negative.
# RESULT:23+11=


# Calculates the modular inverse of the determinant det modulo mod.
def det_inverse(det, mod):
    # Calculate the modular inverse of the determinant
    det_inv = mod_inverse(det, mod)

    # Return the modular inverse modulo the given modulus
    # The modulo operation ensures that the result is within the range [0, mod - 1].
    return det_inv % mod


# The adjugate function calculates the adjugate (or adjoint) of a 3x3 matrix.
# The adjugate matrix is used in the process of finding the inverse of a matrix.
# It returns a new 3x3 matrix where each element is calculated based on the formula for the adjugate:
# adjugate( A[i,j] ) = (-1)^(i+j).minor(A[i,j])
def adjugate(matrix):
    return [
        [matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1], matrix[0][2]*matrix[2][1] - matrix[0][1]*matrix[2][2], matrix[0][1]*matrix[1][2] - matrix[0][2]*matrix[1][1]],
        [matrix[1][2]*matrix[2][0] - matrix[1][0]*matrix[2][2], matrix[0][0]*matrix[2][2] - matrix[0][2]*matrix[2][0], matrix[0][2]*matrix[1][0] - matrix[0][0]*matrix[1][2]],
        [matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0], matrix[0][1]*matrix[2][0] - matrix[0][0]*matrix[2][1], matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]]
    ]


# The inverse_matrix function calculates the inverse of a 3x3 matrix modulo a given modulus (mod).
# The steps involve calculating the determinant, finding its modular inverse, computing the adjugate matrix,
# and finally obtaining the inverse matrix.
def inverse_matrix(matrix, mod):
    # Calculate the determinant of the 3x3 matrix
    det = (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
           matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
           matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])) % mod

    # Calculate the modular inverse of the determinant
    det_inv = det_inverse(det, mod)

    # Calculate the adjugate matrix
    adj = adjugate(matrix)

    # Calculate the inverse matrix using modular arithmetic
    # + mod) % mod: Add the modulus and take the result modulo the modulus again.
    # This step ensures that the result is non-negative and within the range [0, mod - 1].
    inv_matrix = [[((det_inv * adj[i][j]) % mod + mod) % mod for j in range(3)] for i in range(3)]

    return inv_matrix


# This function takes a key string as input, removes spaces, and converts it to uppercase using the up function.
# It then creates a 3x3 matrix from the key, where each element of the matrix corresponds to the numerical value
# of a letter in the key.
def create_key(key):
    # Remove spaces and convert to uppercase
    key = space(key)
    key = up(key)

    # Initialize a 3x3 matrix with zeros
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # Initializes a variable s to keep track of the position in the key string.
    s = 0
    for i in range(3):
        for j in range(3):
            # Assign the numerical value of the corresponding character to the matrix
            matrix[i][j] = letter_to_number(key[s])
            s = s + 1          # Updates the position in the key string.

    # Print the key matrix
    print("Key Matrix:")
    print_matrix(matrix)

    return matrix


# This function performs Hill Cipher encryption.
# It takes a plaintext and a key as input.
# The plaintext is processed to remove spaces and convert to uppercase.
# If the length of the plaintext is not a multiple of 3, it pads the plaintext with 'X' to make it a multiple of 3.
# The key is converted to a matrix using the create_key function.
# The plaintext is divided into blocks of 3 letters each,
# and each block is encrypted using matrix multiplication with the key matrix.
# The result is converted back to letters using the number_to_letter function.
def encryption(plaintext, key):
    # Remove spaces and convert to uppercase
    plaintext = space(plaintext)
    plaintext = up(plaintext)

    # Pad the plaintext with 'X' if its length is not a multiple of 3
    if len(plaintext) % 3 != 0:
        plaintext += 'X' * (3 - len(plaintext) % 3)             # plaintext = plaintext + 'X' * (3 - len(plaintext) % 3)

    # Create the key matrix
    keymat = create_key(key)

    # Convert the plaintext to a list of numerical values
    numtext = [letter_to_number(letter) for letter in plaintext]
    # EX:
    # If plaintext is "HELLO", and letter_to_number maps 'A' to 0, 'B' to 1, and so on,
    # then numtext might become [7, 4, 11, 11, 14] based on the numerical values of 'H', 'E', 'L', 'L', 'O' respectively

    # Initialize an empty string for the ciphertext
    et = ""

    # Process the plaintext in blocks of 3
    for i in range(0, len(numtext), 3):
        # Create a 3x1 block from the numerical values
        block = [[numtext[i]], [numtext[i + 1]], [numtext[i + 2]]]

        # Encrypt the block using the key matrix and mat function
        encrypted_block = mat(keymat, block)

        # Apply modulo 26 to each element in the encrypted block
        encrypted_block = [[num % 26 for num in row] for row in encrypted_block]

        # Convert the numerical values back to letters and append to the ciphertext
        et += number_to_letter(encrypted_block[0][0])                # et = et + number_to_letter(encrypted_block[0][0])
        et += number_to_letter(encrypted_block[1][0])
        et += number_to_letter(encrypted_block[2][0])

    # Return the ciphertext
    return et


# The decryption function is the decryption part of the Hill Cipher algorithm.
# It takes a ciphertext (ct) and a key (key) as input and returns the corresponding plaintext (dt).
def decryption(ct, key):
    # Process the ciphertext
    ct = space(ct)  # Remove spaces from the ciphertext
    ct = up(ct)  # Convert the ciphertext to uppercase

    # Create the key matrix and its inverse
    keymat = create_key(key)
    keymat_inv = inverse_matrix(keymat, 26)

    # Convert the ciphertext letters to numbers
    numtext = [letter_to_number(letter) for letter in ct]

    # Initialize an empty string for the decrypted text
    dt = ""

    # Decrypt the text in blocks of 3 letters
    for i in range(0, len(numtext), 3):
        # Create a block of numbers from the ciphertext
        block = [[numtext[i]], [numtext[i + 1]], [numtext[i + 2]]]

        # Decrypt the block using the inverse key matrix
        decrypted_block = mat(keymat_inv, block)

        # Apply modulo 26 to each element of the decrypted block
        decrypted_block = [[num % 26 for num in row] for row in decrypted_block]

        # Convert the numbers back to letters and append to the decrypted text
        dt += number_to_letter(decrypted_block[0][0])
        dt += number_to_letter(decrypted_block[1][0])
        dt += number_to_letter(decrypted_block[2][0])

    # Return the decrypted text
    return dt


key = input("ENTER THE KEY(9 CHARACTERS)")

while True:
    # Create the key matrix
    key_matrix = create_key(key)

    # Input plaintext from the user
    plaintext = input("Enter Plain Text: ")

    # Encrypt the plaintext
    ciphertext = encryption(plaintext, key)
    print("Cipher Text: ", ciphertext)

    # Decrypt the ciphertext and print
    decrypted_text = decryption(ciphertext, key)
    print("Decrypted Text: ", decrypted_text)
