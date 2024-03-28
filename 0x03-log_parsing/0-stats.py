#!/usr/bin/python3
import sys
import re
import signal

def print_statistics():
    print("File size: {}".format(file_sizes))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

file_sizes = 0
status_codes = {}
line_count = 0

line_pattern = re.compile(r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

for line in sys.stdin:
    match = line_pattern.match(line.strip())
    if match:
        status_code, file_size = match.groups()
        file_sizes += int(file_size)
        status_codes[status_code] = status_codes.get(status_code, 0) + 1

    line_count += 1
    if line_count % 10 == 0:
        print_statistics()

print_statistics()

