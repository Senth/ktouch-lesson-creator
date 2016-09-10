from book import Lesson
import logging

class LessonCreator:
    """Creates lessons out of book chapters"""

    def __init__(self, bookName, minChars):
        self._bookName = bookName
        self._minChars = minChars

    def createLessons(self, chapters):
        logging.debug('createLessons()')
        self._lessons = list()

        for chapter in chapters:
            self._parseChapter(chapter)

        return self._lessons

    def _parseChapter(self, chapter):
        logging.debug('Parse chapter ' + chapter.getName())
        lessons = list()
        lesson = Lesson.Lesson(self._bookName, chapter.getName(), 1)
        logging.debug('New Lesson: ' + lesson.getName())

        for paragraph in chapter.getParagraphs():
            lesson.addParagraph(paragraph)
            logging.debug('Add paragraph with ' + str(paragraph.getCharCount()) + ' chars.')

            # End lesson - long enough
            if lesson.getCharCount() >= self._minChars:
                logging.debug('Lesson long enough (' + str(lesson.getCharCount()) + ' chars)')
                lessons.append(lesson)
                lesson = Lesson.Lesson(self._bookName, chapter.getName(), len(lessons) + 1)
                logging.debug('New Lesson: ' + lesson.getName())

        logging.debug('Done with chapter')
        # Merge last lesson (if too short)
        if lesson.getCharCount() > 0:
            if lesson.getCharCount() < self._minChars and len(lessons) > 0:
                logging.debug('Last lesson too short (' + str(lesson.getCharCount()) + ') merging with last lesson')
                prevLesson = lessons[-1]
                if prevLesson:
                    prevLesson.mergeLesson(lesson)
                    logging.debug('Previous lesson now contains ' + str(prevLesson.getCharCount()) + ' chars')
                else:
                    logging.debug('No previous lesson exists, creating lesson anyway')
                    lessons.append(lesson)
            else:
                lessons.append(lesson)

        # Add all lessons to lesson list
        self._lessons.extend(lessons)
