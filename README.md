# **CipherShift**

CipherShift is a simple implementation of the Caesar cipher, a type of substitution cipher where each letter in the text is replaced by a letter with a fixed number of positions down or up the alphabet. This Python script allows you to encrypt messages by shifting the letters of the alphabet by a user-defined value.

 ## *Features*

Takes a string input from the user.
Encrypts alphabetic characters by shifting them by a user-defined shift value.
Handles both uppercase and lowercase characters.
Preserves non-alphabetic characters (e.g., spaces, punctuation).
Provides error handling for invalid input (non-numeric shift values, shift values outside the valid range of 1-25).

 ## *How to Use*

1. Clone the repository to your local machine:

    git clone https://github.com/Jordenproject/CipherShift.git


2. Navigate to the folder where the repository is located:

    cd CipherShift

3. Run the script:

    Ensure you have Python 3 installed on your machine. Then, run the script as follows:

    python3 cipher_shift.py

4. Input the message and shift value:

    • The program will prompt you to enter the message you'd like to encrypt.  
    • Enter a shift value between 1 and 25 (the number of positions to shift each letter in the alphabet).

5. Get the encrypted message:

    After entering the inputs, the program will output the encrypted message (cipher text).

 ## *Example*

<img width="1160" alt="Screenshot 2025-01-06 at 18 25 11" src="https://github.com/user-attachments/assets/459c4b7c-6779-4d78-a019-f76abe5668d5" />


In this example, the letter 'H' is shifted 3 places forward to 'K', 'e' becomes 'h', and so on. Non-alphabetic characters like spaces and punctuation are not altered.

 ## *Error Handling*

• If you enter a non-numeric shift value, the program will raise an error and prompt you to enter a valid number.

• If the shift value is not between 1 and 25, the program will raise an error and prompt you to enter a valid shift value.

 ## *How It Works*
 
1. User Input: The user is asked to input a message and a shift value.
3. Shift Validation: The program checks if the shift value is numeric and between 1 and 25.
5. Encryption Process: For each alphabetic character, the program shifts it by the specified amount. Non-alphabetic characters are left unchanged.
7. Result: The program outputs the encrypted message.

 ## *Contributions*
 
Feel free to fork this repository, make improvements, or submit issues and pull requests. All contributions are welcome!
