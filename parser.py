import re
from book import Chapter

class Parser:
    """Parses a book and converts it into chapters"""
    sentenceEndCharsPattern = '.*[\.\?][\'\"]?$'
    chapterStartsWith = 'Chapter(.*)'
    paragraphStartPattern = '\s.*'

    def __init__(self, filename, ignore=None):
        self._ignore = ignore
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

    def _parseLine(self, line):
        # Remove newline, ignore pattern, and trailing characters
        line = re.sub('\n', '', line)
        line = line.rstrip()
        if self._ignore:
            line = re.sub(self._ignore, '', line)

        if len(line) > 0:
            # Found (maybe) end of paragraph
            if re.search(Parser.sentenceEndCharsPattern, line):
                self._paragraphMightEnd = True

            # New chapter?
            chapterMatch = re.match(Parser.chapterStartsWith, line)
            if chapterMatch:
                self._endChapter()
                self._startChapter(chapterMatch.group(1).strip())

            # New paragraph?
            if self._paragraphMightEnd and re.match(Parser.paragraphStartPattern, line):
                self._endParagraph()

            # Add paragraph text
            if len(self._paragraph) > 0:
                self._paragraph += ' '
            self._paragraph += line.lstrip()

        # Paragraph has ended (after line break)
        elif self._paragraphMightEnd:
                self._endParagraph()

    def _endParagraph(self):
        if len(self._paragraph) > 0:
            self._chapter.addParagraph(self._paragraph)
            self._paragraph = ''
            self._paragraphMightEnd = False

    def _endChapter(self):
        if self._chapter:
            self._endParagraph()
            self._chapters.append(self._chapter)
            self._chapter = None

    def _startChapter(self, chapterName):
        if self._chapter:
            self._endChapter()

        self._chapter = Chapter(chapterName)
