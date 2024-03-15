# Cipher
This simple Python script implements a Caesar cipher encoder and decoder. The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

How to Use
* Ensure you have Python installed on your system.
* Clone this repository or download the caesar_cipher.py file.
* Run the script using the command python caesar_cipher.py.
* Follow the prompts to input the shift value, choose whether to encode or decode, and enter the word to be encoded or decoded.

**Example**

* Please enter the shift value.
  
  3
* Please type if you would like to encode or decode?
  
  encode
* Please enter the word to be encoded or decoded.
  
  hello
  
  Encoded word: khoor

**Functionality**
* The script accepts a shift value, which determines the number of positions each letter should be shifted.
* It supports encoding and decoding of messages.
* All letters are shifted in a cyclic manner, with 'z' looping back to 'a'.
  
**Code Explanation**
* The script consists of a function encodeLetters(shift, word) that performs the encoding or decoding based on the shift value provided. The main section of the script prompts the user for the shift value, choice 
  of encoding or decoding, and the word to be processed. It then prints the result accordingly.

**Security Note**
* Caesar cipher is a very basic encryption method and is not secure for transmitting sensitive information. It is primarily used for educational purposes or situations where minimal security is required. For 
  stronger encryption, consider using modern cryptographic techniques.


