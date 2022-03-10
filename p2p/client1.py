from p2p import *

peer = PeerToPeer()
peer.send_file("127.0.0.1", 50000, "unknown.jpg", "received.jpg")