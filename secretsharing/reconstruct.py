from .utils import *
import base64
import binascii


def reconstruct_secret_from_file(given_shares):
    
    shares_points = []

    for share in given_shares:
        decoded = base64.b64decode(share).decode('ascii')
        decoded = decoded.rstrip(decoded[-1])

        points = [[int(coord) for coord in point.split(',')] for point in decoded.split(';')]
        points = ([x for x in points if x])

        shares_points.append(points)

    reconstructions = [[] for i in range(len(max(shares_points, key=len)))]

    for points in shares_points:
        for i in range(len(points)):
                    reconstructions[i].append(points[i])

    reconstructed_numbers = []

    for shares in reconstructions:
        reconstructed_numbers.append(reconstruct_secret(shares))

    reconstructed_binary = " ".join(["{0:b}".format(i) for i in reconstructed_numbers])

    reconstructed_secret = "".join([chr(int(binary, 2)) for binary in reconstructed_binary.split(" ")])

    return reconstructed_secret

    