from webtest import TestApp
from home import *

app = TestApp(application)

def test_index():
    response = app.get('/')
    assert 'ForkinRio' in str(response)


