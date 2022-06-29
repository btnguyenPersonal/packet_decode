#!/usr/bin/env python3
import sys

def main():
    if (len(sys.argv) < 2):
        return -1
    file = open(sys.argv[1], "r")
    raw_msg = file.read()
    correct_len = len(raw_msg * 4)
    msg = bin(int(raw_msg, 16))[2:]
    while (len(msg) < correct_len):
        msg = '0' + msg
    print(msg)
    file.close()

if __name__ == "__main__":
    main()
