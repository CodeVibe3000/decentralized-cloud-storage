from secretsharing import *

shares = generate_shares_from_file("lipsum.txt", 10, 3)

reconstructed = reconstruct_secret_from_file(shares[:3])

print(reconstructed)