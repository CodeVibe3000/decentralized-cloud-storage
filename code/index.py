from secretsharing import *

file_name = "lipsum.txt"

shares = generate_shares_from_file(file_name, 10, 3)

export_shares(shares, file_name)

imported = import_shares(file_name, 10)

reconstructed = reconstruct_secret_from_file(imported[:3], file_name)
