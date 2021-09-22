#-*- coding:utf-8 -*-
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class RequestHandler(BaseHTTPRequestHandler):
    '''处理请求并返回页面'''

    # 页面模板
    Page = ""
    with open('hello.html', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            Page += line
    print(Page)

    # 处理一个GET请求
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page.encode())


if __name__ == '__main__':
    serverAddress = ('', 8090)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
