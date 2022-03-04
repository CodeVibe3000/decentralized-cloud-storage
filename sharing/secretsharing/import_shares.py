import zlib

def import_shares(file_name, num_shares):
    shares = []

    for i in range(num_shares):
        with open(file_name+"_share_" + str(i) + ".txt", "rb") as f:
            shares.append(str(zlib.decompress(f.read()))[2:-1])

    return shares