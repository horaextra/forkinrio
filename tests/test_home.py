from webtest import TestApp
from home import *

app = TestApp(application)

def test_index():
    response = app.get('/')
    assert '<img src="images/forkinrio.png" alt="ForkinRio" />' in str(response)

