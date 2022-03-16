import pickle

def import_shares(file_name, num_shares):

    shares = []

    for i in range(num_shares):
        with open(file_name+"_share_" + str(i) + ".txt", "rb") as f:
            shares.append(pickle.loads(f.read()))

    return shares
    