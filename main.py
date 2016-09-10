#!/usr/bin/python3

import argparse
from book import Lesson
from book import LessonCreator
import Parser
import KtouchImporter
import os.path
import sys
import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', filename='log.txt', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger().addHandler(logging.StreamHandler())

scriptDescription = "Parse a book and import it into KTouch\n\nThe book's format should contain chapters. Chapters begin on a new line where the first character will be 'Chapter' (by default) following the chapter's name. Each paragraph in the chapters starts with an empty line or a line that starts with at least one whitespace character. By default each lesson created will contain at least 3000 characters, roughly 600 words." 

parser = argparse.ArgumentParser(description=scriptDescription)
parser.add_argument('filename', help='The book to parse')
parser.add_argument('bookName', help="The book's name in KTouch")
parser.add_argument('--ignorePattern', help="Ignore this pattern on any line")
parser.add_argument('--minChars', type=int, default=3000, help="Minimum number of characters for each lesson")
parser.add_argument('--profileId', type=int, default=1, help="KTouch profile to add the custom lesson to")
parser.add_argument('--keyboardLayout', default='us', help="Keyboard layout to add the custom lesson to")
parser.add_argument('--db', help='Custom DB location. If not specified it uses the default KTouch DB location.')
parser.add_argument('--chapterBeginPattern', default='Chapter(.*)', help='Regex pattern for chapter beginnings. Should contain a group.')

args = parser.parse_args()

# Parse book
if not os.path.exists(args.filename):
    print('File "' + args.filename + '" not found!')
    sys.exit(-1)

bookParser = Parser.Parser(args.filename, args.chapterBeginPattern, args.ignorePattern)
chapters = bookParser.parse()
lessonCreator = LessonCreator.LessonCreator(args.bookName, args.minChars)
lessons = lessonCreator.createLessons(chapters)
ktouchImporter = KtouchImporter.KtouchImporter(args.db, args.profileId, args.keyboardLayout)
ktouchImporter.importLessons(lessons)
print('Done!')
