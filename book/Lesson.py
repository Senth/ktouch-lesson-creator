from uuid import uuid4
import textwrap

class Lesson:
    """A section of a chapter that is created as a lesson"""
    lineLengthMax = 60

    def __init__(self, bookName, chapterName, sectionCount):
        # Generate UUID
        self._id = str(uuid4())
        self._text = ''

        # Create Lesson Name
        self._name = bookName + ' - ' + chapterName + ' ' + str(sectionCount)

    def addParagraph(self, paragraph):
        if len(self._text) > 0:
            self._text += ' '

        self._text += paragraph.getText()

    def mergeLesson(self, lesson):
        if lesson:
            self._text += ' ' + lesson.getText()

    def getCharCount(self):
        if self._text:
            return len(self._text)
        else:
            return 0
    
    def getId(self):
        return self._id

    def getText(self):
        return self._text

    def getTextWrapped(self):
        textLines = textwrap.wrap(self._text, Lesson.lineLengthMax)
        wrappedText = ''
        for textLine in textLines:
            wrappedText += textLine + '\n'
        return wrappedText[:-1]


    def getName(self):
        return self._name
