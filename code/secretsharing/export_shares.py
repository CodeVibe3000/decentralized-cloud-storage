def export_shares(shares, file_name):
    for i in range(len(shares)):
        with open(file_name+"_share_" + str(i) + ".txt", "w") as f:
            f.write(shares[i])