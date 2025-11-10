import json
from typing import Dict, Any


class SummeryLogger:
    
    def __init__(self, data_file: str = "data/summery.json"):
        self.data_file = data_file
        self.summery_data = self._load_data()
    
    def _load_data(self) -> Dict[str, Any]:
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {
                "highest_requests": {"name": "", "number": 0},
                "lowest_requests": {"name": "", "number": 0},
                "highest_handeling_time": {"name": "", "number": 0},
                "lowest": {"name": "", "number": 0}
            }
    
    def _save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.summery_data, f, indent=2)
    
    def enter_endpoint(self, endpoint: str, method: str, handling_time: float, total_requests: int):
        endpoint_name = f"{endpoint} {method}"
        
        # Update highest requests
        if total_requests > self.summery_data["highest_requests"]["number"]:
            self.summery_data["highest_requests"]["name"] = endpoint_name
            self.summery_data["highest_requests"]["number"] = total_requests
        
        # Update lowest requests (only if we have requests)
        current_lowest = self.summery_data["lowest_requests"]["number"]
        if total_requests > 0 and (current_lowest == 0 or total_requests < current_lowest):
            self.summery_data["lowest_requests"]["name"] = endpoint_name
            self.summery_data["lowest_requests"]["number"] = total_requests
        
        # Update highest handling time (only if we have requests and handling time)
        if total_requests > 0 and handling_time > self.summery_data["highest_handling_time"]["number"]:
            self.summery_data["highest_handling_time"]["name"] = endpoint_name
            self.summery_data["highest_handling_time"]["number"] = round(handling_time, 4)
        
        # Update lowest handling time (only if we have requests and handling time)
        current_lowest_time = self.summery_data["lowest_handling_time"]["number"]
        if total_requests > 0 and handling_time > 0 and (current_lowest_time == 0 or handling_time < current_lowest_time):
            self.summery_data["lowest_handling_time"]["name"] = endpoint_name
            self.summery_data["lowest_handling_time"]["number"] = round(handling_time, 4)
        
        self._save_data()
    
    def get_summery(self) -> Dict[str, Any]:
        return self.summery_data


_logger_instance = None

def get_summery_logger() -> SummeryLogger:
    global _logger_instance
    if _logger_instance is None:
        _logger_instance = SummeryLogger()
    return _logger_instance
