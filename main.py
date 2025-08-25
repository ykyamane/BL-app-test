#!/usr/bin/env python

import sys
import nibabel as nib
import os

def main(input_file, output_file):
    img = nib.load(input_file)
    header_str = str(img.header)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write(header_str)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)