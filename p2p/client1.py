from p2p import *
import random

peer = PeerToPeer(50001)
peer.request_file("127.0.0.1", 50000, "unknown.jpg")
# peer.send_message("127.0.0.1", 50000, "hello")