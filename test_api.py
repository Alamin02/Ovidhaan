from run import create_app

app = create_app()


def test_get_search_page():
    with app.test_client() as c:
        res = c.get('api/search?word=a')

        assert res.status_code == 200


def test_get_single_word():
    with app.test_client() as c:
        res = c.get('api/words/a')

        assert res.status_code == 200


def test_count_suggestion():
    with app.test_client() as c:
        res = c.get('api/search?word=a')

        assert len(res.json['words']) == 5


def test_get_if_null():
    with app.test_client() as c:
        res = c.get('api/search?word=')

        assert res.status_code == 200


def test_length_if_null():
    with app.test_client() as c:
        res = c.get('api/search?word=')

        assert len(res.json['words']) == 0
