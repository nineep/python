'''
Check a file exsit and that we can read the file
'''
from __futrue__ import print_function
import sys
import os

def usage():
    print('[-] Usage: python check_file.py [filename1] [filename2] ... [filenameN]')

# Readfile Functions which open the file that is passed to the script
def readfile(filename):
    with open(filename, 'r') as f:
        file = f.read()
    print(file)
    print()
    print('#'*80)
    print()

def main():
    # Check the arguments passed to the script
    if len(sys.argv) >= 2:
        filename = sys.argv[1:]

        filteredfilenames = list(filenames)
        # Iterate for each filename passed in command line argument
        for filename in filenames:
            if not os.path.isfile(filenames):   # Check the File exists
                print('[-] ' + filename ' does not exist.')
                filteredfilenames.remove(filename)  # Remove non existing files from filenames list
                continue

            # Check you can read the file
            if not os.access(filename, os.R_OK):
                print('[-] ' + filename + ' access denied')
                # Remove non readable filenames
                filteredfilesnames.remove(filename)
                continue

        # Read the content of each file that both exists and is readable
        for filename in filteredfilenames:
            # Display message and read the file contents
            print('[+] Reading form : ' + filename)
            readfile(filename)
    else:
        usage() # Print usage if not all parameters passed/checked

if __name__ == '__main__':
    main()
    
