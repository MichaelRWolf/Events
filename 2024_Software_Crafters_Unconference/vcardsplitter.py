#!/usr/bin/env python3

import os
import sys
import vobject

def split_vcards(vcard_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(vcard_file, 'r', encoding='utf-8') as file:
        vcards = vobject.readComponents(file)
        
        for vcard in vcards:
            if hasattr(vcard, 'fn'):
                fn = vcard.fn.value.strip()
                fn_safe = ''.join([c if c.isalnum() or c == '_' else '_' for c in fn])
                output_file = os.path.join(output_dir, f"{fn_safe}.vcf")
                with open(output_file, 'w', encoding='utf-8') as out_file:
                    out_file.write(vcard.serialize())
                print(f"Written: {output_file}")
            else:
                print(f"Warning: No FN field found in vCard entry:\n{vcard.serialize()}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split_vcards.py <vcard_file> <output_directory>")
        sys.exit(1)

    vcard_file = sys.argv[1]
    output_dir = sys.argv[2]

    split_vcards(vcard_file, output_dir)
