import sqlite3

conn = sqlite3.connect('../database-new.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS dictionary (
            word text,
            meaning text
            )""")


class SaveItemPipeline(object):

    @staticmethod
    def process_item(item, spider):

        # Check if already exists on the database to avoid duplicate
        c.execute('SELECT word, meaning FROM dictionary WHERE word = ?', ('{}'.format(item['word']),))
        found_word = c.fetchone()

        # If the word is not a duplicate then save it
        if found_word is None:
            c.execute('INSERT INTO dictionary VALUES ( ?, ?)',
                      ('{}'.format(item['word']), '{}'.format(item['meaning']),))
            conn.commit()

        return item
