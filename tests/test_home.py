from webtest import TestApp
from home import *

app = TestApp(application)

def test_index():
    response = app.get('/')
    assert '<img src="images/forkinrio_logotipo.png"/>' in str(response)


