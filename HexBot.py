import codecs

print("Hello, I am a Hex bot. I can encode and decode Hexadecimal.\n" + "Any input is automatically detected and either encoded or decoded. Type 'exit' to quit.")

while True:
    user_input = input("> ")
    if user_input == "exit":
        break
    
    try:
        # Attempt to decode input if it is in hexadecimal
        decoded_input = codecs.decode(user_input, 'hex').decode()
        if user_input.startswith("0x"):
            print("Decoded: " + "0x" + decoded_input.encode().hex())
        else:
            print("Decoded: " + decoded_input)
    except:
        # Convert input to hexadecimal
        encoded_input = codecs.encode(user_input.encode(), 'hex').decode()
        if user_input.startswith("0x"):
            print("Hex: " + encoded_input)
        else:
            print("Hex: " + "0x" + encoded_input)
