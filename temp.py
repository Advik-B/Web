import os
import sys
import uncompyle6

try:
    your_directory = ''
    for dirpath, b, filenames in os.walk(sys.argv[1]):
        for filename in filenames:
            if not filename.endswith('.pyc'):
                continue

            filepath = dirpath + '/' + filename
            original_filename = filename.split('.')[0]
            original_filepath = dirpath + '/' + original_filename + '.py'
            with open(original_filepath, 'w') as f:
                uncompyle6.decompile_file(filepath, f)
except IndexError:
    print("Usage: python pyc2py.py /User/src")