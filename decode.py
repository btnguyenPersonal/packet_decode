#!/usr/bin/env python3
import sys

def get_next_packet(bundle):
    version = int(bundle[:3], base=2)
    type_id = int(bundle[3:6], base=2)
    output = ""
    i = 6
    if type_id == 4:
        while (bundle[i] != '0'):
            output += bundle[i+1:i+5]
            i += 5
        output += bundle[i+1:i+5]
    elif type_id == 0:
        length = int(bundle[i:i+15], base=2)
        output += bundle[i+15:i+15+length]
    elif type_id == 1:
        length = int(bundle[i:i+11], base=2)
    return output

def main():
    if len(sys.argv) < 2:
        return -1
    file = open(sys.argv[1], "r")
    raw_msg = file.read()
    correct_len = (len(raw_msg) - 1) * 4
    msg = bin(int(raw_msg, 16))[2:]
    print(msg)
    while len(msg) < correct_len:
        msg = '0' + msg
    print(get_next_packet(msg))
    file.close()

if __name__ == "__main__":
    main()
