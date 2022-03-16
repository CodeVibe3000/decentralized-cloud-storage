from .pickleutils import compressed_pickle

def export_shares(shares, file_name):
    for i in range(len(shares)):
        compressed_pickle(file_name+"_share_" + str(i), shares[i])