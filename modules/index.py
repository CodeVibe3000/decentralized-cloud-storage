from secretsharing import *
import sys

if len(sys.argv) != 4:
    print("Invalid arguments")
    sys.exit()

file_name = sys.argv[1]

shares = generate_shares_from_file(file_name, int(sys.argv[2]), int(sys.argv[3]))

export_shares(shares, file_name)

imported = import_shares(file_name, int(sys.argv[3]))

reconstructed = reconstruct_secret_from_file(imported[:int(sys.argv[3])], file_name)
