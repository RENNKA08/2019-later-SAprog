#! /usr/bin/env python
import sys
import io
import datetime
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Content-type: text/html\n")
print("<html>")
print(" <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"></head>")
print(" <body>")
print(  "システムアーキテクトプログラミング演習")
print(  "<br>")
print(   datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(" </body>")
print("</html>")