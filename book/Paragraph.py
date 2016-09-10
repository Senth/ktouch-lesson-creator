from re import findall

class Paragraph:
    """Paragraph of a chapter"""

    def __init__(self, text):
        self._text = text

    def getText(self):
        return self._text;

    def getWordCount(self):
        return findall(r'\w+', self._text);

    def getCharCount(self):
        return len(self._text)
