# User Input
text = input("Enter your message: ")

# Variable that recieves the shift value input.
shift_value = input("Enter a shift value between 1 and 25:")

# Variable in which the cipher text will be generated from. 
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# If the user enters a character that is not a number, an exception will be raised. 
if not shift_value.isdigit():
        raise ValueError("The shift value entered must be a number")

shift_value = int(shift_value)
# If the user does not enter a number between 1 and 25, an exception will be raised.
if not (1 <= shift_value <= 25):
    raise ValueError("The shift value entered must be between 1 and 25")

# Variable will store a list of characters appended from the for loop. 
result = []

# Process each character in the input text
for char in text:
    # Encrypt alphabetic characters
    if char.isalpha():  
        # Check if character is uppercase
        is_upper = char.isupper()  
        # Convert to lowercase for indexing
        char = char.lower()  
        # For each character in text, the for loop will move the character along in relation 
        # to its position in the alphabet variable. The number of spaces the character will be moved along will be specified in 
        # shift_value. 
        new_char = alphabet[(alphabet.index(char) + shift_value) % len(alphabet)]
        if is_upper:
            # Convert back to uppercase if needed
            new_char = new_char.upper()  
        result.append(new_char)
    # Append non-alphabetic characters as-is
    else:  
        result.append(char)
cipher = "".join(result)
print("Your cipher text is:",cipher)
