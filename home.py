from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Home(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('ForkinRio')

application = webapp.WSGIApplication(
                                     [('/', Home)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
