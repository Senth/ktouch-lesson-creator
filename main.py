#!/usr/bin/python3

import argparse

scriptDescription = "Parse a book and import it into KTouch\n\nThe book's format should contain chapters. Chapters begin on a new line where the first character will be 'Chapter' (by default) following the chapter's name. Each paragraph in the chapters starts with an empty line or a line that starts with at least one whitespace character. By default each lesson created will contain at least 3000 characters, roughly 600 words." 

parser = argparse.ArgumentParser(description=scriptDescription)
parser.add_argument('file', type=argparse.FileType('r'), help='The book to parse')
parser.add_argument('bookName', help="The book's name in KTouch")
parser.add_argument('--ignorePattern', help="Ignore this pattern on any line")
parser.add_argument('--minChars', type=int, default=3000, help="Minimum number of characters for each lesson")
parser.add_argument('--profileId', type=int, default=1, help="KTouch profile to add the custom lesson to")
parser.add_argument('--keyboardLayout', default='us', help="Keyboard layout to add the custom lesson to")
parser.add_argument('--db', help='Custom DB location. If not specified it uses the default KTouch DB location.')
parser.add_argument('--chapterBeginPattern', default='Chapter(.*)', help='Regex pattern for chapter beginnings. Should contain a group.')

