from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime

class TimeHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/time':
            current_time = datetime.now().isoformat()
            response_data = {
                "current_time": current_time,
                "status": "success"
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), TimeHandler)
    print("http://localhost:8000")
    server.serve_forever()