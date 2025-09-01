import sys


input_file = sys.argv[1]
output_file = sys.argv[2]

with open(output_file, "w", encoding="utf-8") as file:
    file.write('test')
