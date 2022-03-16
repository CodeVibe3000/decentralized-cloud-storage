from .pickleutils import decompress_pickle

def import_shares(file_name, num_shares):

    shares = []

    for i in range(num_shares):
        shares.append(decompress_pickle(file_name + "_share_" + str(i)))

    return shares
    