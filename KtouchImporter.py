from os import path
import sqlite3
import datetime
import shutil
import logging

class KtouchImporter:
    """Imports KTouch lessons' into its DB"""

    def __init__(self, dbLocation, profileId, keyboardLayoutName):
        self._profileId = profileId
        self._keyboardLayoutName = keyboardLayoutName

        if dbLocation:
            self._dbLocation = dbLocation
        else:
            self._dbLocation = path.join(path.expanduser('~'), '.kde4/share/apps/ktouch/profiles.db')

    def importLessons(self, lessons):
        self._backupDb()

        connection = sqlite3.connect(self._dbLocation)
        self._cursor = connection.cursor()

        for lesson in lessons:
            self._importLesson(lesson)

        connection.commit()
        connection.close()

    def _backupDb(self):
        backupTimestamp = datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S.bak')
        backupLocation = self._dbLocation + ' ' + backupTimestamp
        shutil.copy2(self._dbLocation, backupLocation)

    def _importLesson(self, lesson):
        logging.debug('Import Lesson: ' + lesson.getName() + '\n\n' + lesson.getTextWrapped())
        values = (lesson.getId(), self._profileId, lesson.getName(), lesson.getTextWrapped(), self._keyboardLayoutName)
        self._cursor.execute("INSERT INTO custom_lessons (id, profile_id, title, text, keyboard_layout_name) VALUES (?, ?, ?, ?, ?)", values)
