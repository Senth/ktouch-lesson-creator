from uuid import uuid4

class Lesson:
    """A section of a chapter that is created as a lesson"""
    profile_id = 1
    keyboard_layout_name = 'us'
    book_name = 'book'

    def __init__(self, chapter_name, section_count, paragraphs):
        self._text = ''
        for paragraph in paragraphs:
            self._text = paragraph.getText() + ' '
        
        # Remove the last space
        self._text = self._text[:-1]

        # Generate UUID
        self._id = str(uuid4())

        # Create Lesson Name
        self._name = Lesson.book_name + ' - ' + chapter_name + ' ' + str(section_count)

    def getId(self):
        return self._id

    def getText(self):
        return self._text

    def getName(self):
        return self._name
