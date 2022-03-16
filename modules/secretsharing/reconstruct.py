from .utils import *
import os

def reconstruct_secret_from_file(given_shares, file_name):
    
    shares_points = given_shares

    reconstructions = [[] for i in range(len(max(shares_points, key=len)))]

    for points in shares_points:
        for i in range(len(points)):
                    reconstructions[i].append(points[i])

    reconstructed_numbers = []

    for shares in reconstructions:
        reconstructed_numbers.append(reconstruct_secret(shares))

    reconstructed_strings = [str(x) for x in reconstructed_numbers]

    reconstructed_numbers_new = []
    reconstructed_strings_new = []

    bytes_combined = 8

    for i in range(len(reconstructed_strings)):
        number = reconstructed_strings[i]
        n = 3
        if len(number) % 3 == 0:
            str_num = number
            if len(number) != bytes_combined*3 and i != len(reconstructed_strings)-1:
                str_num = (bytes_combined*3 - len(number))*"0" + number
            str_num = ([int((str_num[i:i+n])) for i in range(0, len(str_num), n)])
            reconstructed_numbers_new += (str_num)
        if len(number) % 3 != 0:
            str_num = ((3-len(number) % 3) * "0") + number
            if len(number) < bytes_combined*3-3 and i != len(reconstructed_strings)-1:
                str_num = (bytes_combined*3 - len(number))*"0" + number
            reconstructed_numbers_new += ([int((str_num[i:i+n])) for i in range(0, len(str_num), n)])

    reconstructed_secret = bytes(reconstructed_numbers_new)

    with open("reconstructed_"+file_name, 'wb') as f:
        f.write(reconstructed_secret)