from .utils import *
import base64
import random

def generate_shares_from_file(filename, num_shares, req):
    data = open(filename, "r").read()
    message_bytes = data.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    decoded_message_bytes = base64.b64decode(base64_bytes)
    decoded_message = decoded_message_bytes.decode('ascii')

    binary_encoded = [int(format(ord(x), 'b'), 2) for x in decoded_message]


    shares = [[] for i in binary_encoded]

    for i in range(len(binary_encoded)):
        shares_i = generate_shares(num_shares, req, binary_encoded[i])
        for j in range(len(shares_i)):
            shares[j].append(shares_i[j])

    shares_exported = []

    for share in shares:

        share_exported = ""

        for point in share:
            share_exported += str(point[0]) + "," + str(point[1]) + ";"

        share_exported = base64.b64encode(share_exported.encode('ascii'))
        shares_exported.append(share_exported.decode('ascii'))

    return shares_exported
