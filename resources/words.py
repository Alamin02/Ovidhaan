from flask_restful import Resource
from .db import get_db


class Words(Resource):
    def get(self, word):
        # Connect to database
        db = get_db()
        c = db.cursor()

        c.execute('SELECT word, meaning FROM dictionary WHERE word = ?', ('{}'.format(word),))
        result = c.fetchone()

        if not result:
            return {'word': []}

        return {'word': list(result)}
