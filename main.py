import string

rangeOfLetters = list(string.ascii_lowercase)

def encodeLetters(shift, word):
    encoded_word = ""
    for c in word:
        if c in rangeOfLetters:
            index = rangeOfLetters.index(c)
            encoded_index = (index + shift) % len(rangeOfLetters)
            encoded_char = rangeOfLetters[encoded_index]
            encoded_word += encoded_char
        else:
            encoded_word += c  # If character not in rangeOfLetters, keep it unchanged
    return encoded_word

shift = int(input("Please enter the shift value. \n"))
choiceOfProcess = input("Please type if you would like to encode or decode? \n")
word = input("Please enter the word to be encoded or decoded. \n")

if choiceOfProcess.lower() == 'encode':
    encoded_word = encodeLetters(shift, word.lower())
    print("Encoded word:", encoded_word)
elif choiceOfProcess.lower() == 'decode':
    decoded_word = encodeLetters(-shift, word.lower())  # Decoding is just encoding with negative shift
    print("Decoded word:", decoded_word)
else:
    print("Invalid choice of process. Please enter 'encode' or 'decode'.")
