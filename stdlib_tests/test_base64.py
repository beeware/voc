import base64

encoded_data = base64.b64encode(b'Here is the string to be encoded')
print("Base 64 Encoded data: ", encoded_data)
decoded_data = base64.b64decode(encoded_data)
print("Base 64 Decoded data: ", decoded_data)
