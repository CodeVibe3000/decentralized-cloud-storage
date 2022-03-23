from p2p import *
import sys

peer = PeerToPeer(int(sys.argv[1]))

peer.listen()