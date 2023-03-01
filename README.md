# encode-decode-bots
bots to encode and decode text and encryption

#### Binary-Bot

This program is a simple chatbot that encodes and decodes binary strings. It begins by printing a welcome message to the user, then enters a loop where it prompts the user to input text. If the user enters "exit," the program exits the loop and prints a closing message.

For non-"exit" inputs, the program first checks whether the input is binary or not by calling the is_binary() function. If the input is binary, the program calls the decode_binary() function to convert the binary string to a regular string and prints the decoded text. If the input is not binary, the program calls the encode_binary() function to convert the regular string to a binary string and prints the encoded text.

The encode_binary() function takes a regular string as input, converts each character in the string to its binary representation using the ord() and format() functions, and then joins the resulting binary strings together with spaces.

The decode_binary() function takes a binary string as input, splits the string into a list of binary strings using the split() method, converts each binary string to its corresponding character using the int() and chr() functions, and then joins the resulting characters together into a regular string.

The is_binary() function takes a string as input and returns True if all the characters in the string are either "0", "1", or " ", and False otherwise.

Finally, the program prints a closing message to the user.

#### Encoder-Bot

This is a Python script that provides a simple command-line interface for encoding and decoding strings using a combination of hexadecimal, binary, and base64 encoding.

The script contains two main functions: encode and decode. The encode function takes an input string, first encodes it in hexadecimal, then converts the resulting hexadecimal string to binary, and finally encodes the binary string in base64. The decode function performs the reverse process: it first decodes the base64-encoded string to binary, then converts the binary string to hexadecimal, and finally decodes the resulting hexadecimal string to the original input string.

The script runs in an infinite loop, prompting the user to enter a string to encode or decode. If the user enters "quit", the loop exits. Otherwise, the script attempts to decode the input string using the decode function. If decoding fails (i.e., the input string is not base64-encoded), the script assumes that the input string needs to be encoded and uses the encode function to encode it.

Overall, this script provides a simple way to encode and decode strings using a combination of popular encoding methods. It could be useful for situations where string data needs to be transmitted or stored in a format that is more compact or secure than plain text.

#### Hex-Bot

This code defines a chatbot that can encode and decode hexadecimal strings. The chatbot uses the codecs module, which provides functions for encoding and decoding various data formats, including hexadecimal.

The chatbot greets the user and prompts for input. If the input is "exit", the chatbot exits the loop and terminates. Otherwise, the chatbot attempts to decode the input using the codecs.decode() function. If the input is a valid hexadecimal string, the function returns the decoded string, which is then printed to the console. If the input is not a valid hexadecimal string, the codecs.encode() function is used to convert the input to hexadecimal, and the resulting string is printed to the console.

The chatbot distinguishes between two types of hexadecimal strings: those that start with "0x" and those that do not. If the input starts with "0x", the chatbot includes the "0x" prefix in the output.

Overall, this chatbot is a simple tool for encoding and decoding hexadecimal strings, which may be useful for developers or users working with low-level data formats.
