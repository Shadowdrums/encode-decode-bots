import base64

def encode(input_str):
    # Encode input string in hexadecimal
    hex_encoded = input_str.encode('utf-8').hex()
    
    # Convert hexadecimal string to binary
    binary_encoded = bin(int(hex_encoded, 16))[2:]
    
    # Encode binary string in base64
    base64_encoded = base64.b64encode(bytes(binary_encoded, 'utf-8')).decode('utf-8')
    
    return base64_encoded

def decode(input_str):
    # Decode base64 string to binary
    binary_decoded = base64.b64decode(input_str).decode('utf-8')
    
    # Convert binary string to hexadecimal
    hex_decoded = hex(int(binary_decoded, 2))[2:]
    
    # Convert hexadecimal string back to bytes
    bytes_decoded = bytes.fromhex(hex_decoded)
    
    # Decode bytes object to string
    original_str = bytes_decoded.decode('utf-8')
    
    return original_str

while True:
    # Prompt for input string to encode or decode
    input_str = input('Enter a string to encode or decode (or "quit" to exit): ')
    
    if input_str.lower() == 'quit':
        # Exit the loop if the user enters "quit"
        break
    
    try:
        # Attempt to decode the input string from base64
        decoded_str = decode(input_str)
        print(f'Decoded string: {decoded_str}')
    except:
        # If decoding fails, assume the input string is not base64-encoded and encode it
        encoded_str = encode(input_str)
        print(f'Encoded string: {encoded_str}')
