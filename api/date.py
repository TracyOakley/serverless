#https://vercel.com/docs/concepts/functions/serverless-functions/supported-languages#python

# http.server module from the standard library for handling HTTP requests
from http.server import BaseHTTPRequestHandler
# datetime module from the standard library for handling dates in python
from datetime import datetime

# declaring a new subclass called handler that extends BaseHTTPRequestHandler
class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    return

# when you "Visit" Button from Vercel (get 404 error) you have to add /api/date to url to get the date to show up