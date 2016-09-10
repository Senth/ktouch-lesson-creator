from os import path

class KtouchImporter:
    """Imports KTouch lessons' into its DB"""
    dbLocation = path.join(path.expanduser('~'), '.local/ktouch/DB/profiles.db')
    TABLE_NAME = 'custom_lesson'
    COL_ID = 'id'
    COL_TITLE = 'title'
    COL_TEXT = 'text'
    COL_LAYOUT_NAME = 'keyboard_layout'

    def import(self, lessons):
