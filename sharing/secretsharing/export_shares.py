import zlib

def export_shares(shares, file_name):
    for i in range(len(shares)):
        with open(file_name+"_share_" + str(i) + ".txt", "wb") as f:
            uncompressed = bytes(shares[i].encode())
            compressed = zlib.compress(uncompressed, zlib.Z_BEST_COMPRESSION)
            f.write(compressed)