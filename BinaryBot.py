import sys

# Binary encoding functions
def encode_binary(string):
    binary_string = ' '.join(format(ord(char), 'b') for char in string)
    return binary_string

def decode_binary(string):
    binary_list = string.split(' ')
    decoded_string = ''.join([chr(int(char, 2)) for char in binary_list])
    return decoded_string

# Function to check if input is binary
def is_binary(string):
    return all(char in '01 ' for char in string)

# Opening message
print("Welcome to the Binary Chatbot! Enter 'exit' to quit.")

# User input loop
while True:
    text = input("Enter text: ")

    # Exit command
    if text == "exit":
        break

    if is_binary(text):
        decoded_text = decode_binary(text)
        print(f"Decoded text: {decoded_text}")
    else:
        encoded_text = encode_binary(text)
        print(f"Encoded text: {encoded_text}")

# Closing message
print("Thanks for using the Binary Chatbot!")
