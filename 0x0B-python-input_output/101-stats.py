#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""


import sys
import signal

count = 1
f_size = 0
status_c = {'200': 0, '301': 0, '400': 0, '401': 0,
            '403': 0, '404': 0, '405': 0, '500': 0}


def print_summary():
    """Function prints a summary of data"""
    sorted_status = sorted(status_c)
    print("File size: {}".format(f_size))
    for elem in sorted_status:
        if status_c[elem] != 0:
            print("{}: {}".format(elem, status_c[elem]))


def signal_handler(sig, frame):
    """Function signal handler"""
    print_summary()
    sys.exit(0)

for line in sys.stdin:
    l = line.split()
    f_size += int(l[8])
    status_c[l[7]] += 1
    if count == 10:
        print_summary()
        count = 0
    count += 1
    signal.signal(signal.SIGINT, signal_handler)
