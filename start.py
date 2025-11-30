#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, HTTPServer

class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # キャッシュ無効化ヘッダーを追加
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    PORT = 8888
    print("次のURLにブラウザでアクセスしてください:")
    print(f"[URL] http://localhost:{PORT}/")
    HTTPServer(('0.0.0.0', PORT), NoCacheHandler).serve_forever()