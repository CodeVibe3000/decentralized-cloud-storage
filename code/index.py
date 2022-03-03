from secretsharing import *

file_name = "lipsum.txt"

shares = generate_shares_from_file(file_name, 10, 3)

reconstructed = reconstruct_secret_from_file(shares[:3], file_name)
