from main import app
from my_log import LOG


def test_send_words():
    with app.test_client() as c:
        words = 'ball,eggs,pool,wild,daily'
        words = 'ball,ball,ball,ball,eggs,eggs,pool,pool,wild,daily'
        js = {'words': words}
        rv = c.post('/words', json=js)

        assert rv.status_code == 204, f'ERROR test_send_words: error code is {rv.status_code}'


def test_get_words_stat():
    with app.test_client() as c:
        rv = c.get('/words')

        assert rv.status_code == 200, f'ERROR test_get_words_stat: error code is {rv.status_code}'
        LOG.debug(f'test_get_words_stat : {rv.json}')


if __name__ == '__main__':
    test_send_words()
    test_get_words_stat()
