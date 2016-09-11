import re
import logging
from book import Chapter
from book import Paragraph

class Parser:
    """Parses a book and converts it into chapters"""
    sentenceEndCharsPattern = '.*[\.\?][\'\"]?$'
    paragraphStartPattern = '\s.*'

    def __init__(self, filename, chapterBeginWith, ignore=None):
        self._ignore = ignore
        self._chapterBeginWith = chapterBeginWith
        self._filename = filename
        self._chapters = list()
        self._chapter = None
        self._paragraph = ''
        self._paragraphMightEnd = False

    def parse(self):
        with open(self._filename) as book_file:
            for line in book_file:
                self._parseLine(line)
        self._endChapter()
        return self._chapters

    def _parseLine(self, line):
        # Remove newline, ignore pattern, and trailing characters
        line = re.sub('\n', '', line)
        line = line.rstrip()
        if self._ignore:
            line = re.sub(self._ignore, '', line)

        logging.debug('Parse line: ' + line)

        if len(line) > 0:
            # Found (maybe) end of paragraph
            if re.search(Parser.sentenceEndCharsPattern, line):
                self._paragraphMightEnd = True

            # New paragraph?
            if self._paragraphMightEnd and re.match(Parser.paragraphStartPattern, line):
                self._endParagraph()

            # New chapter?
            chapterMatch = re.match(self._chapterBeginWith, line)
            if chapterMatch:
                self._endChapter()
                self._startChapter(chapterMatch.group(1).strip())
            # Add paragraph text
            else:
                # Add space between paragraphs
                if len(self._paragraph) > 0 and not self._paragraph.endswith('-'):
                    self._paragraph += ' '

                # Add to paragraph, double spaces are converted to single space
                self._paragraph += re.sub('\s+', ' ', line.strip()).strip()

        # Paragraph has ended (after line break)
        elif self._paragraphMightEnd:
                self._endParagraph()

    def _endParagraph(self):
        if self._paragraph and len(self._paragraph) > 0:
            logging.debug('End Paragraph')
            self._chapter.addParagraph(Paragraph.Paragraph(self._paragraph))
            self._paragraph = ''
            self._paragraphMightEnd = False

    def _endChapter(self):
        if self._chapter:
            logging.debug('End Chapter')
            self._endParagraph()
            self._chapters.append(self._chapter)
            self._chapter = None

    def _startChapter(self, chapterName):
        logging.debug('Start Chapter: ' + chapterName)
        if self._chapter:
            self._endChapter()

        self._paragraphMightEnd = False
        self._paragraph = ''
        self._chapter = Chapter.Chapter(chapterName)
