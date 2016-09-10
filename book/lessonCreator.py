from .book import Lesson

class LessonCreator:
    """Creates lessons out of book chapters"""
    minChars = 3000

    def createLessons(self, chapters):
        self._lessons = list()

        for chapter in chapters:
            self._parseChapter(chapter)

        return self._lessons

    def _parseChapter(self, chapter):
        lessons = list()
        lesson = Lesson(chapter.getName(), 1)

        for paragraph in chapter.getParagraphs():
            lesson.addParagraph(paragraph)

            # End lesson - long enough
            if lesson.getCharCount() >= LessonCreator.minChars:
                lessons.append(lesson)
                lesson = Lesson(chapter.getName(), len(lessons) + 1)

        # Merge last lesson (if too short)
        if lesson.getCharCount() < LessonCreator.minChars and len(lessons) > 0:
            prevLesson = lessons[-1]
            prevLesson.mergeLesson(lesson)
        else:
            lessons.append(lesson)

        # Add all lessons to lesson list
        self._lessons.extend(lessons)
