#!/usr/bin/python3
"""Log Parser"""

import sys
import re

fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
count = 0;
status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}
total_size = 0
for line in sys.stdin:
    if re.fullmatch(log_fmt, line):
        line = line.split(" ")
        file_size = int(line[-1].strip("\n"))
        status_code = line[-2]
        if status_code in status_codes_dict.keys():
            status_codes_dict[status_code] += 1
        total_size += file_size
        count += 1
        if count == 10:
            try:
                count = 0
                print("File size: {}".format(total_size))
                for key, value in sorted(status_codes_dict.items()):
                    if value != 0:
                        print("{}: {}".format(key, value))
            except(KeyboardInterrupt, EOFError):
                print("File size: {}".format(total_size))
                for key, value in sorted(status_codes_dict.items()):
                    if value != 0:
                        print("{}: {}".format(key, value))
