#!/usr/bin/env python

import BaseHTTPServer
import SimpleHTTPServer
import urlparse
import sqlite3
import sys

PORT = 8081
DB_PATH = "/var/tmp/ip.db"

# example:
# $ wget -O - -q -t1 http://example.com:8081/ip?host=machineid

def store(host, ip):
    print "storing %s=%s" % (host, ip)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS hosts (host UNIQUE, ip);')
    cur.execute('INSERT OR REPLACE INTO hosts (host, ip) VALUES (?, ?)', (host, ip))
    conn.commit()
    cur.close()

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        o = urlparse.urlparse(self.path)
        if (o.path == '/ip'):
            try:
                q = urlparse.parse_qs(o.query)
                host = q['host'][0]
                ip = self.client_address[0]
                result = "ok %s=%s\n" % (host, ip)
                store(host, ip)
            except:
                result = "error\n"
                print sys.exc_info()
        else:
            result = "error\n"
        self.wfile.write(result)


if __name__ == "__main__":
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, MyHandler)
    print "serving on port %d, db is %s ..." % (PORT, DB_PATH)
    server.serve_forever()

