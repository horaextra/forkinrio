import os
from google.appengine.ext.webapp import template

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Home(webapp.RequestHandler):
    def get(self):
#        self.response.headers['Content-Type'] = 'text/plain'
#        self.response.out.write('ForkinRio')
        
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, {}))

application = webapp.WSGIApplication(
                                     [('/', Home)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
