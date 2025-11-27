from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime
from typing import Dict, Any

class TimeHandler(BaseHTTPRequestHandler):
    
    def _send_json_response(self, data: Dict[str, Any], status_code: int = 200) -> None:
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def do_GET(self) -> None:
        if self.path == '/time':
            current_time: str = datetime.now().isoformat()
            
            response_data: Dict[str, Any] = {
                "current_time": current_time,
                "status": "success"
            }
            
            self._send_json_response(response_data)
        else:
            error_data: Dict[str, Any] = {
                "error": "Not Found",
                "message": f"Path {self.path} not found"
            }
            self._send_json_response(error_data, 404)

def run_server() -> None:
    server_address: tuple[str, int] = ('localhost', 8000)
    server: HTTPServer = HTTPServer(server_address, TimeHandler)
    
    print("Server running at http://localhost:8000")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
        server.server_close()

if __name__ == '__main__':
    run_server()
