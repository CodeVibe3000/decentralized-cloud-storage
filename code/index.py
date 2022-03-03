from secretsharing import *

file_name = "unknown.jpg"

shares = generate_shares_from_file(file_name, 10, 3)

export_shares(shares, file_name)

reconstructed = reconstruct_secret_from_file(shares[:3], file_name)
