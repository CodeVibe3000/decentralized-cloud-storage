from .utils import *
from .constants import bytes_combined

def generate_shares_from_file(filename, num_shares, req):
    data = open(filename, "rb").read()

    binary_encoded = [x for x in data]

    str_binary_encoded = [str(x).zfill(3) for x in binary_encoded]

    binary_encoded = [int("".join(str_binary_encoded[i:i+bytes_combined])) for i in range(0, len(binary_encoded)-1, bytes_combined)]

    shares = [[] for i in range(num_shares)]

    for i in range(len(binary_encoded)):
        shares_i = generate_shares(num_shares, req, binary_encoded[i])
        for j in range(len(shares_i)):
            shares[j].append(shares_i[j])

    for i in range(len(shares)):
        shares[i] = [item for t in shares[i] for item in t]

    return shares
