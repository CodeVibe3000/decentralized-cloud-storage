from secretsharing import *
from p2p import *
import sys

if len(sys.argv) != 4:
    print("Invalid arguments")
    sys.exit()

file_name = sys.argv[1]

shares = generate_shares_from_file(file_name, int(sys.argv[2]), int(sys.argv[3]))

export_shares(shares, file_name)

peer = PeerToPeer(50000)

peer_ports = [50001, 50002, 50003]

for i in range(len(shares)):
    share_name = file_name+"_share_" + str(i) + ".pbz2"
    peer.send_file("127.0.0.1", peer_ports[i], share_name, share_name, "share")

for i in range(3):
    share_name = "rec_"+file_name+"_share_" + str(i) + ".pbz2"
    peer.request_file("127.0.0.1", peer_ports[i], share_name)

imported = import_shares("req_rec_"+file_name, int(sys.argv[3]))

reconstructed = reconstruct_secret_from_file(imported[:int(sys.argv[3])], file_name)
