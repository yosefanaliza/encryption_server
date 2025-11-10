import json
from typing import Dict, Any, Optional


class EndpointLogger:
    
    def __init__(self, data_file: str = "data/endpoints_data.json"):
        self.data_file = data_file
        self.endpoints_data = self._load_data()
    
    def _load_data(self) -> list:
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    
    def _save_data(self):        
        with open(self.data_file, 'w') as f:
            json.dump(self.endpoints_data, f, indent=2)
    

    def _get_endpoint(self, url: str, method: str) -> Optional[Dict[str, Any]]:
        for ep in self.endpoints_data:
            if ep['url'] == url and ep['method'] == method:
                return ep
        return None
    
    def request_received(self, url: str, method: str):
        endpoint = self._get_endpoint(url, method)
        if endpoint is None:
            return
        
        endpoint['stats']['total_requests_received'] += 1
        self._save_data()

    def update_handling_time(self, url: str, method: str, handling_time: float):
        endpoint = self._get_endpoint(url, method)
        if endpoint is None:
            return
        
        stats = endpoint['stats']
        total_requests = stats['total_requests_received']
        current_avg = stats['avg_handling_time']
        
        # Calculate new average
        new_avg = (current_avg * total_requests + handling_time) / total_requests
        
        stats['avg_handling_time'] = round(new_avg, 4)
        
        self._save_data()
        

    def get_request_count(self, url: str, method: str) -> int:
        endpoint = self._get_endpoint(url, method)
        if endpoint is None:
            return 0
        return endpoint['stats']['total_requests_received']

_logger_instance = None

def get_endpoint_logger() -> EndpointLogger:
    global _logger_instance
    if _logger_instance is None:
        _logger_instance = EndpointLogger()
    return _logger_instance
