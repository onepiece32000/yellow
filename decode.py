#!/usr/bin/python3

import base64

str_example = "this is string example.....wow!!!"
str_encoded = base64.b64encode(str_example.encode('utf-8')).decode('utf-8')

print("Encoded string:", str_encoded)

str_decoded = base64.b64decode(str_encoded).decode('utf-8')
print("Decoded string:", str_decoded)

