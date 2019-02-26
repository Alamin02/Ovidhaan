from flask_restful import Resource
from flask_restful import reqparse
from .db import get_db


class Search(Resource):
    def get(self):
        # Parsing the request arguments
        parser = reqparse.RequestParser()
        parser.add_argument('word', type=str)
        args = parser.parse_args()

        requested_word = args['word']

        # Connect to database
        db = get_db()
        c = db.cursor()

        if not requested_word:
            return {'words': []}

        c.execute('SELECT word FROM dictionary WHERE word LIKE ? ORDER BY word', ('{}%'.format(requested_word),))
        results = c.fetchmany(5)

        data = []

        for result in results:
            data.append(list(result)[0])

        return {'words': data}
