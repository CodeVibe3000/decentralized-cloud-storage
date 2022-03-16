import pickle

def export_shares(shares, file_name):
    for i in range(len(shares)):
        with open(file_name+"_share_" + str(i) + ".txt", "wb") as f:
            pickled = pickle.dumps(shares[i])
            f.write(pickled)