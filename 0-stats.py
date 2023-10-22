#!/usr/bin/python3
"""Log parsing"""


import sys
import re

pattern = r'^([\d.]+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'

line_count = 0
status_code_list = [200, 301, 400, 401, 403, 404, 405, 500]
status_code_dict = {int(code): 0 for code in status_code_list}
total_file_size = 0

try:
    for line in sys.stdin:
        if re.match(pattern, line):
            parts = line.split()
            status_code = int(parts[7])
            file_size = parts[8]
            total_file_size += int(file_size)
            status_code_dict[status_code] += 1
            line_count += 1
            if line_count % 10 != 0:
                print("File_size: {}".format(total_file_size))
                for code in status_code_dict:
                    print("{}:{}".format(code, status_code_dict[code]))
except KeyboardInterrupt:
    print("File_size: {}".format(total_file_size))
    for code in status_code_dict:
        print("{}:{}".format(code, status_code_dict[code]))
