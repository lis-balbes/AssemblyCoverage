import sys

file_name = sys.argv[1]
if file_name == '':
    print("Usage: python assembly_coverage.py <filename>")
    exit(1)

with open(file_name, 'r') as inp:
    print(inp.readline())
