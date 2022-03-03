from .utils import *
import base64
import os


def convert_string_to_bytes(string):
    bytesv = b''
    for i in string:
        bytesv += struct.pack("B", ord(i))
    return bytesv


def reconstruct_secret_from_file(given_shares, file_name):
    
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

    reconstructed_secret = bytes(reconstructed_numbers)

    with open("reconstructed_"+file_name, 'wb') as f:
        f.write(reconstructed_secret)