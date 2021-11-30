import http.client
import urllib.parse
import configparser
config = configparser.RawConfigParser()
config.read('config.properties')

def send_listing(message, url):
    ukey = config.get('Pushover', 'push.user_key')
    tkn = config.get('Pushover', 'push.token')

    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.parse.urlencode({
        "token": tkn,
        "user": ukey,
        "title": "New Ebay Listing!",
        "message": message,
        "url": url,
      }), {"Content-type": "application/x-www-form-urlencoded"})
    conn.getresponse()

def send_message(message):
    ukey = config.get('Pushover', 'push.user_key')
    tkn = config.get('Pushover', 'push.token')

    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.parse.urlencode({
        "token": tkn,
        "user": ukey,
        "message": message,
      }), {"Content-type": "application/x-www-form-urlencoded"})
    conn.getresponse()