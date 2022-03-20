import os, sys
import cyrtranslit
from optparse import OptionParser
from langdetect import detect
parser = OptionParser()
parser.add_option("-e", "--ext", dest="ext",
                  help="Choose extention of files to be renamed", metavar="EXT")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

ext = options.ext
if ext is None:
    print('Error: You must specify file extantion\ntype -h for more information')
    sys.exit()
dir = os.getcwd()
counter = 0
for file in os.listdir(dir):
    if file.endswith(ext):
            new_file = file.split(".")
            if detect(new_file[0]) != 'en':
                new_file = cyrtranslit.to_cyrillic(new_file[0], "ru")
                os.rename(f'{dir}/{file}', f'{dir}/{new_file}.{ext}')
                counter += 1
                if options.verbose:
                    print(f'{file}' + ' renamed to ' + f'{new_file}.{ext}')

print(f'{counter}' + " files succesfully renamed")
