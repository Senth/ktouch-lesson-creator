class Chapter:
    """Chapter information for a book"""
    

    def __init__(self, name):
        self._name = name
        self._paragraphs = list()

    def addParagraph(self, paragraph):
        self._paragraphs.append(paragraph)

    def getWordCount(self):
        count = 0
        for paragraph in self._paragraphs:
            count += paragraph.getWordCount()
        return count

    def getCharCount(self):
        count = 0
        for paragraph in self._paragraphs:
            count += paragraph.getCharCount()
        return count

    def getParagraphs(self):
        return self._paragraphs
