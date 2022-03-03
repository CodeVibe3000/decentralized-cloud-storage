import zlib

def export_shares(shares, file_name):
    for i in range(len(shares)):
        with open(file_name+"_share_" + str(i) + ".txt", "wb") as f:
            f.write(zlib.compress(bytes(shares[i].encode()), zlib.Z_BEST_COMPRESSION))