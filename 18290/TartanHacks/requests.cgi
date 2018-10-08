#!/usr/bin/python

import cgi

print ("Content-Type: text/html\n\n")
print ("""
        <!DOCTYPE html>
        <html>
        <head> <script type = 'text/javascript' src = "hello.js"></script> </head>
        <Title> Hello in HTML </Title>
        <body><script type = 'text/javascript'>
          hello();
            </script></body>
            </html>""")
