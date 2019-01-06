#!/usr/bin/env python3
import argparse
import re
from PyPDF2 import PdfFileReader

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file") 	# naming it "file"
    args = parser.parse_args()
    f = open(args.file, 'rb')
    reader = PdfFileReader(f)
    contents = reader.getPage(0).extractText()
    f.close()

    text = 'aa33bbb44'
    re.findall('\d+',contents)

    print(contents)

    #pull out file/date/file type
    #identify compound number
    #identify file type (first run vs integrity check)
    #identify date of run



if __name__ == "__main__":
    main()
